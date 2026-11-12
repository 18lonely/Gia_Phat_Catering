// Read-only source checks; outputs strictly inside E9/validation.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const base=path.resolve(__dirname,'..'),root=path.resolve(base,'../..');
const walk=p=>fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)]);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');let checks=[];const ck=(name,ok)=>checks.push({name,passed:!!ok});
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'protected-baseline.json')));
for(const f of baseline.files)ck('protected hash '+f.path,fs.existsSync(path.join(root,f.path))&&hash(fs.readFileSync(path.join(root,f.path)))===f.sha256);
for(const dir of baseline.dirs){const now=walk(path.join(root,'docs',dir)).map(p=>path.relative(root,p).replaceAll('\\','/')).sort();const old=baseline.files.filter(f=>f.path.startsWith('docs/'+dir+'/')).map(f=>f.path).sort();ck('protected inventory '+dir,JSON.stringify(now)===JSON.stringify(old));}
for(const f of baseline.append)ck('append prefix '+f.path,hash(fs.readFileSync(path.join(root,f.path)).subarray(0,f.bytes))===f.sha256);
const schema=fs.readFileSync(path.join(root,'docs/nen-tang/srs/schema.dbml'),'utf8');ck('65 tables',(schema.match(/^Table\s+\w+\s*\{/gm)||[]).length===65);
const index=JSON.parse(fs.readFileSync(path.join(__dirname,'design-index.json'))),catalog=JSON.parse(fs.readFileSync(path.join(base,'api/endpoint-catalog.json')));
ck('six features',JSON.stringify(index.features.map(f=>f.id))===JSON.stringify(['060','061','062','063','064','065'].map(x=>'FEAT-'+x)));
ck('five designed + one gate',index.features.filter(f=>!f.gateOnly).length===5&&index.features.find(f=>f.gateOnly).id==='FEAT-063');
const get=p=>fs.readFileSync(path.join(base,p),'utf8'),frs=index.requirements;
ck('13 unique FR',new Set(frs.map(d=>d.fr)).size===13);
const story=get('userstories/backlog.md'),ac=get('userstories/acceptance-criteria.md'),tc=get('test/test-cases.md'),rtm=get('test/traceability.md'),spec=get('srs/spec.md'),wire=get('html-wireframe/agent-workbench.html');
for(const d of frs){ck(d.fr+' naming',/^FR-AIN-[A-Z]{2,4}-\d{3}$/.test(d.fr));ck(d.fr+' SRS',spec.includes(d.fr));ck(d.fr+' UC',fs.existsSync(path.join(base,'usecases',d.uc+'.md')));ck(d.fr+' story',story.includes(d.us));ck(d.fr+' RTM',[d.fr,d.uc,d.us,d.api,d.ui].every(x=>rtm.includes(x)));ck(d.fr+' API',catalog.some(c=>c.fr===d.fr));ck(d.fr+' UI',wire.includes('id="'+d.ui+'"'));for(let j=1;j<=3;j++){let n=d.n+'-0'+j;ck('AC '+n,ac.includes('AC-AIN-'+n));ck('TC '+n,tc.includes('TC-AIN-'+n));}}
ck('unique catalog IDs',new Set(catalog.map(x=>x.id)).size===catalog.length);ck('11 HTTP / 4 ports',catalog.filter(x=>x.method!=='PORT').length===11&&catalog.filter(x=>x.method==='PORT').length===4);
for(const c of catalog){ck(c.id+' FR',frs.some(f=>f.fr===c.fr));for(const e of c.errors)ck(c.id+' '+e,get('srs/error-matrix.md').includes(e));}
const qrows=get('review/questions.md').split('\n').filter(l=>/^\| E9-Q\d+ \|/.test(l));ck('14 questions',qrows.length===14);for(const line of qrows){const cols=line.split('|').slice(1,-1).map(x=>x.trim());ck(cols[0]+' answer blank',cols[5]===''&&cols[6]==='');ck(cols[0]+' blocked branch',cols[3].length>0);}
for(const file of ['test/test-cases.md','test/system-cases.md'])for(const line of get(file).split('\n').filter(l=>/^\| TC-AIN-/.test(l))){const cols=line.split('|').slice(1,-1).map(x=>x.trim());ck(cols[0]+' status/evidence',['NOT RUN','BLOCKED'].includes(cols.at(-3))&&cols.at(-2)===''&&cols.at(-1)==='');}
const roadmap=fs.readFileSync(path.join(root,'docs/gia-phat/02-roadmap.md'),'utf8');for(const prefix of ['| `R9`','**Cổng G-Next**']){const l=roadmap.split(/\r?\n/).find(l=>l.startsWith(prefix));ck('verbatim '+prefix,get('epic-spec.md').includes(l));}
for(const f of walk(base).filter(p=>/\.(md|html)$/.test(p))){const text=fs.readFileSync(f,'utf8');let links=f.endsWith('.md')?[...text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)].map(m=>m[1]):[...text.matchAll(/(?:href|src)="([^"]+)"/g)].map(m=>m[1]);for(const l of links){if(/^(https?:|mailto:|data:|javascript:|#)/.test(l))continue;const clean=decodeURIComponent(l.split('#')[0]).replaceAll('&amp;','&');ck('link '+path.relative(base,f)+' → '+clean,fs.existsSync(path.resolve(path.dirname(f),clean)));}}
ck('wireframe no network/storage',!/(fetch\s*\(|XMLHttpRequest|WebSocket|localStorage|sessionStorage|https?:\/\/)/.test(wire));
for(const p of ['epic-spec.md','api/api-spec.md','api/data-mapping.md','srs/states.md','review/dependencies.md','test/r9-acceptance.md','preview.html','validation/report.md'])ck('required '+p,fs.existsSync(path.join(base,p)));
const errors=checks.filter(c=>!c.passed);fs.writeFileSync(path.join(__dirname,'structure-result.json'),JSON.stringify({scope:'Document structure only; not product tests',protectedFiles:baseline.files.length,checks,errors},null,2));console.log(JSON.stringify({checks:checks.length,protectedFiles:baseline.files.length,errors},null,2));if(errors.length)process.exitCode=1;
