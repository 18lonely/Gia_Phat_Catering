---
id: DOC-DINH-DUONG-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E4
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e4]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E4: Dinh dưỡng

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E4) |

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

## 2. Yêu cầu riêng E4

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Nguồn số liệu | Ấn bản, trang, mã thực phẩm của từng nguyên liệu; người mapping | 100% nguyên liệu của 30 món có đủ 4 chỉ số có nguồn (R4) |
| Đối soát 5 suất | Bảng tính tay độc lập có người lập, ngày, phương pháp; output hệ thống | Khớp theo làm tròn và dung sai được duyệt ở NUTR-Q04, không mượn dung sai Cost |
| Lịch sử | `nutrient_value_revisions`, `nutrition_calculations` trước và sau khi sửa số liệu | Kết quả cũ giữ snapshot; kết quả mới dùng revision mới |
| Nhãn | Ảnh màn hình mọi nơi hiện tổng | Có nhãn "ước tính từ định lượng sống", đơn vị, trạng thái thiếu |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
