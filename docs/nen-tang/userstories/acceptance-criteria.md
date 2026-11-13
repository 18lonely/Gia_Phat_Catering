---
id: DOC-NEN-TANG-USERSTORIES-ACCEPTANCE-CRITERIA
title: AC E1
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# AC E1

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mọi scenario là thiết kế; dữ liệuU1/K1 và thời gian mô phỏng là fixture, không tài khoản thật.

## AC-CORE-001-1: US-CORE-001

```gherkin
Scenario: Đăng nhập nội bộ / 1
  Given Tài khoản ACTIVE U1; mật khẩu hợp lệ; chưa đủ5 lần sai
  When thực hiện đăng nhập nội bộ với input: tên đăng nhập, mật khẩu
  Then Xác thực nhân viên bằng tên đăng nhập và mật khẩu. Kiểm tra tài khoản đang hoạt động, chưa bị khoá. Ghi nhật ký đăng nhập cả khi thành công lẫn thất bại. Dạng tên đăng nhập: [N-01] Kết quả: access token, refresh token (cookie `HttpOnly`), hồ sơ người dùng, danh sách vai trò và phạm vi
```

FR-AUTH-LGN-001; NOT RUN.

## AC-CORE-001-2: US-CORE-001

```gherkin
Scenario: Đăng nhập nội bộ / 2
  Given Tài khoản ACTIVE U1; mật khẩu hợp lệ; chưa đủ5 lần sai
  When sai mật khẩu lần5
  Then 423 ERR-AUTH-423-01; khóa15 phút; log thất bại
```

FR-AUTH-LGN-001; NOT RUN.

## AC-CORE-001-3: US-CORE-001

```gherkin
Scenario: Đăng nhập nội bộ / 3
  Given Tài khoản ACTIVE U1; mật khẩu hợp lệ; chưa đủ5 lần sai
  When gửi11 lần/phút từ cùng IP
  Then 429 ERR-AUTH-429-01; không xác thực vượt giới hạn
```

FR-AUTH-LGN-001; NOT RUN.

## AC-CORE-002-1: US-CORE-002

```gherkin
Scenario: Làm mới phiên / 1
  Given U1 có refresh R1 chưa dùng và chưa hết7 ngày
  When thực hiện làm mới phiên với input: refresh token
  Then Đổi refresh token còn hạn lấy access token mới; refresh token cũ bị vô hiệu ngay (xoay vòng). Dùng lại refresh token đã vô hiệu → thu hồi mọi phiên của tài khoản. Kết quả: access token mới, refresh token mới
```

FR-AUTH-LGN-002; NOT RUN.

## AC-CORE-002-2: US-CORE-002

```gherkin
Scenario: Làm mới phiên / 2
  Given U1 có refresh R1 chưa dùng và chưa hết7 ngày
  When dùng lại R1 sau khi xoay thành R2
  Then 401 ERR-AUTH-401-02; thu hồi các phiên trong≤60 giây
```

FR-AUTH-LGN-002; NOT RUN.

## AC-CORE-002-3: US-CORE-002

```gherkin
Scenario: Làm mới phiên / 3
  Given U1 có refresh R1 chưa dùng và chưa hết7 ngày
  When hai request đồng thời dùng R1
  Then chỉ một refresh thành công; lần reuse kích hoạt thu hồi; client không gửi refresh song song
```

FR-AUTH-LGN-002; NOT RUN.

## AC-CORE-003-1: US-CORE-003

```gherkin
Scenario: Đăng xuất / 1
  Given U1 có hai phiên S1/S2
  When thực hiện đăng xuất với input: không áp dụng
  Then Thu hồi phiên hiện tại; tuỳ chọn thu hồi mọi phiên của mình. Kết quả: Phiên bị vô hiệu
```

FR-AUTH-LGN-003; NOT RUN.

## AC-CORE-003-2: US-CORE-003

```gherkin
Scenario: Đăng xuất / 2
  Given U1 có hai phiên S1/S2
  When dùng lại access token của phiên vừa logout sau thời hạn thu hồi
  Then 401 ERR-AUTH-401-02; không đọc nghiệp vụ
```

FR-AUTH-LGN-003; NOT RUN.

## AC-CORE-003-3: US-CORE-003

```gherkin
Scenario: Đăng xuất / 3
  Given U1 có hai phiên S1/S2
  When chọn allSessions=true
  Then cảS1/S2 bị thu hồi, logout lại không tạo tác dụng phụ
```

FR-AUTH-LGN-003; NOT RUN.

## AC-CORE-004-1: US-CORE-004

```gherkin
Scenario: Xác thực 2 bước / 1
  Given N-04 được chốt bật MFA, tài khoản GIAM_DOC có secret đã đăng ký
  When thực hiện xác thực 2 bước với input: mã 6 số
  Then Vai trò `GIAM_DOC`, `KT_DOANH_THU`, `QUAN_TRI` nhập thêm mã 6 số từ ứng dụng xác thực. Có làm hay không: [N-04] Kết quả: Như `FR-AUTH-LGN-001
```

FR-AUTH-LGN-004; BLOCKED: N-04, E1-Q03.

## AC-CORE-004-2: US-CORE-004

```gherkin
Scenario: Xác thực 2 bước / 2
  Given N-04 được chốt bật MFA, tài khoản GIAM_DOC có secret đã đăng ký
  When nhập mã6 số sai
  Then 401 ERR-AUTH-401-03; không cấp phiên đầy đủ
```

FR-AUTH-LGN-004; BLOCKED: N-04, E1-Q03.

## AC-CORE-004-3: US-CORE-004

```gherkin
Scenario: Xác thực 2 bước / 3
  Given N-04 được chốt bật MFA, tài khoản GIAM_DOC có secret đã đăng ký
  When mã đúng nhưng đã dùng trong bước xác thực trước
  Then không cho replay; cách đăng ký/recovery chờ E1-Q03
```

FR-AUTH-LGN-004; BLOCKED: N-04, E1-Q03.

## AC-CORE-005-1: US-CORE-005

```gherkin
Scenario: Đổi mật khẩu / 1
  Given U1 có phiênS1 vàS2, mật khẩu mới NewPass1234 chưa thuộc3 mật khẩu gần nhất
  When thực hiện đổi mật khẩu với input: mật khẩu cũ, mật khẩu mới
  Then Người dùng đổi mật khẩu của mình; phải nhập đúng mật khẩu hiện tại. Sau khi đổi, mọi phiên khác bị thu hồi. Kết quả: Xác nhận
```

FR-AUTH-PWD-001; NOT RUN.

## AC-CORE-005-2: US-CORE-005

```gherkin
Scenario: Đổi mật khẩu / 2
  Given U1 có phiênS1 vàS2, mật khẩu mới NewPass1234 chưa thuộc3 mật khẩu gần nhất
  When đặt mật khẩu9 ký tự hoặc thuộc3 mật khẩu gần nhất
  Then 422 ERR-AUTH-422-01; mật khẩu không đổi
```

FR-AUTH-PWD-001; NOT RUN.

## AC-CORE-005-3: US-CORE-005

```gherkin
Scenario: Đổi mật khẩu / 3
  Given U1 có phiênS1 vàS2, mật khẩu mới NewPass1234 chưa thuộc3 mật khẩu gần nhất
  When đổi thành công từS1 rồi gọi bằngS2
  Then S1 giữ, S2 thu hồi≤60 giây; không ghi mật khẩu/token vào audit
```

FR-AUTH-PWD-001; NOT RUN.

## AC-CORE-006-1: US-CORE-006

```gherkin
Scenario: Cấp lại mật khẩu / 1
  Given QUAN_TRI có quyền reset U1 và lý do10 ký tự
  When thực hiện cấp lại mật khẩu với input: mã tài khoản, lý do
  Then QUAN_TRI` cấp mật khẩu tạm cho một tài khoản. Mật khẩu tạm hết hạn sau 24 giờ và buộc đổi ở lần đăng nhập đầu. Kết quả: Mật khẩu tạm hiển thị một lần
```

FR-AUTH-PWD-002; NOT RUN.

## AC-CORE-006-2: US-CORE-006

```gherkin
Scenario: Cấp lại mật khẩu / 2
  Given QUAN_TRI có quyền reset U1 và lý do10 ký tự
  When reset userId không tồn tại
  Then 404 ERR-AUTH-404-01; không trả mật khẩu
```

FR-AUTH-PWD-002; NOT RUN.

## AC-CORE-006-3: US-CORE-006

```gherkin
Scenario: Cấp lại mật khẩu / 3
  Given QUAN_TRI có quyền reset U1 và lý do10 ký tự
  When dùng mật khẩu tạm sau24 giờ
  Then không đăng nhập; mật khẩu tạm chỉ hiển thị một lần, retry không trả lại secret
```

FR-AUTH-PWD-002; NOT RUN.

## AC-CORE-007-1: US-CORE-007

```gherkin
Scenario: Tạo tài khoản nội bộ / 1
  Given QUAN_TRI tạo Unew vai trò BEP_TRUONG cơ sởK1
  When thực hiện tạo tài khoản nội bộ với input: họ tên, tên đăng nhập, vai trò, cơ sở
  Then QUAN_TRI` tạo tài khoản, gán ít nhất 1 vai trò; vai trò `QL_CO_SO`, `BEP_TRUONG` bắt buộc gán ít nhất 1 cơ sở. Kết quả: Tài khoản ở trạng thái "chờ đổi mật khẩu"
```

FR-AUTH-ACC-001; NOT RUN.

## AC-CORE-007-2: US-CORE-007

```gherkin
Scenario: Tạo tài khoản nội bộ / 2
  Given QUAN_TRI tạo Unew vai trò BEP_TRUONG cơ sởK1
  When bỏ kitchenIds hoặc roles rỗng
  Then 422 ERR-AUTH-422-02; không tạo user/role một phần
```

FR-AUTH-ACC-001; NOT RUN.

## AC-CORE-007-3: US-CORE-007

```gherkin
Scenario: Tạo tài khoản nội bộ / 3
  Given QUAN_TRI tạo Unew vai trò BEP_TRUONG cơ sởK1
  When hai request tạo cùng tên đăng nhập
  Then một tài khoản được tạo; request còn lại409 ERR-AUTH-409-01
```

FR-AUTH-ACC-001; NOT RUN.

## AC-CORE-008-1: US-CORE-008

```gherkin
Scenario: Khoá / mở khoá tài khoản / 1
  Given QUAN_TRI, U1 đang ACTIVE có phiên đang dùng
  When thực hiện khoá / mở khoá tài khoản với input: mã tài khoản, lý do
  Then Khoá làm tài khoản không đăng nhập được và thu hồi mọi phiên trong ≤ 60 giây. Kết quả: Trạng thái mới
```

FR-AUTH-ACC-002; NOT RUN.

## AC-CORE-008-2: US-CORE-008

```gherkin
Scenario: Khoá / mở khoá tài khoản / 2
  Given QUAN_TRI, U1 đang ACTIVE có phiên đang dùng
  When bỏ lý do hoặc nhập9 ký tự
  Then 422 ERR-SYS-422-01; trạng thái không đổi
```

FR-AUTH-ACC-002; NOT RUN.

## AC-CORE-008-3: US-CORE-008

```gherkin
Scenario: Khoá / mở khoá tài khoản / 3
  Given QUAN_TRI, U1 đang ACTIVE có phiên đang dùng
  When khóa rồi thử API ở giây60
  Then mọi phiên bị thu hồi; mở khóa không hồi sinh phiên cũ
```

FR-AUTH-ACC-002; NOT RUN.

## AC-CORE-009-1: US-CORE-009

```gherkin
Scenario: Sửa vai trò và cơ sở / 1
  Given QUAN_TRI đổi U1 từ BEP_TRUONG K1 sangK2
  When thực hiện sửa vai trò và cơ sở với input: mã tài khoản, vai trò, cơ sở, lý do
  Then Thay đổi có hiệu lực ở yêu cầu kế tiếp của người dùng, không cần đăng nhập lại. Kết quả: Tài khoản đã cập nhật
```

FR-AUTH-ACC-003; NOT RUN.

## AC-CORE-009-2: US-CORE-009

```gherkin
Scenario: Sửa vai trò và cơ sở / 2
  Given QUAN_TRI đổi U1 từ BEP_TRUONG K1 sangK2
  When gửi version cũ
  Then 409 ERR-SYS-409-02; không ghi đè
```

FR-AUTH-ACC-003; NOT RUN.

## AC-CORE-009-3: US-CORE-009

```gherkin
Scenario: Sửa vai trò và cơ sở / 3
  Given QUAN_TRI đổi U1 từ BEP_TRUONG K1 sangK2
  When U1 gọi API K1 ngay yêu cầu kế tiếp
  Then 404 ERR-SYS-404-01; quyền mới có hiệu lực, không cần đăng nhập lại
```

FR-AUTH-ACC-003; NOT RUN.

## AC-CORE-010-1: US-CORE-010

```gherkin
Scenario: Xem nhật ký đăng nhập / 1
  Given QUAN_TRI lọc login_logs U1 trong ngày thử
  When thực hiện xem nhật ký đăng nhập với input: bộ lọc
  Then Lọc theo tài khoản, khoảng ngày, kết quả. Mỗi dòng: thời điểm, kết quả, địa chỉ IP, thiết bị. Kết quả: Danh sách phân trang
```

FR-AUTH-ACC-004; NOT RUN.

## AC-CORE-010-2: US-CORE-010

```gherkin
Scenario: Xem nhật ký đăng nhập / 2
  Given QUAN_TRI lọc login_logs U1 trong ngày thử
  When pageSize=101
  Then 422 ERR-SYS-422-03; không tự cắt về100
```

FR-AUTH-ACC-004; NOT RUN.

## AC-CORE-010-3: US-CORE-010

```gherkin
Scenario: Xem nhật ký đăng nhập / 3
  Given QUAN_TRI lọc login_logs U1 trong ngày thử
  When trang lớn hơn trang cuối
  Then items rỗng,total đúng; không có mật khẩu/token trong log
```

FR-AUTH-ACC-004; NOT RUN.

## AC-CORE-011-1: US-CORE-011

```gherkin
Scenario: Kiểm quyền mỗi yêu cầu / 1
  Given U1 có quyền read trênK1, tài nguyênR1 thuộcK1
  When thực hiện kiểm quyền mỗi yêu cầu với input: token, tài nguyên
  Then Mỗi API khai báo quyền cần có. Hệ thống kiểm (1) tài khoản có quyền đó qua vai trò, (2) bản ghi được yêu cầu nằm trong phạm vi dữ liệu của tài khoản. Thiếu (1) → 403. Thiếu (2) → 404, để không lộ sự tồn tại của bản ghi. Kết quả: Cho phép / từ chối
```

FR-AUTH-RBAC-001; NOT RUN.

## AC-CORE-011-2: US-CORE-011

```gherkin
Scenario: Kiểm quyền mỗi yêu cầu / 2
  Given U1 có quyền read trênK1, tài nguyênR1 thuộcK1
  When U1 đọc id thuộcK2
  Then 404 ERR-SYS-404-01; không lộ tồn tại
```

FR-AUTH-RBAC-001; NOT RUN.

## AC-CORE-011-3: US-CORE-011

```gherkin
Scenario: Kiểm quyền mỗi yêu cầu / 3
  Given U1 có quyền read trênK1, tài nguyênR1 thuộcK1
  When U1 có hai vai trò, bỏ quyền ở một vai trò còn vai trò khác cấp
  Then hợp quyền vai trò được áp dụng cùng phạm vi; không tự mở scopeK2
```

FR-AUTH-RBAC-001; NOT RUN.

## AC-CORE-012-1: US-CORE-012

```gherkin
Scenario: Xem ma trận vai trò – quyền / 1
  Given Người có quyền xem matrix nội bộ
  When thực hiện xem ma trận vai trò – quyền với input: không áp dụng
  Then Hiển thị vai trò nào có quyền nào. Bản đầu chỉ đọc; thay đổi ma trận qua bản phát hành. Kết quả: Ma trận
```

FR-AUTH-RBAC-002; NOT RUN.

## AC-CORE-012-2: US-CORE-012

```gherkin
Scenario: Xem ma trận vai trò – quyền / 2
  Given Người có quyền xem matrix nội bộ
  When thử PATCH ma trận vai trò
  Then không có endpoint ghi; 405 hoặc không route; không sửa dữ liệu
```

FR-AUTH-RBAC-002; NOT RUN.

## AC-CORE-012-3: US-CORE-012

```gherkin
Scenario: Xem ma trận vai trò – quyền / 3
  Given Người có quyền xem matrix nội bộ
  When vai trò QUAN_TRI mở Cost không được cấp
  Then không suy QUAN_TRI có toàn quyền nghiệp vụ;403 ERR-AUTH-403-02
```

FR-AUTH-RBAC-002; NOT RUN.

## AC-CORE-013-1: US-CORE-013

```gherkin
Scenario: Uỷ quyền duyệt khi vắng / 1
  Given O-06 đã chốt; người duyệt ủy quyền choU2 trong khoảng ngày
  When thực hiện uỷ quyền duyệt khi vắng với input: người được uỷ, quyền, từ ngày, đến ngày
  Then Người có quyền duyệt chỉ định người thay trong một khoảng ngày. Người thay nhận đúng các quyền duyệt được uỷ, hết hạn tự thu hồi. Phụ thuộc [O-06] Kết quả: Bản ghi uỷ quyền
```

FR-AUTH-RBAC-003; BLOCKED: O-06.

## AC-CORE-013-2: US-CORE-013

```gherkin
Scenario: Uỷ quyền duyệt khi vắng / 2
  Given O-06 đã chốt; người duyệt ủy quyền choU2 trong khoảng ngày
  When ủy quyền chính mình hoặc ngày kết thúc trước ngày bắt đầu
  Then 422 ERR-AUTH-422-03
```

FR-AUTH-RBAC-003; BLOCKED: O-06.

## AC-CORE-013-3: US-CORE-013

```gherkin
Scenario: Uỷ quyền duyệt khi vắng / 3
  Given O-06 đã chốt; người duyệt ủy quyền choU2 trong khoảng ngày
  When U2 là người sửa cuối bản ghi được đề nghị duyệt
  Then 403 ERR-SYS-403-01; ủy quyền không phá tách người tạo/sửa và duyệt
```

FR-AUTH-RBAC-003; BLOCKED: O-06.

## AC-CORE-014-1: US-CORE-014

```gherkin
Scenario: Tài khoản dịch vụ cho agent / 1
  Given svc-agent-noi-bo có allowlist; người hỏi chỉ có quyềnK1
  When thực hiện tài khoản dịch vụ cho agent với input: không áp dụng
  Then Hai tài khoản tách biệt: `svc-agent-noi-bo`, `svc-agent-dinh-duong-vien`. Mỗi tài khoản có danh sách quyền gắn cứng, không đăng nhập qua giao diện. Kết quả: không áp dụng
```

FR-AUTH-SVC-001; NOT RUN.

## AC-CORE-014-2: US-CORE-014

```gherkin
Scenario: Tài khoản dịch vụ cho agent / 2
  Given svc-agent-noi-bo có allowlist; người hỏi chỉ có quyềnK1
  When agent phía khách gọi cost hoặc SELECT bảng Cost bằng service DB account
  Then 403 ở API và denied DB; không trả số trong lỗi
```

FR-AUTH-SVC-001; NOT RUN.

## AC-CORE-014-3: US-CORE-014

```gherkin
Scenario: Tài khoản dịch vụ cho agent / 3
  Given svc-agent-noi-bo có allowlist; người hỏi chỉ có quyềnK1
  When quyền user bị thu hồi giữa hai tool call
  Then tool thứ hai từ chối; giao quyền service/user tính mỗi lần, không đăng nhập UI
```

FR-AUTH-SVC-001; NOT RUN.

## AC-CORE-015-1: US-CORE-015

```gherkin
Scenario: Ghi nhật ký thay đổi / 1
  Given Thao tác sửa giá có actor/service và requestId
  When thực hiện ghi nhật ký thay đổi với input: không có (tự động)
  Then Mọi lệnh tạo, sửa, huỷ, duyệt trên bảng nghiệp vụ sinh 1 bản ghi nhật ký trong cùng giao dịch cơ sở dữ liệu: ai, lúc nào, thực thể, mã bản ghi, hành động, giá trị cũ → mới của từng trường đổi, lý do, mã yêu cầu. Nếu thao tác do agent thực hiện: ghi cả tài khoản dịch vụ và người dùng đang dùng agent. Kết quả: Bản ghi nhật ký
```

FR-SYS-AUD-001; NOT RUN.

## AC-CORE-015-2: US-CORE-015

```gherkin
Scenario: Ghi nhật ký thay đổi / 2
  Given Thao tác sửa giá có actor/service và requestId
  When gây lỗi ghi audit sau bước update
  Then rollback cả update; không thay đổi nghiệp vụ không audit
```

FR-SYS-AUD-001; NOT RUN.

## AC-CORE-015-3: US-CORE-015

```gherkin
Scenario: Ghi nhật ký thay đổi / 3
  Given Thao tác sửa giá có actor/service và requestId
  When gửi retry cùng idempotency key
  Then chỉ một thay đổi và một audit nghiệp vụ; ghi đủ before/after và on_behalf
```

FR-SYS-AUD-001; NOT RUN.

## AC-CORE-016-1: US-CORE-016

```gherkin
Scenario: Tra cứu nhật ký / 1
  Given Người đọc có quyền entityK1 và lọc thời gian
  When thực hiện tra cứu nhật ký với input: bộ lọc
  Then Lọc theo thực thể, mã bản ghi, người, khoảng ngày, hành động. Xem lịch sử của một bản ghi theo thứ tự thời gian. Kết quả: Danh sách phân trang
```

FR-SYS-AUD-002; NOT RUN.

## AC-CORE-016-2: US-CORE-016

```gherkin
Scenario: Tra cứu nhật ký / 2
  Given Người đọc có quyền entityK1 và lọc thời gian
  When truy vấn history entityK2
  Then 404 ERR-SYS-404-01 hoặc list rỗng theo scope; không lộ dữ liệu
```

FR-SYS-AUD-002; NOT RUN.

## AC-CORE-016-3: US-CORE-016

```gherkin
Scenario: Tra cứu nhật ký / 3
  Given Người đọc có quyền entityK1 và lọc thời gian
  When hai bản ghi cùng timestamp
  Then thứ tự ổn định timestamp,id; kiểm trang tiếp không mất/lặp dòng
```

FR-SYS-AUD-002; NOT RUN.

## AC-CORE-017-1: US-CORE-017

```gherkin
Scenario: Bắt buộc lý do / 1
  Given Thao tác sửa vai trò yêu cầu reason
  When thực hiện bắt buộc lý do với input: lý do
  Then Thao tác thuộc danh sách ở `BR-AUD-001` bị từ chối nếu thiếu lý do từ 10 ký tự. Kết quả: không áp dụng
```

FR-SYS-AUD-003; NOT RUN.

## AC-CORE-017-2: US-CORE-017

```gherkin
Scenario: Bắt buộc lý do / 2
  Given Thao tác sửa vai trò yêu cầu reason
  When reason chỉ có9 ký tự sau trim
  Then 422 ERR-SYS-422-01; không ghi
```

FR-SYS-AUD-003; NOT RUN.

## AC-CORE-017-3: US-CORE-017

```gherkin
Scenario: Bắt buộc lý do / 3
  Given Thao tác sửa vai trò yêu cầu reason
  When reason đủ10 ký tự có chuỗi HTML
  Then lưu chuỗi văn bản; UI escape; không chạy script
```

FR-SYS-AUD-003; NOT RUN.

## AC-CORE-018-1: US-CORE-018

```gherkin
Scenario: Huỷ thay cho xoá / 1
  Given Bản ghi nháp không được tham chiếu và người dùng có quyền hủy
  When thực hiện huỷ thay cho xoá với input: mã bản ghi, lý do
  Then Không có API xoá cứng bản ghi nghiệp vụ. Huỷ đặt cờ, giữ dữ liệu, bản ghi huỷ không xuất hiện ở danh sách mặc định. Kết quả: Bản ghi ở trạng thái huỷ
```

FR-SYS-AUD-004; NOT RUN.

## AC-CORE-018-2: US-CORE-018

```gherkin
Scenario: Huỷ thay cho xoá / 2
  Given Bản ghi nháp không được tham chiếu và người dùng có quyền hủy
  When hủy nguyên liệu được công thức hiệu lực tham chiếu
  Then 409 ERR-SYS-409-01; không hủy
```

FR-SYS-AUD-004; NOT RUN.

## AC-CORE-018-3: US-CORE-018

```gherkin
Scenario: Huỷ thay cho xoá / 3
  Given Bản ghi nháp không được tham chiếu và người dùng có quyền hủy
  When sau hủy tìm list mặc định và history
  Then list không có; history giữ dữ liệu/cờ hủy; không SQL DELETE nghiệp vụ
```

FR-SYS-AUD-004; NOT RUN.

## AC-CORE-019-1: US-CORE-019

```gherkin
Scenario: Quản lý tham số / 1
  Given QUAN_TRI tạo tham số cùng mã ở scopeK1, ngàyD+1
  When thực hiện quản lý tham số với input: mã, giá trị, phạm vi, ngày hiệu lực, lý do
  Then Mỗi tham số có: mã, kiểu, giá trị, phạm vi áp dụng (toàn hệ thống / cơ sở / công ty khách / điểm phục vụ), ngày hiệu lực từ. Giá trị dùng cho một ngày nghiệp vụ là giá trị có hiệu lực tại ngày đó ở phạm vi hẹp nhất. Danh mục khởi tạo ở Phụ lục 4.3. Kết quả: Phiên bản tham số mới
```

FR-SYS-PRM-001; NOT RUN.

## AC-CORE-019-2: US-CORE-019

```gherkin
Scenario: Quản lý tham số / 2
  Given QUAN_TRI tạo tham số cùng mã ở scopeK1, ngàyD+1
  When effectiveFrom=D-1 hoặc value sai kiểu
  Then 422 ERR-SYS-422-02; không sửa giá quá khứ
```

FR-SYS-PRM-001; NOT RUN.

## AC-CORE-019-3: US-CORE-019

```gherkin
Scenario: Quản lý tham số / 3
  Given QUAN_TRI tạo tham số cùng mã ở scopeK1, ngàyD+1
  When tra ngàyD vàD+1 có tham số toàn hệ thống vàK1
  Then D dùng bản cũ; D+1 dùng phạm vi hẹp nhất đã được duyệt; thiếu VAT vẫn null
```

FR-SYS-PRM-001; NOT RUN.

## AC-CORE-020-1: US-CORE-020

```gherkin
Scenario: Duyệt thay đổi tham số / 1
  Given NgườiA đề nghị COST_NGUONG_PCT, GIAM_DOC B duyệt
  When thực hiện duyệt thay đổi tham số với input: mã đề nghị, quyết định, lý do
  Then Tham số gắn cờ "cần duyệt" chỉ có hiệu lực sau khi người có quyền duyệt chấp thuận; người đề nghị không tự duyệt. Kết quả: Trạng thái đề nghị
```

FR-SYS-PRM-002; NOT RUN.

## AC-CORE-020-2: US-CORE-020

```gherkin
Scenario: Duyệt thay đổi tham số / 2
  Given NgườiA đề nghị COST_NGUONG_PCT, GIAM_DOC B duyệt
  When A hoặc người sửa cuối tự duyệt
  Then 403 ERR-SYS-403-01; giữ trạng thái chờ
```

FR-SYS-PRM-002; NOT RUN.

## AC-CORE-020-3: US-CORE-020

```gherkin
Scenario: Duyệt thay đổi tham số / 3
  Given NgườiA đề nghị COST_NGUONG_PCT, GIAM_DOC B duyệt
  When B duyệt rồi truy giá trị ngày trước hiệu lực
  Then chỉ có hiệu lực từ ngày đã khai; audit bất biến
```

FR-SYS-PRM-002; NOT RUN.

## AC-CORE-021-1: US-CORE-021

```gherkin
Scenario: Tạo thông báo trong hệ thống / 1
  Given Sự kiện có idE1, người nhận thuộcK1
  When thực hiện tạo thông báo trong hệ thống với input: sự kiện
  Then Module nghiệp vụ phát sự kiện; SYS tạo thông báo cho người nhận theo vai trò và phạm vi. Mỗi thông báo: loại, tiêu đề, nội dung, liên kết tới bản ghi, mức độ. Kết quả: Thông báo
```

FR-SYS-NTF-001; NOT RUN.

## AC-CORE-021-2: US-CORE-021

```gherkin
Scenario: Tạo thông báo trong hệ thống / 2
  Given Sự kiện có idE1, người nhận thuộcK1
  When payload tham chiếuK2 mà người nhận chỉ cóK1
  Then không tạo/hiển thị dữ liệuK2; không để link bypass scope
```

FR-SYS-NTF-001; NOT RUN.

## AC-CORE-021-3: US-CORE-021

```gherkin
Scenario: Tạo thông báo trong hệ thống / 3
  Given Sự kiện có idE1, người nhận thuộcK1
  When worker nhận lạiE1
  Then đề xuất một thông báo/người/event; cách lưu unique chờ E1-Q04
```

FR-SYS-NTF-001; NOT RUN.

## AC-CORE-022-1: US-CORE-022

```gherkin
Scenario: Trạng thái thông báo / 1
  Given U1 có thông báoNEW của mình
  When thực hiện trạng thái thông báo với input: mã thông báo, trạng thái
  Then 3 trạng thái: mới, đã xem, đã xử lý. Danh sách lọc theo trạng thái; hiện số thông báo mới trên thanh điều hướng. Kết quả: không áp dụng
```

FR-SYS-NTF-002; NOT RUN.

## AC-CORE-022-2: US-CORE-022

```gherkin
Scenario: Trạng thái thông báo / 2
  Given U1 có thông báoNEW của mình
  When U2 sửa trạng thái thông báoU1
  Then 404 ERR-SYS-404-01
```

FR-SYS-NTF-002; NOT RUN.

## AC-CORE-022-3: US-CORE-022

```gherkin
Scenario: Trạng thái thông báo / 3
  Given U1 có thông báoNEW của mình
  When U1 đánh dấu SEEN rồi RESOLVED và retry
  Then đếm NEW giảm một; không tạo thông báo mới; hồi trạng thái chờ E1-Q04
```

FR-SYS-NTF-002; NOT RUN.

## AC-CORE-023-1: US-CORE-023

```gherkin
Scenario: Gửi qua kênh ngoài / 1
  Given Q-14 đã chốt adapter và thông báo chờ gửi
  When thực hiện gửi qua kênh ngoài với input: người nhận, mẫu, dữ liệu
  Then Giao diện gửi chung cho mọi kênh; gửi qua hàng đợi, thử lại tối đa 3 lần, lưu kết quả từng lần gửi. Kênh cụ thể: [Q-14] Kết quả: Trạng thái gửi
```

FR-SYS-NTF-003; BLOCKED: Q-14.

## AC-CORE-023-2: US-CORE-023

```gherkin
Scenario: Gửi qua kênh ngoài / 2
  Given Q-14 đã chốt adapter và thông báo chờ gửi
  When provider lỗi cả3 lần
  Then trạng thái failed; ERR-SYS-502-01 ở job; không tự gửi lần4
```

FR-SYS-NTF-003; BLOCKED: Q-14.

## AC-CORE-023-3: US-CORE-023

```gherkin
Scenario: Gửi qua kênh ngoài / 3
  Given Q-14 đã chốt adapter và thông báo chờ gửi
  When retry sau provider đã nhận nhưng callback mất
  Then cần provider messageId/idempotency; nếu chưa đối soát không phát lặp mù
```

FR-SYS-NTF-003; BLOCKED: Q-14.

## AC-CORE-024-1: US-CORE-024

```gherkin
Scenario: Tải tệp lên / 1
  Given Tệp PNG thật dưới10MB, entity thuộc quyền
  When thực hiện tải tệp lên với input: tệp, thực thể gắn kèm
  Then Nhận JPG, PNG, WEBP, PDF; tối đa 10 MB mỗi tệp. Kiểm tra loại tệp theo nội dung, không theo đuôi tên. Tệp nội bộ chỉ truy cập qua liên kết có chữ ký, hết hạn sau 15 phút. Kết quả: Mã tệp
```

FR-SYS-FILE-001; NOT RUN.

## AC-CORE-024-2: US-CORE-024

```gherkin
Scenario: Tải tệp lên / 2
  Given Tệp PNG thật dưới10MB, entity thuộc quyền
  When đổi đuôi exe thành png hoặc tệp lớn hơn10MB
  Then 415 ERR-SYS-415-01 hoặc413 ERR-SYS-413-01
```

FR-SYS-FILE-001; NOT RUN.

## AC-CORE-024-3: US-CORE-024

```gherkin
Scenario: Tải tệp lên / 3
  Given Tệp PNG thật dưới10MB, entity thuộc quyền
  When mở signed URL sau15 phút hoặc actor khác entity
  Then URL hết hạn/không được cấp; không công khai object storage
```

FR-SYS-FILE-001; NOT RUN.

## AC-CORE-025-1: US-CORE-025

```gherkin
Scenario: Tác vụ nền / 1
  Given JobJ1 có eventId và khóa lịch
  When thực hiện tác vụ nền với input: không áp dụng
  Then Hàng đợi có: thử lại với khoảng cách tăng dần, tối đa 5 lần; hàng đợi lỗi cho tác vụ hỏng hẳn; khoá chống chạy trùng cho tác vụ định giờ. `QUAN_TRI` xem được trạng thái và chạy lại tác vụ lỗi. Kết quả: không áp dụng
```

FR-SYS-JOB-001; NOT RUN.

## AC-CORE-025-2: US-CORE-025

```gherkin
Scenario: Tác vụ nền / 2
  Given JobJ1 có eventId và khóa lịch
  When worker lỗi đủ5 lần
  Then chuyển hàng đợi lỗi; log từng lần; không retry vô hạn
```

FR-SYS-JOB-001; NOT RUN.

## AC-CORE-025-3: US-CORE-025

```gherkin
Scenario: Tác vụ nền / 3
  Given JobJ1 có eventId và khóa lịch
  When hai worker claim cùng job định giờ
  Then chỉ một hiệu ứng nghiệp vụ; admin replay không nhân đôi effect đã commit
```

FR-SYS-JOB-001; NOT RUN.

## AC-CORE-026-1: US-CORE-026

```gherkin
Scenario: Kiểm tra sức khoẻ / 1
  Given API/DB/Redis/queue hoạt động
  When thực hiện kiểm tra sức khoẻ với input: không áp dụng
  Then Điểm kiểm tra `/v1/health` trả trạng thái API, MySQL, Redis, hàng đợi; dùng cho cân bằng tải và giám sát. Kết quả: Trạng thái từng thành phần
```

FR-SYS-HLT-001; NOT RUN.

## AC-CORE-026-2: US-CORE-026

```gherkin
Scenario: Kiểm tra sức khoẻ / 2
  Given API/DB/Redis/queue hoạt động
  When ngắt MySQL
  Then 503 ERR-SYS-503-01; readiness không đạt
```

FR-SYS-HLT-001; NOT RUN.

## AC-CORE-026-3: US-CORE-026

```gherkin
Scenario: Kiểm tra sức khoẻ / 3
  Given API/DB/Redis/queue hoạt động
  When gọi health từ Internet không có quyền nội bộ
  Then chỉ minimal status; không lộ DSN/secret/topology chi tiết
```

FR-SYS-HLT-001; NOT RUN.
