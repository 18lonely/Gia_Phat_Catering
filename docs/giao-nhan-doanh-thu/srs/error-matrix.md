---
id: DOC-E7-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| Mã | HTTP | Trigger / log reason | UI message | Localization key | Severity | Next action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-E7-401-01 | 401 | Phiên không hợp lệ | Phiên hết hạn. Đăng nhập lại. | e7.auth_required | High | Đăng nhập, không tự gửi lại lệnh |
| ERR-E7-403-01 | 403 | Thiếu quyền/link không hợp lệ/tự duyệt | Không đủ quyền xác nhận thao tác. | e7.forbidden | High | Kiểm quyền, không hiện secret |
| ERR-E7-404-01 | 404 | Không tồn tại hoặc ngoài scope | Không tìm thấy dữ liệu. | e7.not_found | Medium | Kiểm phạm vi |
| ERR-E7-409-01 | 409 | Version/nguồn đã thay | Dữ liệu đã đổi. Tải lại và đối chiếu. | e7.stale_version | High | Không tự ghi đè |
| ERR-E7-503-01 | 503 | Nguồn không sẵn sàng/policy chưa chốt | Chưa đủ điều kiện xử lý. | e7.dependency_blocked | High | Hiện gate, không điền 0 |
| ERR-DLV-422-01 | 422 | Suất âm/không nguyên hoặc sai tham chiếu | Kiểm tra số suất và phiếu nguồn. | e7.invalid_quantity | Medium | Sửa dữ liệu |
| ERR-DLV-422-02 | 422 | Thiếu bằng chứng/thỏa thuận | Chưa đủ bằng chứng để thống nhất. | e7.agreement_missing | Medium | Giữ nháp |
| ERR-FIN-422-01 | 422 | Thiếu căn cứ số tính tiền/giá/VAT | Chưa xác định được doanh thu. | e7.pricing_unresolved | High | Kiểm nguồn |
| ERR-FIN-422-02 | 422 | Kỳ/biên bản/lý do/điều kiện khóa sai | Kiểm tra điều kiện đối soát và lý do. | e7.period_invalid | Medium | Rà dòng chặn |
| ERR-FIN-422-03 | 422 | Tiền thu sai hoặc chứng từ trùng | Kiểm tra số tiền và chứng từ thu. | e7.receipt_invalid | Medium | Đối chiếu trước gửi lại |
| ERR-FIN-409-02 | 409 | Ghi ảnh hưởng kỳ khóa | Kỳ đã khóa. Cần Giám đốc duyệt mở lại. | e7.period_locked | High | Lập yêu cầu |
| ERR-FIN-422-04 | 422 | Thiếu mẫu/mapping MISA | Chưa có mẫu nhập MISA được xác nhận. | e7.template_missing | High | Không xuất file giả |
| ERR-E7-500-01 | 500 | Lỗi xử lý/kết quả chưa rõ | Chưa xác định kết quả. Đối chiếu trước thử lại. | e7.unexpected | High | Tra requestId, không ghi lặp |

Mã đề xuất consumer E7, không đổi E6. Log không chứa token/upstream body. 503 hiển thị mã gate, không là quyền thay policy.
