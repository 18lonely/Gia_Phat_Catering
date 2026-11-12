// Tests only the BA wireframes/previews, never production/backend behavior.
const fs=require('fs'),path=require('path'),assert=require('assert/strict'),{pathToFileURL}=require('url');
const dep=process.argv[2]||path.join(process.env.TEMP,'gia-phat-cost-validation');
const {chromium}=require(path.join(dep,'node_modules/playwright'));
const docs=path.resolve(__dirname,'../..');
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true});const errors=[],results=[];
try{
const page=await browser.newPage({viewport:{width:1440,height:1000}});page.on('pageerror',e=>errors.push(String(e)));
const open=async p=>page.goto(pathToFileURL(path.join(docs,p)).href);
const tab=async n=>page.click('[data-tab="'+n+'"]');
const has=async(id,s)=>assert((await page.locator('#'+id).innerText()).includes(s),id+' lacks '+s);
await open('nen-tang/html-wireframe/foundation-workbench.html');
for(let i=0;i<5;i++){await page.fill('#password','wrong-pass');await page.click('#loginForm button');}await has('loginResult','423');
await page.reload();await page.fill('#password','DemoPass1234');await page.click('#loginForm button');await has('loginResult','thành công');assert.equal(await page.inputValue('#password'),'');
await tab(2);await page.fill('#roleReason','Lý do sửa giả định');await page.click('#roleForm button');await has('roleResult','422');await page.selectOption('#kitchen','K1');await page.click('#roleForm button');await has('roleResult','Đã lưu');
await tab(4);await page.click('#paramForm button');await has('paramResult','PENDING');await page.click('#approve');await has('paramResult','403');await page.selectOption('#approver','other');await page.click('#approve');await has('paramResult','APPROVED');const audit=await page.locator('#audit li').count();await page.click('#approve');assert.equal(await page.locator('#audit li').count(),audit);
await page.selectOption('#env','offline');await page.click('#paramForm button');await has('paramResult','Mất mạng');assert.equal(await page.locator('#audit li').count(),audit);await page.selectOption('#env','online');
await tab(5);await page.click('#seen');await has('noticeResult','SEEN');await page.click('#resolved');await has('noticeResult','RESOLVED');await tab(6);await page.click('#retryJob');await page.click('#retryJob');await has('jobResult','không nhân đôi');
await tab(4);await page.screenshot({path:path.join(__dirname,'foundation-desktop.png'),fullPage:true});
for(const width of [360,390]){await page.setViewportSize({width,height:900});for(let n=1;n<=6;n++){await tab(n);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'CORE overflow'+width+'/'+n);}}
results.push('CORE: six screens at360/390px, login5-fail/password clearing, role scope, separate approval, idempotent mock approval, offline and job retry');

await page.setViewportSize({width:1440,height:1000});await open('dinh-duong/html-wireframe/nutrition-workbench.html');await tab(2);await page.click('#calcDish');await has('dishResult','40.00 kcal');await has('dishResult','4.00 g');
await tab(3);await page.click('#calcMeal');await has('mealResult','50.00 kcal');await page.selectOption('#mainDish','both');await page.click('#calcMeal');await has('mealResult','422');await page.selectOption('#mainDish','A');
await tab(1);await page.fill('#source','<img src=x onerror=alert(1)> GIẢ ĐỊNH');await page.click('#saveNutr');assert.equal(await page.locator('#history img').count(),0);await tab(2);await page.click('#showOld');await has('dishResult','NGUỒN ĐÃ ĐỔI');await has('dishResult','40.00');await page.click('#calcDish');await page.screenshot({path:path.join(__dirname,'nutrition-desktop.png'),fullPage:true});
await tab(1);await page.click('#missingNutr');await tab(2);await page.click('#calcDish');await has('dishResult','Tổng: --');await page.selectOption('#env','stale');await page.click('#calcDish');await has('dishResult','409');
for(const width of [360,390]){await page.setViewportSize({width,height:900});for(let n=1;n<=3;n++){await tab(n);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'NUTR overflow');}}
await page.screenshot({path:path.join(__dirname,'nutrition-mobile.png'),fullPage:true});results.push('NUTR: three screens, fixture40/50kcal, selected combination, missing source, immutable old snapshot, version conflict, escaped source,360/390px');

await page.setViewportSize({width:1440,height:1000});await open('agent-noi-bo/html-wireframe/agent-workbench.html');await page.fill('#week','2026-11-17');await page.click('#runAgent');await has('runResult','thứ Hai');await page.fill('#week','2026-11-16');
for(const mode of ['NEEDS_INPUT','BLOCKED_DATA','NO_SOLUTION','TIMEOUT']){await page.selectOption('#outcome',mode);await page.click('#runAgent');assert(await page.locator('#apply').isDisabled());await has('runResult',mode);}
await page.selectOption('#outcome','VALID');await page.fill('#instruction','<img src=x onerror=alert(1)> test-only');await page.click('#runAgent');await tab(2);assert(!(await page.locator('#apply').isDisabled()));await page.click('#apply');await page.click('#cancelApply');await has('applyResult','chưa ghi');await page.click('#apply');await page.click('#confirmApply');await has('applyResult','MENU DRAFT');const count=await page.locator('#runLog li').count();await page.click('#apply');await page.click('#confirmApply');await has('applyResult','Replay');assert.equal(await page.locator('#runLog li').count(),count);assert.equal(await page.locator('#runLog img').count(),0);
await page.selectOption('#env','stale');await page.click('#apply');await has('applyResult','409');await page.selectOption('#env','online');await page.click('#revise');await has('diff','thứ Tư');await page.screenshot({path:path.join(__dirname,'agent-desktop.png'),fullPage:true});
for(const width of [360,390]){await page.setViewportSize({width,height:900});for(let n=1;n<=3;n++){await tab(n);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'AIO overflow');}}await page.screenshot({path:path.join(__dirname,'agent-mobile.png'),fullPage:true});
results.push('AIO: three screens, Monday validation, all4 non-valid outcomes block apply, confirm/cancel/replay, stale guard, revision/diff, escaped log,360/390px');

for(const f of ['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo']){
 await open(f+'/preview.html');assert(await page.locator('article>section:not([hidden])').count()===1);assert(await page.locator('aside a').count()>0);await page.locator('aside a').last().click();assert(await page.locator('article>section:not([hidden])').count()===1);await page.fill('#search','SRS');assert(await page.locator('aside a:not([hidden])').count()>0);assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'preview overflow'+f);
}
await page.setViewportSize({width:1440,height:1000});await open('dinh-duong/preview.html');await page.screenshot({path:path.join(__dirname,'preview-desktop.png'),fullPage:true});
assert.deepEqual(errors,[]);const report={scope:'BA HTML simulation only; backend/model tests=0',results,previewPages:5,jsErrors:errors};fs.writeFileSync(path.join(__dirname,'ui-review-result.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1});
