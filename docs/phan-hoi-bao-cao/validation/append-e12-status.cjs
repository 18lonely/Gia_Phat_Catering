// Append-only status update. Refuses to append twice or if old prefixes changed.
const fs=require('fs'),path=require('path'),crypto=require('crypto'),root=path.resolve(__dirname,'../../..');
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'baseline.json'),'utf8'));
const text=`

## Mốc hiện hành — gói BA nháp E12, 12/11/2026

Theo yêu cầu người dùng, chỉ mở tài liệu E12 — Phản hồi và báo cáo cho FEAT-079–087: 7 P1 và 2 P2. Chỉ dẫn lịch sử “E12/E13 chưa mở” được thay riêng đối với E12; E13/FEAT-088 chưa mở. Các mục phía trên giữ nguyên byte và là lịch sử.

[Preview E12](phan-hoi-bao-cao/preview.html) · [Bàn giao](phan-hoi-bao-cao/review/handoff.md) · [Câu hỏi](phan-hoi-bao-cao/review/questions.md) · [Phụ thuộc](phan-hoi-bao-cao/review/dependencies.md) · [Báo cáo kiểm](phan-hoi-bao-cao/validation/report.md).

9/9 feature có thiết kế nháp có điều kiện, 0 feature E12 chỉ gate. 20 FR / 20 UC / 20 story; 60 AC và 60 ca chức năng (23 BLOCKED, 37 NOT RUN). Có 12 ca hệ thống và 8 ca lỗi overlap (5 BLOCKED, 15 NOT RUN); 3 dòng R12 BLOCKED. 20 HTTP endpoint đề xuất và 7 port chỉ đọc/kiểm thuần; 12 màn HTML, 5 state và 2 flow. 18 câu E12-Q01–18 có cột Trả lời trống. Mọi ca sản phẩm NOT RUN hoặc BLOCKED, Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (65 + 9) / 78 = 74/78 ≈ 94,9 %**. Ba feature FEAT-046/047/063 chỉ gate O-03 ghi riêng, không cộng tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. R12 cần R6, R7, R10, R11 xong; chưa có bằng chứng. G-Next và R12 chưa nghiệm thu.

Tỷ lệ món chỉ từ lựa chọn thật E6, mẫu số chưa chọn, không suy từ sản xuất. Dashboard bốn vai trò có catalog nguồn/công thức/mẫu số/quyền; cost % ngày giữ định nghĩa E3, cost % theo khách chờ Q08. Bốn feature AI FEAT-082–085 chỉ công cụ đọc theo quyền người dùng tại tool/DB và đề xuất nháp chờ người thật duyệt; không tự ghi nghiệp vụ. FEAT-084 chỉ nối đọc E10, không sửa E10.

FEAT-086 là mục tiêu nhóm, công thức/ngưỡng chờ NUTR-Q01–04. FEAT-087 chỉ bữa đã ăn và giá trị dinh dưỡng của suất, tự nguyện/có đồng ý/xóa được; không thu, suy luận hoặc lưu sức khỏe và không gợi ý cá nhân. Thiết kế độc lập không dùng FEAT-046/047; mở rộng sang hồ sơ/gợi ý chỉ gate O-03. Identity, bằng chứng đã ăn và retention còn chờ, không suy đã ăn từ lựa chọn/giao nhận.

Cost nguyên liệu gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất riêng theo đơn, không giảm phải trả NCC và không tự trừ tiền khách. NFR-COST-002 giữ ≤ 1 đ cho cost món và ≤ 0,01 điểm phần trăm cho cost % ngày; BO-02 ≤ 3 điểm phần trăm thuộc mục tiêu R11. FR-MENU-RCP-007/O-02 và FEAT-046/047/063/O-03 vẫn chặn.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp producer đang chờ.

Baseline chụp 945 file cũ trước viết E12; schema giữ 65 bảng. Chỉ hai tổng quan được append; kết quả bốn checker và ảnh desktop/mobile tại báo cáo E12. Không backend, migration, gọi mô hình AI, system prompt thật, chọn nhà cung cấp/model AI, commit hoặc xóa file.
`;
const drift=JSON.parse(fs.readFileSync(path.join(__dirname,'pre-append-drift.json'),'utf8'));
for(const rel of ['docs/OVERVIEW.md','docs/project-dashboard.md']){const p=path.join(root,rel),bytes=fs.readFileSync(p),entry=drift.files.find(f=>f.path===rel);if(bytes.toString('utf8').includes('## Mốc hiện hành — gói BA nháp E12'))throw Error('E12 milestone already exists: '+rel);if(bytes.length!==entry.observedBytes||crypto.createHash('sha256').update(bytes).digest('hex')!==entry.observedSha256)throw Error('File changed again before append: '+rel);fs.appendFileSync(p,text,'utf8')}
console.log('Appended E12 milestone to two overviews; old bytes retained.');
