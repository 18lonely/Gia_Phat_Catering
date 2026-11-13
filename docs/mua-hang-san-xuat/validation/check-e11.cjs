const fs=require('fs'),path=require('path');const base=path.resolve(__dirname,'..'),root=path.resolve(base,'../..');
const errors=[],checks=[];const ck=(name,ok)=>{checks.push({name,ok:!!ok});if(!ok)errors.push(name)};
const read=p=>fs.readFileSync(path.join(base,p),'utf8');
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)])}
const required=['epic-spec.md','srs/spec.md','srs/data-dictionary.md','srs/error-matrix.md','srs/states.md','usecases/index.md','userstories/backlog.md','userstories/acceptance-criteria.md','ui/screens.md','ui/user-flow.md','api/api-spec.md','api/data-mapping.md','api/endpoint-catalog.json','html-wireframe/purchase-workbench.html','test/checklist.md','test/test-cases.md','test/system-cases.md','test/traceability.md','test/r11-acceptance.md','review/handoff.md','review/questions.md','review/dependencies.md','validation/report.md','validation/files-created.json','preview.html'];
required.forEach(p=>ck('Required '+p,fs.existsSync(path.join(base,p))));
const rows=JSON.parse(read('validation/design-index.json')),cat=JSON.parse(read('api/endpoint-catalog.json')),fixture=JSON.parse(read('test/fixtures/synthetic.json'));
ck('5 features exact',JSON.stringify([...new Set(rows.map(r=>r.feature))])===JSON.stringify(['FEAT-074','FEAT-075','FEAT-076','FEAT-077','FEAT-078']));
const definitions=[...rows.flatMap(r=>[r.fr,r.uc,r.us,r.api,r.br,r.err,...r.ac,...r.tc]),...cat.ports.map(p=>p.id),'NFR-PUR-001','NFR-PUR-002','NFR-PUR-003','NFR-PUR-004','NFR-PUR-005','ERR-PUR-409-11','ERR-PUR-503-11','ERR-PUR-422-99'];
ck('Unique new IDs',new Set(definitions).size===definitions.length);
// 13/11/2026 BA — XC-04: historical baseline references a removed uc-refresh folder.
// Check current E1-E10 declarations, not references added by later reports or previews.
// Historical baseline remains unchanged; session diff checker verifies file preservation.
const priorDirs=['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo','chon-mon-order','giao-nhan-doanh-thu','website-cong-khai','agent-dinh-duong-vien','crm-ban-hang'];
const declared=new Set();
for(const dir of priorDirs)for(const file of walk(path.join(root,'docs',dir)).filter(p=>p.endsWith('.md')&&!/[\\/](?:validation|review)[\\/]/.test(p)&&!/(?:traceability|dependencies)\.md$/.test(p))){
 for(const line of fs.readFileSync(file,'utf8').split(/\r?\n/)){
  const m=line.match(/^\|\s*[`*]*((?:FR|BR|NFR|ERR|UC|US|AC|TC|API|PORT)-[A-Z0-9-]+)[`*]*\s*\|/)||line.match(/^#{1,6}\s+[`*]*((?:UC|US|AC|TC)-[A-Z0-9-]+)\b/);
  if(m)declared.add(m[1]);
 }
}
for(const id of definitions)ck('No E1-E10 declaration collision '+id,!declared.has(id));
for(const r of rows){
 ck('FR defined '+r.fr,read('srs/spec.md').includes(r.fr));
 ck('UC Cockburn '+r.uc,fs.existsSync(path.join(base,'usecases',r.uc+'.md'))&&['Actor','Trigger','Tiền điều kiện','Hậu điều kiện','Luồng chính','Ngoại lệ',r.fr].every(x=>read('usecases/'+r.uc+'.md').includes(x)));
 ck('Story '+r.us,[r.us,r.fr,r.uc].every(x=>read('userstories/backlog.md').includes(x)));
 for(let j=0;j<3;j++){const ac=read('userstories/acceptance-criteria.md').split('### '+r.ac[j]+' ')[1]?.split('### ')[0]||'';ck('GWT '+r.ac[j],['Given ','When ','Then '].every(x=>ac.includes(x)));ck('Case '+r.tc[j],fixture.cases.some(t=>t.id===r.tc[j]&&t.ac===r.ac[j]&&t.fr===r.fr&&t.expected===r.scenarios[j][1])&&read('test/test-cases.md').includes(r.tc[j]));}
 const line=read('test/traceability.md').split('\n').find(l=>l.startsWith('| '+r.feature+' | '+r.fr+' |'))||'';
 ck('RTM complete '+r.fr,[r.uc,r.us,...r.ac,...r.tc,r.api,r.screen].every(x=>line.includes(x)));
 ck('API backtrace '+r.api,cat.endpoints.some(e=>e.id===r.api&&e.fr.includes(r.fr))&&read('api/api-spec.md').includes('## '+r.api+' —')&&read('api/data-mapping.md').includes(r.api));
 ck('Screen '+r.screen,read('ui/screens.md').includes(r.screen)&&read('html-wireframe/purchase-workbench.html').includes('id="'+r.screen+'"'));
}
for(const e of [...cat.endpoints,...cat.ports])ck('Every API has valid FR '+e.id,e.fr.length>0&&e.fr.every(f=>rows.some(r=>r.fr===f)));
const mdFiles=walk(base).filter(p=>p.endsWith('.md')),docIds=[];
function slug(s){return s.toLowerCase().replace(/<[^>]+>/g,'').replace(/[^\p{L}\p{N}\s_-]/gu,'').trim().replace(/\s/g,'-')}
function spacing(text){return text.replace(/\b[a-f0-9]{7,64}\b/gi,'').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/,'').replace(/```[\s\S]*?```/g,'').replace(/`[^`]*`/g,'').replace(/\]\([^)]*\)/g,']').replace(/\b[A-Z][A-Z0-9_-]*(?:[–/][A-Z0-9_-]+)*/g,'').replace(/\b(?:[A-Za-z]+\d+)+\b/g,'').match(/\d[\p{L}]/gu)||[]}
for(const p of mdFiles){const rel=path.relative(base,p),s=fs.readFileSync(p,'utf8');ck('Frontmatter '+rel,/^---\r?\n/.test(s)&&['id:','title:','version:','phase:','domain:','tags:','depends_on:','related_diagrams:','author:','last_updated:'].every(k=>s.split('---')[1]?.includes(k)));docIds.push((s.match(/^id: (.+)$/m)||[])[1]);ck('Revision '+rel,s.includes('| Phiên bản |'));ck('Spacing '+rel,spacing(s).length===0);
 const text=s.replace(/```[\s\S]*?```/g,'');for(const m of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){const target=m[1];if(/^(https?:|mailto:)/.test(target))continue;const [file,anchor]=target.split('#'),dest=file?path.resolve(path.dirname(p),decodeURIComponent(file)):p;ck('Link '+rel+' → '+target,fs.existsSync(dest));if(anchor&&fs.existsSync(dest)&&dest.endsWith('.md')){const content=fs.readFileSync(dest,'utf8');ck('Anchor '+target,[...content.matchAll(/^#+ (.+)$/gm)].some(x=>slug(x[1])===anchor)||content.includes('id="'+anchor+'"'))}}
}
ck('Document IDs unique',new Set(docIds).size===docIds.length);
const q=read('review/questions.md').split('\n').filter(l=>/^\| E11-Q\d+ /.test(l));ck('15 questions blank',q.length===15&&q.every(l=>l.split('|').at(-2).trim()===''));
for(const p of ['test/test-cases.md','test/system-cases.md']){const lines=read(p).split('\n').filter(l=>/^\| TC-/.test(l));ck('Product statuses '+p,lines.every(l=>/\| (NOT RUN|BLOCKED) \|/.test(l)&&!l.includes('| PASS |')));ck('Empty Actual Evidence '+p,lines.every(l=>l.split('|').slice(-3,-1).every(c=>c.trim()==='')))}
const baseline=JSON.parse(read('validation/baseline.json'));for(const name of ['OVERVIEW.md','project-dashboard.md']){const f=baseline.files.find(x=>x.path==='docs/'+name),b=fs.readFileSync(path.join(root,f.path));ck('Append spacing '+name,spacing(b.subarray(f.size).toString('utf8')).length===0)}
ck('65 baseline schema tables',(fs.readFileSync(path.join(root,'docs/nen-tang/srs/schema.dbml'),'utf8').match(/^Table /gm)||[]).length===65);
// Test the spacing detector itself, including prose digits adjacent to accented letters.
ck('Spacing detector positive',spacing('65bảng và 3điểm').length===2);ck('Spacing detector code exemption',spacing('FR-PUR-DEM-001 và 65 bảng').length===0);
const manifest=JSON.parse(read('validation/files-created.json'));ck('Manifest complete',walk(base).every(p=>manifest.files.includes(path.relative(base,p).replaceAll('\\','/'))));
const result={scope:'Artifact structure and traceability only',counts:{fr:rows.length,uc:rows.length,story:rows.length,ac:fixture.cases.length,functionalCases:fixture.cases.length,http:cat.endpoints.length,ports:cat.ports.length,screens:9},checks:checks.length,errors,details:checks};fs.writeFileSync(path.join(__dirname,'structure-result.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({checks:checks.length,errors},null,2));if(errors.length)process.exitCode=1;
