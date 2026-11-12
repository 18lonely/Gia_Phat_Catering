---
id: DOC-E11-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

| Mã | HTTP | Điều kiện / log kỹ thuật | Khóa bản địa hóa | Thông báo | Mức | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-PUR-422-11 | 422 | Thiếu hệ số g/kg; không log giá/ảnh nhạy cảm | pur.case_001 | Chặn tổng hợp khác đơn vị; không coi hệ số là 1 | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-12 | 422 | Số lượng âm hoặc thiếu NCC; không log giá/ảnh nhạy cảm | pur.case_002 | Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-13 | 422 | Client tự gắn APPROVED; không log giá/ảnh nhạy cảm | pur.case_003 | Không công nhận trạng thái do client tự khai | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-14 | 422 | Hàng tươi được gửi yêu cầu quản lý lô; không log giá/ảnh nhạy cảm | pur.case_004 | Không tạo lô cho hàng tươi | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-15 | 422 | Chấp nhận 9 kg khi chỉ nhận 8 kg; không log giá/ảnh nhạy cảm | pur.case_005 | Chặn dữ liệu mâu thuẫn, không ghi phiếu | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-16 | 422 | File của cơ sở ngoài scope; không log giá/ảnh nhạy cảm | pur.case_006 | Không lộ nội dung/URL tệp, không gắn chéo | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-17 | 422 | Thiếu số dư đầu kỳ; không log giá/ảnh nhạy cảm | pur.case_007 | Không báo tổng công nợ hoàn chỉnh | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-18 | 422 | Thực mua của cơ sở khác hoặc ngày chưa phân bổ; không log giá/ảnh nhạy cảm | pur.case_008 | Không ghép với dự toán để kết luận đạt | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-403-11 | 403 | Người không có cost.cost.read yêu cầu tiền; không log giá/ảnh nhạy cảm | pur.case_009 | Không trả tiền hoặc cost trong body/lỗi/log hiển thị | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-20 | 422 | Nhân sự ngoài cơ sở được phép; không log giá/ảnh nhạy cảm | pur.case_010 | Từ chối gắn vào ca | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-21 | 422 | Client bỏ mục không đạt khỏi yêu cầu; không log giá/ảnh nhạy cảm | pur.case_011 | Không kết luận đủ dựa trên tập mục thiếu | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-22 | 422 | Thiếu mã bữa hoặc cơ sở; không log giá/ảnh nhạy cảm | pur.case_012 | Chặn bản ghi không truy được nguồn | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-23 | 422 | Đổi món MAIN sang SOUP; không log giá/ảnh nhạy cảm | pur.case_013 | Chặn khác vai trò, không tạo thay thế hợp lệ | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-24 | 422 | Thiếu giá hoặc thiếu căn cứ dị ứng; không log giá/ảnh nhạy cảm | pur.case_014 | BLOCKED; không trả đạt dù quy tắc khác đạt | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-25 | 422 | Quy tắc cứng vi phạm hoặc thiếu cost; không log giá/ảnh nhạy cảm | pur.case_015 | Không được chuyển như đã đạt; giữ ứng viên | High | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |

Lỗi dùng chung kế thừa E1: 401 hết phiên, 403 thiếu quyền, 404 ngoài scope/không tồn tại; đề xuất ERR-PUR-409-11 khi version đổi, ERR-PUR-503-11 khi nguồn không sẵn sàng, ERR-PUR-422-99 khi policy chưa duyệt. Không trả stack/URL ảnh công khai. Chi tiết envelope và đồng thời chờ E11-Q13/E1-Q01.
