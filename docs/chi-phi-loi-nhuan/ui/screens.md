---
id: DOC-E13-UI-SCREENS-MD
title: Danh mục màn EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Danh mục màn EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

| Màn | Tên | FR | Trường/hành động | Gate |
| :--- | :--- | :--- | :--- | :--- |
| UI-EXP-01 | Kỳ chi phí | FR-EXP-PER-001 | Cơ sở synthetic A · Kỳ thử K-A; Chọn phạm vi kỳ; không mặc định lịch khóa.; Kỳ tham chiếu | OPEN (chính sách khóa chờ E13-Q02) |
| UI-EXP-02 | Chi phí cơ sở | FR-EXP-COST-001 | Khoản trực tiếp synthetic: 120.000 đ; Khoản trực tiếp gắn khách A; chi phí chung để pool riêng. Không nhập lại nguồn nguyên liệu.; Chứng từ tham chiếu | DRAFT (danh mục loại chi phí chờ E13-Q01) |
| UI-EXP-03 | Chấm công và nhân công | FR-EXP-TIME-001, FR-EXP-LAB-001 | Người synthetic P-A · Ca tham chiếu E11; Phân ca không chứng minh đã làm. Nguồn đơn giá hoặc bảng lương chờ duyệt; chỉ PER-07/PER-08 có quyền chi tiết.; Nguồn chấm công | DRAFT (chưa có giờ thực tế được xác nhận) |
| UI-EXP-04 | Phiên bản phương pháp | FR-EXP-METH-001, FR-EXP-APRV-001 | Phiên bản nháp synthetic M-A; Không chọn sẵn phân bổ theo suất, doanh thu, giờ công hay diện tích. Người duyệt khác người lập/sửa cuối.; Căn cứ đề xuất | DRAFT (chưa có bản được Giám đốc duyệt) |
| UI-EXP-05 | Nguồn và cổng phân bổ | FR-EXP-ALLOC-001, FR-EXP-SRC-001 | Manifest synthetic · E3 / E7 / E10 / E11; Doanh thu từ E7 đã đối soát; không lấy số suất giao nhân giá. Thiếu nguồn không bằng 0.; Nguồn cần review | BLOCKED (thiếu phương pháp đã duyệt) |
| UI-EXP-06 | Lợi nhuận theo khách | FR-EXP-PROF-001, FR-EXP-SAFE-001 | Khách synthetic A · Cơ sở A; Chi phí trực tiếp synthetic: 120.000 đ. Lợi nhuận và biên lợi nhuận: chưa xác định. Nhân công trong báo cáo này chỉ tổng hợp. Không gửi tài liệu E13 cho khách.; Ghi chú review | BLOCKED (chỉ xem chi phí trực tiếp) |
| UI-EXP-07 | Đối chiếu cơ sở | FR-EXP-RECON-001 | Bài minh họa bảo toàn · synthetic; Ví dụ này giả định nguồn và phương pháp đã duyệt, chỉ để giải thích số học, không đại diện báo cáo đang BLOCKED.; Căn cứ kết quả cơ sở | Chưa nghiệm thu R13 |
| UI-EXP-08 | Điều chỉnh sau khóa | FR-EXP-ADJ-001 | Kỳ synthetic K-A đã khóa; Bút toán đề nghị riêng; lý do và người duyệt bắt buộc. Bản gốc và nguồn E7 không thay đổi.; Lý do điều chỉnh | PENDING (quyền duyệt và kỳ đích chờ E13-Q10) |

Tám màn là workspace nội bộ, không có màn dành cho khách. Mỗi màn có Normal/Loading/Empty/Error/Offline/Blocked, kiểm trường trống và hộp review. Màn 07 có ví dụ số học tách rõ khỏi báo cáo hiện hành. Không có nút giả duyệt phương pháp hoặc giả hoàn tất R13.
