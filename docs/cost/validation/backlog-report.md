# Báo cáo kiểm tra backlog, AC và test Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft, chưa nghiệm thu nghiệp vụ.

## Kết quả

| Hạng mục | Kết quả kiểm tra tài liệu |
| :--- | :--- |
| User story | 28; giữ P0/P1/P2 theo từng FR nguồn; điểm sơ bộ chờ đội dev ước lượng |
| AC / test case | 108 cặp tương ứng; mỗi story ít nhất 3 kịch bản |
| FR | 43/43 yêu cầu có luồng được gắn story/AC/test; 2 FR hoãn ghi riêng, không tạo test thành công giả |
| Quy tắc dữ liệu/tính toán | 24/24 BR-PRC, BR-CALC, BR-EST có ca tham chiếu trực tiếp |
| Lỗi | 14/14 mã ERR-COST của SRS và 6/6 mã API bổ sung đề xuất có ca |
| Phi chức năng | 8/8 NFR Cost có ca: hiệu năng, đối soát kế toán, quyền dữ liệu, log, decimal |
| Trạng thái thực thi | 62 NOT RUN; 46 BLOCKED do quyết định, dữ liệu hoặc môi trường; 0 test phần mềm đã chạy |

Kiểm cấu trúc bằng [check-backlog.py](check-backlog.py): mã không trùng, FR khớp nguồn, ưu tiên không đổi, mỗi scenario có Given/When/Then, liên kết file tồn tại. Kiểm này không chứng minh thuật toán hay backend hoạt động đúng, và không phải BA/QA ký duyệt checklist.

```powershell
python docs/cost/validation/check-backlog.py
```

[build-backlog.py](build-backlog.py) chứa các scenario được biên soạn để tái tạo bộ Markdown và [catalog](../test/scenario-catalog.json). Nếu sửa nội dung, sửa nguồn này rồi chạy lại cả hai script để giữ các tài liệu đồng bộ.

## Điểm mới cần review

**QA-COST-Q01 — mã lỗi NCC ngừng:** `ERR-COST-404-01` mô tả nguyên liệu/NCC không tồn tại hoặc không còn dùng; `ERR-COST-422-02` cũng mô tả NCC đã ngừng. Cả hai đều cấm nhập giá mới, nhưng mã trả về cho NCC tồn tại ở INACTIVE chưa nhất quán. BA/Tech lead cần chọn mã chính thức và đồng bộ SRS/API; ca TC-COST-002-06 giữ BLOCKED. Báo cáo không tự thay hợp đồng đã viết.

Các ca chờ Q04 (tỷ trọng/delta khi mẫu số 0), Q06 (giá đổi khi PENDING), Q07 (giao dịch dự toán tuần), Q09 (ngân sách vừa vượt vừa thiếu), E3-Q15/Q16 (nhiều món chính/hiệu lực bảng đặc thù) không có kết quả số tự đặt. P1/P2 giữ đúng ưu tiên; ngoại lệ CHAN và chặn chuyển bếp vẫn hoãn.

Có test hồi quy các quy tắc BR-COST-008/009/010/012 thuộc MENU; không tuyên bố Cost hiện thực lại các quy tắc này. Test bảo mật bao gồm người sửa cuối không tự duyệt, dữ liệu tiền trong lỗi/nested field/tệp xuất và phạm vi cơ sở. Wireframe hiện có chỉ hỗ trợ review một phần các luồng, không đủ làm môi trường chạy bộ này.

## Tài liệu bàn giao và việc tiếp theo

- [Backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md).
- [Checklist](../test/checklist.md), [test case](../test/test-cases.md), [ma trận truy vết](../test/traceability.md).
- BA/QA review checklist và các oracle; chủ sở hữu trả lời điểm mở; Tech lead review API, concurrency, outbox và migration.
- Kế toán cung cấp 10 món/10 ngày đối soát và cấu hình đi kèm; QA chuẩn bị môi trường/fixture, chạy test và lưu evidence. Chưa có lịch hoặc cam kết công sức được phê duyệt.

Phần trăm bao phủ SRS toàn sản phẩm/MVP không thay đổi trong đợt này; bổ sung chiều sâu tài liệu Cost không tương đương tăng tỷ lệ phần mềm đã hoàn thành.
