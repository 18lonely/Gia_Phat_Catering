---
id: DOC-AGENT-NOI-BO-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E5
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e5]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E5: Agent Nội bộ

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E5) |

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

## 2. Yêu cầu riêng E5

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Bộ 20 yêu cầu | Manifest đã khóa trước khi chạy (mã ca, input hash, oracle, người duyệt); phiên bản mô hình và lời nhắc | 100% không vi phạm quy tắc cứng, không vượt cost; 0 món ngoài danh mục |
| Kiểm và áp dụng | `agent_run_contexts` (candidate hash, evidence), kết quả MENU và COST cùng hash, `menus` trước và sau | Áp dụng đúng một lần, nguyên tử, chỉ tạo bản nháp |
| Nhật ký lượt chạy | `agent_runs`, `agent_tool_events` kể cả lượt timeout | 100% lượt chạy có nhật ký bền vững |
| Thời gian | Số đo trước MVP và sau MVP cùng cách đo | Thời gian dựng tuần giảm ≥ 50% (BO-03); một tuần ≤ 60 giây |
| Bảo mật | Câu chèn lệnh, yêu cầu ngoài quyền, log hiển thị | 0 thao tác vượt giao quyền; 0 secret trong response, log |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
