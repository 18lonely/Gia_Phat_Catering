// Chỉ nối thêm hai file được phép, kiểm hash trước ghi và không chạy lặp.
const fs=require('fs'),path=require('path'),crypto=require('crypto');const root=path.resolve(__dirname,'../../..'),baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'baseline.json'))),sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const marker='## Mốc hiện hành — gói BA nháp E10, 12/11/2026';
const text=`\n\n${marker}

Theo yêu cầu người dùng ngày 12/11/2026, chỉ mở tài liệu E10 — CRM và bán hàng cho FEAT-070–073, đều P1. Chỉ dẫn lịch sử “E10–E13 chưa mở” được thay đối với E10; E11–E13 vẫn chưa mở. FEAT-084 không có đặc tả hoặc công cụ AI mới. Các mục phía trên giữ nguyên là lịch sử.

[Preview E10](crm-ban-hang/preview.html) · [Bàn giao](crm-ban-hang/review/handoff.md) · [Câu hỏi](crm-ban-hang/review/questions.md) · [Phụ thuộc](crm-ban-hang/review/dependencies.md) · [Báo cáo kiểm](crm-ban-hang/validation/report.md).

E10 có 4/4 feature thiết kế nháp có điều kiện, 0 feature chỉ gate; 16 FR tương ứng 16 UC và 16 story; 48 AC tương ứng 48 ca chức năng (21 BLOCKED, 27 NOT RUN). 10 ca hệ thống có overlap (5 BLOCKED, 5 NOT RUN), không cộng vào tỷ lệ nghiệm thu. 23 HTTP endpoint và 7 port logic đề xuất; 9 màn trong một HTML, 4 sơ đồ trạng thái và 2 sơ đồ luồng đã render SVG/HTML. 15 câu E10-Q01–15 giữ CHỜ TRẢ LỜI, cột trả lời trống.

Độ phủ **thiết kế tài liệu nháp 60/78 ≈ 76,9%** = 23 E1–E5 + 17 E6 + 5 E7 + 6 E8 + 5 E9 + 4 E10. Ba feature chỉ gate FEAT-046/047/063 ghi riêng, không tính vào độ phủ. Đây không phải BA được duyệt, công sức hoặc tiến độ phần mềm. Mở tài liệu E10 không miễn G-Next; R10 chưa nghiệm thu. Nguồn E1–E9 vẫn nháp, không cố định hợp đồng giao tiếp.

Hồ sơ 360° ghi trạng thái thiếu nguồn riêng; không tự tính doanh thu từ số giao. Tiêu chí phát hiện trùng chưa chọn; gộp phải có người duyệt và hoàn tác có lịch sử. Vòng đời/nguy cơ rời theo lịch từng điểm, chưa đặt ngưỡng. Báo giá có phiên bản, bản khách không chứa cost hoặc biên lợi nhuận. Hợp đồng/phụ lục có giá theo loại suất, khoảng hiệu lực không chồng, không ghi đè pricing snapshot lịch sử.

Baseline chụp toàn bộ 763 file cũ trước khi viết E10; mọi file cũ ngoài hai tổng quan này được yêu cầu giữ nguyên SHA256. Hai tổng quan chỉ append, giữ nguyên byte prefix cũ; kết quả cuối tại báo cáo kiểm. PRD/roadmap không sửa hoặc append vì E9 không append hai file đó. Schema 65 bảng giữ nguyên; dữ liệu mới chỉ đề xuất. Đã kiểm cấu trúc/truy vết/liên kết, render và UI mock ở 1440, 390, 360 px; kiểm mock không thay test sản phẩm.

Các câu vẫn chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04. Không hỏi lại hoặc tự trả lời, không đặc tả tiếp producer đang chờ. E8-Q06 và E9-Q06 vẫn chặn bàn giao lead/đề xuất thật; E10 không tự được coi là đầu nhận đã duyệt.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không VAT 0%. CK% và tiền suất riêng theo đơn không giảm số phải trả nhà cung cấp; không tự khấu trừ số khách phải trả. NFR-COST-002 giữ nguyên. Không backend, migration, gọi mô hình AI hoặc UAT; không commit hoặc xóa file.
`;
for(const p of baseline.appendAllowed){const f=baseline.files.find(f=>f.path===p),raw=fs.readFileSync(path.join(root,p));if(raw.toString('utf8').includes(marker))throw Error('Đã append, không chạy lặp: '+p);if(raw.length!==f.bytes||sha(raw)!==f.sha256)throw Error('Nguồn đổi trước append: '+p);}
for(const p of baseline.appendAllowed)fs.appendFileSync(path.join(root,p),text,'utf8');console.log('Đã append OVERVIEW và project-dashboard; không sửa lịch sử.');
