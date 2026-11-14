---
id: DOC-COST-SRS-ERROR-MATRIX
title: Ma trận lỗi E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e3]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E3: Cost

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 14 dòng mã lỗi từ [SRS E3](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E3](spec.md).

| Mã ERR | HTTP | Điều kiện phát sinh | Khoá bản địa hoá | Thông báo hiển thị | Mức | Hành động tiếp theo |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `ERR-COST-404-01` | 404 | Nguyên liệu hoặc nhà cung cấp không tồn tại hoặc không còn dùng | `cost.ref_not_found` | "Không tìm thấy nguyên liệu hoặc nhà cung cấp." | Medium | Chọn lại |
| `ERR-COST-404-02` | 404 | Không có giá tham chiếu cho nguyên liệu tại cơ sở và ngày yêu cầu | `cost.price_not_found` | "Nguyên liệu {tên} chưa có giá nhập cho ngày {ngày}." | High | Nhập giá |
| `ERR-COST-409-01` | 409 | Tên nhà cung cấp trùng | `cost.supplier_duplicate` | "Nhà cung cấp này đã tồn tại." | Medium | Dùng bản ghi có sẵn |
| `ERR-COST-409-02` | 409 | Đã có giá cho cùng nguyên liệu, nhà cung cấp, cơ sở, ngày hiệu lực | `cost.price_exists` | "Đã có giá của nhà cung cấp này cho ngày hiệu lực đã chọn." | Medium | Đổi ngày hiệu lực |
| `ERR-COST-409-03` | 409 | Sửa hoặc huỷ giá đã hiệu lực | `cost.price_immutable` | "Giá đã hiệu lực không sửa hoặc huỷ được. Hãy nhập giá mới." | Medium | Nhập dòng mới |
| `ERR-COST-422-01` | 422 | Giá không phải số nguyên > 0 | `cost.price_invalid` | "Giá nhập phải là số nguyên lớn hơn 0." | Medium | Sửa giá |
| `ERR-COST-422-02` | 422 | Ngày hiệu lực ngoài khoảng cho phép (`BR-PRC-003`) hoặc nhà cung cấp đã ngừng | `cost.price_date_invalid` | "Ngày hiệu lực không hợp lệ, hoặc nhà cung cấp đã ngừng." | Medium | Sửa ngày hoặc nhà cung cấp |
| `ERR-COST-422-03` | 422 | Không tính được cost vì thiếu giá của ít nhất một nguyên liệu | `cost.missing_price` | "Chưa tính được cost vì thiếu giá: {danh sách nguyên liệu}." | High | Nhập giá còn thiếu |
| `ERR-COST-422-04` | 422 | Món đặc thù chưa có bảng tính cost đã duyệt còn hiệu lực; hoặc lập bảng tính cho món không có cờ đặc thù | `cost.sheet_required` | "Món {tên} cần bảng tính cost được duyệt trước khi vào thực đơn." | High | Lập và gửi duyệt bảng tính |
| `ERR-COST-422-05` | 422 | Chưa đặt `VAT_PCT`, hoặc doanh thu chưa VAT bằng 0 | `cost.vat_not_set` | "Chưa cấu hình thuế suất VAT nên chưa tính được cost %." | Critical | Người có quyền đặt tham số |
| `ERR-COST-422-06` | 422 | Khoản khoán có số tiền âm, không phải số nguyên, hoặc thiếu ngày hiệu lực | `cost.allowance_invalid` | "Khoản khoán không hợp lệ." | Medium | Sửa |
| `ERR-COST-422-07` | 422 | Gửi duyệt thực đơn có ngày vượt ngưỡng khi `COST_CHE_DO_KIEM` = `CHAN` | `cost.over_threshold` | "Thực đơn có {n} ngày vượt ngưỡng cost: {ngày và cost %}." | High | Đổi món hoặc định lượng |
| `ERR-COST-422-08` | 422 | Số suất âm, không phải số nguyên, hoặc tổng bằng 0 | `cost.servings_invalid` | "Số suất không hợp lệ." | Medium | Sửa số suất |
| `ERR-COST-429-01` | 429 | Vượt giới hạn gọi dịch vụ ngân sách trong một phiên | `cost.budget_rate_limited` | (không hiện cho người dùng cuối; agent trả lời rằng cần gửi thực đơn cho Gia Phát xem) | Low | Không áp dụng |
