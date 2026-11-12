---
id: DOC-E13-USECASES-UC-EXP-008-MD
title: UC-EXP-008 — Tra cứu lợi nhuận theo khách
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-EXP-008 — Tra cứu lợi nhuận theo khách

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

- **Phạm vi**: E13 / FEAT-088; P2; FR-EXP-PROF-001.
- **Cấp độ**: Sea level.
- **Tác nhân chính**: PER-07/PER-08.
- **Bên liên quan và kỳ vọng**: Kế toán cần truy nguồn; Giám đốc cần đối chiếu; người lao động cần bảo vệ chi tiết lương; khách không nhận lợi nhuận nội bộ.
- **Tác nhân hỗ trợ**: Nền E1 kiểm quyền và audit; nguồn E3/E7/E10/E11 chỉ đọc theo scope.
- **Tiền điều kiện**: Đăng nhập, quyền đúng cơ sở và hành động. Nhánh thành công phụ thuộc chính sách chỉ dùng khi có bằng chứng E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15; chưa có thì đi nhánh 3b.
- **Kích hoạt**: Người dùng chọn “Tra cứu lợi nhuận theo khách” ở UI-EXP-06.
- **Hậu điều kiện**: Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định.
- **Bảo đảm tối thiểu**: Không sửa snapshot khóa, không ghi dở giao dịch, không lộ tiền/lương ngoài quyền.

## Luồng chính

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn runRef, customerRef, kitchenRef, periodRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Đọc snapshot có nguồn E7 đã đối soát và cost E3/E11; không tính lại từ suất giao hay giá hiện hành E10. Thiếu bất kỳ căn cứ công thức/nguồn/phương pháp thì lợi nhuận null; báo cáo chỉ phần trực tiếp được phép.
5. Hệ thống trả Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

## Nhánh và ngoại lệ

- **3a**: Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- **3b**: Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- **3c**: Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- **4a**: Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- **4b**: Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- **4c — đặc thù**: doanh thu chưa đối soát hoặc không có căn cứ thành phần lợi nhuận; khi mở báo cáo khách thì ERR-EXP-422-02; BLOCKED, không gọi chênh thu trừ nguyên liệu là lợi nhuận.
- **4d — biên**: khách có nguồn ở hai cơ sở; khi lọc theo từng cơ sở rồi tổng khách thì không trộn khóa; không cộng nguồn trùng; chỉ tổng khi từng phần đủ căn cứ.

## Quy tắc và truy vết

BR-EXP-008; quyền nền BR-SEC-008 áp dụng khi duyệt. US-EXP-008; AC-EXP-008-1, AC-EXP-008-2, AC-EXP-008-3; TC-EXP-008-1, TC-EXP-008-2, TC-EXP-008-3; API-EXP-008.

[RTM](../test/traceability.md) · [SRS](../srs/spec.md) · [Câu hỏi](../review/questions.md).
