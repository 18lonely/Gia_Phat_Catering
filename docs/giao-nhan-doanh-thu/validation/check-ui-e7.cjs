
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
const deps=process.argv[2]||path.join(process.env.TEMP,'gia-phat-cost-validation');
const {chromium}=require(path.join(deps,'node_modules/playwright'));
const base=path.resolve(__dirname,'..'),out=path.join(__dirname,'screenshots');fs.mkdirSync(out,{recursive:true});
let checks=[],errors=[];function check(name,ok){checks.push({name,passed:!!ok});if(!ok)errors.push(name);}
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true});
try{
const page=await browser.newPage();page.on('pageerror',e=>errors.push('JS '+e.message));
await page.goto(pathToFileURL(path.join(base,'html-wireframe/revenue-workbench.html')).href);
for(const mode of ['loading','empty','error','offline','normal']){await page.selectOption('#scenario',mode);check('scenario '+mode,mode==='normal'?await page.locator('#scenario-message').isHidden():await page.locator('#scenario-message').isVisible());}
await page.fill('#delivered','-1');await page.locator('#delivery-form button.primary').click();check('negative delivery',(await page.textContent('#delivery-result')).includes('ERR-DLV-422-01'));
await page.fill('#delivered','98');await page.locator('#delivery-form button.primary').click();check('delivery gate',(await page.textContent('#delivery-result')).includes('BLOCKED CG05/06/08'));
await page.locator('nav [data-go="02"]').click();await page.click('#no-response');check('Q13',(await page.textContent('#received-result')).includes('BLOCKED Q-13')&&(await page.textContent('#received-label'))==='Chưa xác định');
await page.locator('nav [data-go="03"]').click();await page.click('#resolution-check');check('agreement required',(await page.textContent('#resolution-result')).includes('ERR-DLV-422-02'));
await page.locator('nav [data-go="04"]').click();await page.selectOption('#revenue-context','missing');check('missing revenue',(await page.textContent('#revenue-result')).includes('ERR-FIN-422-01'));
await page.locator('nav [data-go="05"]').click();await page.click('#attempt-edit');check('locked',(await page.textContent('#period-result')).includes('ERR-FIN-409-02'));
await page.locator('nav [data-go="06"]').click();await page.locator('#cash-form button').click();check('payment',(await page.textContent('#remaining')).includes('3.000.000'));await page.locator('#cash-form button').click();check('duplicate receipt',(await page.textContent('#cash-result')).includes('trùng'));
await page.locator('nav [data-go="07"]').click();await page.click('#request-reopen');check('reason10',(await page.textContent('#reopen-result')).includes('10 ký tự'));await page.fill('#reason','Sửa sai số liệu synthetic');await page.click('#request-reopen');check('pending locked',(await page.textContent('#reopen-result')).includes('vẫn LOCKED'));
await page.selectOption('#decision-role','self');await page.click('#approve');check('self approval blocked',(await page.textContent('#reopen-result')).includes('ERR-E7-403-01'));
await page.selectOption('#decision-role','director');await page.click('#reject');check('reject locked',(await page.textContent('#reopen-result')).includes('vẫn khóa'));
await page.click('#request-reopen');await page.click('#approve');check('approve reopened',(await page.locator('#UI-E7-07 .period-state').textContent())==='REOPENED');
await page.locator('nav [data-go="05"]').click();await page.click('#attempt-edit');check('dialog',await page.locator('#edit-dialog').isVisible());await page.click('#close-dialog');
await page.locator('nav [data-go="08"]').click();await page.click('#export-check');check('MISA gate',(await page.textContent('#export-result')).includes('BLOCKED E7-Q07'));check('no fake file',await page.locator('#UI-E7-08 button:disabled').count()===1);
await page.reload();
for(const [label,width,height]of [['desktop',1440,1000],['mobile',390,1300]]){
 await page.setViewportSize({width,height});
 for(let i=1;i<=8;i++){const id=String(i).padStart(2,'0');await page.locator('nav [data-go="'+id+'"]').click();check(label+' panel '+id,await page.locator('#UI-E7-'+id).isVisible());check(label+' no overflow '+id,await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.screenshot({path:path.join(out,label+'-'+id+'.png'),fullPage:true});}
}
await page.goto(pathToFileURL(path.join(base,'preview.html')).href);
check('preview content',await page.locator('article>section').count()>=34);
const nav=page.locator('aside a');for(let i=0;i<await nav.count();i++){const href=await nav.nth(i).getAttribute('href');await page.evaluate(h=>location.hash=h,href);check('preview '+href,await page.locator('article>section:not([hidden])').count()===1);}
for(const label of ['desktop','mobile'])for(const batch of [0,1]){
 const ids=[1,2,3,4].map(x=>String(x+batch*4).padStart(2,'0'));
 const tileWidth=label==='desktop'?720:390;
 const body=ids.map(id=>'<div><b>'+label+' · UI-E7-'+id+'</b><img src="'+('data:image/png;base64,'+fs.readFileSync(path.join(out,label+'-'+id+'.png')).toString('base64'))+'"></div>').join('');
 const p=await browser.newPage({viewport:{width:label==='desktop'?1440:1560,height:1000}});
 await p.setContent('<html><style>body{margin:0;font:18px Arial;display:grid;grid-template-columns:repeat('+ (label==='desktop'?2:4)+','+tileWidth+'px)}div{border:1px solid #888}img{display:block;width:100%}b{display:block;padding:5px}</style>'+body+'</html>');
 await p.waitForFunction(()=>[...document.images].every(i=>i.complete&&i.naturalWidth>0));
 await p.screenshot({path:path.join(out,label+'-sheet-'+(batch+1)+'.png'),fullPage:true});await p.close();
}
fs.writeFileSync(path.join(__dirname,'ui-result.json'),JSON.stringify({date:'2026-11-12',scope:'E7 wireframe and preview only; no backend',checks:checks.length,errors,screenshots:16,contactSheets:4},null,2));
console.log(JSON.stringify({checks:checks.length,errors,screenshots:16,contactSheets:4}));if(errors.length)process.exitCode=1;
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1});


