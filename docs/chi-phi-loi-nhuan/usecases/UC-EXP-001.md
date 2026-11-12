---
id: DOC-E13-USECASES-UC-EXP-001-MD
title: UC-EXP-001 — Quản lý và khóa kỳ chi phí
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-EXP-001 — Quản lý và khóa kỳ chi phí

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

- **Phạm vi**: E13 / FEAT-088; P2; FR-EXP-PER-001.
- **Cấp độ**: Sea level.
- **Tác nhân chính**: PER-07.
- **Bên liên quan và kỳ vọng**: Kế toán cần truy nguồn; Giám đốc cần đối chiếu; người lao động cần bảo vệ chi tiết lương; khách không nhận lợi nhuận nội bộ.
- **Tác nhân hỗ trợ**: Nền E1 kiểm quyền và audit; nguồn E3/E7/E10/E11 chỉ đọc theo scope.
- **Tiền điều kiện**: Đăng nhập, quyền đúng cơ sở và hành động. Nhánh thành công phụ thuộc chính sách chỉ dùng khi có bằng chứng E13-Q02; chưa có thì đi nhánh 3b.
- **Kích hoạt**: Người dùng chọn “Quản lý và khóa kỳ chi phí” ở UI-EXP-01.
- **Hậu điều kiện**: Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu.
- **Bảo đảm tối thiểu**: Không sửa snapshot khóa, không ghi dở giao dịch, không lộ tiền/lương ngoài quyền.

## Luồng chính

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn periodRef, kitchenRef, fromDate, toDate, version, lockDecisionRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm scope, nguồn và quyết định khóa; kỳ mở cho nhập nháp. Chỉ khóa khi chính sách và quyền đã được duyệt; giữ snapshot bất biến.
5. Hệ thống trả Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

## Nhánh và ngoại lệ

- **3a**: Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- **3b**: Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- **3c**: Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- **4a**: Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- **4b**: Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- **4c — đặc thù**: kỳ đã LOCKED; khi gửi sửa trực tiếp kỳ thì ERR-EXP-409-01; không đổi byte dữ liệu gốc.
- **4d — biên**: hai thao tác cùng version cũ; khi gửi khóa đồng thời với ghi chi phí thì chỉ một version hợp lệ; thao tác còn lại ERR-EXP-409-02.

## Quy tắc và truy vết

BR-EXP-001; quyền nền BR-SEC-008 áp dụng khi duyệt. US-EXP-001; AC-EXP-001-1, AC-EXP-001-2, AC-EXP-001-3; TC-EXP-001-1, TC-EXP-001-2, TC-EXP-001-3; API-EXP-001.

[RTM](../test/traceability.md) · [SRS](../srs/spec.md) · [Câu hỏi](../review/questions.md).
