---
id: DOC-E13-USECASES-UC-EXP-002-MD
title: "UC-EXP-002: Ghi chi phí theo cơ sở và loại"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-EXP-002: Ghi chi phí theo cơ sở và loại

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

- **Phạm vi**: E13 / FEAT-088; P2; FR-EXP-COST-001.
- **Cấp độ**: Sea level.
- **Tác nhân chính**: PER-07.
- **Bên liên quan và kỳ vọng**: Kế toán cần truy nguồn; Giám đốc cần đối chiếu; người lao động cần bảo vệ chi tiết lương; khách không nhận lợi nhuận nội bộ.
- **Tác nhân hỗ trợ**: Nền E1 kiểm quyền và audit; nguồn E3/E7/E10/E11 chỉ đọc theo scope.
- **Tiền điều kiện**: Đăng nhập, quyền đúng cơ sở và hành động. Nhánh thành công phụ thuộc chính sách chỉ dùng khi có bằng chứng E13-Q01; chưa có thì đi nhánh 3b.
- **Kích hoạt**: Người dùng chọn “Ghi chi phí theo cơ sở và loại” ở UI-EXP-02.
- **Hậu điều kiện**: Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức.
- **Bảo đảm tối thiểu**: Không sửa snapshot khóa, không ghi dở giao dịch, không lộ tiền/lương ngoài quyền.

## Luồng chính

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn periodRef, kitchenRef, typeVersionRef, amount, evidenceRef, sourceKey, customerRef?.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm kỳ mở, căn cứ khoản tiền và loại. Khoản trực tiếp phải có khách và căn cứ gán trực tiếp; khoản chung giữ pool riêng. Không nhận lại cost E3/E11 như khoản mới.
5. Hệ thống trả Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

## Nhánh và ngoại lệ

- **3a**: Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- **3b**: Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- **3c**: Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- **4a**: Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- **4b**: Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- **4c. Đặc thù**: dòng chi phí thiếu chứng từ hoặc loại; khi gửi lưu thì ERR-EXP-422-01 và chỉ ra trường thiếu; không ghi dòng.
- **4d. Biên**: sourceKey đã nằm trong cost E3/E11 của cùng kỳ; khi nhập lại khoản đó thì ERR-EXP-409-03; không cộng hai lần.

## Quy tắc và truy vết

BR-EXP-002; quyền nền BR-SEC-008 áp dụng khi duyệt. US-EXP-002; AC-EXP-002-1, AC-EXP-002-2, AC-EXP-002-3; TC-EXP-002-1, TC-EXP-002-2, TC-EXP-002-3; API-EXP-002.

[RTM](../test/traceability.md) · [SRS](../srs/spec.md) · [Câu hỏi](../review/questions.md).
