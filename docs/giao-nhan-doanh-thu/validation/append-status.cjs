
const fs=require('fs'),path=require('path');const root=path.resolve(__dirname,'../../..'),base=path.join(root,'docs/giao-nhan-doanh-thu');
const targets=['docs/OVERVIEW.md','docs/project-dashboard.md','docs/gia-phat/review/progress-assessment.md','docs/gia-phat/review/next-session-prompt.md'];
const baseline=path.join(__dirname,'history-prefixes.json');
if(fs.existsSync(baseline))throw Error('Already appended; edit current E7 section directly.');
fs.writeFileSync(baseline,JSON.stringify(Object.fromEntries(targets.map(p=>[p,fs.readFileSync(path.join(root,p),'utf8')])),null,2));
for(const p of targets){
 const prefix=p.includes('/review/')?'../../giao-nhan-doanh-thu/':'giao-nhan-doanh-thu/';
 let text='\n\n## Mốc hiện hành — mở gói BA nháp E7, 12/11/2026\n\n';
 text+='Theo xác nhận người dùng 12/11/2026, mở **chỉ E7**; chỉ dẫn này thay phạm vi cũ “không mở E7–E13” đối với E7. E8–E13 chưa mở. E6 dừng chờ trả lời CG01/08/05/06, không hỏi lại/tự điền/đặc tả tiếp phần phụ thuộc;14/14 CG OPEN. Các mục phía trên là lịch sử và được giữ nguyên.\n\n';
 text+='[Preview E7]('+prefix+'preview.html) · [Bàn giao]('+prefix+'review/handoff.md) · [Câu hỏi]('+prefix+'review/questions.md) · [Phụ thuộc E6→E7]('+prefix+'review/dependencies.md) · [Kiểm tra]('+prefix+'validation/report.md).\n\n';
 text+='E7 FEAT-049→053:5/5 feature có thiết kế nháp có điều kiện,0 feature chỉ gate;13 FR/UC/story,39 AC và39 ca tương ứng,8 ca hệ thống có overlap,18 endpoint đề xuất,8 màn HTML,4 sơ đồ flow/state. FEAT-053 có preflight/provenance/luồng xuất, chưa mapping cột và chưa thử nhập MISA. Q-13 CHỜ TRẢ LỜI, cột trả lời trống; nhánh phụ thuộc BLOCKED. Không coi contract E6 đã freeze.\n\n';
 text+='Độ phủ tài liệu nháp **45/78≈57,7%** =23 E1–E5 +17 E6 +5 E7; tách riêng2 feature E6 gate-only O-03. Đây không phải BA được duyệt hoặc tiến độ phần mềm.65 bảng giữ nguyên;0 backend/migration/UAT. E6 vẫn99 mô tả ca overlap,0/14 CG đóng; E6-EVID-001/002, Cost/VAT/CK, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 và O-02/O-03/O-04 không đổi.\n';
 if(p.endsWith('next-session-prompt.md'))text+='\n### Prompt tiếp nối hiện hành\n\nTiếp tục BA tại D:\\BA, chỉ tài liệu. Đọc mục hiện hành ngày12/11/2026 này trước các prompt lịch sử; đọc AGENTS nếu có, skill phù hợp, OVERVIEW/dashboard, PRD/roadmap R7/G-Next, và docs/giao-nhan-doanh-thu/review/handoff.md, questions.md, dependencies.md, validation/report.md, SRS/API/RTM.\n\nE7 đã có gói nháp cho5 feature; tiếp tục chỉ khi có phản hồi/nguồn mới hoặc phát hiện sai lệch cụ thể. Ưu tiên đối chiếu mẫu nhập MISA chính thức, căn cứ số tính tiền, quy tắc kỳ/thu tiền nếu được cung cấp; đồng bộ đúng FR→UC→story→AC→API→UI→test, giữ phần thiếu BLOCKED. Không tự trả lời Q-13/E7-Q, không hỏi lại CG01/08/05/06 hoặc scope/C→S/S+C vượtT của E6. Không sửa producer E6 khi chưa có câu trả lời;14CG vẫnOPEN. Không mở E8–E13, không backend/migration. Không chạy build-e6.py/extend-e6.py/api-e6.py/finalize-e6.py hoặc ghi đè baseline/manifest/report/snapshot lịch sử. Không chạy lại author-e7.cjs (helper tạo bản đầu, không công cụ cập nhật).\n\nNếu sửa E7, dùng validation/check-e7.cjs và render-e7.cjs (output chỉ E7); chỉ chạy check-ui-e7.cjs và xem ảnh desktop/mobile nếu wireframe thay đổi. Báo file/kiểm/giới hạn; không coi mock PASS là runtime. Không gán ngày triển khai/story point/người phụ trách; giữ VAT cost gồm VAT phải trả NCC, invoice flag riêng, CK riêng không giảm tiền phải trả.\n';
 fs.appendFileSync(path.join(root,p),text);
}
console.log('Appended current dated E7 sections to4 files; history prefixes saved.');

