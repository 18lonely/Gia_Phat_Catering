---
id: DOC-THUC-DON-REVIEW-QUESTIONS
title: Sổ câu hỏi mở E2
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [questions, e2]
author: BA
last_updated: 2026-11-16
---
# Sổ câu hỏi mở E2: Thực đơn và định lượng

Draft · 16/11/2026 · Chỉ mục, chưa có câu nào được trả lời.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo chỉ mục câu hỏi E2 theo khuôn chung của các epic; không đổi nội dung hay trạng thái câu nào |

Câu hỏi E2 được ghi gốc ở [SRS E2 mục 4.5](../srs/spec.md) và [API E2](../api/api-spec.md). File này chỉ gom lại thành một chỗ theo khuôn các epic khác; **trả lời phải ghi tại nơi gốc và tại [sổ quyết định](../../gia-phat/review/decision-pack/decision-register.md)**, không ghi ở đây. Cột nhóm DEC, người quyết định, chặn release và mức lấy từ sổ quyết định.

## 1. Câu hỏi nghiệp vụ E2

| Mã | Câu hỏi (link về nơi gốc) | Nhóm DEC | Người quyết định | Chặn release | Mức |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E2-Q1 | [Cách kiểm ngưỡng giá suất](../../thuc-don-dinh-luong/srs/spec.md#L411) | [DEC-28](../../gia-phat/review/decision-pack/decision-groups.md#dec-28) | Dinh dưỡng viên, Giám đốc | R2 | P-MVP |
| E2-Q2 | [Quy tắc tuần có xét tuần trước không](../../thuc-don-dinh-luong/srs/spec.md#L412) | [DEC-27](../../gia-phat/review/decision-pack/decision-groups.md#dec-27) | Người soạn docx | R2 | P-MVP |
| E2-Q3 | [Tuần phục vụ gồm những ngày nào](../../thuc-don-dinh-luong/srs/spec.md#L413) | [DEC-30](../../gia-phat/review/decision-pack/decision-groups.md#dec-30) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q4 | [Thực đơn chung hay riêng theo khách](../../thuc-don-dinh-luong/srs/spec.md#L414) | [DEC-31](../../gia-phat/review/decision-pack/decision-groups.md#dec-31) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q5 | [Khoảng định lượng và chất độn dùng chuẩn từng món hay bảng theo nguyên liệu/kiểu món; lưu ở đâu?](../../thuc-don-dinh-luong/srs/spec.md#L421) | [DEC-38](../../gia-phat/review/decision-pack/decision-groups.md#dec-38) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q6 | [Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)](../../thuc-don-dinh-luong/srs/spec.md#L415) | [DEC-32](../../gia-phat/review/decision-pack/decision-groups.md#dec-32) | Dinh dưỡng viên, người duyệt | R2 | P-MVP |
| E2-Q7 | [Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?](../../thuc-don-dinh-luong/srs/spec.md#L416) | [DEC-33](../../gia-phat/review/decision-pack/decision-groups.md#dec-33) | Giám đốc | R2 | P-MVP |
| E2-Q8 | [Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?](../../thuc-don-dinh-luong/srs/spec.md#L417) | [DEC-34](../../gia-phat/review/decision-pack/decision-groups.md#dec-34) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q9 | [Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)](../../thuc-don-dinh-luong/srs/spec.md#L418) | [DEC-35](../../gia-phat/review/decision-pack/decision-groups.md#dec-35) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q10 | [Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)](../../thuc-don-dinh-luong/srs/spec.md#L419) | [DEC-36](../../gia-phat/review/decision-pack/decision-groups.md#dec-36) | Dinh dưỡng viên | R2 | P-MVP |
| E2-Q11 | [Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)](../../thuc-don-dinh-luong/srs/spec.md#L420) | [DEC-37](../../gia-phat/review/decision-pack/decision-groups.md#dec-37) | Người duyệt | R2 | P-MVP |

## 2. Câu hỏi hợp đồng API E2

| Mã | Câu hỏi (link về nơi gốc) | Nhóm DEC | Người quyết định | Chặn release | Mức |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MENU-API-Q01 | [Route thay đổi/hủy cặp kỵ và quyết định menu-rule-change dùng service chung hay API riêng; lifecycle/error chi tiết?](../api/api-spec.md) | Chưa có | Tech lead, BA | Chưa ghi | Chưa ghi |
| MENU-API-Q02 | [Giá bị trả lại có trạng thái RETURNED hay hủy đề nghị; đồng bộ trạng thái DBML trước migration?](../api/api-spec.md) | Chưa có | BA, Tech lead | Chưa ghi | Chưa ghi |
| MENU-API-Q03 | [TTL/size XLSX, nơi lưu validation hash/version, idempotency/output job export?](../api/api-spec.md) | Chưa có | Tech lead | Chưa ghi | Chưa ghi |

## 3. Điểm mở liên quan ghi ở nơi khác

- `DL-01`: bộ quy tắc thực đơn được duyệt, chặn phần số liệu của bộ kiểm quy tắc. Xem [roadmap](../../gia-phat/02-roadmap.md) và [quy tắc thực đơn](../../gia-phat/brainstorms/quy-tac-thuc-don.md).
- `O-02`: một món một hay nhiều cỡ định lượng, chặn `FR-MENU-RCP-007`. Xem [BRD mục 11](../../gia-phat/06-brd.md).

Ba câu MENU-API-Q chưa có trong sổ quyết định 13/11/2026; cần đưa vào ở lần rà kế tiếp. Tất cả câu giữ CHỜ TRẢ LỜI.
