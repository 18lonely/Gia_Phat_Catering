# Báo cáo kiểm tra use case và user flow Cost

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: kiểm tra tài liệu đạt; chờ review nghiệp vụ.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bàn giao nháp use case, luồng, truy vết và câu hỏi cần làm rõ |

## Đầu ra

- [16 use case và ma trận FR](../srs/usecase-diagram.md), từ UC-COST-001 đến UC-COST-016; mỗi use case có tác nhân, quyền, điều kiện, kết quả, luồng chính và ngoại lệ đánh số.
- [User flow](../ui/user-flow.md): 18 màn Cost đề xuất, tái sử dụng màn MENU, một điểm dịch vụ agent; 7 luồng chính và trạng thái Normal/Loading/Empty/Error/Offline.
- Tổng 10 sơ đồ Mermaid: 3 sơ đồ use case và 7 luồng thao tác.
- 45/45 FR của SRS có dòng truy vết: 43 FR có luồng nháp, 2 FR hoãn được chỉ rõ. Con số này là bao phủ diễn giải, không phải hoàn thành 95,6% sản phẩm.
- [SRS v0.1.2](../srs/spec.md), [epic v0.2.1](../epic-spec.md) và [overview v0.2.0](../../OVERVIEW.md) đã liên kết các đầu ra mới. SRS sửa mô tả cũ về số quy tắc (4 đăng ký mới, 4 có ở E2), ba trạng thái ngân sách và kiểu lưu kết quả tính theo ERD; không tự chốt câu hỏi nghiệp vụ.

## Kết quả kiểm tra

| Kiểm tra | Kết quả |
| :--- | :--- |
| Cấu trúc 16 use case | Đạt; các mục Cockburn chính hiện diện |
| Số bước và tham chiếu nhánh ngoại lệ | Đạt; các nhánh trỏ tới bước tồn tại |
| Mã FR/BR/ERR/NFR | Đạt; các mã dùng trong tài liệu mới có định nghĩa trong SRS Cost/MENU/nền tảng hoặc bảng quy tắc |
| Ma trận FR | Đạt; 45 dòng duy nhất, không bỏ sót; MEAL-007 và ALR-004 được đánh dấu hoãn |
| Liên kết file và anchor dùng trong use case/flow | Đạt |
| Mã câu hỏi luồng | Đạt; 10 mã FLOW-COST-Q01–Q10 có mục giải thích, không bị ghi như BR đã duyệt |
| Mermaid | 10/10 parse và render SVG thành công bằng Mermaid/Chrome headless |
| Xem trực quan mẫu | Đã xem sơ đồ use case nguồn giá và flow soạn/duyệt; nhãn và mũi tên đọc được |
| Rà luồng nhập bảng tính | Phân biệt nhập giá Cost không cần duyệt với giá bán E2 vào PENDING; kế thừa kiểm tệp/giao dịch, tối đa 2.000 dòng |
| Rà phân quyền | Không gán quyền ghi giá cho DDV; Bếp trưởng chỉ lượng theo cơ sở; agent phía khách chỉ một trạng thái, không có con số |

Kiểm tra tự động không chứng minh quy tắc nghiệp vụ đã đúng với thực tế Gia Phát. Không chạy kiểm thử chức năng backend hoặc nghiệm thu phần mềm trong đợt này.

## Những nhánh cần review ưu tiên

1. **Giá/tham số đổi trong thời gian chờ duyệt:** xác định kiểm lại tại duyệt cuối và bộ dữ liệu được chụp (FLOW-COST-Q06).
2. **Dự toán tuần có một ngày lỗi:** chọn lưu toàn bộ hoặc từng ngày; quy tắc hiện tại mới rõ tính nguyên tử của một bản ngày (Q07).
3. **Đọc khoản khoán và cảnh báo nguyên liệu:** bổ sung quyền đọc; xác định lưu/đóng cảnh báo giá cũ hoặc NCC ngừng (Q03/Q05).
4. **Huỷ tham chiếu tương lai và mất phản hồi lệnh ghi:** chốt lựa chọn giá thay thế và cơ chế chống gửi trùng trước thiết kế API (Q01/Q02).

Q04 là cách hiển thị khi mẫu số bằng 0; Q08 thuộc cảnh báo P1; Q09 trước tích hợp E9; Q10 thuộc mô phỏng P2. Mọi câu hỏi gốc trong SRS vẫn mở. Chưa tạo luồng cho ngoại lệ vượt ngưỡng và chặn chuyển bếp vì E3-Q9/Q10 chưa quyết.

## Chạy lại kiểm tra

```powershell
python D:/BA/docs/cost/validation/check-usecases.py
$costFlowCheckDir = Join-Path $env:TEMP 'gia-phat-cost-validation'
npm.cmd install --prefix $costFlowCheckDir --no-audit --no-fund mermaid playwright
node D:/BA/docs/cost/validation/check-diagrams.cjs $costFlowCheckDir
```

Script render dùng Chrome đã cài và lưu SVG/ảnh mẫu trong thư mục tạm. Không yêu cầu thêm dependency vào dự án sản phẩm. Bước tiếp theo là review điểm mở, đặc tả API và wireframe chi tiết; sau đó sinh backlog/AC và test case từ luồng đã chốt.
