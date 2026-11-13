---
id: DOC-DECISION-PACK-README
title: Gói chuẩn bị quyết định — Gia Phát
version: 0.2.0
phase: Review
domain: Gia Phát
tags: [decision-pack, draft, review]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Gói chuẩn bị quyết định — Gia Phát

Nháp · 13/11/2026 · Chuẩn bị quyết định, chưa phê duyệt.

| Phiên bản | Ngày | Vai trò | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.2.0 | 13/11/2026 | BA | DEC-27; BA-Q; XC-01–12; gói rà tiếp |
| 0.1.0 | 13/11/2026 | BA | Hợp nhất nguồn để review; giữ câu mở |

Trong 5 phút: đọc 10 nhóm dưới; mở buổi họp theo vai trò; xem câu gốc trước khi ký. 224 mã nguồn, 214 nhóm; **0 câu được trả lời/đóng** trong gói. Độ phủ giữ **75/78**, 0 feature được duyệt, 0 ca sản phẩm đã chạy. FEAT-046/047/063 chỉ gate O-03.

- [DEC-01 — Phạm vi sức khỏe và điều kiện mở gợi ý cá nhân](decision-groups.md#dec-01) · [Buổi 1](meeting-agenda.md#buoi-1).
- [DEC-02 — Nguồn lực, hạ tầng và cấu hình ngân sách AI](decision-groups.md#dec-02) · [Buổi 1](meeting-agenda.md#buoi-1).
- [DEC-03 — Người duyệt ngoại lệ và cơ chế thay thế](decision-groups.md#dec-03) · [Buổi 1](meeting-agenda.md#buoi-1).
- [DEC-27 — Duyệt 43 quy tắc](decision-groups.md#dec-27) · [Buổi 2](meeting-agenda.md#buoi-2).
- [DEC-04 — Cỡ định lượng của một món](decision-groups.md#dec-04) · [Buổi 2](meeting-agenda.md#buoi-2).
- [DEC-05 — Thành phần cost và VAT bán ra còn thiếu](decision-groups.md#dec-05) · [Buổi 3](meeting-agenda.md#buoi-3).
- [DEC-80 — Ai phụ trách cung cấp và xác nhận 10 món/10 ngày thực tế? Khi nào có dữ liệu?](decision-groups.md#dec-80) · [Buổi 3](meeting-agenda.md#buoi-3).
- [DEC-07 — Xác minh người ăn và binding danh tính](decision-groups.md#dec-07) · [Buổi 4](meeting-agenda.md#buoi-4).
- [DEC-108 — Customer master/account/service lifecycle; ORD-Q03/11](decision-groups.md#dec-108) · [Buổi 4](meeting-agenda.md#buoi-4).
- [DEC-11 — Phát hành, xác nhận revision và bắt đầu sản xuất](decision-groups.md#dec-11) · [Buổi 4](meeting-agenda.md#buoi-4).

[Sổ quyết định](decision-register.md) · [Bản máy](decision-register.json) · [Toàn bộ nhóm](decision-groups.md) · [Chương trình họp](meeting-agenda.md) · [Nhất quán liên epic](cross-epic-consistency.md) · [Báo cáo kiểm và số đếm nguồn](validation/report.md).

Ba buổi đầu bao phủ gate MVP; buổi 4 ưu tiên CG01 → CG08 → CG05 → CG06 → CG12. Các nhóm còn lại theo vai trò ở buổi 5–9. Người quyết định/release chưa có căn cứ ghi “chưa rõ”; BA phải xác minh trước ký. Không lấy việc đọc gói hoặc đồng ý một hướng làm bằng chứng đã triển khai.

## Prompt tiếp nối

> Là BA tại D:\BA. Chỉ cập nhật tài liệu epic theo quyết định đã ký có nguồn. Mỗi lần xử lý một nhóm DEC trong gói decision-pack. Đọc sổ, các câu nguồn, phạm vi chữ ký và bằng chứng trước. Dùng skill cr để phân tích tác động tài liệu, dữ liệu/API, kiểm thử và phụ thuộc; không tự đặt story point hoặc ngày. Chỉ sửa phần được quyết định cho phép; phần mơ hồ giữ mở. Không lấy câu trả lời một phần làm đóng toàn nhóm. Giữ nguyên Cost/VAT/chiết khấu, NFR-COST-002, O-02/O-03 và trạng thái ca chưa chạy. Chụp baseline mới cho phiên đó, kiểm bảo toàn, báo cáo phạm vi thay đổi. Không backend, migration, gọi AI, commit hoặc xóa file. Nếu chưa có quyết định ký kèm nguồn, chỉ ghi thiếu bằng chứng và tiếp tục rà phần độc lập.

## Rà tiếp ngày 13/11/2026

[Sổ BA-Q](ba-open-questions.md) · [Báo cáo hiện hành](followup-2026-11-13/report.md) · [Xử lý XC](followup-2026-11-13/xc-resolution.md) · [Quy ước](followup-2026-11-13/conventions.md).

6 trong 89 câu thiếu vai trò được làm rõ bằng nguồn; 83 câu còn lại có BA-Q. Cả 4 câu thiếu release có BA-Q. 197 nhóm gốc còn 209 sau khi gộp 6 nhóm và tách 18 câu có phạm vi/người ký khác; 5 câu mới đưa tổng lên 214 nhóm. 219 câu gốc giữ đủ, thêm 5 câu epic; câu hỏi thẩm quyền riêng không thay câu nghiệp vụ. XC-01 đã sửa; XC-04 đã sửa cách mô tả, contract vẫn chờ; 10 XC còn chờ quyết định. 0 câu được trả lời, 0 feature được duyệt, độ phủ giữ 75/78. Đây không phải BA được duyệt.
