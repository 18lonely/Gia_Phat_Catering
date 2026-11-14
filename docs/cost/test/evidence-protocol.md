---
id: DOC-COST-TEST-EVIDENCE-PROTOCOL
title: Protocol bằng chứng E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, evidence, e3]
author: BA
last_updated: 2026-11-16
---
# Protocol bằng chứng E3: Cost

Draft · 16/11/2026 · Quy ước ghi bằng chứng khi chạy test thật sau này. Chưa có lần chạy nào.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic (mẫu ghi chung và yêu cầu riêng E3) |

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

## 2. Yêu cầu riêng E3

| Nhóm | Bằng chứng cần có | Đủ để kết luận khi |
| :--- | :--- | :--- |
| Đối soát số học | Bảng tính tay của kế toán có người lập, ngày, phiên bản; output hệ thống; script so Decimal | Cost món lệch ≤ 1 đ, cost % ngày lệch ≤ 0,01 điểm phần trăm (NFR-COST-002) |
| Cổng gửi duyệt | Chế độ kiểm, cost %, ngưỡng, kết quả gửi duyệt, `menu_cost_snapshots` | CHAN chặn, CANH_BAO cảnh báo, thiếu đầu vào luôn chặn |
| Cách ly cost | Quyền CSDL của tài khoản agent khách, log `FR-COST-RUL-003`, response | Không lộ cost, giá nhập; SELECT bị từ chối ở CSDL |
| Kế toán | Giá báo, cơ sở giá, VAT, cờ hóa đơn, chiết khấu, số phải trả | Giá cost gồm VAT; cờ hóa đơn không làm VAT thành 0; chiết khấu không giảm phải trả |

## 3. Không đủ làm bằng chứng

- Kiểm wireframe, ảnh mock hay script kiểm tài liệu.
- Dữ liệu giả lập trong `test/fixtures/` khi tiêu chí release đòi dữ liệu thật.
- Ca có expected phụ thuộc câu hỏi chưa trả lời: giữ BLOCKED, không đổi sang PASS.
