const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../../..'),base=JSON.parse(fs.readFileSync(path.join(__dirname,'baseline.json'),'utf8'));
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const errors=[],unchanged=[],appended=[];
for(const f of base.files){const p=path.join(root,f.path);if(!fs.existsSync(p)){errors.push('Missing '+f.path);continue}const b=fs.readFileSync(p);if(['docs/OVERVIEW.md','docs/project-dashboard.md'].includes(f.path)){if(b.length<f.size||hash(b.subarray(0,f.size))!==f.sha256)errors.push('Old prefix changed '+f.path);else if(b.length>f.size)appended.push(f.path);else unchanged.push(f.path)}else if(hash(b)!==f.sha256)errors.push('Changed '+f.path);else unchanged.push(f.path)}
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)])}
const old=new Set(base.files.map(f=>f.path));for(const f of walk(path.join(root,'docs'))){const rel=path.relative(root,f).replaceAll('\\','/');if(!old.has(rel)&&!rel.startsWith('docs/mua-hang-san-xuat/'))errors.push('New outside package '+rel)}
const result={scope:'All old docs files, SHA256 and append-only prefix',baselineFiles:base.files.length,unchanged:unchanged.length,appendOnly:appended,errors};fs.writeFileSync(path.join(__dirname,'hash-result.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));if(errors.length)process.exitCode=1;
