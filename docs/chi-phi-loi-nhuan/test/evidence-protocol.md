---
id: DOC-E13-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e13]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E13: Chi phí và lợi nhuận

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E13) |

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

## 2. Yêu cầu riêng E13

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Kỳ và chi phí | Kỳ, khoản chi phí, sourceKey, chống trùng với E3, E11 | Không ghi khi kỳ khóa; không trùng nguồn |
| Phương pháp phân bổ | Phiên bản, hash, người lập, người duyệt, bằng chứng duyệt | Giám đốc duyệt khác người lập và sửa cuối |
| Đối chiếu cơ sở | Manifest nguồn, kết quả theo khách, phần chưa phân bổ, số chuẩn cơ sở | Tổng khách cộng phần chưa phân bổ khớp số chuẩn; không giấu phần dư |
| Lương | Quyền đọc chi tiết, projection gửi khách | Chỉ PER-07, PER-08 đọc chi tiết; bản cho khách không có lợi nhuận |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
