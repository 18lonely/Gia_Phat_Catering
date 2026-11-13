---
id: DOC-E6-USERSTORIES-ACCEPTANCE-CRITERIA
title: 57 AC Given / When / Then E6
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# 57 AC Given / When / Then E6

**Draft để review · 11/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |

Mọi số liệu ví dụ là **synthetic**. Với nghiệp vụ còn mở, Then là **kỳ vọng đề xuất để review**, không phải quyết định đã duyệt. AC của FEAT-046/047 chỉ kiểm gate; happy path nghiệp vụ sức khỏe vẫn BLOCKED O-03.

## US-E6-001: Cấp quyền người đặt tổng

FR-AUTH-EXT-001; FEAT-030 / P0; gate ORD-Q01.

### AC-E6-001-1: Thành công có điều kiện / gate

```gherkin
Scenario: Cấp quyền người đặt tổng (thành công có điều kiện / gate)
  Given nhân viên được cấp quyền quản trị khách A và hợp đồng hợp lệ
  When cấp vai trò người đặt tổng cho user U ở A
  Then tài khoản chỉ có quyền A; audit ghi người cấp và phạm vi
```

### AC-E6-001-2: Lỗi nghiệp vụ

```gherkin
Scenario: Cấp quyền người đặt tổng (lỗi nghiệp vụ)
  Given U là người đặt tổng A
  When U cấp quyền nội bộ cho mình
  Then 403 ERR-ORD-403-01; không thay user_roles
```

### AC-E6-001-3: Biên và bảo mật

```gherkin
Scenario: Cấp quyền người đặt tổng (biên và bảo mật)
  Given quản trị chỉ được giao A
  When gửi customerId B
  Then 404 ERR-ORD-404-01; không tiết lộ B
```

## US-E6-002: Đăng ký qua QR công ty

FR-AUTH-QREG-001; FEAT-031 / P0; gate ORD-Q01.

### AC-E6-002-1: Thành công có điều kiện / gate

```gherkin
Scenario: Đăng ký qua QR công ty (thành công có điều kiện / gate)
  Given QR A ACTIVE và identity policy đã được duyệt
  When xác minh và đăng ký với identity hợp lệ
  Then liên kết eater với tài khoản và A; không cấp quyền người đặt tổng
```

### AC-E6-002-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đăng ký qua QR công ty (lỗi nghiệp vụ)
  Given QR đã ROTATED
  When đăng ký bằng token cũ
  Then 401 ERR-ORD-401-01; không tạo eater
```

### AC-E6-002-3: Biên và bảo mật

```gherkin
Scenario: Đăng ký qua QR công ty (biên và bảo mật)
  Given identity đã có trên thiết bị khác
  When đăng ký lần nữa
  Then kết quả theo ORD-Q01; không tuyên bố cookie ngăn trùng người
```

## US-E6-003: Mở phiên QR giới hạn

FR-AUTH-QSES-001; FEAT-032 / P0; gate ORD-Q01.

### AC-E6-003-1: Thành công có điều kiện / gate

```gherkin
Scenario: Mở phiên QR giới hạn (thành công có điều kiện / gate)
  Given QR A ACTIVE, policy định danh đã chốt
  When mở phiên guest ngày 2026-11-16 tại điểm A1
  Then phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần
```

### AC-E6-003-2: Lỗi nghiệp vụ

```gherkin
Scenario: Mở phiên QR giới hạn (lỗi nghiệp vụ)
  Given phiên guest thuộc A1 ngày 16
  When gọi ngày 17 hoặc điểm B1
  Then 404 ERR-ORD-404-01; không trả thực đơn ngoài scope
```

### AC-E6-003-3: Biên và bảo mật

```gherkin
Scenario: Mở phiên QR giới hạn (biên và bảo mật)
  Given phiên đã hết hạn
  When gửi lựa chọn
  Then 401 ERR-ORD-401-01; không tăng bộ đếm
```

## US-E6-004: Quản lý QR và danh sách người ăn

FR-AUTH-QRM-001; FEAT-033 / P0; gate ORD-Q02.

### AC-E6-004-1: Thành công có điều kiện / gate

```gherkin
Scenario: Quản lý QR và danh sách người ăn (thành công có điều kiện / gate)
  Given người đặt tổng A có QR ACTIVE version hiện tại
  When quay vòng QR với lý do
  Then token cũ ROTATED; chỉ trả token mới một lần; lịch sử giữ nguyên
```

### AC-E6-004-2: Lỗi nghiệp vụ

```gherkin
Scenario: Quản lý QR và danh sách người ăn (lỗi nghiệp vụ)
  Given danh sách thuộc khách B
  When người đặt tổng A đọc danh sách
  Then 404 ERR-ORD-404-01; không lộ tên người ăn B
```

### AC-E6-004-3: Biên và bảo mật

```gherkin
Scenario: Quản lý QR và danh sách người ăn (biên và bảo mật)
  Given eater đã có order khóa
  When gỡ eater
  Then giữ lịch sử; tác động phiên/lựa chọn chưa khóa BLOCKED ORD-Q02
```

## US-E6-005: Quản lý dữ liệu phục vụ

FR-CUS-SVC-001; FEAT-034 / P0; gate ORD-Q03.

### AC-E6-005-1: Thành công có điều kiện / gate

```gherkin
Scenario: Quản lý dữ liệu phục vụ (thành công có điều kiện / gate)
  Given DDV được phân công khách A
  When lưu điểm A1, bếp K1 và lịch thứ Hai ca LUNCH
  Then điểm thuộc A, lịch duy nhất theo điểm/ca/thứ, version tăng
```

### AC-E6-005-2: Lỗi nghiệp vụ

```gherkin
Scenario: Quản lý dữ liệu phục vụ (lỗi nghiệp vụ)
  Given A1 thuộc A
  When lưu lịch với customer B
  Then 422 ERR-ORD-422-04; không tạo quan hệ chéo khách
```

### AC-E6-005-3: Biên và bảo mật

```gherkin
Scenario: Quản lý dữ liệu phục vụ (biên và bảo mật)
  Given order cũ khóa ở K1
  When đề xuất đổi bếp sang K2
  Then snapshot cũ giữ K1; hiệu lực tương lai chờ ORD-Q03
```

## US-E6-006: Đặt định mức công ty

FR-ORD-QTA-001; FEAT-035 / P0; gate ORD-Q04.

### AC-E6-006-1: Thành công có điều kiện / gate

```gherkin
Scenario: Đặt định mức công ty (thành công có điều kiện / gate)
  Given loại suất đã duyệt và policy hiệu lực đã xác nhận
  When người đặt tổng lưu định mức chung
  Then version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người
```

### AC-E6-006-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đặt định mức công ty (lỗi nghiệp vụ)
  Given chưa có định mức hiệu lực
  When người ăn chọn món
  Then 422 ERR-ORD-422-01; không ghi lựa chọn
```

### AC-E6-006-3: Biên và bảo mật

```gherkin
Scenario: Đặt định mức công ty (biên và bảo mật)
  Given đã có lựa chọn theo quota v1
  When lưu quota v2 giữa ngày
  Then không âm thầm tính lại v1; xử lý theo ORD-Q04
```

## US-E6-007: Chọn và đổi một món chính

FR-ORD-SEL-001; FEAT-036 / P0; gate ORD-Q01, ORD-Q04.

### AC-E6-007-1: Thành công có điều kiện / gate

```gherkin
Scenario: Chọn và đổi một món chính (thành công có điều kiện / gate)
  Given eater E chọn A version 1 trước hạn, giá tổ hợp B hợp lệ
  When đổi A sang B version 1 và replay cùng key/body
  Then version 2; A giảm 1, B tăng 1 đúng một lần
```

### AC-E6-007-2: Lỗi nghiệp vụ

```gherkin
Scenario: Chọn và đổi một món chính (lỗi nghiệp vụ)
  Given định mức synthetic 40000đ, tổ hợp 40001đ
  When gửi chọn tổ hợp
  Then 422 ERR-ORD-422-01; lựa chọn/counter không đổi
```

### AC-E6-007-3: Biên và bảo mật

```gherkin
Scenario: Chọn và đổi một món chính (biên và bảo mật)
  Given định mức synthetic 40000đ, tổ hợp đúng 40000đ và đủ cơ cấu
  When gửi chọn trước hạn với version hiện tại
  Then được nhận; không yêu cầu người ăn bù tiền
```

## US-E6-008: Gửi lựa chọn cả tuần

FR-ORD-WEEK-001; FEAT-037 / P1; gate ORD-Q05.

### AC-E6-008-1: Thành công có điều kiện / gate

```gherkin
Scenario: Gửi lựa chọn cả tuần (thành công có điều kiện / gate)
  Given tài khoản có 5 ngày công bố còn mở, ORD-Q05 đã chốt
  When gửi lựa chọn tuần kèm version từng ngày
  Then trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt
```

### AC-E6-008-2: Lỗi nghiệp vụ

```gherkin
Scenario: Gửi lựa chọn cả tuần (lỗi nghiệp vụ)
  Given guest QR chỉ có phạm vi ngày
  When gửi lựa chọn tuần
  Then 403 ERR-ORD-403-01; không ghi ngày nào
```

### AC-E6-008-3: Biên và bảo mật

```gherkin
Scenario: Gửi lựa chọn cả tuần (biên và bảo mật)
  Given 4 ngày hợp lệ và 1 ngày đã khóa
  When gửi tuần
  Then không báo thành công toàn tuần; atomic rollback hoặc partial receipt chờ ORD-Q05
```

## US-E6-009: Chốt tổng suất và phân bổ

FR-ORD-SUB-001; FEAT-038 / P0; gate ORD-Q06.

### AC-E6-009-1: Thành công có điều kiện / gate

```gherkin
Scenario: Chốt tổng suất và phân bổ (thành công có điều kiện / gate)
  Given synthetic S=60,C=10,T=100 và ORD-Q06 đã duyệt
  When gửi tổng
  Then SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa
```

### AC-E6-009-2: Lỗi nghiệp vụ

```gherkin
Scenario: Chốt tổng suất và phân bổ (lỗi nghiệp vụ)
  Given synthetic S=60,C=10,T=65
  When gửi tổng
  Then đề xuất 422 ERR-ORD-422-02; không xóa 5 lựa chọn; chờ ORD-Q06
```

### AC-E6-009-3: Biên và bảo mật

```gherkin
Scenario: Chốt tổng suất và phân bổ (biên và bảo mật)
  Given synthetic S=60,C=10,T=70
  When gửi tổng rồi khóa đủ điều kiện
  Then D=0; không tạo dòng default ảo
```

## US-E6-010: Gán món mặc định khi khóa

FR-ORD-DEF-001; FEAT-039 / P0; gate ORD-Q06, ORD-Q07.

### AC-E6-010-1: Thành công có điều kiện / gate

```gherkin
Scenario: Gán món mặc định khi khóa (thành công có điều kiện / gate)
  Given synthetic T=100,S=60,C=10; default A hợp lệ
  When scheduler khóa
  Then D=30 cho A; MAIN tổng 100; không tạo 30 eater giả
```

### AC-E6-010-2: Lỗi nghiệp vụ

```gherkin
Scenario: Gán món mặc định khi khóa (lỗi nghiệp vụ)
  Given default không thuộc MAIN ngày công bố
  When scheduler khóa
  Then 422 ERR-ORD-422-03; không phát hành kế hoạch
```

### AC-E6-010-3: Biên và bảo mật

```gherkin
Scenario: Gán món mặc định khi khóa (biên và bảo mật)
  Given chưa có total; có 100 người đăng ký
  When scheduler khóa
  Then total vẫn chưa xác định; không tự coi T=100; xử lý ORD-Q07
```

## US-E6-011: Khóa tại hạn và phát hành nguồn kế hoạch

FR-ORD-LOCK-001; FEAT-040 / P0; gate Q-16, ORD-Q07.

### AC-E6-011-1: Thành công có điều kiện / gate

```gherkin
Scenario: Khóa tại hạn và phát hành nguồn kế hoạch (thành công có điều kiện / gate)
  Given đã gửi tổng và đủ snapshot, deadline cấu hình hợp lệ
  When scheduler khóa scope điểm/ngày/ca
  Then order LOCKED; một revision và một outbox event bền vững
```

### AC-E6-011-2: Lỗi nghiệp vụ

```gherkin
Scenario: Khóa tại hạn và phát hành nguồn kế hoạch (lỗi nghiệp vụ)
  Given clock server đúng bằng deadline
  When người ăn gửi PUT
  Then đề xuất 409 ERR-ORD-409-01; không ghi; biên deadline chờ ORD-Q07
```

### AC-E6-011-3: Biên và bảo mật

```gherkin
Scenario: Khóa tại hạn và phát hành nguồn kế hoạch (biên và bảo mật)
  Given lock event đã xử lý, worker mất phản hồi
  When retry cùng eventKey
  Then trả revision cũ; không tăng plan revision lần hai
```

## US-E6-012: Đề nghị và duyệt thay đổi sau khóa

FR-ORD-CHG-001; FEAT-041 / P0; gate Q-16, O-06, ORD-Q08.

### AC-E6-012-1: Thành công có điều kiện / gate

```gherkin
Scenario: Đề nghị và duyệt thay đổi sau khóa (thành công có điều kiện / gate)
  Given order LOCKED rev1; ngưỡng và người duyệt đã chốt
  When người khác người tạo/sửa cuối duyệt delta hợp lệ
  Then tạo rev2, giữ rev1; bếp nhận delta có nguồn rev2
```

### AC-E6-012-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đề nghị và duyệt thay đổi sau khóa (lỗi nghiệp vụ)
  Given đề nghị PENDING do U tạo
  When U tự duyệt
  Then 403 ERR-ORD-403-01; order vẫn rev1
```

### AC-E6-012-3: Biên và bảo mật

```gherkin
Scenario: Đề nghị và duyệt thay đổi sau khóa (biên và bảo mật)
  Given đề nghị dựa rev1 nhưng hiện hành rev2
  When duyệt đề nghị cũ
  Then 409 ERR-ORD-409-01; không áp delta lên sai baseline
```

## US-E6-013: Điều phối nhập hộ

FR-ORD-PXY-001; FEAT-042 / P0; gate ORD-Q06.

### AC-E6-013-1: Thành công có điều kiện / gate

```gherkin
Scenario: Điều phối nhập hộ (thành công có điều kiện / gate)
  Given DDV được giao A có chứng cứ synthetic điện thoại
  When nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason
  Then order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân
```

### AC-E6-013-2: Lỗi nghiệp vụ

```gherkin
Scenario: Điều phối nhập hộ (lỗi nghiệp vụ)
  Given người ăn tự chọn có phiên hợp lệ
  When gửi source ZALO để giả vai DDV
  Then 403 ERR-ORD-403-01; không ghi order
```

### AC-E6-013-3: Biên và bảo mật

```gherkin
Scenario: Điều phối nhập hộ (biên và bảo mật)
  Given người đặt tổng và DDV cùng đọc version 1
  When cả hai gửi tổng
  Then một commit version 2; bên sau 409; không ghi đè mù
```

## US-E6-014: Nhắc người chưa chọn

FR-ORD-REM-001; FEAT-043 / P1; gate Q-14.

### AC-E6-014-1: Thành công có điều kiện / gate

```gherkin
Scenario: Nhắc người chưa chọn (thành công có điều kiện / gate)
  Given kênh đã được duyệt, người nhận có định danh và còn đủ điều kiện
  When scheduler lập nhắc trước hạn
  Then chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi
```

### AC-E6-014-2: Lỗi nghiệp vụ

```gherkin
Scenario: Nhắc người chưa chọn (lỗi nghiệp vụ)
  Given Q-14 chưa chốt hoặc thiếu cấu hình kênh
  When job nhắc chạy
  Then BLOCKED_CONFIGURATION; không gọi SMS/Zalo/email
```

### AC-E6-014-3: Biên và bảo mật

```gherkin
Scenario: Nhắc người chưa chọn (biên và bảo mật)
  Given event nhắc đã thành công
  When worker nhận lại eventId
  Then không gửi lần hai; đối soát kết quả không tạo thông báo trùng
```

## US-E6-015: Đổi chế độ chọn món

FR-ORD-MODE-001; FEAT-044 / P1; gate ORD-Q09.

### AC-E6-015-1: Thành công có điều kiện / gate

```gherkin
Scenario: Đổi chế độ chọn món (thành công có điều kiện / gate)
  Given khách chưa có lựa chọn và policy ngày hiệu lực đã duyệt
  When người đặt tổng tắt chọn món
  Then người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền
```

### AC-E6-015-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đổi chế độ chọn món (lỗi nghiệp vụ)
  Given khách đã tắt chọn từ đầu ngày
  When người ăn PUT trực tiếp
  Then 409 ERR-ORD-409-01; không thay số suất
```

### AC-E6-015-3: Biên và bảo mật

```gherkin
Scenario: Đổi chế độ chọn món (biên và bảo mật)
  Given đã có 60 lựa chọn
  When đề nghị tắt giữa ngày
  Then giữ 60 lựa chọn và lịch sử; tác động chờ ORD-Q09
```

## US-E6-016: Xem thông tin món công bố

FR-NUTR-DSP-001; FEAT-045 / P0; gate NUTR-Q03.

### AC-E6-016-1: Thành công có điều kiện / gate

```gherkin
Scenario: Xem thông tin món công bố (thành công có điều kiện / gate)
  Given món thuộc menu PUBLISHED có nguồn dinh dưỡng đủ
  When người ăn mở chi tiết
  Then hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính
```

### AC-E6-016-2: Lỗi nghiệp vụ

```gherkin
Scenario: Xem thông tin món công bố (lỗi nghiệp vụ)
  Given thiếu dữ liệu dinh dưỡng một nguyên liệu
  When mở tổ hợp
  Then totals=null và lý do thiếu; không hiển thị 0 như kết quả thật
```

### AC-E6-016-3: Biên và bảo mật

```gherkin
Scenario: Xem thông tin món công bố (biên và bảo mật)
  Given client dò field cost và id khách khác
  When gọi available-meals
  Then DTO chỉ allowlist; ngoài scope 404; lỗi không lộ cost/giá nhập
```

## US-E6-017: Giữ cổng hồ sơ sức khỏe

FR-NUTR-PROF-001; FEAT-046 / P1; gate O-03.

### AC-E6-017-1: Thành công có điều kiện / gate

```gherkin
Scenario: Giữ cổng hồ sơ sức khỏe (thành công có điều kiện / gate)
  Given O-03 còn mở
  When người dùng mở hồ sơ
  Then thấy chưa mở tính năng; không có form hoặc request thu sức khỏe
```

### AC-E6-017-2: Lỗi nghiệp vụ

```gherkin
Scenario: Giữ cổng hồ sơ sức khỏe (lỗi nghiệp vụ)
  Given client cố gửi bệnh lý khi gate đóng
  When gọi đường ghi chưa công bố
  Then không ghi dữ liệu; không tạo consent ngầm; contract chưa mở
```

### AC-E6-017-3: Biên và bảo mật

```gherkin
Scenario: Giữ cổng hồ sơ sức khỏe (biên và bảo mật)
  Given người dùng không đồng ý hoặc rút đồng ý trong thiết kế tương lai
  When review hồ sơ
  Then chưa được thu thập; tiêu chí xóa/lưu vết cần O-03 và ORD-Q15
```

## US-E6-018: Giữ cổng gợi ý cá nhân

FR-NUTR-REC-001; FEAT-047 / P1; gate O-03.

### AC-E6-018-1: Thành công có điều kiện / gate

```gherkin
Scenario: Giữ cổng gợi ý cá nhân (thành công có điều kiện / gate)
  Given O-03 còn mở
  When người ăn mở gợi ý
  Then tính năng chưa mở; chọn món thủ công vẫn có theo quyền
```

### AC-E6-018-2: Lỗi nghiệp vụ

```gherkin
Scenario: Giữ cổng gợi ý cá nhân (lỗi nghiệp vụ)
  Given không có consent/hồ sơ hợp lệ
  When yêu cầu suy bệnh từ lịch sử chọn
  Then không suy diễn và không tự tạo hồ sơ
```

### AC-E6-018-3: Biên và bảo mật

```gherkin
Scenario: Giữ cổng gợi ý cá nhân (biên và bảo mật)
  Given gợi ý tương lai được duyệt
  When review hành vi áp dụng
  Then phải có lựa chọn tường minh; không tự ghi selection hoặc đổi order
```

## US-E6-019: Đọc kế hoạch sản xuất phiên bản

FR-PLAN-MEAL-001; FEAT-048 / P0; gate ORD-Q10.

### AC-E6-019-1: Thành công có điều kiện / gate

```gherkin
Scenario: Đọc kế hoạch sản xuất phiên bản (thành công có điều kiện / gate)
  Given 2 order khóa cùng bếp/ca, MAIN A lần lượt 60 và 40
  When worker tổng hợp và bếp đọc kế hoạch
  Then A=100; hiện source revision từng order, plan revision và thời điểm
```

### AC-E6-019-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đọc kế hoạch sản xuất phiên bản (lỗi nghiệp vụ)
  Given bếp K1 yêu cầu kế hoạch K2
  When GET theo id K2
  Then 404 ERR-ORD-404-01; không lộ tổng K2
```

### AC-E6-019-3: Biên và bảo mật

```gherkin
Scenario: Đọc kế hoạch sản xuất phiên bản (biên và bảo mật)
  Given một nguồn đổi rev1 sang rev2 tăng A 5 suất
  When tạo kế hoạch kế tiếp
  Then A tăng 5 đúng một lần; plan cũ bất biến; không cộng cả hai source revisions
```

