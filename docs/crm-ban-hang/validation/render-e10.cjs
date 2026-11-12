// Offline artifact renderer; uses already installed local Mermaid/marked/Playwright.
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const deps=process.argv[2]||path.join(process.env.TEMP,'gia-phat-cost-validation');
const {chromium}=require(path.join(deps,'node_modules/playwright'));
const root=path.resolve(__dirname,'../../..'),docs=path.join(root,'docs');
const folders=['crm-ban-hang'];
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(d=>d.isDirectory()&&!['validation','diagrams'].includes(d.name)?walk(path.join(p,d.name)):d.isFile()&&d.name.endsWith('.md')?[path.join(p,d.name)]:[]);}
const slug=p=>'doc-'+p.replace(/[^a-zA-Z0-9_-]/g,'-');
const css=`*{box-sizing:border-box}body{margin:0;background:#f6f6f6;color:#191919;font:16px/1.55 Arial,sans-serif}header{padding:22px 30px;background:#fff;border-bottom:2px solid #333}h1{font-size:28px;line-height:1.25}h2{margin-top:32px}a{color:#222;text-underline-offset:3px}main{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1600px;margin:auto}aside{padding:20px;position:sticky;top:0;max-height:100vh;overflow:auto}aside a{display:block;padding:7px 0;overflow-wrap:anywhere}input,select,button{font:inherit;padding:9px;max-width:100%}article{min-width:0;background:white;border-left:1px solid #ccc;padding:30px}section[hidden]{display:none}.table-wrap{overflow:auto}table{border-collapse:collapse;font-size:14px;width:100%}th,td{border:1px solid #ccc;padding:9px;vertical-align:top;min-width:85px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eee;padding:18px}code{overflow-wrap:anywhere}figure{margin:18px 0;border:1px solid #ccc;padding:12px;overflow:auto}figure svg{max-width:none;height:auto}img{max-width:100%}.badge{border:1px solid #333;padding:5px 10px;display:inline-block}.toolbar{display:flex;gap:12px;flex-wrap:wrap}a:focus-visible,button:focus-visible,input:focus-visible{outline:3px solid #444;outline-offset:3px}@media(max-width:700px){header,article{padding:16px}main{display:block}aside{position:static;max-height:240px;border-bottom:1px solid #aaa}article{border-left:0}h1{font-size:24px}}`;
(async()=>{
const {marked}=await import(pathToFileURL(require.resolve('marked',{paths:[path.join(deps,'node_modules')]})).href);
const browser=await chromium.launch({channel:'chrome',headless:true});let results=[];
try{
 const page=await browser.newPage();
 await page.setContent('<html><body><div id="render"></div></body></html>');
 await page.addScriptTag({path:path.join(deps,'node_modules/mermaid/dist/mermaid.min.js')});
 await page.evaluate(()=>mermaid.initialize({startOnLoad:false,theme:'neutral',securityLevel:'strict',fontFamily:'Arial',flowchart:{htmlLabels:false,useMaxWidth:false},sequence:{useMaxWidth:false},maxTextSize:300000}));
 let num=0;
 for(const folder of folders){
  const base=path.join(docs,folder),files=walk(base),outdir=path.join(base,'srs/diagrams');fs.mkdirSync(outdir,{recursive:true});
  let sections=[],nav=[],gallery=[];
  for(const file of files){
   const rel=path.relative(base,file).replaceAll('\\','/');let source=fs.readFileSync(file,'utf8').replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/,'');
   const title=(source.match(/^# (.+)/m)||[])[1]||rel;
   let i=0;
   for(const match of [...source.matchAll(/```mermaid\r?\n([\s\S]*?)```/g)]){
    i++;num++;const id='g'+num,basename=rel.replace(/\.md$/,'').replaceAll('/','-')+'-'+i;
    try{
     const svg=await page.evaluate(async({id,source})=>{await mermaid.parse(source);return(await mermaid.render(id,source)).svg;},{id,source:match[1]});
     fs.writeFileSync(path.join(outdir,basename+'.svg'),svg);
     fs.writeFileSync(path.join(outdir,basename+'.html'),'<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'+esc(title)+'</title><style>'+css+'</style><header><h1>'+esc(title)+'</h1><p>Draft · nguồn '+esc(rel)+' · không phải hệ thống đã triển khai</p><a href="'+basename+'.svg">Mở SVG</a></header><figure>'+svg+'</figure></html>');
     source=source.replace(match[0],'<figure>'+svg+'<figcaption><a href="srs/diagrams/'+basename+'.html">Mở sơ đồ lớn</a> · <a href="srs/diagrams/'+basename+'.svg" download>Tải SVG</a></figcaption></figure>');
     gallery.push({title,file:basename});results.push({folder,source:rel,diagram:i,status:'RENDERED'});
    }catch(e){results.push({folder,source:rel,diagram:i,status:'ERROR',message:String(e)});}
   }
   // Rebase original markdown links before parsing; raw figure links already relative to preview.
   source=source.replace(/(!?\[[^\]]*\])\(([^)]+)\)/g,(m,label,target)=>{
    if(/^(https?:|mailto:|#)/.test(target))return m;
    const [f,anchor]=target.split('#'),absolute=path.resolve(path.dirname(file),f);
    let rebased=path.relative(base,absolute).replaceAll('\\','/');
    if(f.endsWith('.md')&&files.includes(absolute))rebased='#'+slug(path.relative(base,absolute).replaceAll('\\','/'));
    else if(anchor)rebased+='#'+anchor;
    return label+'('+rebased+')';
   });
   let body=marked.parse(source).replace(/<table>/g,'<div class="table-wrap"><table>').replace(/<\/table>/g,'</table></div>');
   const sid=slug(rel);nav.push('<a href="#'+sid+'">'+esc(title)+'</a>');
   sections.push('<section id="'+sid+'" hidden><p><a href="'+rel+'">Mở Markdown nguồn</a> · '+esc(rel)+'</p>'+body+'</section>');
  }
  const galleries=gallery.map(g=>'<figure><h2>'+esc(g.title)+'</h2><a href="'+g.file+'.html">Mở lớn</a> · <a href="'+g.file+'.svg">SVG</a><img loading="lazy" src="'+g.file+'.svg" alt="'+esc(g.title)+'"></figure>').join('');
  fs.writeFileSync(path.join(outdir,'index.html'),'<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Sơ đồ '+folder+'</title><style>'+css+'</style><header><h1>Sơ đồ '+folder+'</h1><p>Draft · '+gallery.length+' sơ đồ xuất bằng Mermaid cục bộ, không phụ thuộc mạng.</p></header><article>'+galleries+'</article></html>');
  const wire=path.join(base,'html-wireframe');let links=fs.existsSync(wire)?fs.readdirSync(wire).filter(x=>x.endsWith('.html')).map(x=>'<a href="html-wireframe/'+x+'">'+esc(x)+'</a>').join(' · '):'';
  const content='<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Hồ sơ BA '+folder+'</title><style>'+css+'</style></head><body><header><span class="badge">GIA PHÁT · BA REVIEW · DRAFT</span><h1>'+folder+'</h1><p>'+files.length+' tài liệu · '+gallery.length+' sơ đồ · Chưa ký duyệt / chưa triển khai backend.</p><div class="toolbar"><a href="../OVERVIEW.md">Tổng quan</a><a href="../project-dashboard.md">Dashboard</a><a href="srs/diagrams/index.html">Gallery sơ đồ</a>'+links+'</div></header><main><aside><label>Tìm tài liệu <input id="search" placeholder="SRS, API, test..."></label><nav>'+nav.join('')+'</nav></aside><article>'+sections.join('')+'</article></main><script>const sections=[...document.querySelectorAll("article>section")];function show(){let id=location.hash.slice(1);if(!sections.some(s=>s.id===id))id=sections[0].id;sections.forEach(s=>s.hidden=s.id!==id);}window.addEventListener("hashchange",show);show();document.querySelector("#search").oninput=e=>document.querySelectorAll("aside a").forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(e.target.value.toLowerCase()));</script></body></html>';
  fs.writeFileSync(path.join(base,'preview.html'),content);
  console.log(folder+': '+files.length+' docs, '+gallery.length+' diagrams rendered');
 }
 fs.writeFileSync(path.join(__dirname,'diagram-render-result.json'),JSON.stringify(results,null,2));
 const errors=results.filter(r=>r.status==='ERROR');console.log('Render errors: '+errors.length);if(errors.length){console.log(JSON.stringify(errors,null,2));process.exitCode=1;}
}finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});

