---
id: DOC-E11-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e11]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E11: Mua hàng và sản xuất

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E11) |

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

## 2. Yêu cầu riêng E11

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Nhu cầu và đơn mua | Plan revision, dự toán, nhu cầu, đơn mua trước và sau | Đúng nguồn; không tự trừ tồn khi chưa có quyết định E11-Q01 |
| Nhận hàng | Lượng đặt, nhận, chấp nhận từng dòng; ảnh chứng từ; quyền tệp | Giữ riêng ba lượng; ảnh không xác nhận giá |
| BO-02 | Dự toán và thực mua cùng ngày, cơ sở; định nghĩa được duyệt ở E11-Q08 | Chênh cost thực mua so với dự toán ≤ 3 điểm phần trăm theo cách đo được duyệt |
| Mẫu lưu | Sổ mẫu từng bữa, mã mẫu, bằng chứng | 100% bữa có mẫu lưu theo chính sách E11-Q11 |
| Thay món | Ba kết quả kiểm dị ứng, quy tắc, cost cùng phiên bản; cổng MENU | Thiếu một kết quả thì chặn; CHAN chặn vượt cost |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
