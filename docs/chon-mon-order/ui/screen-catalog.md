---
id: DOC-E6-UI-SCREEN-CATALOG
title: Danh mục 13 màn wireframe E6
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Danh mục 13 màn wireframe E6

Draft · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.

[Mở wireframe tương tác](../html-wireframe/order-workbench.html). Tất cả dữ liệu là **synthetic**; trạng thái chỉ trong bộ nhớ; không gọi backend. Màn 06 mô phỏng một lựa chọn độc lập; màn 08–13 dùng fixture gộp S=60 để review số suất, không giả hai fixture là cùng dữ liệu thật. Màn setup chủ yếu minh họa gate và quyền, không CRUD đầy đủ.

| Screen | Tên / actor | Feature / UC | Nhánh mô phỏng / giới hạn |
| :--- | :--- | :--- | :--- |
| UI-ORD-01 | Cấp tài khoản / quản trị khách | FEAT-030 / UC-ORD-001 | lý do thiếu, khác khách, preview quyền; chưa tạo account |
| UI-ORD-02 | QR / người ăn | FEAT-031/032 / UC-ORD-002/003 | account/guest, token revoked; identity policy chưa chốt |
| UI-ORD-03 | Quản lý QR/người / người đặt tổng | FEAT-033 / UC-ORD-004 | rotation/removal và cảnh báo bảo toàn lịch sử |
| UI-ORD-04 | Phục vụ / DDV | FEAT-034 / UC-ORD-005 | xem bếp/ca, tác động snapshot; chưa CRUD lịch |
| UI-ORD-05 | Định mức/mode / người đặt tổng | FEAT-035/044 / UC-ORD-006/015 | nhãn quota, mode pending; không tự áp chính sách |
| UI-ORD-06 | Chọn ngày/xem món / người ăn | FEAT-036/045 / UC-ORD-007/016 | bằng/vượt 1đ, đổi, replay, thiếu nguồn, khóa, empty/offline/stale |
| UI-ORD-07 | Chọn tuần / tài khoản | FEAT-037 / UC-ORD-008 | policy chưa chốt; giả định atomic/partial; guest403 |
| UI-ORD-08 | Chốt tổng / người đặt tổng | FEAT-038 / UC-ORD-009 | T<S+C; T=S+C; preview/confirm/quay lại; chưa chốt ORD-Q06 |
| UI-ORD-09 | Job khóa/nhắc / vận hành | FEAT-039/040/043 / UC-ORD-010/011/014 | thiếu total/default, retry, nhắc gated; không provider |
| UI-ORD-10 | Đổi sau khóa / người đề nghị và duyệt | FEAT-041 / UC-ORD-012 | pending, tự duyệt, gate policy, approve/reject/replay |
| UI-ORD-11 | Nhập hộ / DDV | FEAT-042 / UC-ORD-013 | source/evidence/reason, sau hạn sang đề nghị; không gửi Zalo |
| UI-ORD-12 | Gate sức khỏe / người ăn | FEAT-046/047 / UC-ORD-017/018 | chỉ thông báo chưa mở; không form sức khỏe |
| UI-ORD-13 | Phiếu bếp / bếp | FEAT-048 / UC-ORD-019 | version cũ/mới, tổng MAIN và delta mẫu; chưa phân rã món phụ |

Desktop: sidebar + nội dung; mobile: thanh màn cuộn riêng, form một cột; có label, focus, aria-live, modal xác nhận. Test UI chỉ chứng minh hành vi mô phỏng đã kiểm, không chứng minh quyền/transaction/backend thực.


Review E6-RV-08: màn09 cho phép sửa default rồi bấm khóa để xem nhánh thành công; demo **giả định đã được phép xử lý nguồn sau hạn**. Không mô phỏng cấp quyền ngoại lệ/quyết định gia hạn; không dùng demo làm bằng chứng ai cũng được retry với nguồn mới. Xem [DR-03](../review/decision-review.md).

## Bổ sung consistency độc lập — 11/11/2026

Xem [mapping UI/API/data](../api/data-mapping.md) và [lifecycle review](../srs/lock-plan-review.md). Phân biệt token tổng, version order, revision order/plan; lock thành công không hứa plan đã sẵn sàng. Các trường completeness/ack/publish vẫn là delta review, chưa thêm vào catalog hoặc wireframe; không thay E6-EVID-001/002.

## Giới hạn demo so với contract hiện hành

[Bảng evidence và giới hạn mock](../test/evidence-protocol.md) ghi cụ thể UI06/09/10/13: replay mock kiểm stale trước receipt; plan tạo ngay; order/plan dùng cùng số revision; chưa manifest đầy đủ. Wireframe chỉ minh họa một nguồn/món, không phải expected cho async hoặc delta đa định lượng. Không suy publish/ack/start đã có từ kết quả demo.
