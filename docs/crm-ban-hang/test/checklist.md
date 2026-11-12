---
id: DOC-E10-TEST-CHECKLIST-MD
title: Checklist review và chuẩn bị kiểm E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Checklist review và chuẩn bị kiểm E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

- [ ] Đúng 4 feature P1, không mở E11–E13; 16 FR/UC/story, 48 AC/ca.
- [ ] Chủ nguồn xác nhận contract còn nháp và từng gate trong dependencies.
- [ ] Rà quyền theo khách/cơ sở; cost/margin chỉ nội bộ; projection khách không chứa trường nhạy cảm.
- [ ] Rà tiêu chí phát hiện trùng chưa tự chọn; gộp có duyệt, hoàn tác có diff và audit.
- [ ] Vòng đời/rủi ro theo lịch điểm và ngoại lệ, không tự đặt ngưỡng.
- [ ] Báo giá revision bất biến, thực đơn đúng hash, bằng chứng chấp thuận đúng phiên bản.
- [ ] Hợp đồng/phụ lục từ–đến không chồng, cạnh tranh nguyên tử, không sửa snapshot lịch sử.
- [ ] VAT phải trả, cờ hóa đơn riêng, CK riêng; không tự đóng câu kế toán.
- [ ] Kiểm lỗi, biên, bảo mật, tải, giao diện và phục hồi theo ca hệ thống.
- [ ] Duyệt manifest khách/hợp đồng R10 độc lập; không lấy dữ liệu đã nhập làm mẫu số.
- [ ] Có môi trường/build/dữ liệu thật và bằng chứng trước kết luận sản phẩm.

[Ca chức năng](test-cases.md) · [Ca hệ thống](system-cases.md) · [RTM](traceability.md). Checklist chưa được stakeholder duyệt; ca chi tiết soạn để review, không coi đã qua cổng review.
