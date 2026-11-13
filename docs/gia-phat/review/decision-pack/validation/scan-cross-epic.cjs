const c=require('./common.cjs');const {read,walk,root,path,rel,json}=c;
const dirs=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/draft-register.json')).epicDirs;
let definitions=[],endpoints=[],files=[];
for(const [i,dir]of dirs.entries()){
 const base='docs/'+dir;
 for(const full of walk(path.resolve(root,base)).filter(p=>p.endsWith('.md')&&(/[/\\]srs[/\\]/.test(p)||/[/\\]usecases?[/\\]/.test(p)))){
 const file=rel(full);files.push(file);let heading='';
 read(file).split(/\r?\n/).forEach((line,n)=>{
 if(/^#{1,6} /.test(line))heading=line;
 const row=line.match(/^\|\s*[`*]*((?:FR|BR|NFR|ERR|UC)-[A-Z0-9]+(?:-[A-Z0-9]+)+)[`*]*(?:\s*\/[^|]*)?\s*\|/);
 const h=line.match(/^#{1,6}\s+(?:\*\*|`)?(UC-[A-Z0-9-]+)\b/);
 if((row||h)&&!/(truy vết|mapping|traceability|điểm mở)/i.test(heading))definitions.push({code:(row||h)[1],epic:'E'+(i+1),file,line:n+1,text:line});
 });
 }
 const file=base+'/api/endpoint-catalog.json';files.push(file);
 const raw=read(file),parsed=JSON.parse(raw),items=Array.isArray(parsed)?parsed:[...(parsed.endpoints||parsed.routes||[]),...(parsed.ports||[])];
 for(const e of items){const p=e.path||'',method=(e.method||'').toUpperCase();endpoints.push({...e,method,path:p,epic:'E'+(i+1),file,line:raw.slice(0,Math.max(0,raw.indexOf('"'+e.id+'"'))).split('\n').length});}
}
let findings=[];
function duplicate(list,key,kind){const m=new Map();for(const e of list){const k=key(e);if(k){if(!m.has(k))m.set(k,[]);m.get(k).push(e);}}for(const [key,occ]of m){if(new Set(occ.map(x=>x.epic)).size>1){const seen=new Set();const occurrences=occ.filter(o=>{const k=o.file+':'+o.line;if(seen.has(k))return false;seen.add(k);return true;});findings.push({kind,key,severity:kind==='code'?'Trung bình':'Cao',occurrences});}}}
duplicate(definitions,x=>x.code,'code');
duplicate(endpoints,x=>x.path.startsWith('/')?x.method+' '+x.path.replace(/\{[^}]+\}/g,'{}'):null,'endpoint-method-path');
duplicate(endpoints,x=>x.path.startsWith('/')?x.path.replace(/\{[^}]+\}/g,'{}'):null,'endpoint-path');
// Cùng FR là dấu hiệu trùng chức năng; không kết luận thay review ngữ nghĩa.
const expanded=endpoints.flatMap(e=>(Array.isArray(e.fr)?e.fr:typeof e.fr==='string'?e.fr.match(/FR-[A-Z0-9-]+/g)||[]:[]).map(fr=>({...e,functionKey:fr})));
duplicate(expanded,x=>x.functionKey,'endpoint-function');
findings.sort((a,b)=>(a.kind+a.key).localeCompare(b.kind+b.key));findings.forEach((f,i)=>f.id='XC-'+String(i+1).padStart(2,'0'));
json('validation/cross-epic-result.json',{scope:'13 epic; chỉ đọc SRS/usecase và endpoint-catalog; ứng viên mã định nghĩa trùng cần phân loại tái dùng hay xung đột',files:[...new Set(files)],definitionOccurrences:definitions.length,endpoints:endpoints.length,findings,errors:[]});
console.log(JSON.stringify({findings:findings.length,byKind:findings.reduce((o,f)=>(o[f.kind]=(o[f.kind]||0)+1,o),{}),endpoints:endpoints.length,errors:0}));
