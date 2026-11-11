---
id: DOC-E6-TEST-REVIEW-TEST-CASES
title: 57 ca thiết kế liên kết AC E6
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# 57 ca thiết kế liên kết AC E6

**Draft để review · 11/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

Giữ nguyên [10 ca khởi đầu](test-cases.md). Bộ dưới đây bổ sung 57 ca liên kết AC; không cộng 10 ca cũ thành độ phủ độc lập vì có mục tiêu trùng. **Actual/Evidence: chưa có cho tất cả ca. Không ca nào PASS phần mềm.**

Quy trình theo loại thao tác (làm rõ 12/11/2026): tạo fixture **synthetic** theo Given trong môi trường test; dùng actor/principal và contract ở UC. Ca ghi HTTP mới dùng Idempotency-Key/version theo route và đối soát resource/audit; ca GET kiểm DTO/scope, dữ liệu nghiệp vụ không đổi, không đòi receipt hoặc commit. Ca worker gọi port/event bằng service principal có scope, đối soát eventKey/eventId, outcome và outbox; không đăng nhập UI thay service. Vận hành chỉ đọc kết quả qua route GET đã có. Ca gate kiểm không có form/request thu sức khỏe, không gọi endpoint chưa công bố. Lưu evidence phù hợp từng loại; chưa thực thi trong phiên BA này.

TC-E6-019-1/3 và AC tương ứng là ca liên thông producer+read: worker chuẩn bị revision từ event trước, bếp GET sau; GET không kích hoạt tổng hợp. TC-E6-001-1 chỉ xét grant phạm vi A của yêu cầu synthetic, không kết luận tài khoản chỉ thuộc một công ty. TC-E6-010/011 dùng cùng PORT-LOCK, không cộng hai lần khóa. Cách diễn giải đối chiếu [ma trận UC](../review/uc-operation-review.md); giữ nguyên toàn bộ dòng ca và Status bên dưới.

## US-E6-001 / UC-ORD-001

API/port: API-ORD-006, API-ORD-007; UI-ORD-01. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-001-1 / AC-E6-001-1 | nhân viên được cấp quyền quản trị khách A và hợp đồng hợp lệ | cấp vai trò người đặt tổng cho user U ở A | tài khoản chỉ có quyền A; audit ghi người cấp và phạm vi | BLOCKED ORD-Q01 |
| TC-E6-001-2 / AC-E6-001-2 | U là người đặt tổng A | U cấp quyền nội bộ cho mình | 403 ERR-ORD-403-01; không thay user_roles | NOT RUN |
| TC-E6-001-3 / AC-E6-001-3 | quản trị chỉ được giao A | gửi customerId B | 404 ERR-ORD-404-01; không tiết lộ B | NOT RUN |

## US-E6-002 / UC-ORD-002

API/port: API-ORD-008; UI-ORD-02. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-002-1 / AC-E6-002-1 | QR A ACTIVE và identity policy đã được duyệt | xác minh và đăng ký với identity hợp lệ | liên kết eater với tài khoản và A; không cấp quyền người đặt tổng | BLOCKED ORD-Q01 |
| TC-E6-002-2 / AC-E6-002-2 | QR đã ROTATED | đăng ký bằng token cũ | 401 ERR-ORD-401-01; không tạo eater | NOT RUN |
| TC-E6-002-3 / AC-E6-002-3 | identity đã có trên thiết bị khác | đăng ký lần nữa | kết quả theo ORD-Q01; không tuyên bố cookie ngăn trùng người | BLOCKED ORD-Q01 |

## US-E6-003 / UC-ORD-003

API/port: API-ORD-009; UI-ORD-02. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-003-1 / AC-E6-003-1 | QR A ACTIVE, policy định danh đã chốt | mở phiên guest ngày 2026-11-16 tại điểm A1 | phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần | BLOCKED ORD-Q01 |
| TC-E6-003-2 / AC-E6-003-2 | phiên guest thuộc A1 ngày 16 | gọi ngày 17 hoặc điểm B1 | 404 ERR-ORD-404-01; không trả thực đơn ngoài scope | NOT RUN |
| TC-E6-003-3 / AC-E6-003-3 | phiên đã hết hạn | gửi lựa chọn | 401 ERR-ORD-401-01; không tăng bộ đếm | NOT RUN |

## US-E6-004 / UC-ORD-004

API/port: API-ORD-010, API-ORD-011, API-ORD-012; UI-ORD-03. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-004-1 / AC-E6-004-1 | người đặt tổng A có QR ACTIVE version hiện tại | quay vòng QR với lý do | token cũ ROTATED; chỉ trả token mới một lần; lịch sử giữ nguyên | BLOCKED ORD-Q02 |
| TC-E6-004-2 / AC-E6-004-2 | danh sách thuộc khách B | người đặt tổng A đọc danh sách | 404 ERR-ORD-404-01; không lộ tên người ăn B | NOT RUN |
| TC-E6-004-3 / AC-E6-004-3 | eater đã có order khóa | gỡ eater | giữ lịch sử; tác động phiên/lựa chọn chưa khóa BLOCKED ORD-Q02 | BLOCKED ORD-Q02 |

## US-E6-005 / UC-ORD-005

API/port: API-ORD-013, API-ORD-014, API-ORD-026; UI-ORD-04. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-005-1 / AC-E6-005-1 | DDV được phân công khách A | lưu điểm A1, bếp K1 và lịch thứ Hai ca LUNCH | điểm thuộc A, lịch duy nhất theo điểm/ca/thứ, version tăng | BLOCKED ORD-Q03 |
| TC-E6-005-2 / AC-E6-005-2 | A1 thuộc A | lưu lịch với customer B | 422 ERR-ORD-422-04; không tạo quan hệ chéo khách | NOT RUN |
| TC-E6-005-3 / AC-E6-005-3 | order cũ khóa ở K1 | đề xuất đổi bếp sang K2 | snapshot cũ giữ K1; hiệu lực tương lai chờ ORD-Q03 | BLOCKED ORD-Q03 |

## US-E6-006 / UC-ORD-006

API/port: API-ORD-015, API-ORD-016; UI-ORD-05. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-006-1 / AC-E6-006-1 | loại suất đã duyệt và policy hiệu lực đã xác nhận | người đặt tổng lưu định mức chung | version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người | BLOCKED ORD-Q04 |
| TC-E6-006-2 / AC-E6-006-2 | chưa có định mức hiệu lực | người ăn chọn món | 422 ERR-ORD-422-01; không ghi lựa chọn | NOT RUN |
| TC-E6-006-3 / AC-E6-006-3 | đã có lựa chọn theo quota v1 | lưu quota v2 giữa ngày | không âm thầm tính lại v1; xử lý theo ORD-Q04 | BLOCKED ORD-Q04 |

## US-E6-007 / UC-ORD-007

API/port: API-ORD-001, API-ORD-002, API-ORD-017; UI-ORD-06. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-007-1 / AC-E6-007-1 | eater E chọn A version 1 trước hạn, giá tổ hợp B hợp lệ | đổi A sang B version 1 và replay cùng key/body | version 2; A giảm 1, B tăng 1 đúng một lần | BLOCKED ORD-Q01, ORD-Q04 |
| TC-E6-007-2 / AC-E6-007-2 | định mức synthetic 40000đ, tổ hợp 40001đ | gửi chọn tổ hợp | 422 ERR-ORD-422-01; lựa chọn/counter không đổi | NOT RUN |
| TC-E6-007-3 / AC-E6-007-3 | định mức synthetic 40000đ, tổ hợp đúng 40000đ và đủ cơ cấu | gửi chọn trước hạn với version hiện tại | được nhận; không yêu cầu người ăn bù tiền | NOT RUN |

## US-E6-008 / UC-ORD-008

API/port: API-ORD-018; UI-ORD-07. Priority P1.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-008-1 / AC-E6-008-1 | tài khoản có 5 ngày công bố còn mở, ORD-Q05 đã chốt | gửi lựa chọn tuần kèm version từng ngày | trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt | BLOCKED ORD-Q05 |
| TC-E6-008-2 / AC-E6-008-2 | guest QR chỉ có phạm vi ngày | gửi lựa chọn tuần | 403 ERR-ORD-403-01; không ghi ngày nào | NOT RUN |
| TC-E6-008-3 / AC-E6-008-3 | 4 ngày hợp lệ và 1 ngày đã khóa | gửi tuần | không báo thành công toàn tuần; atomic rollback hoặc partial receipt chờ ORD-Q05 | BLOCKED ORD-Q05 |

## US-E6-009 / UC-ORD-009

API/port: API-ORD-003, API-ORD-004, API-ORD-019; UI-ORD-08. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-009-1 / AC-E6-009-1 | synthetic S=60,C=10,T=100 và ORD-Q06 đã duyệt | gửi tổng | SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa | BLOCKED ORD-Q06 |
| TC-E6-009-2 / AC-E6-009-2 | synthetic S=60,C=10,T=65 | gửi tổng | đề xuất 422 ERR-ORD-422-02; không xóa 5 lựa chọn; chờ ORD-Q06 | BLOCKED ORD-Q06 |
| TC-E6-009-3 / AC-E6-009-3 | synthetic S=60,C=10,T=70 | gửi tổng rồi khóa đủ điều kiện | D=0; không tạo dòng default ảo | NOT RUN |

## US-E6-010 / UC-ORD-010

API/port: PORT-LOCK; UI-ORD-09. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-010-1 / AC-E6-010-1 | synthetic T=100,S=60,C=10; default A hợp lệ | scheduler khóa | D=30 cho A; MAIN tổng 100; không tạo 30 eater giả | BLOCKED ORD-Q06, ORD-Q07 |
| TC-E6-010-2 / AC-E6-010-2 | default không thuộc MAIN ngày công bố | scheduler khóa | 422 ERR-ORD-422-03; không phát hành kế hoạch | NOT RUN |
| TC-E6-010-3 / AC-E6-010-3 | chưa có total; có 100 người đăng ký | scheduler khóa | total vẫn chưa xác định; không tự coi T=100; xử lý ORD-Q07 | BLOCKED ORD-Q06, ORD-Q07 |

## US-E6-011 / UC-ORD-011

API/port: PORT-LOCK, API-ORD-020; UI-ORD-09. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-011-1 / AC-E6-011-1 | đã gửi tổng và đủ snapshot, deadline cấu hình hợp lệ | scheduler khóa scope điểm/ngày/ca | order LOCKED; một revision và một outbox event bền vững | BLOCKED Q-16, ORD-Q07 |
| TC-E6-011-2 / AC-E6-011-2 | clock server đúng bằng deadline | người ăn gửi PUT | đề xuất 409 ERR-ORD-409-01; không ghi; biên deadline chờ ORD-Q07 | BLOCKED Q-16, ORD-Q07 |
| TC-E6-011-3 / AC-E6-011-3 | lock event đã xử lý, worker mất phản hồi | retry cùng eventKey | trả revision cũ; không tăng plan revision lần hai | NOT RUN |

## US-E6-012 / UC-ORD-012

API/port: API-ORD-005, API-ORD-021, API-ORD-022; UI-ORD-10. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-012-1 / AC-E6-012-1 | order LOCKED rev1; ngưỡng và người duyệt đã chốt | người khác người tạo/sửa cuối duyệt delta hợp lệ | tạo rev2, giữ rev1; bếp nhận delta có nguồn rev2 | BLOCKED Q-16, O-06, ORD-Q08 |
| TC-E6-012-2 / AC-E6-012-2 | đề nghị PENDING do U tạo | U tự duyệt | 403 ERR-ORD-403-01; order vẫn rev1 | NOT RUN |
| TC-E6-012-3 / AC-E6-012-3 | đề nghị dựa rev1 nhưng hiện hành rev2 | duyệt đề nghị cũ | 409 ERR-ORD-409-01; không áp delta lên sai baseline | NOT RUN |

## US-E6-013 / UC-ORD-013

API/port: API-ORD-003, API-ORD-004; UI-ORD-11. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-013-1 / AC-E6-013-1 | DDV được giao A có chứng cứ synthetic điện thoại | nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason | order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân | BLOCKED ORD-Q06 |
| TC-E6-013-2 / AC-E6-013-2 | người ăn tự chọn có phiên hợp lệ | gửi source ZALO để giả vai DDV | 403 ERR-ORD-403-01; không ghi order | NOT RUN |
| TC-E6-013-3 / AC-E6-013-3 | người đặt tổng và DDV cùng đọc version 1 | cả hai gửi tổng | một commit version 2; bên sau 409; không ghi đè mù | NOT RUN |

## US-E6-014 / UC-ORD-014

API/port: PORT-REM, API-ORD-023; UI-ORD-09. Priority P1.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-014-1 / AC-E6-014-1 | kênh đã được duyệt, người nhận có định danh và còn đủ điều kiện | scheduler lập nhắc trước hạn | chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi | BLOCKED Q-14 |
| TC-E6-014-2 / AC-E6-014-2 | Q-14 chưa chốt hoặc thiếu cấu hình kênh | job nhắc chạy | BLOCKED_CONFIGURATION; không gọi SMS/Zalo/email | NOT RUN |
| TC-E6-014-3 / AC-E6-014-3 | event nhắc đã thành công | worker nhận lại eventId | không gửi lần hai; đối soát kết quả không tạo thông báo trùng | NOT RUN |

## US-E6-015 / UC-ORD-015

API/port: API-ORD-024; UI-ORD-05. Priority P1.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-015-1 / AC-E6-015-1 | khách chưa có lựa chọn và policy ngày hiệu lực đã duyệt | người đặt tổng tắt chọn món | người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền | BLOCKED ORD-Q09 |
| TC-E6-015-2 / AC-E6-015-2 | khách đã tắt chọn từ đầu ngày | người ăn PUT trực tiếp | 409 ERR-ORD-409-01; không thay số suất | NOT RUN |
| TC-E6-015-3 / AC-E6-015-3 | đã có 60 lựa chọn | đề nghị tắt giữa ngày | giữ 60 lựa chọn và lịch sử; tác động chờ ORD-Q09 | BLOCKED ORD-Q09 |

## US-E6-016 / UC-ORD-016

API/port: API-ORD-001; UI-ORD-06. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-016-1 / AC-E6-016-1 | món thuộc menu PUBLISHED có nguồn dinh dưỡng đủ | người ăn mở chi tiết | hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính | NOT RUN |
| TC-E6-016-2 / AC-E6-016-2 | thiếu dữ liệu dinh dưỡng một nguyên liệu | mở tổ hợp | totals=null và lý do thiếu; không hiển thị 0 như kết quả thật | NOT RUN |
| TC-E6-016-3 / AC-E6-016-3 | client dò field cost và id khách khác | gọi available-meals | DTO chỉ allowlist; ngoài scope 404; lỗi không lộ cost/giá nhập | NOT RUN |

## US-E6-017 / UC-ORD-017

API/port: GATE-046; UI-ORD-12. Priority P1.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-017-1 / AC-E6-017-1 | O-03 còn mở | người dùng mở hồ sơ | thấy chưa mở tính năng; không có form hoặc request thu sức khỏe | NOT RUN |
| TC-E6-017-2 / AC-E6-017-2 | client cố gửi bệnh lý khi gate đóng | gọi đường ghi chưa công bố | không ghi dữ liệu; không tạo consent ngầm; contract chưa mở | NOT RUN |
| TC-E6-017-3 / AC-E6-017-3 | người dùng không đồng ý hoặc rút đồng ý trong thiết kế tương lai | review hồ sơ | chưa được thu thập; tiêu chí xóa/lưu vết cần O-03 và ORD-Q15 | BLOCKED O-03 |

## US-E6-018 / UC-ORD-018

API/port: GATE-047; UI-ORD-12. Priority P1.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-018-1 / AC-E6-018-1 | O-03 còn mở | người ăn mở gợi ý | tính năng chưa mở; chọn món thủ công vẫn có theo quyền | NOT RUN |
| TC-E6-018-2 / AC-E6-018-2 | không có consent/hồ sơ hợp lệ | yêu cầu suy bệnh từ lịch sử chọn | không suy diễn và không tự tạo hồ sơ | NOT RUN |
| TC-E6-018-3 / AC-E6-018-3 | gợi ý tương lai được duyệt | review hành vi áp dụng | phải có lựa chọn tường minh; không tự ghi selection hoặc đổi order | BLOCKED O-03 |

## US-E6-019 / UC-ORD-019

API/port: API-ORD-020, API-ORD-025; UI-ORD-13. Priority P0.

| TC / AC | Given — fixture / tiền điều kiện | When — thao tác | Then — expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-019-1 / AC-E6-019-1 | 2 order khóa cùng bếp/ca, MAIN A lần lượt 60 và 40 | worker tổng hợp và bếp đọc kế hoạch | A=100; hiện source revision từng order, plan revision và thời điểm | BLOCKED ORD-Q10 |
| TC-E6-019-2 / AC-E6-019-2 | bếp K1 yêu cầu kế hoạch K2 | GET theo id K2 | 404 ERR-ORD-404-01; không lộ tổng K2 | NOT RUN |
| TC-E6-019-3 / AC-E6-019-3 | một nguồn đổi rev1 sang rev2 tăng A 5 suất | tạo kế hoạch kế tiếp | A tăng 5 đúng một lần; plan cũ bất biến; không cộng cả hai source revisions | NOT RUN |

