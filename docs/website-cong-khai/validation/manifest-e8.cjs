const fs=require('fs'),path=require('path'),crypto=require('crypto');const base=path.resolve(__dirname,'..');
const walk=p=>fs.readdirSync(p,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(p,e.name)):[path.join(p,e.name)]);
const files=walk(base).filter(p=>p!==path.join(__dirname,'files-created.json')).map(p=>{const b=fs.readFileSync(p);return {path:path.relative(base,p).replaceAll('\\','/'),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};});
fs.writeFileSync(path.join(__dirname,'files-created.json'),JSON.stringify({date:new Date().toISOString(),scope:'E8 only; excludes self',files},null,2));console.log(files.length+' E8 files listed; plus manifest itself');
