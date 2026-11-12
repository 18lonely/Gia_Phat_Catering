const fs=require('fs'),path=require('path'),crypto=require('crypto'),root=path.resolve(__dirname,'../../..');
const baseline=JSON.parse(fs.readFileSync(path.join(__dirname,'baseline.json'),'utf8'));
const text=`

## Mốc hiện hành — gói BA nháp E13, 12/11/2026

Theo yêu cầu người dùng, mở riêng tài liệu E13 — Chi phí và lợi nhuận cho FEAT-088, EXP / M10, P2, PER-07/PER-08. Chỉ dẫn lịch sử “E13 chưa mở” được thay đối với E13; mọi byte trước mục này giữ nguyên là lịch sử. Đây là epic cuối theo PRD; việc tiếp theo là review/chốt câu hỏi với stakeholder trên bằng chứng, không coi các release đã nghiệm thu.

[Preview E13](chi-phi-loi-nhuan/preview.html) · [Bàn giao](chi-phi-loi-nhuan/review/handoff.md) · [Câu hỏi](chi-phi-loi-nhuan/review/questions.md) · [Phụ thuộc](chi-phi-loi-nhuan/review/dependencies.md) · [Báo cáo kiểm](chi-phi-loi-nhuan/validation/report.md).

1/1 feature có thiết kế nháp có điều kiện; 0 feature E13 chỉ gate. 12 FR / 12 UC / 12 story; 36 AC và 36 ca chức năng (16 BLOCKED, 20 NOT RUN). Có 13 ca hệ thống overlap (4 BLOCKED, 9 NOT RUN), 4 dòng R13 BLOCKED; 18 endpoint đề xuất, 5 port ranh giới; 8 màn, 5 state và 2 flow. 14 câu E13-Q01–14 có cột Trả lời trống. Mọi ca sản phẩm NOT RUN hoặc BLOCKED, Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (74 + 1) / 78 = 75/78 ≈ 96,2 %**. FEAT-046/047/063 chỉ gate O-03 ghi riêng, không cộng tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. R13 cần R7, R11 xong và Giám đốc duyệt nguyên tắc phân bổ chi phí; chưa có bằng chứng, R13/G-Next chưa nghiệm thu.

Chưa chọn phương pháp phân bổ: phương pháp là dữ liệu có phiên bản/người duyệt; chưa có bản duyệt thì lợi nhuận khách BLOCKED, chỉ xem chi phí trực tiếp. Mọi báo cáo giữ phiên bản phương pháp và nguồn. Đối chiếu từng cơ sở có phần chưa phân bổ và chênh lệch riêng; cầu nối khớp khi còn phần chưa phân bổ chưa đủ R13. Không giấu phần dư vào khách nào. Doanh thu lấy E7 đã đối soát; cost nguyên liệu giữ nguồn E3/E11, không định nghĩa lại.

Chấm công chỉ phục vụ chi phí nhân công theo người/cơ sở/ca/giờ/nguồn đơn giá; không tính lương, bảo hiểm hoặc thuế TNCN. Chi tiết lương chỉ PER-07/PER-08 theo quyền tối thiểu; báo cáo khách nội bộ chỉ tổng hợp, tài liệu gửi khách không có lợi nhuận/biên lợi nhuận. Kỳ khóa không ghi đè; điều chỉnh là bút toán riêng có lý do và người duyệt, chưa chọn kỳ đích/người cụ thể.

Cost nguyên liệu gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả NCC hoặc tự giảm phải trả khách. NFR-COST-002 giữ ≤ 1 đ và ≤ 0,01 điểm phần trăm; BO-01 ≤ 52 % và BO-02 ≤ 3 điểm phần trăm là mục tiêu kinh doanh. FR-MENU-RCP-007/O-02 và FEAT-046/047/063/O-03 giữ gate.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại hoặc tự đặc tả tiếp producer đang chờ.

Baseline E13 chụp 1070 file cũ, lần đối chiếu ngay sau không phát hiện thay đổi. Bốn checker và ảnh desktop/mobile tại báo cáo E13; hai tổng quan chỉ append, schema giữ 65 bảng. Không sửa bằng chứng hash lịch sử E12. Không backend, migration, gọi mô hình AI, commit hoặc xóa file.
`;
const targets=['docs/OVERVIEW.md','docs/project-dashboard.md'];
// Check both files before writing either one.
for(const rel of targets){const bytes=fs.readFileSync(path.join(root,rel)),e=baseline.files.find(f=>f.path===rel);if(bytes.toString('utf8').includes('## Mốc hiện hành — gói BA nháp E13'))throw Error('Milestone already exists; refuse duplicate');if(bytes.length!==e.bytes||crypto.createHash('sha256').update(bytes).digest('hex')!==e.sha256)throw Error('Concurrent drift before append: '+rel)}
for(const rel of targets)fs.appendFileSync(path.join(root,rel),text,'utf8');
console.log('Appended E13 to exactly two overview files; baseline prefixes preserved.');
