const fs=require('fs'),path=require('path'),crypto=require('crypto');const base=path.resolve(__dirname,'..');
const walk=p=>fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)]);
const out=path.join(__dirname,'files-created.json');const files=walk(base).filter(p=>p!==out).map(p=>({path:path.relative(base,p).replaceAll('\\','/'),bytes:fs.statSync(p).size,sha256:crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex')}));
fs.writeFileSync(out,JSON.stringify({date:'2026-11-12',root:'docs/agent-dinh-duong-vien',scope:'All E9 files except this manifest; no producer writes',count:files.length,files},null,2));console.log(files.length+' files + manifest');
