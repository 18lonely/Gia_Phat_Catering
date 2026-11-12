const fs=require('fs'),path=require('path'),base=path.resolve(__dirname,'..');
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()?walk(path.join(p,d.name)):[path.join(p,d.name)])}
const files=[...new Set([...walk(base).map(p=>path.relative(base,p).replaceAll('\\','/')),'validation/files-created.json','validation/structure-result.json'])].sort();
fs.writeFileSync(path.join(__dirname,'files-created.json'),JSON.stringify({scope:'docs/phan-hoi-bao-cao only',files},null,2));console.log(files.length+' E12 file paths');
