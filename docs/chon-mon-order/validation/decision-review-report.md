---
id: DOC-E6-DECISION-REVIEW-REPORT
title: Báo cáo review quyết định E6
version: 0.1.0
phase: Validation
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Báo cáo review quyết định E6

11/11/2026 · Review tài liệu, không kiểm thử backend hoặc phê duyệt nghiệp vụ.

## Kết quả nội dung

- Tạo [DR-01–04](../review/decision-review.md): căn cứ, phương án thay thế, khuyến nghị, ví dụ synthetic và tác động FR/UC/API/data/UI.
- Ghi E6-EVID-001 từ câu trả lời trực tiếp “Có danh sách và người quản lý xác nhận”. Chỉ xác nhận đầu vào thực tế, chưa xác nhận cơ chế credential/dedup/scope.
- Ghi [8 phát hiện](../review/decision-findings.md). Làm rõ summary token; sửa nhãn transition publish→IN_PRODUCTION; đồng bộ khóa delta revision/recipe/portion; ghi giả định quyền xử lý sau hạn của demo.
- Bổ sung [8 ca TC-E6-DR](../test/decision-review-cases.md), đều BLOCKED. Bộ57ca/57AC hiện có không đổi số; không cộng số mô tả test thành số mục tiêu độc lập.
- ORD-Q01–15 tiếp tục mở theo phần chưa được xác nhận; không thêm quyết định đã duyệt chỉ từ khuyến nghị. Chưa freeze schema/API; không mở E7–E13.

## File thay đổi

Mới: decision-review.md, decision-findings.md trong review; test/decision-review-cases.md; báo cáo này. Cập nhật questions.md, handoff.md, SRS operational-rules/states/erd, api-spec.md, screen-catalog.md, nhãn giới hạn wireframe, gap-analysis, RTM, OVERVIEW và dashboard. Preview và8sơ đồ được render lại từ nguồn; kết quả checker/UI JSON và ảnh được làm mới khi chạy.

## Kiểm tra tái chạy

```powershell
python docs/chon-mon-order/validation/check-e6.py
node docs/chon-mon-order/validation/render-e6.cjs
node docs/chon-mon-order/validation/check-ui.cjs
```

[Check kết cấu](check-result.json), [render](diagram-render-result.json), [UI](ui-result.json) là bằng chứng lần chạy; chỉ coi đạt khi exit0 và không lỗi. Các kiểm này không chứng minh các nhánh C→S, S vượt T hoặc acknowledgement đã được triển khai: các nhánh đó chỉ có thiết kế review.

Kết quả lần chạy cuối: check-e6.py exit0,0lỗi;8/8sơ đồ render,0lỗi;13màn ở1440/390/360px không tràn trang,0lỗiJS; các nhánh mock cũ đạt. Bộ8ca review mới chưa chạy backend.

DBML65bảng không sửa; checker so hash nguồn schema, business-rules kế toán và accountant-input với baseline. Giữ Cost cóVAT phải trả, cờ hóa đơn riêng, chiết khấu khoản riêng không giảm phải trả; CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, FR-MENU-RCP-007/O-02 và FEAT-046/047/O-03 không đổi.

## Điều kiện chuyển bước

Cần trả lời cụ thể DR-01–04 (từng phần có thể chốt riêng). Ghi nguồn/người/ngày, cập nhật contract và ca expected liên quan trước schema delta. Không cần hỏi lại việc danh sách có tồn tại, nhưng vẫn cần xác minh mã duy nhất và cách cấp/khôi phục credential; không dùng mã nhân viên công khai làm bí mật xác thực.

## Cập nhật phản hồi E6-EVID-002

Ngày11/11/2026, người dùng yêu cầu giữ mở cả phạm vi người đặt tổng (ORD-Q11), chuyển chọn hộ→tự chọn và xử lý S+C vượt T (ORD-Q06). Đã ghi vào sổ câu hỏi và bảng DR. Không áp phương án mặc định; test phụ thuộc vẫn BLOCKED, schema/API chưa freeze. Không có thay đổi backend hoặc quy tắc nghiệp vụ được duyệt.
