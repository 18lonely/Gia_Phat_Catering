---
id: DOC-NEN-TANG-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e1]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E1: Nền tảng

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E1) |

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

## 2. Yêu cầu riêng E1

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Phân quyền, phạm vi | Request với ID ngoài phạm vi, response đã lọc, log hiển thị | 404 và không lộ tồn tại bản ghi; đúng tiêu chí R1 cơ sở A không đọc cơ sở B |
| Nhật ký | Bản ghi `audit_logs` trước và sau, `request_id` khớp response | 100% thao tác sửa số liệu có audit đủ actor, trước sau, lý do |
| Phiên, mật khẩu, MFA | Trạng thái `sessions` trước và sau, không chụp token | Thu hồi đúng phiên; không lưu hay in token, mật khẩu |
| Tải | Profile, số người dùng đồng thời, p95 đọc và ghi, tỷ lệ lỗi, cấu hình máy | p95 đọc ≤ 300 ms, ghi ≤ 800 ms ở 1000 người đồng thời trên API mẫu |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
