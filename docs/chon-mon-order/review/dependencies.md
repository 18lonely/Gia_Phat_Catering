---
id: DOC-E6-REVIEW-DEPENDENCIES
title: Hợp đồng phụ thuộc và điểm cần đồng bộ
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Hợp đồng phụ thuộc và điểm cần đồng bộ

Draft · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.

| Miền / nguồn | E6 dùng gì | Tác động / ràng buộc |
| :--- | :--- | :--- |
| [Nền tảng](../../nen-tang/srs/spec.md), [schema](../../nen-tang/srs/schema.dbml) | Phiên, authorize, audit, params, files, jobs | users.customer_id và user_type SERVICE đã có; thiếu scope nhiều điểm/guest session và policy binding. Không nói SERVICE hoàn toàn chưa có; ORD-Q11/E1-Q02/04 |
| [MENU](../../thuc-don-dinh-luong/srs/spec.md) | PUBLISHED, default MAIN, recipe/price version, WITHDRAWN | ORD-Q04/12 xử lý nguồn thay; không vượt cổng MENU; FR-MENU-RCP-007 giữ BLOCKED O-02 |
| [Cost](../../cost/srs/spec.md), [kế toán](../../cost/accounting/business-rules.md) | Kiểm định mức theo giá bán/cơ cấu; tham chiếu pricing snapshot | Không lộ cost người ăn; không tạo nguồn giá song song. VAT cost phải trả; invoice flag riêng; chiết khấu riêng không giảm phải trả. CK-Q01–10, DATA-COST-Q01–06 không đóng; chưa10món/10ngày thật |
| [Dinh dưỡng](../../dinh-duong/srs/spec.md) | 4 chỉ số và provenance qua safe adapter | Missing không0; nhãn ước tính định lượng sống; NUTR-Q03/04 còn mở. Không dùng dung sai Cost cho dinh dưỡng |
| [Agent Nội bộ](../../agent-noi-bo/srs/spec.md) | Nguồn DRAFT MENU gián tiếp | Agent không chọn/chốt/duyệt order; E6 chỉ đọc MENU sau công bố, không lấy candidate VALID thay PUBLISHED |

Đã thêm liên kết ngược từ SRS E1–E5 và ERD nền tới gói E6. Không sửa công thức Cost, schema DBML, CK/DATA-COST hoặc thuật toán Agent. API/port đều đề xuất, chưa server hoặc migration. NFR-COST-002 giữ cost món≤1đ và cost% ngày≤0,01 điểm phần trăm.

## Cổng customer/account tối thiểu cho E6 ngày 11/11/2026

Đọc [API nền](../../nen-tang/api/api-spec.md) và [mapping E6](../api/data-mapping.md): API-CORE-007 tạo user, CORE-008 đổi trạng thái, CORE-009 gán role, CORE-014 tra user là hợp đồng nháp hiện có; không chứng minh đã hỗ trợ đầy đủ principal khách/guest.

| Dependency contract logic | Producer / consumer | Đầu vào tối thiểu và kiểm tại ranh giới | Gap / failure |
| :--- | :--- | :--- | :--- |
| Customer reference | Master Nền tảng → E6 | customerId tồn tại, tên hiển thị, trạng thái được phép phục vụ, source/version | Chưa write/read customer master được đặc tả; owner/quyền tạo chờ ORD-Q03/11; không lấy API026 tạo điểm thay tạo khách |
| Account provisioning | AUTH → API-ORD-006 | userId tồn tại, trạng thái, role eligibility, credential phát qua luồng AUTH; không đưa mật khẩu vào Grant | customer binding/scope nhiều khách còn mở; CORE-007 thành công không tự cấp quyền order |
| Grant scoped | API-ORD-006 → authorize E6 | customerId/userId/pointIds/version; mọi point thuộc customer; kiểm actor được cấp quyền tại lúc ghi | Không auto-grant bằng tên/mã nhân viên; ngoài scope404/thiếu quyền403; policy chưa cấu hình503 |
| Service readiness | API-ORD-013/014/026 → chọn/chốt | point→customer→kitchen, lịch ca/ngày và version; quota/menu được công bố | Thiếu master không tạo điểm mồ côi; quan hệ sai422-04; lịch hiệu lực/đổi bếp ORD-Q03 |
| Membership identity | Danh sách được quản lý xác nhận → E6 | Logical member reference, customer/point, trạng thái, provenance xác nhận; account/guest binding cần bằng chứng | E6-EVID-001 chỉ xác nhận có danh sách; chưa chọn khóa hay credential; không merge theo tên/phone giống nhau |

Trình tự review: có customer reference → account hợp lệ → grant → service context/quota/menu → identity policy → cho chọn/chốt. Nếu account tạo thành công nhưng grant lỗi, giữ account chưa có quyền E6, retry grant bằng key/receipt; không tự xóa account hoặc cấp role rộng để bù. Chưa định nghĩa distributed transaction giữa AUTH/E6. QA dùng ID synthetic qua adapter test, không phải bản ghi khách thật hoặc migration. Không mở CRM E10, hợp đồng thương mại hay dữ liệu sức khỏe.

## Review adapter ngày 11/11/2026

[Adapter E1/MENU/NUTR→E6](../api/adapter-contract-review.md) chỉ ra envelope chưa thống nhất, Calculation provenance đa revision và thiếu cơ chế refresh/cache được duyệt. GET E6 không ngầm tạo Calculation qua POST nội bộ; principal/quyền service và mapping lỗi dependency cần review. NUTR-Q03/E1-Q01/ORD-Q04/12 tiếp tục mở.
