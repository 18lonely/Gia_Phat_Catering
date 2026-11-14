---
id: DOC-THUC-DON-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e2]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E2: Thực đơn và định lượng

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E2) |

## 1. Mẫu ghi cho mỗi lần chạy

| Trường | Giá trị cần ghi |
| :--- | :--- |
| runId, caseId | Mã lần chạy riêng và mã TC; không dùng requestId thay runId |
| Môi trường | Bản build, cấu hình, phiên bản CSDL, múi giờ; thiếu thì ghi UNKNOWN |
| Dữ liệu | Tên và hash file fixture hoặc dữ liệu thật đã được cung cấp; người cung cấp và ngày |
| Thực hiện | Thời điểm, tài khoản test, quyền đã cấp, requestId |
| Expected, Actual | Expected lấy từ phiên bản tài liệu; chưa chạy thì để trống, không chép expected sang Actual |
| Bằng chứng | Response đã lọc, dữ liệu trước và sau, audit; mỗi tệp có hash |
| Kết luận | PASS, FAIL chỉ sau khi chạy và đủ bằng chứng; BLOCKED khi còn chờ quyết định; INCONCLUSIVE khi mất bằng chứng |

Không lưu mật khẩu, token, secret hay dữ liệu sức khỏe vào bằng chứng. Nơi lưu, thời hạn và quyền đọc bằng chứng cần môi trường và người phụ trách xác nhận.

## 2. Yêu cầu riêng E2

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Quy tắc thực đơn | Phiên bản danh mục quy tắc, input thực đơn, `menu_rule_results` | Mỗi quy tắc được duyệt ở DL-01 có 1 ca đạt và 1 ca vi phạm có bằng chứng |
| Duyệt | `approvals`, người lập, người duyệt, trạng thái trước và sau | Người tạo không tự duyệt; thực đơn vi phạm quy tắc cứng không gửi duyệt được |
| Phiên bản công thức | `recipes` các phiên bản, ngày hiệu lực, thực đơn dùng công thức | Thực đơn ngày cũ vẫn dùng phiên bản cũ |
| Dữ liệu 30 món | Danh sách 30 món, 12 thuộc tính, công thức đã duyệt, nguồn DL-03 đến DL-05 | Đủ thuộc tính và công thức đã duyệt theo tiêu chí R2 |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
