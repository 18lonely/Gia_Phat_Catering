// One-time local renderer preparation. Reads E8 renderer, writes/runs none of E8.
const fs=require('fs'),path=require('path');const base=path.resolve(__dirname,'..');
const target=path.join(__dirname,'render-e9.cjs');if(fs.existsSync(target))throw Error('Renderer already exists');
const source=fs.readFileSync(path.resolve(__dirname,'../../website-cong-khai/validation/render-e8.cjs'),'utf8').replace("const folders=['website-cong-khai'];","const folders=['agent-dinh-duong-vien'];");
fs.writeFileSync(target,source);
const p=path.join(base,'api/endpoint-catalog.json'),c=JSON.parse(fs.readFileSync(p));
c.push({id:'PORT-AIN-HANDOFF',fr:'FR-AIN-SEND-001',method:'PORT',path:'PORT-AIN-HANDOFF',permission:'application only after client confirmation and durable proposal; not model callable',requestResponse:'proposalRef/source/candidateRevision/consentRef → receiver receipt or pending/error',success:'internal receipt',errors:['ERR-AIN-503-01','ERR-AIN-500-01'],gate:'E9-Q06, E9-Q10, E9-Q13',ui:'UI-AIN-04'});fs.writeFileSync(p,JSON.stringify(c,null,2));
console.log('E9 renderer and handoff catalog prepared.');
