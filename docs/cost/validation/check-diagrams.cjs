// node docs/cost/validation/check-diagrams.cjs <directory with node_modules>
const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const dep=path.resolve(process.argv[2]);
const {chromium}=require(path.join(dep,'node_modules/playwright'));
const root=path.resolve(__dirname,'../../..');
const inputs=['docs/cost/srs/usecase-diagram.md','docs/cost/ui/user-flow.md'];
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1600,height:1100}});
  await page.setContent('<html><body style="font-family:Arial;padding:20px"><main id="out"></main></body></html>');
  await page.addScriptTag({path:path.join(dep,'node_modules/mermaid/dist/mermaid.min.js')});
  await page.evaluate(()=>mermaid.initialize({startOnLoad:false,theme:'neutral',securityLevel:'strict'}));
  let count=0;
  for(const file of inputs){
   const blocks=[...fs.readFileSync(path.join(root,file),'utf8').matchAll(/```mermaid\r?\n([\s\S]*?)```/g)];
   for(const [,source]of blocks){
    const id='costflow'+(++count);
    const svg=await page.evaluate(async({source,id})=>{
     await mermaid.parse(source);
     const result=await mermaid.render(id,source);
     document.getElementById('out').innerHTML=result.svg;
     return result.svg;
    },{source,id});
    assert(svg.includes('<svg'));
    fs.writeFileSync(path.join(dep,id+'.svg'),svg);
    if(count===1||count===7)await page.screenshot({path:path.join(dep,id+'.png'),fullPage:true});
   }
  }
  assert.equal(count,10);
  console.log('PASS: 10 Mermaid diagrams parsed and rendered to SVG.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
