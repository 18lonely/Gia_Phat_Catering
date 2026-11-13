// Run an explicitly allowed local checker/renderer; redirect historical JSON output before writing.
const fs=require('fs'),path=require('path'),Module=require('module');
const root=path.resolve(__dirname,'../../../../..'),requested=path.resolve(root,process.argv[2]||'');
if(!/(?:render-e1[123]|check-e1[123]|check-decision-pack|scan-cross-epic)\.cjs$/.test(requested))throw Error('Script not authorized by follow-up');
const originalWrite=fs.writeFileSync,originalLoad=Module._load;
const proxy={...fs,writeFileSync(file,data,...rest){const p=path.resolve(String(file));if(/[/\\]validation[/\\][^/\\]*-result\.json$/.test(p)){const label=path.basename(path.dirname(path.dirname(requested)));file=path.join(__dirname,label+'-'+path.basename(p));}else if(/[/\\]validation[/\\](?:report\.md|baseline[^/\\]*\.json|files-created\.json)$/.test(p))throw Error('Historical write blocked '+p);
if(/render-e/.test(requested)&&typeof data==='string'){
 const history='<table aria-label="Lịch sử phiên bản"><tr><th>Phiên bản</th><th>Ngày</th><th>Người thực hiện</th><th>Nội dung</th></tr><tr><td>0.1.1</td><td>13/11/2026</td><td>BA</td><td>Render lại tài liệu XC-01–12; không phê duyệt nghiệp vụ</td></tr></table>';
 if(p.endsWith('.html'))data=data.includes('</body>')?data.replace('</body>',history+'</body>'):data+history;
 if(p.endsWith('.svg'))data=data.replace('</svg>','<metadata id="revision-history">'+history+'</metadata></svg>');
}
return originalWrite.call(fs,file,data,...rest);}};
Module._load=function(id,parent,isMain){if(id==='fs'||id==='node:fs')return proxy;return originalLoad.apply(this,arguments);};
// Renderers interpret argv[2] as their optional local dependency directory.
process.argv=[process.argv[0],requested,...process.argv.slice(3)];require(requested);
