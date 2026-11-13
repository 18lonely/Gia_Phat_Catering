# Bàn giao E9 ngày 12/11/2026

## Gói này gồm gì

E9 mô tả Agent Dinh dưỡng viên cho khách dựng thực đơn tập thể, xem/giải thích, chỉnh và kiểm lại, gửi đề xuất cho Gia Phát, cùng kiểm soát lượt/ngân sách và ranh giới dữ liệu. FEAT-063 chỉ mô tả gate đóng cho gợi ý cá nhân; không có thuật toán, hồ sơ sức khỏe hoặc luồng mở.

Candidate là phương án nháp có revision/hash, chưa phải MENU. Proposal là đề xuất chờ người thật; receipt chứng minh tiếp nhận, không chứng minh duyệt/áp dụng. Reservation là ngân sách AI giữ chỗ, khác cost thực phẩm.

## Đọc theo thứ tự nào

1. Đọc [Epic](../epic-spec.md) và [SRS](../srs/spec.md) để phân biệt phạm vi có điều kiện với gate-only.
2. Theo [Preview](../preview.html) tới sổ câu hỏi, phụ thuộc và UC; chú ý nguồn producer đều là nháp, chưa freeze.
3. Đọc [API/tool allowlist](../api/api-spec.md) và [Mapping](../api/data-mapping.md) để hiểu biên công cụ, quyền, public projection, admission và receipt.
4. Dùng [RTM](../test/traceability.md) để lần từ FR qua story/AC tới ca kiểm. [Báo cáo kiểm](../validation/report.md) là bằng chứng tài liệu/mock lịch sử, không thay kiểm sản phẩm.

## Số liệu chính

- 6 feature đúng phạm vi PRD: 5/6 feature P0 có thiết kế nháp có điều kiện; 1/6 là FEAT-063 P1 chỉ gate.
- 13 FR tương ứng 13 UC và 13 story; 39 AC tương ứng 39 ca chức năng, gồm 12 BLOCKED và 27 NOT RUN.
- 13 ca hệ thống có overlap với mục tiêu chức năng; không cộng thành số mục tiêu độc lập hoặc tỷ lệ nghiệm thu.
- 11 HTTP endpoint và 4 control port đề xuất; 7 màn HTML, 3 sơ đồ trạng thái và 2 sơ đồ luồng.
- Toàn dự án có 56/78 feature thiết kế nháp ≈ 71,8%; 3 feature chỉ gate FEAT-046/047/063 được ghi riêng. Đây không phải BA được duyệt, effort hay tiến độ phần mềm.
- 14/14 câu E9-Q01–14 để trống trả lời; không có backend, migration hoặc lời gọi mô hình AI trong gói.

## Những điểm người review cần quyết định

- E9-Q01: Provider/model, hạ tầng, vùng xử lý và đường chuyển dữ liệu theo O-04.
- E9-Q02: Nhóm người dùng được phép, xác minh identity và gắn quyền/nhóm từ server.
- E9-Q03: Danh mục khẩu vị/kiêng kỵ, giới hạn và xử lý nội dung tự do có sức khỏe.
- E9-Q04: Có hiển thị giá suất không và nguồn/hiệu lực/nhãn giá được duyệt.
- E9-Q05: Phản hồi nhánh không đạt ngưỡng kinh tế mà không lộ lý do cost.
- E9-Q06: Nơi nhận nháp, người nhận/duyệt, trạng thái khách thấy và receipt; chưa mở CRM E10.
- E9-Q07: Định nghĩa lượt, nhóm, cửa sổ/reset, cap ngày, đơn vị/tỷ giá/múi giờ và chạm trần.
- E9-Q08: Quyền xem/sửa/duyệt hạn mức, hiệu lực và xử lý lượt đang chạy.
- E9-Q09: Bộ 30 yêu cầu thực đơn, 20 câu dò cost, 20 câu bệnh lý; oracle/rubric và lời nhắc bắt buộc.
- E9-Q10: Consent, lưu/xóa hội thoại, quyền xem và bản sao/log/provider.
- E9-Q11: Quan hệ bộ dựng E8 với E9 và contract kiểm nguồn/quy tắc/public.
- E9-Q12: Điều kiện nguồn public, xử lý thiếu/stale/thu hồi, ngày phục vụ và nhiều cỡ.
- E9-Q13: Idempotency, TTL, retry/deadline/concurrency, receipt, quota/ledger và profile tải.
- E9-Q14: Điều kiện xem xét mở FEAT-063 sau O-03/FEAT-046/047 và quyền dùng của người ăn qua QR.

## Giới hạn

Chưa chọn provider/model, quota, giá token, retention, đầu nhận hoặc giá suất; không viết system prompt hay chạy mô hình. UI là mock synthetic. Không thu/suy luận dữ liệu sức khỏe; nội dung lời nhắc bệnh lý hiện chỉ placeholder chờ xác nhận. FEAT-061 phải kiểm lại E2 toàn tuần sau chỉnh; FEAT-062 chỉ gửi đề xuất, không áp dụng; FEAT-065 kiểm quyền/công cụ/DB/projection, không chỉ dựa prompt.

E6 CG01/08/05/06, E7 Q-13/E7-Q01–08 và E8-Q01–12 vẫn chờ; 14/14 CG OPEN, E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04, AIO-Q01–06, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 không đóng. Cost gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn không phải VAT 0%; CK riêng theo đơn không giảm tiền khách phải trả. E10–E13 chưa mở.

## Việc tiếp theo

Review các điểm mở và bằng chứng nguồn; chỉ sửa chuỗi FR → UC → story → AC → API → UI → test khi có phản hồi có căn cứ hoặc sai lệch cụ thể. Không đặc tả tiếp producer đang chờ hoặc mở feature mới. Checker phiên thay checker E9 cũ sau chỉnh hash E7/E8; kết quả artifact không thay test sản phẩm.
