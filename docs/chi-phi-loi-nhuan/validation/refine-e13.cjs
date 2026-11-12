// Local documentation review corrections; no source package writes.
const fs=require('fs'),path=require('path'),base=path.resolve(__dirname,'..');
const edit=(p,fn)=>fs.writeFileSync(path.join(base,p),fn(fs.readFileSync(path.join(base,p),'utf8')));
edit('srs/data-dictionary.md',s=>s.replaceAll('UUID','BIGINT UNSIGNED').replaceAll('(36, PK','(20 chữ số tối đa, PK').replaceAll('| 36 |','| 20 chữ số |').replaceAll('36 / —','20 chữ số / —').replace('quy tắc cấp ID, độ dài và lưu trữ chờ Q12.','Khóa mới đề xuất kế thừa BIGINT UNSIGNED của nền; API truyền định danh dạng chuỗi để không mất chính xác. Trường liệt kê là enum logic, physical đề xuất VARCHAR(24) + CHECK theo nền, không phải MySQL ENUM. Thời điểm lưu UTC, ngày nghiệp vụ theo giờ Việt Nam; biên kỳ cụ thể vẫn chờ Q02. Độ dài trường chưa có căn cứ và lưu trữ chi tiết chờ Q12.'));
const fixes={'API-EXP-014':'Bảng SUBMITTED giữ revision và bằng chứng; chưa tự xác nhận giờ công','API-EXP-015':'Phiên bản SUBMITTED chờ Giám đốc; chưa có hiệu lực phân bổ','API-EXP-016':'Quyết định REJECTED hoặc POSTED theo chính sách đã duyệt; bản gốc bất biến'};
const ep=JSON.parse(fs.readFileSync(path.join(base,'api/endpoint-catalog.json'),'utf8'));
for(const e of ep.endpoints)if(fixes[e.id])e.response=fixes[e.id];
fs.writeFileSync(path.join(base,'api/endpoint-catalog.json'),JSON.stringify(ep,null,2));
edit('api/api-spec.md',s=>s.replace(/(### (API-EXP-014|API-EXP-015|API-EXP-016) — [\s\S]*?- Response data: )[^\n]+/g,(m,p,id)=>p+fixes[id]+'; thêm id, version, status, sourceRefs theo đối tượng.'));
edit('validation/summary.json',s=>{let d=JSON.parse(s);d.systemBlocked=4;d.systemNotRun=9;return JSON.stringify(d,null,2)});
// Give each screen concrete, source-aware fields without choosing unresolved policy.
const blocks={
 '01':'<label>Cơ sở <select aria-label="Cơ sở"><option>Cơ sở A · synthetic</option><option>Cơ sở B · synthetic</option></select></label><p>Kỳ thử K-A · Biên ngày và lịch khóa chưa chọn. Nút khóa chỉ được mở sau E13-Q02.</p>',
 '02':'<div class="grid"><label>Loại chi phí <select aria-label="Loại chi phí"><option value="">Chưa có danh mục duyệt</option></select></label><label>Khoản trực tiếp <input aria-label="Khoản trực tiếp" value="120000" readonly></label><label>Khách <input aria-label="Khách" value="Khách A · synthetic" readonly></label></div><p>Nguồn chứng từ synthetic DOC-A · Không trộn vào cost E3/E11.</p>',
 '03':'<div class="grid"><div>Người tham chiếu<br><strong>P-A · synthetic</strong></div><div>Ca dự kiến E11<br><strong>SHIFT-A / revision 1</strong></div><div>Giờ thực tế<br><strong>Chưa xác nhận</strong></div></div><p>Nguồn đơn giá: chưa có · Chi phí nhân công: chưa xác định.</p>',
 '04':'<label>Phương pháp đề xuất <select aria-label="Phương pháp đề xuất"><option value="">Chưa chọn — chờ Giám đốc</option></select></label><p>Người duyệt: chưa có · Bằng chứng: chưa có · Hiệu lực: chưa xác định. Mọi lựa chọn sẽ được review trong E13-Q05.</p>',
 '05':'<p><strong>E7:</strong> chưa gắn snapshot đối soát · <strong>E3/E11:</strong> chưa có manifest đủ nguồn · <strong>E10:</strong> giữ khóa khách và hợp đồng.</p><p>methodVersionRef: chưa có · Lần chạy: BLOCKED.</p>',
 '06':'<div class="grid"><div>Trực tiếp synthetic<br><strong>120.000 đ</strong></div><div>Lợi nhuận<br><strong>Chưa xác định</strong></div><div>Biên lợi nhuận<br><strong>Chưa xác định</strong></div></div><p>Nhân công chỉ được tổng hợp tại đây khi có nguồn. Không có dữ liệu người, giờ hoặc đơn giá trong báo cáo theo khách.</p>',
 '08':'<p>Bản gốc: ENTRY-A / snapshot K-A · synthetic</p><p>Điều chỉnh đề nghị: −20.000 đ · Kỳ đích: chưa chọn · Người duyệt: chưa có.</p>'
};
edit('html-wireframe/profit-workbench.html',s=>{for(const [id,block] of Object.entries(blocks))s=s.replace(new RegExp('(<section id="UI-EXP-'+id+'"[\\s\\S]*?<p class="state-message" role="status"></p>)'),'$1<div class="card">'+block+'</div>');return s.replaceAll('f.querySelector("input").value.trim()','f.querySelector(".review-note").value.trim()')});
// The primary note remains the validation control even with additional read-only fields.
edit('validation/check-ui-e13.cjs',s=>s.replaceAll("screen.locator('input')","screen.locator('.review-note')"));
console.log('Reviewed IDs, lifecycle responses, summary and screen fields.');
