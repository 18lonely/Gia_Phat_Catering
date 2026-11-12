---
id: DOC-E13-TEST-R13-ACCEPTANCE-MD
title: Khung nghiệm thu R13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Khung nghiệm thu R13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

Tiêu chí roadmap: báo cáo lợi nhuận theo khách đối chiếu được với kết quả kinh doanh từng cơ sở. Chưa có dữ liệu thật, quyết định phân bổ hoặc bằng chứng hoàn tất phụ thuộc.

| Mã | Điều kiện / dữ liệu | Bước kiểm | Expected / bằng chứng cần | FR | Status | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R13-GATE | Bằng chứng hoàn tất R7, R11 và Giám đốc duyệt nguyên tắc | Đối chiếu phạm vi/phiên bản các quyết định với kỳ thử | Đủ cả ba, không suy từ tài liệu nháp; E13-Q14 | FR-EXP-APRV-001 | BLOCKED |  |  |
| R13-SOURCE | Manifest toàn bộ khách/cơ sở/kỳ có số chuẩn độc lập | Kiểm đủ E7 đối soát, E3/E11 cost và công, các khoản được duyệt | Không thiếu hoặc trùng nguồn; định nghĩa kết quả cơ sở Q08 được duyệt | FR-EXP-SRC-001 | BLOCKED |  |  |
| R13-RECON | Từng cơ sở và từng khách trong kỳ nghiệm thu | So P, U, B và D trên cùng thành phần/version; kiểm tổng chéo khách nhiều cơ sở | U = 0, D = 0, P = B; mọi phần dư được giải thích, không giấu; phương pháp/làm tròn đã duyệt | FR-EXP-RECON-001 | BLOCKED |  |  |
| R13-SAFE | Các persona và tài liệu xuất nội bộ/khách | Kiểm các đường truy cập/thu hồi quyền và projection | Không lộ lương/lợi nhuận; bản khóa bất biến, điều chỉnh có lý do và duyệt | FR-EXP-SAFE-001; FR-EXP-ADJ-001 | BLOCKED |  |  |

Bộ bằng chứng phải ghi người xác nhận thực tế, thời điểm, manifest nguồn, methodVersion, định nghĩa, bảng đối chiếu và audit. Không tự điền các giá trị này. Cầu nối tổng khớp khi còn phần chưa phân bổ không đủ nghiệm thu R13.
