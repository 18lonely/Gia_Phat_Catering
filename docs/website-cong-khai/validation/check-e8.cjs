const fs=require('fs'),path=require('path'),crypto=require('crypto');
const base=path.resolve(__dirname,'..'),root=path.resolve(base,'../..');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const walk=p=>fs.readdirSync(p,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(p,e.name)):[path.join(p,e.name)]);
let checks=[];const check=(name,passed,detail='')=>checks.push({name,passed:!!passed,detail});
const read=p=>fs.readFileSync(path.join(base,p),'utf8');
const baseline=JSON.parse(read('validation/protected-baseline.json'));
const changed=baseline.files.filter(f=>!fs.existsSync(path.join(root,f.path))||sha(fs.readFileSync(path.join(root,f.path)))!==f.sha256);
check('E1–E7 and PRD/roadmap SHA256 unchanged',!changed.length,changed);
const protectedDirs=['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo','chon-mon-order','giao-nhan-doanh-thu'];
const originalPaths=new Set(baseline.files.map(f=>f.path));
const extra=protectedDirs.flatMap(d=>walk(path.join(root,'docs',d))).map(p=>path.relative(root,p).replaceAll('\\','/')).filter(p=>!originalPaths.has(p));
check('No added files in E1–E7',!extra.length,extra);
for(const h of baseline.history){const b=fs.readFileSync(path.join(root,h.path));check('Append-only '+h.path,b.length>=h.bytes&&sha(b.subarray(0,h.bytes))===h.sha256);}
const index=JSON.parse(read('validation/design-index.json')),catalog=JSON.parse(read('api/endpoint-catalog.json'));
check('Exactly six features 054–059',index.features.map(f=>f[0]).join(',')==='054,055,056,057,058,059');
check('5P0 and 057 P1',index.features.filter(f=>f[3]==='P0').length===5&&index.features.find(f=>f[0]==='057')[3]==='P1');
for(const d of index.data){for(const [file,token]of [['srs/spec.md',d.fr],['usecases/'+d.uc+'.md',d.fr],['userstories/backlog.md',d.us],['userstories/acceptance-criteria.md','AC-PUB-'+d.n+'-H'],['test/test-cases.md','TC-PUB-'+d.n+'-H'],['test/traceability.md',d.fr],['html-wireframe/public-workbench.html','id="'+d.ui+'"']])check(file+' '+token,read(file).includes(token));check('Catalog FR '+d.fr,catalog.some(a=>a.fr===d.fr));for(const x of ['H','E','B'])check('AC/test '+d.n+x,read('userstories/acceptance-criteria.md').includes('AC-PUB-'+d.n+'-'+x)&&read('test/test-cases.md').includes('TC-PUB-'+d.n+'-'+x));}
check('No duplicate routes/IDs',new Set(catalog.map(a=>a.method+' '+a.path)).size===catalog.length&&new Set(catalog.map(a=>a.id)).size===catalog.length);
for(const a of catalog){for(const e of a.errors)check(a.id+' error '+e,read('srs/error-matrix.md').includes(e));}
const qrows=read('review/questions.md').split('\n').filter(l=>/^\| E8-Q\d+/.test(l));
check('12 unanswered questions',qrows.length===12&&qrows.every(r=>{const c=r.split('|');return c[5].trim()===''&&c[6].trim()==='';}));
const r8=fs.readFileSync(path.join(root,'docs/gia-phat/02-roadmap.md'),'utf8').split(/\r?\n/).find(l=>l.startsWith('| `R8`'));
check('R8 verbatim',read('epic-spec.md').includes(r8));
check('Schema remains65tables',(fs.readFileSync(path.join(root,'docs/nen-tang/srs/schema.dbml'),'utf8').match(/^Table /gm)||[]).length===65);
const broken=[];
for(const file of walk(base).filter(f=>f.endsWith('.md'))){const s=fs.readFileSync(file,'utf8');for(const m of s.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){let target=m[1].split('#')[0];if(!target||/^(https?:|mailto:)/.test(target))continue;if(!fs.existsSync(path.resolve(path.dirname(file),target)))broken.push({file:path.relative(base,file),target});}}
check('Local Markdown links exist',!broken.length,broken);
const brokenHtml=[];
for(const file of walk(base).filter(f=>f.endsWith('.html'))){const s=fs.readFileSync(file,'utf8');for(const m of s.matchAll(/(?:href|src)="([^"]+)"/g)){const target=m[1].split('#')[0];if(!target||/^(https?:|data:|mailto:|javascript:)/.test(target))continue;if(!fs.existsSync(path.resolve(path.dirname(file),target)))brokenHtml.push({file:path.relative(base,file),target});}}
check('Local HTML links/assets exist',!brokenHtml.length,brokenHtml);
const forbidden=walk(base).filter(f=>/\.(sql|dbml)$/.test(f));check('No SQL/DBML migration output',!forbidden.length);
const result={date:new Date().toISOString(),scope:'Document structure only; not backend',protectedFiles:baseline.files.length,fr:index.data.length,features:index.features.length,endpoints:catalog.length,checks,failed:checks.filter(c=>!c.passed)};
fs.writeFileSync(path.join(__dirname,'structure-result.json'),JSON.stringify(result,null,2));console.log(JSON.stringify({checks:checks.length,failures:result.failed,protectedFiles:baseline.files.length},null,2));if(result.failed.length)process.exitCode=1;
