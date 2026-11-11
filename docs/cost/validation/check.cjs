// Usage: node docs/cost/validation/check.cjs <directory containing node_modules>
// Dependencies used for verification only: @dbml/core, playwright.
const fs=require('fs'),path=require('path'),assert=require('assert/strict');
const deps=path.resolve(process.argv[2]);
const {exporter}=require(path.join(deps,'node_modules/@dbml/core'));
const {chromium}=require(path.join(deps,'node_modules/playwright'));
const root=path.resolve(__dirname,'../../..');
const schema=fs.readFileSync(path.join(root,'docs/nen-tang/srs/schema.dbml'),'utf8');
const sql=exporter.export(schema,'mysql');
assert(sql.includes('CREATE TABLE'));
const tableNames=[...schema.matchAll(/^Table (\w+) \{/gm)].map(m=>m[1]);
assert.equal(new Set(tableNames).size,tableNames.length);
const costNames=schema.match(/TableGroup cost \{([^}]+)\}/)[1].trim().split(/\s+/);
assert.equal(costNames.length,15);
const erd=fs.readFileSync(path.join(root,'docs/nen-tang/srs/erd.md'),'utf8');
for(const t of costNames)assert(erd.includes('##### `'+t+'`'),`Dictionary missing: ${t}`);
const menuDays=schema.match(/Table menu_days \{([\s\S]*?)\n\}/)[1];
assert(!menuDays.includes('cost_pct'));
const params=['COST_MON_CHINH_CACH_TINH','COST_AP_HAO_HUT','COST_CHE_DO_KIEM','COST_BANG_TINH_HIEU_LUC_NGAY','GIA_NHAP_HOI_TO_NGAY','GIA_NHAP_LECH_CANH_BAO_PCT'];
const foundation=fs.readFileSync(path.join(root,'docs/nen-tang/srs/spec.md'),'utf8');
for(const p of params)assert.equal(foundation.split('| `'+p+'` |').length-1,1,p);
for(const file of ['docs/nen-tang/srs/erd.md','docs/nen-tang/srs/spec.md','docs/cost/srs/spec.md','docs/cost/epic-spec.md']){
 const content=fs.readFileSync(path.join(root,file),'utf8');
 for(const m of content.matchAll(/\]\(([^)]+)\)/g)){
  const target=m[1].split('#')[0];
  if(target&&!/^https?:/.test(target))assert(fs.existsSync(path.resolve(root,path.dirname(file),target)),`Broken link ${file}: ${target}`);
 }
}
console.log(`PASS DBML -> MySQL: ${tableNames.length} tables; 15 Cost dictionaries; 6 parameters; local links.`);
(async()=>{
 const browser=await chromium.launch({channel:'chrome',headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1080}});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto('file:///'+path.join(root,'docs/thuc-don-dinh-luong/html-wireframe/soan-thuc-don-tuan.html').replaceAll('\\','/'));
  assert.equal(await page.locator('.costrow td').count(),6);
  assert(await page.evaluate(()=>DAYS.some(([d])=>{const r=dayCost(d,'A');return r.state==='READY'&&!r.over;})));
  assert((await page.locator('.costrow td[data-d="T7"]').innerText()).includes('Chưa đủ món'));
  const first=await page.locator('.costrow td[data-d="T2"]').innerText();
  await page.selectOption('#costKitchen','B');
  assert.notEqual(await page.locator('.costrow td[data-d="T2"]').innerText(),first);
  const warning=await page.evaluate(()=>check().filter(r=>r.code==='BR-COST-001').map(r=>r.type));
  assert(warning.length>0);assert(warning.every(t=>t==='SOFT'));
  await page.selectOption('#costMode','CHAN');
  assert((await page.evaluate(()=>check().filter(r=>r.code==='BR-COST-001').map(r=>r.type))).every(t=>t==='HARD'));
  await page.selectOption('#costPermission','no');
  assert(!/%/.test(await page.locator('.costrow').innerText()));
  await page.selectOption('#costScenario','missing');
  assert((await page.locator('.costrow td[data-d="T3"]').innerText()).includes('Thiếu giá'));
  assert(await page.evaluate(()=>check().some(r=>r.code==='COST-INPUT'&&r.type==='HARD')));
  await page.selectOption('#costScenario','vat');
  assert((await page.locator('.costrow td[data-d="T2"]').innerText()).includes('Chưa cấu hình VAT'));
  await page.selectOption('#costScenario','ready');
  await page.selectOption('#costPermission','yes');
  await page.selectOption('#costMode','CANH_BAO');
  await page.screenshot({path:path.join(deps,'cost-desktop.png'),fullPage:true});
  const before=await page.locator('.costrow td[data-d="T2"]').innerText();
  await page.locator('.cell[data-c="T2:M1"] .x').click();
  assert.notEqual(await page.locator('.costrow td[data-d="T2"]').innerText(),before);
  await page.locator('[data-st="normal"]').click();
  await page.setViewportSize({width:390,height:844});
  await page.locator('[data-day="T3"]').click();
  assert.equal(await page.locator('.costrow td:visible').count(),1);
  assert.equal(await page.locator('.costrow td:visible').getAttribute('data-d'),'T3');
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  await page.screenshot({path:path.join(deps,'cost-mobile.png'),fullPage:true});
  await page.locator('[data-st="empty"]').click();
  assert((await page.locator('.costrow').innerText()).includes('Chưa xếp món'));
  assert.deepEqual(errors,[]);
  console.log('PASS UI: 6 days, per-kitchen cost, warning/block, permissions, missing price/VAT, edit refresh, empty state, mobile; no JS errors.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
