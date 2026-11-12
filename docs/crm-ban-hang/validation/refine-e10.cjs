// Làm rõ giao tiếp và bổ sung truy vết quy tắc; chỉ thay tài liệu E10.
const fs=require('fs'),path=require('path'),base=path.resolve(__dirname,'..');
const edit=(p,f)=>fs.writeFileSync(path.join(base,p),f(fs.readFileSync(path.join(base,p),'utf8')));
edit('api/api-spec.md',s=>s.replace('quoteRef, baseRevision, lines:[','quoteRef/baseRevision bắt buộc khi sửa, vắng cả hai khi tạo lần đầu; lines:['));
edit('html-wireframe/crm-workbench.html',s=>s.replace("document.querySelector('#scenario').value='sample';state()","document.querySelector('#scenario').value='sample';state();const active=document.querySelector('nav [data-go=\"'+id+'\"]');active.scrollIntoView({block:'nearest',inline:'center'})").replace('</footer><script>','</footer><script>'));
const coverage=`
## Truy vết quy tắc và lỗi bổ sung

Các dòng sau chỉ liên kết lại ca đã có, không tạo thêm ca hoặc AC.

| Quy tắc | Ca kiểm có mục tiêu tương ứng |
| :--- | :--- |
| BR-CRM-001 | TC-CRM-001-03; TC-CRM-S001 |
| BR-CRM-002 | TC-CRM-001-02; TC-CRM-008-02 |
| BR-CRM-003 | TC-CRM-004-02; TC-CRM-005-01/02 |
| BR-CRM-004 | TC-CRM-006-01/02/03; TC-CRM-S004 |
| BR-CRM-005 | TC-CRM-007-02; TC-CRM-008-01/02; TC-CRM-S007 |
| BR-CRM-006 | TC-CRM-010-01/03; TC-CRM-011-03 |
| BR-CRM-007 | TC-CRM-012-01/02/03; TC-CRM-S002 |
| BR-CRM-008 | TC-CRM-014-01/02/03; TC-CRM-S005 |
| BR-CRM-009 | TC-CRM-015-02; TC-CRM-016-03; TC-CRM-S006 |
| BR-CRM-010 | TC-CRM-S003; TC-CRM-016-02 |
| BR-CRM-011 | TC-CRM-003-03; TC-CRM-010-03; TC-CRM-015-03; TC-CRM-S004 |
| BR-CRM-012 | TC-CRM-003-02; TC-CRM-004-02; TC-CRM-006-02 |

| Lỗi | Ca kiểm / nhánh |
| :--- | :--- |
| ERR-CRM-400-01 | TC-CRM-010-02: trường người duyệt/tổng ngoài schema |
| ERR-CRM-401-01 | TC-CRM-S001: phiên thiếu/hết hạn trước kiểm phạm vi |
| ERR-CRM-403-01 | TC-CRM-005-02; TC-CRM-012-03 |
| ERR-CRM-404-01 | TC-CRM-001-03; TC-CRM-012-03 |
| ERR-CRM-409-01 | TC-CRM-005-03; TC-CRM-010-03; TC-CRM-013-02 |
| ERR-CRM-409-02 | TC-CRM-003-03: cùng định danh nguồn, khác hash |
| ERR-CRM-409-03 | TC-CRM-014-02; TC-CRM-016-02 |
| ERR-CRM-422-01 | TC-CRM-006-02; TC-CRM-009-02; TC-CRM-013-03 |
| ERR-CRM-500-01 | TC-CRM-S004: lỗi ghi/audit trước hoặc sau commit, chưa xác định kết quả |
| ERR-CRM-503-01 | TC-CRM-003-02; TC-CRM-006-02 khi policy chưa đủ |
`;
edit('test/traceability.md',s=>s.includes('## Truy vết quy tắc và lỗi bổ sung')?s:s+coverage);
edit('test/system-cases.md',s=>s.replace('Đổi customerRef, publicationRef và cache key','Dùng phiên thiếu/hết hạn; đổi customerRef, publicationRef và cache key').replace('Lỗi trước/sau commit; hai người duyệt','Chèn lỗi ghi/audit trước/sau commit, kiểm ERR-CRM-500-01 và không xác nhận thành công giả; hai người duyệt'));
const note=`
## Các hành động chuyển trạng thái chưa có wire contract riêng

Ma trận trạng thái thể hiện các sự kiện nghiệp vụ để review, không khẳng định mọi cạnh đã có route runtime. Gửi/trả duyệt, chấp thuận/thu hồi/hết hạn báo giá và chấm dứt hợp đồng còn E10-Q08/10/13; không tự tạo endpoint hoặc chọn tác vụ nền khi chưa có quyết định. API-CRM-012 chỉ tạo bản phát hành sau kiểm bằng chứng duyệt, không thay toàn bộ quy trình duyệt. API-CRM-014 nhận amendmentRef/amendmentVersion khi kích hoạt một phụ lục thuộc hợp đồng; áp cùng kiểm nguyên tử và hiệu lực với bộ giá đầu. Phần workflow chưa đủ contract giữ BLOCKED, không tính route chưa tồn tại vào catalog.
`;
edit('api/api-spec.md',s=>s.includes('## Các hành động chuyển trạng thái chưa có wire contract riêng')?s:s+note);
console.log('Đã bổ sung ranh giới workflow, tạo báo giá lần đầu và truy vết BR/ERR.');
