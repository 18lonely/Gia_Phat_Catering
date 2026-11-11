const fs=require('fs'),path=require('path'),assert=require('assert');
const {pathToFileURL}=require('url');
const {chromium}=require(path.join(process.argv[2],'node_modules/playwright'));
const root=path.resolve(__dirname,'../../..'), catalog=JSON.parse(fs.readFileSync(path.join(root,'docs/cost/api/endpoint-catalog.json')));
const spec=fs.readFileSync(path.join(root,'docs/cost/srs/spec.md'),'utf8');
const fr=new Set(spec.match(/FR-COST-[A-Z]+-\d{3}/g));
const covered=new Set([...catalog.endpoints.flatMap(e=>e.fr),...Object.keys(catalog.internalMappings),...catalog.deferred]);
assert.equal(catalog.endpoints.length,37);assert.equal(new Set(catalog.endpoints.map(e=>e.method+' '+e.path)).size,37);
assert.deepEqual([...covered].sort(),[...fr].sort());
(async()=>{const browser=await chromium.launch({channel:'chrome',headless:true});try{
const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
page.on('pageerror',e=>errors.push(e.message));
await page.goto(pathToFileURL(path.join(root,'docs/cost/html-wireframe/cost-workbench.html')).href);
async function route(n,role='KT'){await page.selectOption('#role',role);await page.evaluate(n=>go(n),n);await page.waitForFunction(n=>document.querySelector('#screenCode').textContent==='SCR-COST-'+String(n).padStart(2,'0'),n);}
for(let n=1;n<=18;n++){await route(n,n===13?'GD':'KT');assert((await page.locator('#content').innerText()).length>20);}
await route(2);await page.evaluate(()=>{selectedSupplier=0;render();});await page.fill('[name=name]','NCC kiểm thử');await page.locator('#supplierForm button.primary').click();assert.equal(await page.evaluate(()=>db.suppliers.length),3);
await page.selectOption('#state','offline');await page.fill('[name=name]','Không được lưu');await page.locator('#supplierForm button.primary').click();assert.equal(await page.evaluate(()=>db.suppliers.at(-1).name),'NCC kiểm thử');await page.selectOption('#state','normal');
await route(9,'DD');await page.locator('#sheetForm button').click();assert.equal(await page.evaluate(()=>db.sheets.length),2);
await route(10,'GD');await page.locator('[data-action="approveSheet:2"]').click();await page.click('#modalConfirm');assert.equal(await page.evaluate(()=>db.sheets[1].status),'APPROVED');
await page.selectOption('#kitchen','B');await route(9,'QL');assert(!(await page.locator('#content').innerText()).includes('Người lập:'));
await route(15,'CHEF');assert(!(await page.locator('#content').innerText()).includes('Tổng chi phí'));assert.equal(await page.locator('#content tbody tr').first().locator('td').nth(2).innerText(),'B');
await page.click('[data-action=exportPdf]');assert(!(await page.locator('#modalBody').innerText()).includes('đ'));await page.click('#modalCancel');
await page.click('#reset');await page.selectOption('#kitchen','A');
await route(4);await page.fill('[name=price]','180000');await page.locator('#priceForm button.primary').click();assert(await page.locator('#modal').isVisible());assert.equal(await page.evaluate(()=>db.prices.length),3);await page.click('#modalConfirm');assert.equal(await page.evaluate(()=>db.prices.length),4);
await route(5);await page.selectOption('#importScenario','invalid');await page.click('[data-action=checkImport]');assert(await page.locator('[data-action=commitImport]').isDisabled());await page.selectOption('#importScenario','valid');await page.click('[data-action=checkImport]');await page.click('[data-action=commitImport]');assert.equal(await page.evaluate(()=>db.prices.length),5);
await route(13,'QT');await page.fill('[name=date]','2026-11-16');await page.fill('[name=reason]','Kiểm thử đề nghị tương lai');await page.locator('#modeForm button').click();await page.selectOption('#role','GD');await page.click('[data-action=approveMode]');await page.click('#modalConfirm');assert.equal(await page.evaluate(()=>db.mode),'CANH_BAO');assert.equal(await page.evaluate(()=>db.proposal.status),'APPROVED');
await route(14);await page.selectOption('[name=data]','missing');await page.locator('#estimateForm button.primary').click();assert.equal(await page.evaluate(()=>db.estimates.length),2);await page.selectOption('[name=data]','ready');await page.locator('#estimateForm button.primary').click();assert.equal(await page.evaluate(()=>db.estimates.at(-1).version),2);assert.equal(await page.evaluate(()=>db.estimates[0].total),1880000);
await route(1);for(const state of ['loading','empty','error']){await page.selectOption('#state',state);assert((await page.locator('#content').innerText()).length>10);}await page.selectOption('#state','normal');
await route(15);await page.screenshot({path:path.join(__dirname,'cost-desktop.png'),fullPage:true});
await page.setViewportSize({width:390,height:844});for(let n=1;n<=18;n++){await route(n,n===13?'GD':'KT');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`overflow screen ${n}`);}
await route(14);await page.screenshot({path:path.join(__dirname,'cost-mobile.png'),fullPage:true});
assert.deepEqual(errors,[]);console.log(JSON.stringify({endpoints:37,fr:fr.size,screens:18,mobileScreens:18,checks:'price confirmation, import mock, future mode, estimate version/missing price, supplier, offline, sheet approval, kitchen scope, chef redaction, export preview, loading/empty/error',pageErrors:errors}));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1)});
