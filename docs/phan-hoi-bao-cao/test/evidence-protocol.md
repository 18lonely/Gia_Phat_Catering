---
id: DOC-E12-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e12]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E12: Phản hồi và báo cáo

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E12) |

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

## 2. Yêu cầu riêng E12

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Phản hồi | Đánh giá, khiếu nại, receipt, phạm vi người gửi | Chỉ thang được duyệt; khiếu nại tách khỏi điểm |
| Chỉ số | metricDefinitionRef, sourceRefs, asOf, completeness của từng ô | Không có ô hiện số khi thiếu định nghĩa hoặc nguồn |
| Đề xuất AI | Lượt chạy AIO, công cụ đã gọi, quyền giao, đề xuất nháp, người review | Chỉ công cụ đọc; không ghi MENU, CRM, PUR |
| Nhật ký bữa đã ăn | Consent, bằng chứng đã ăn, snapshot dinh dưỡng, yêu cầu xóa và bằng chứng hoàn tất | Không thu sức khỏe; xóa trong thời hạn theo nền, không xóa nguồn E6, E7 |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
