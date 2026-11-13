const c=require('./common.cjs');const {read,walk,root,pack,path,fs,rel,json,tableRows,clean}=c;
let errors=[],checks=0;const check=(ok,msg)=>{checks++;if(!ok)errors.push(msg);};
const {rows}=JSON.parse(read('docs/gia-phat/review/decision-pack/decision-register.json'));
const inventory=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/source-inventory.json'));
const groups=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/group-index.json'));
let expected=[];for(const [file,,pattern] of inventory.configs){const ids=tableRows(file).map(x=>clean(x.cells[0])).filter(x=>new RegExp(pattern).test(x));expected.push(...ids);check(ids.length===inventory.registers.find(r=>r.file===file).count,'Source count changed: '+file);}
check(new Set(expected).size===expected.length,'Source configuration overlaps');
check(rows.length===expected.length,'Inventory/register count mismatch');
for(const id of expected)check(rows.filter(x=>x.sourceCode===id).length===1,'Missing/duplicate '+id);
const regMd=tableRows('docs/gia-phat/review/decision-pack/decision-register.md').filter(r=>expected.includes(r.cells[0]));
check(regMd.length===rows.length,'MD/JSON row count mismatch');
const groupText=read('docs/gia-phat/review/decision-pack/decision-groups.md'),agenda=read('docs/gia-phat/review/decision-pack/meeting-agenda.md');
for(const r of rows){
 check(expected.includes(r.sourceCode),'Extra code '+r.sourceCode);
 check(new RegExp('(?<![A-Z0-9-])'+r.sourceCode+'(?![A-Z0-9-])').test(read(r.sourceFile)),'Code not in source '+r.sourceCode);
 check(read(r.sourceFile).split(/\r?\n/)[r.sourceLine-1]?.includes(r.sourceCode),'Source line mismatch '+r.sourceCode);
 check(r.answer==='','Answer filled '+r.sourceCode);
 check(r.question.trim().split(/\s+/).length<=30,'Question >30 words '+r.sourceCode);
 check(!!r.decisionOwner&&r.blockedReleases.length>0,'Missing owner/release '+r.sourceCode);
 const m=regMd.find(x=>x.cells[0]===r.sourceCode);const norm=s=>clean(s).replaceAll('&#124;','|');
 check(!!m&&m.cells.length===10,'Bad columns '+r.sourceCode);
 if(m){check(norm(m.cells[2])===r.question,'MD/JSON question differs '+r.sourceCode);check(norm(m.cells[3])===r.decisionGroup,'MD/JSON group differs '+r.sourceCode);check(m.cells[9]==='','MD answer filled '+r.sourceCode);check(norm(m.cells[4])===r.decisionOwner&&m.cells[5]===r.blockedReleases.join(', ')&&m.cells[6]===r.priority&&m.cells[7]===r.blockedCount&&norm(m.cells[8])===clean(r.recommendation),'MD/JSON metadata differs '+r.sourceCode);}
 const g=groups.find(g=>g.id===r.decisionGroup);check(!!g&&g.members.includes(r.sourceCode),'Missing group '+r.sourceCode);
 if(r.priority==='P-MVP')check(g.meeting<=3,'MVP not in first 3 meetings '+r.sourceCode);
}
for(const g of groups){check(groupText.includes('<a id="'+g.id.toLowerCase()+'"></a>'),'Missing group heading '+g.id);const section=agenda.split('<a id="buoi-'+g.meeting+'"></a>')[1]?.split('<a id="buoi-')[0]||'';check(section.includes(g.id),'Group not in meeting '+g.id);}
const consistency=read('docs/gia-phat/review/decision-pack/cross-epic-consistency.md');
const machine=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/cross-epic-result.json'));
const manual=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/manual-findings.json'));
for(const f of [...machine.findings,...manual])check(consistency.includes('## '+f.id+' —'),'Finding absent from report '+f.id);
for(const r of rows)if(r.recommendation)check(clean(read(r.sourceFile)).includes(clean(r.recommendation)),'Recommendation not copied from source '+r.sourceCode);
const manifest=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/files-created.json'));
for(const p of walk(pack).map(rel))check(manifest.created.includes(p),'New file not in manifest '+p);
let links=0,sourceQuotesExcluded=0;
for(const full of walk(pack).filter(p=>p.endsWith('.md'))){const text=fs.readFileSync(full,'utf8'),file=rel(full);const front=text.match(/^---\r?\n([\s\S]*?)\r?\n---/);check(!!front,'Missing frontmatter '+file);for(const field of ['id','title','version','phase','domain','tags','depends_on','related_diagrams','author','last_updated'])check(!!front&&new RegExp('^'+field+':','m').test(front[1]),'Missing metadata '+field+' '+file);
 check(/version: \d+\.\d+\.\d+/.test(front?.[1]||''),'Bad version '+file);
 check(text.includes('| Phiên bản | Ngày |'),'Missing revision history '+file);
 let fenced=false;for(const [i,line]of text.split(/\r?\n/).entries()){
 if(line.startsWith('```')){fenced=!fenced;continue;}if(fenced)continue;
 if(line.startsWith('>')){sourceQuotesExcluded++;continue;}
 let prose=line.replace(/\[[^\]]*\]\([^)]*\)/g,m=>m.slice(1,m.indexOf(']'))).replace(/`[^`]*`/g,'').replace(/\b[A-Z]+[A-Z0-9]*(?:-[A-Z0-9]+)+\b/g,'').replace(/\b(?:E|R|P|PER)\d+\b/g,'').replace(/https?:\S+/g,'').replace(/<[^>]+>/g,'');
 if(file.endsWith('decision-register.md')&&line.startsWith('|')){const cells=line.split('|');if(expected.includes(cells[1]?.trim()))prose=cells.slice(1,9).join(' ').replace(/\[[^\]]*\]\([^)]*\)/g,m=>m.slice(1,m.indexOf(']'))).replace(/\b[A-Z]+[A-Z0-9]*(?:-[A-Z0-9]+)+\b/g,'').replace(/\b(?:E|R|P)\d+\b/g,'');}
 prose=prose.replace(/\b[a-f0-9]{7,64}\b/gi,'');
 check(!/\d\p{L}/u.test(prose),'Số dính chữ '+file+':'+(i+1));
 }
 for(const m of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){let target=m[1];if(/^(https?:|mailto:)/.test(target))continue;links++;const [p,frag]=target.split('#');const resolved=p?path.resolve(path.dirname(full),decodeURI(p)):full;check(fs.existsSync(resolved),'Broken link '+file+': '+target);if(frag&&fs.existsSync(resolved)&&/^L\d+$/.test(frag))check(Number(frag.slice(1))<=fs.readFileSync(resolved,'utf8').split(/\r?\n/).length,'Line out of range '+target);else if(frag&&fs.existsSync(resolved)){const contents=fs.readFileSync(resolved,'utf8');check(contents.includes('id="'+frag+'"'),'Broken anchor '+target);}}
 if(file.endsWith('meeting-agenda.md')){for(const r of tableRows(file))if(r.cells.length===4&&!r.cells[0].startsWith(':')&&!['Quyết định','Việc sau quyết định','Phiên bản','0.1.0'].includes(r.cells[0]))check(r.cells.every(x=>x===''),'Meeting decision populated');}
}
const result={status:errors.length?'FAIL':'PASS',checks,sourceCodes:rows.length,groups:groups.length,links,sourceQuotesExcluded,numberSpacingScope:'Văn xuôi mới; nguyên văn nguồn trong blockquote và cột khuyến nghị được giữ byte nội dung, không sửa số dính chữ lịch sử.',errors};json('validation/structure-result.json',result);console.log(JSON.stringify(result,null,2));process.exitCode=errors.length?1:0;
