---
id: DOC-E10-EPIC-SPEC-MD
title: "E10: CRM và bán hàng"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# E10: CRM và bán hàng

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Mục tiêu và phạm vi

Tập trung lịch sử khách, cơ hội và điều khoản giá để nhân viên chăm sóc khách hàng tra cứu có nguồn. CRM là quản lý quan hệ khách hàng; cost là chi phí theo định nghĩa nguồn; projection là tập trường được phép trả cho một nhóm người xem.

| Feature | Phân hệ PRD | Nội dung | UC-CRM | Ưu tiên | Phân loại |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-070 | CUS | Hồ sơ khách hàng 360°; phát hiện và gộp trùng | 001–006 | P1 | Có thiết kế nháp có điều kiện |
| FEAT-071 | CUS | Vòng đời và nguy cơ rời theo lịch điểm | 007–008 | P1 | Có thiết kế nháp có điều kiện |
| FEAT-072 | SALE | Cơ hội, báo giá có phiên bản và thực đơn | 009–012 | P1 | Có thiết kế nháp có điều kiện |
| FEAT-073 | SALE | Hợp đồng và phụ lục giá theo loại suất | 013–016 | P1 | Có thiết kế nháp có điều kiện |

4 feature có thiết kế có điều kiện; 0 feature chỉ gate trong E10. Mỗi feature có luồng, dữ liệu và invariant độc lập để review; nhánh cần quyết định vẫn BLOCKED. Không lấy số câu hỏi mở làm lý do tự đếm cả feature là hoàn tất. Độ phủ mới 60/78 ≈ 76,9% = 56 + 4; FEAT-046/047/063 vẫn chỉ gate và không được tính. Không phải tiến độ phát triển hoặc BA được duyệt.

## R10 và cổng phát hành

Theo [PRD mục 4.3–6](../gia-phat/01-prd.md), [roadmap](../gia-phat/02-roadmap.md), [URD](../gia-phat/05-urd.md), [BRD](../gia-phat/06-brd.md). R10 · v2.0.0, cỡ L, ngày chưa đặt, điều kiện bắt đầu: G-Next đạt. Nghiệm thu: **100% khách đang phục vụ có hồ sơ; 100% hợp đồng hiệu lực có phụ lục giá trong hệ thống**.

G-Next: ≥ 90% order của các công ty đã chuyển lên hệ thống ghi nhận qua cổng; ≥ 70% suất có lựa chọn trước hạn chốt; phiên truy cập tự nhiên sau 60 ngày ≥ 90% mức trước chuyển đổi. Chưa có bằng chứng đạt; mở tài liệu theo yêu cầu không miễn cổng triển khai Later.

Thứ tự chuẩn bị: review phụ thuộc → thống nhất quyết định E10 → duyệt bộ dữ liệu/người chịu trách nhiệm R10 → đối chiếu G-Next → mới xét triển khai. Không đặt ngày hoặc công sức giả.

## Ranh giới

Chỉ FEAT-070–073. E11–E13 chưa mở. FEAT-084 không có thiết kế, endpoint, công cụ hoặc lời nhắc; nếu nối tương lai chỉ theo quyền đọc của người dùng và phiên BA riêng. Phản hồi trong hồ sơ là ô đọc nguồn hiện hữu nếu có; chưa có thì ghi chưa có nguồn, không xây FEAT-079. Không tạo khách chủ, điểm phục vụ hoặc tài khoản thay E6-CG-08.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.

Schema 65 bảng giữ nguyên. Không backend, migration, gọi mô hình AI, gửi tin cho người khác, commit hoặc xóa file.

[Phụ thuộc](review/dependencies.md) · [Câu hỏi](review/questions.md) · [SRS](srs/spec.md) · [Bàn giao](review/handoff.md).
