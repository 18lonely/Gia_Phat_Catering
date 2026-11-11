# Rà soát khoảng trống tài liệu Cost

Phiên bản 0.1.0 · Ngày 11/11/2026 · Người rà soát: BA · Draft.

Phạm vi: SRS v0.1.4, API v0.1.0, use case/user flow, wireframe v0.1.0 và 108 kịch bản kiểm thử. Đây là rà soát tài liệu và bản mô phỏng; không phải kiểm toán code hay kết quả chạy backend.

| Mã phát hiện | Nguồn và bằng chứng | Ảnh hưởng | Đề xuất / trạng thái |
| :--- | :--- | :--- | :--- |
| GAP-COST-01 | [SRS ma trận lỗi](srs/spec.md): 404-01 và422-02 cùng nói NCC không còn dùng/đã ngừng | Cao: client và test chưa có mã trả về duy nhất | QA-COST-Q01 trong [sổ quyết định](review/decision-register.md); đề xuất422 cho INACTIVE đang chờ review |
| GAP-COST-02 | [Flow Q06](ui/user-flow.md): giá/params thay khi MENU PENDING | Cao: bộ số được chụp tại duyệt chưa xác định | Quyết định chính sách kiểm lại và trạng thái khi không đạt; chưa đổi snapshot contract |
| GAP-COST-03 | [Flow Q07](ui/user-flow.md), API batch chưa có success contract cuối | Cao: lưu một phần tuần và retry có thể khác kỳ vọng | Review giao dịch cả batch/ngày, failure payload, key và version trước code |
| GAP-COST-04 | [API mục7](api/api-spec.md): version bảng tính/khoản khoán và request store chưa có schema | Cao: chống gửi lặp/cạnh tranh mới là đề xuất | Tech lead review migration, claim key, atomic commit, outbox và retry; chưa coi DBML đã hỗ trợ |
| GAP-COST-05 | Flow Q03: cảnh báo nguyên liệu khác cảnh báo ngày thực đơn | Cao: thiếu nơi lưu/khóa chống trùng/vòng đời | Chốt identity/scope/close event trước khi thêm bảng hoặc mở rộng notifications |
| GAP-COST-06 | E3-Q16, Q05 và E3-Q11: hiệu lực bảng đặc thù/quyền đọc còn mở | Cao: người dùng có thể hiểu nhầm quyền/điều kiện đủ | Review ma trận quyền và ví dụ89/90/91ngày, cơ sở A/B; giữ test phụ thuộc BLOCKED |
| GAP-COST-07 | NFR-COST-002 yêu cầu bảng tính kế toán; workspace mới có fixture giả | Cao: chưa có oracle thực tế độc lập | Đã tạo [phiếu cung cấp](review/accountant-input.md); vẫn chờ dữ liệu có nguồn và xác nhận |
| GAP-COST-08 | [108 test case](test/test-cases.md): có RBAC/redaction/schema tests, chưa có bộ ca chuyên biệt SQL injection/stored XSS qua tên/ghi chú và tệp xuất | Trung bình: coverage chưa bao trùm mọi kiểu đầu vào độc hại | QA bổ sung sau thiết kế backend/UI: chuỗi SQL không thay logic truy vấn; HTML/JS hiển thị như dữ liệu, không thực thi; không cấm toàn bộ dấu tiếng Việt/ký tự đặc biệt |
| GAP-COST-09 | Wireframe chỉ giữ dữ liệu bộ nhớ, import/export giả; test tài liệu không gọi dịch vụ | Cao nếu nhầm là đã triển khai | Đã ghi giới hạn trong [hướng dẫn](html-wireframe/README.md); cần môi trường thật để chạy chức năng và lỗi mạng/timeout |
| GAP-COST-10 | Q04 mẫu số0; Q09 vừa vượt vừa không tính được | Trung bình/Cao: oracle số/trạng thái chưa chốt | Đề xuất — cho tỷ lệ không áp dụng; thảo luận ưu tiên KHONG_XAC_DINH; chưa ghi thành BR đã duyệt |

## Đã chuẩn bị trong đợt này

- [Sổ32 điểm mở](review/decision-register.md) có chủ sở hữu theo vai trò và đề xuất review; O-01 đã PARTIALLY_CONFIRMED theo phiên kế toán, các phần chưa chốt giữ mở.
- [Bảng46 ca BLOCKED](review/blocked-tests.md) tách điều kiện và bằng chứng mở khóa.
- [10 món/10 ngày mẫu](test/fixtures/README.md) kiểm số học bằng Decimal; các giá trị là giả định.
- [Gói bàn giao](review/handoff.md) có phiếu quyết định, điều kiện triển khai/UAT và mẫu evidence.

Các việc trên hoàn thiện vật liệu review, không tự giải quyết điểm nghiệp vụ, không có chữ ký nghiệm thu và không làm thay đổi 62 NOT RUN/46 BLOCKED của bộ test hiện tại.

## Cập nhật kế toán

[CR-COST-2026-001](cr/CR-COST-2026-001.md) bổ sung xác nhận giá cost gồm VAT phải trả và chiết khấu ghi riêng. Đồng thời phát hiện tiêu chí đối soát1% trong epic chưa khớp1đ/0,01 điểm phần trăm trong SRS; cần thống nhất baseline trước nghiệm thu. API/schema/wireframe hiện tại chưa đủ bao phủ phần bổ sung, dù các điểm đã xác nhận không còn là giả định.
