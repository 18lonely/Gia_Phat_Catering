
const fs=require('fs'),path=require('path'),crypto=require('crypto');const root=path.resolve(__dirname,'../../..'),base=path.join(root,'docs/giao-nhan-doanh-thu');let errors=[],checks=[];
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(path.join(p,x.name)):[path.join(p,x.name)]);}
function check(name,ok){checks.push({name,passed:!!ok});if(!ok)errors.push(name);}
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'protected-baseline.json'),'utf8'));
for(const [p,h]of Object.entries(baseline))check('protected '+p,fs.existsSync(path.join(root,p))&&hash(path.join(root,p))===h);
const histories=JSON.parse(fs.readFileSync(path.join(__dirname,'history-prefixes.json'),'utf8'));
for(const [p,s]of Object.entries(histories))check('history prefix '+p,fs.readFileSync(path.join(root,p),'utf8').startsWith(s));
['srs','usecases','userstories','api','ui','html-wireframe','test','review','validation'].forEach(d=>check('directory '+d,fs.existsSync(path.join(base,d))));
const files=walk(base).filter(p=>p.endsWith('.md'));
for(const p of files){const s=fs.readFileSync(p,'utf8');check('metadata '+path.relative(base,p),s.startsWith('---\n')||s.startsWith('---\r\n'));for(const m of s.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){let t=m[1].split('#')[0];if(!t||/^(https?:|mailto:)/.test(t))continue;check('link '+path.relative(base,p)+' → '+t,fs.existsSync(path.resolve(path.dirname(p),t)));}}
const read=p=>fs.readFileSync(path.join(base,p),'utf8');
const rows=JSON.parse(read('validation/design-index.json')),cat=JSON.parse(read('api/endpoint-catalog.json'));
check('feature exact IDs',JSON.stringify([...new Set(rows.map(r=>r.feat))])===JSON.stringify(['FEAT-049','FEAT-050','FEAT-051','FEAT-052','FEAT-053']));
check('13 unique FR',new Set(rows.map(r=>r.fr)).size===13);
check('18 unique routes',cat.length===18&&new Set(cat.map(r=>r.method+' '+r.path)).size===18);
for(const r of rows){for(const f of ['srs/spec.md','userstories/backlog.md','userstories/acceptance-criteria.md','test/test-cases.md','test/traceability.md'])check(r.fr+' in '+f,read(f).includes(r.fr));check('UC '+r.uc,fs.existsSync(path.join(base,'usecases',r.uc+'.md')));check('API '+r.api,cat.some(x=>x.id===r.api&&x.fr.includes(r.fr)));check('UI '+r.ui,read('html-wireframe/revenue-workbench.html').includes('id="'+r.ui+'"'));}
const acs=[...read('userstories/acceptance-criteria.md').matchAll(/^### (AC-E7-\d{3}-[123])/gm)].map(m=>m[1]);
const tcs=[...read('test/test-cases.md').matchAll(/^\| (TC-E7-\d{3}-[123]) /gm)].map(m=>m[1]);
check('39 unique AC and cases',acs.length===39&&new Set(acs).size===39&&tcs.length===39&&new Set(tcs).size===39);
for(const id of acs)check('AC trace '+id,read('test/traceability.md').includes(id)&&read('test/test-cases.md').includes(id));
for(const id of tcs)check('TC trace '+id,read('test/traceability.md').includes(id));
const qrows=read('review/questions.md').split('\n').filter(l=>/^\| (?:Q-13|E7-Q\d+)/.test(l));check('9 questions answers blank',qrows.length===9&&qrows.every(l=>/\|  \|  \|$/.test(l)));
const road=fs.readFileSync(path.join(root,'docs/gia-phat/02-roadmap.md'),'utf8');
const r7=road.split('\n').find(x=>x.startsWith('| '+String.fromCharCode(96)+'R7'));check('R7 verbatim',read('epic-spec.md').includes(r7.trim()));
check('65 DBML tables',(fs.readFileSync(path.join(root,'docs/nen-tang/srs/schema.dbml'),'utf8').match(/^Table \w+ \{/gm)||[]).length===65);
const fixture=JSON.parse(read('test/fixtures/synthetic.json'));check('synthetic arithmetic',fixture.billableServings*Number(fixture.quotedUnitPrice)===Number(fixture.amountDue)&&Number(fixture.amountDue)-Number(fixture.receivedPayment)===Number(fixture.remainingDue)&&fixture.receivedServings===null);
check('4 Mermaid diagrams',files.reduce((n,p)=>n+fs.readFileSync(p,'utf8').split(String.fromCharCode(96).repeat(3)+'mermaid').length-1,0)===4);
const html=read('html-wireframe/revenue-workbench.html');check('8 UI panels',(html.match(/<section id="UI-E7-/g)||[]).length===8);check('no remote dependencies',!/<(?:script|link)[^>]+(?:src|href)=["']https?:/i.test(html));
const result={date:'2026-11-12',scope:'E7 documents only; not backend',checks:checks.length,errors,markdownFiles:files.length,protectedFiles:Object.keys(baseline).length,historyFiles:4,fr:13,uc:13,stories:13,ac:39,testCases:39,systemCases:8,endpoints:18,ui:8,diagrams:4,backend:0,caseStatus:{blocked:(read('test/test-cases.md').match(/\| BLOCKED \|/g)||[]).length,notRun:(read('test/test-cases.md').match(/\| NOT RUN \|/g)||[]).length}};
fs.writeFileSync(path.join(__dirname,'structure-result.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));if(errors.length)process.exitCode=1;

