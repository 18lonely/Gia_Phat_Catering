---
id: DOC-E13-TEST-CHECKLIST-MD
title: Checklist kiểm thử E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Checklist kiểm thử E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

Checklist và ca chi tiết đều nháp theo yêu cầu phiên; chưa có xác nhận review BA/QA. Không chuyển thành test đã chạy.

| Nhóm | Nội dung | Truy vết |
| :--- | :--- | :--- |
| Chức năng / dữ liệu / quyền | Quản lý và khóa kỳ chi phí; đủ nguồn, lỗi và biên | FR-EXP-PER-001 / BR-EXP-001 |
| Chức năng / dữ liệu / quyền | Ghi chi phí theo cơ sở và loại; đủ nguồn, lỗi và biên | FR-EXP-COST-001 / BR-EXP-002 |
| Chức năng / dữ liệu / quyền | Ghi giờ công thực tế theo ca; đủ nguồn, lỗi và biên | FR-EXP-TIME-001 / BR-EXP-003 |
| Chức năng / dữ liệu / quyền | Tham chiếu chi phí nhân công; đủ nguồn, lỗi và biên | FR-EXP-LAB-001 / BR-EXP-004 |
| Chức năng / dữ liệu / quyền | Soạn phiên bản phương pháp phân bổ; đủ nguồn, lỗi và biên | FR-EXP-METH-001 / BR-EXP-005 |
| Chức năng / dữ liệu / quyền | Ghi duyệt phương pháp của Giám đốc; đủ nguồn, lỗi và biên | FR-EXP-APRV-001 / BR-EXP-006 |
| Chức năng / dữ liệu / quyền | Kiểm cổng và lập lần phân bổ; đủ nguồn, lỗi và biên | FR-EXP-ALLOC-001 / BR-EXP-007 |
| Chức năng / dữ liệu / quyền | Tra cứu lợi nhuận theo khách; đủ nguồn, lỗi và biên | FR-EXP-PROF-001 / BR-EXP-008 |
| Chức năng / dữ liệu / quyền | Đối chiếu lợi nhuận với từng cơ sở; đủ nguồn, lỗi và biên | FR-EXP-RECON-001 / BR-EXP-009 |
| Chức năng / dữ liệu / quyền | Lập điều chỉnh sau khóa có phê duyệt; đủ nguồn, lỗi và biên | FR-EXP-ADJ-001 / BR-EXP-010 |
| Chức năng / dữ liệu / quyền | Bảo vệ lương và đầu ra nội bộ; đủ nguồn, lỗi và biên | FR-EXP-SAFE-001 / BR-EXP-011 |
| Chức năng / dữ liệu / quyền | Kiểm nguồn và truy nguyên lần báo cáo; đủ nguồn, lỗi và biên | FR-EXP-SRC-001 / BR-EXP-012 |

Nhóm bổ sung: bảo mật payload/log/cache/export; đối chiếu độc lập R13; xung đột phiên bản; tải theo profile chờ duyệt; UI ở ba chiều rộng; khôi phục nguồn/timeout; bảo toàn VAT/CK. Các lỗi chung cũng có ca hệ thống.
