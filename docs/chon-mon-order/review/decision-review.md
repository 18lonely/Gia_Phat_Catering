---
id: DOC-E6-DECISION-REVIEW
title: Review quyết định identity, số suất, khóa hạn và kế hoạch
version: 0.1.0
phase: Review
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Review quyết định E6

11/11/2026 · Đã rà tài liệu; **chưa ký baseline schema/API**. Đề nghị thực hiện review không được hiểu là duyệt tất cả phương án. [Sổ câu hỏi](questions.md) là nguồn trạng thái; [phát hiện](decision-findings.md) chỉ rõ chỗ cần sửa/chốt.

## Căn cứ đã có

| Nguồn | Kết luận có căn cứ | Không được suy rộng |
| :--- | :--- | :--- |
| D-04 tại [kế hoạch](../../gia-phat/00-ke-hoach-tong-the.md) | Người ăn chọn1 trong3 MAIN | Không tự mở nhiều MAIN hoặc nhiều suất/người |
| D-14 | Tổng suất do người đặt tổng chốt; phần chưa chọn nhận món mặc định; người đặt tổng được sửa trước hạn | Chưa quyết C là gộp hay theo người, hủy/chuyển suất và khi S vượt T |
| D-19 | QR công ty là cơ chế xác minh | Không chứng minh một mã QR dùng chung định danh được mỗi người |
| D-21 | Định mức chung; vượt mức bị chặn; không người ăn tự bù tiền | Không tự quyết policy đổi quota giữa ngày |
| E6-EVID-001 — người dùng trả lời trực tiếp ngày11/11/2026 | **“Có danh sách và người quản lý xác nhận”** | Chỉ xác nhận sự tồn tại của danh sách và khả năng quản lý xác nhận. Chưa xác nhận mã nhân viên duy nhất/ổn định, phương thức cấp credential, OTP, SLA duyệt hoặc mô hình dữ liệu |

E6-EVID-001 làm ORD-Q01 **có thêm căn cứ**, chưa đủ đóng ORD-Q01. Người xác nhận: người dùng trong chat này; không tự ghi tên/chức danh hoặc biên bản ký. Chưa có dữ liệu danh sách thực được cung cấp, không tạo fixture mang danh tính thật.

## DR-01 — Một người, một liên kết danh tính

**Đề xuất:** dùng một membership người ăn trong danh sách được công ty xác nhận; cả tài khoản và QR guest ánh xạ về membership đó. Không dùng tài khoản hoặc cookie làm khóa nghiệp vụ duy nhất. Mã nhân viên chỉ là mã tra cứu, không phải mật khẩu.

| Phương án | Lợi ích | Hạn chế / quyết định còn cần |
| :--- | :--- | :--- |
| Danh sách + quản lý xác nhận + credential cá nhân (khuyến nghị) | Tận dụng E6-EVID-001; liên kết account/guest; đổi thiết bị vẫn cùng người | Cần chốt cấp/recovery credential; dữ liệu mã người ăn ổn định; người thay quản lý |
| Danh sách + OTP tới liên hệ đã xác minh | Tự xác minh trên thiết bị mới | Chưa có bằng chứng công ty có liên hệ phù hợp/kênh OTP; không tự thêm nhà cung cấp hoặc chi phí |
| Chỉ QR công ty + nhập mã nhân viên | Ít bước | Có thể mạo danh nếu biết mã; không đủ để cam kết0lựa chọn trùng/giả mạo |

Phương án khuyến nghị chưa chọn cụ thể PIN, link một lần, passkey hoặc OTP. Khi một người đã có account rồi mở QR, hệ thống phải tìm cùng membership trước tạo selection. Không tự merge hai người chỉ vì tên/điện thoại giống nhau. Mã bị tái sử dụng cho nhân viên mới không được kế thừa lựa chọn/lịch sử của người cũ.

**Scope đề xuất:** một người đặt tổng thuộc một khách trong R6, được giao một hoặc nhiều điểm của khách đó; DDV có tập khách/điểm được phân công; bếp chỉ cơ sở của mình. Quyền phải còn hiệu lực tại lúc ghi, không chỉ lúc mở màn. Nhu cầu một người đặt tổng quản lý nhiều pháp nhân cần xác nhận riêng ORD-Q11, không suy từ khả năng schema.

**Thu hồi đề xuất:** gỡ người ăn chặn thao tác mới, giữ lịch sử; quay QR chặn tạo phiên bằng token cũ. Thu hồi tất cả phiên đang mở hay chỉ phiên liên quan QR là lựa chọn ORD-Q02; không tự xóa các suất đã chọn.

**Tác động:** FEAT-030–033/036; API-ORD-006–012/002; users.customer_id, eaters.user_id nullable unique chưa đủ canonical membership; cần binding/identity proof và audit actor guest. UC-ORD-001–004/007, UI-ORD-01–03/06, AC-E6-001–004/007 cần cập nhật sau quyết định. **CHỜ ORD-Q01/02/11.**

## DR-02 — Số suất, chọn hộ và chuyển sang tự chọn

**Đề xuất khuyến nghị:** S là suất người ăn tự chọn; C là suất chọn hộ gắn một người trong danh sách khi có thể; D là phần tổng suất chưa có lựa chọn cụ thể. Trong mô hình1MAIN/suất: `T = S + C + D`. Người ăn tự chọn sau khi đã được chọn hộ thì **chuyển nguồn C→S**, không thêm suất thứ hai.

| Tình huống synthetic | Expected đề xuất | Điều còn chờ |
| :--- | :--- | :--- |
| T=100,S=60,C=10 | D=30 tại khóa | Công thức và nghĩa C chờ ORD-Q06 |
| E nằm trong C rồi tự chọn | S=61,C=9,D=30; chuyển món/counter nguyên tử nếu cần | Quyền tự thay lựa chọn hộ, lưu actor và lịch sử |
| C=10 là lượng gộp không có danh tính; người mới tự chọn | Không thể xác định có trùng C bằng phép đếm | Nên yêu cầu rà phần nhập gộp; không tự giảm C hoặc tuyên bố chống trùng người |
| T=70,S=60,C=10; một người mới chọn | Đề xuất giữ T do người đặt tổng xác nhận, từ chối ghi vượt với lý do đủ suất; người đặt tổng điều chỉnh T rồi người ăn gửi lại | Đây là **policy mới cần ORD-Q06**, không phải suy ra từ D-14 |
| Người đặt tổng gửi T=65 khi S+C=70 | Từ chối bản gửi; không tự xóa5lựa chọn | Giữ phương án ORD-Q06 đang chờ |
| Đổi A→B, S không đổi | Chỉ chuyển món; không làm tăng T hoặc S | Version/counter phải cùng giao dịch |
| Chưa gửi T | Người ăn có thể chọn nếu menu/quota/identity hợp lệ theo luồng hiện có; chưa có D xác định | Giới hạn tối đa và hành vi T=0 chờ ORD-Q13 |

Phương án thay cho chặn S vượt T: nhận lựa chọn nhưng đánh dấu tổng cần xác nhận lại, chặn khóa đến khi giải quyết. Cách này ít từ chối người ăn nhưng tăng rủi ro tồn order không khóa; **không tự chọn một trong hai ở backend**. T tự tăng theo S không khuyến nghị vì làm thay số người đặt tổng đã xác nhận.

`summaryVersion` cần đổi khi selection, C, T hoặc phạm vi nguồn liên quan đổi. `orders.version` và version lựa chọn cá nhân không đủ thay thế revision tổng hợp. Client đọc summary phải dùng cùng token lúc gửi; nếu token cũ thì409, tải lại trước xác nhận.

**Tác động:** FEAT-036/038/039/042; API-ORD-002/003/004, PORT-LOCK; UC-ORD-007/009/010/013; selection/coordinator allocation/summary revision; UI06/08/11. Không viết hợp đồng `coordinatorLines` gộp như đã giải quyết trùng người. **CHỜ ORD-Q06/13.**

## DR-03 — Khóa hạn và thiếu dữ liệu

**Đề xuất:** hạn chốt là mốc server có version theo điểm/ngày/ca, quy đổi UTC; trước hạn cho ghi, đúng/sau hạn không nhận ghi thường. Không dùng15:00D-1 hoặc5%/10suất/06:00 làm mặc định đã duyệt.

| Nhánh | Phương án khuyến nghị để review | Chặn |
| :--- | :--- | :--- |
| Gửi trước hạn nhưng chờ khóa transaction qua hạn | Kiểm thời gian tại bước ghi trong transaction; từ chối nếu đã qua hạn | Q-16/ORD-Q07/12 cần xác nhận ranh giới |
| Thiếu T/default hoặc menu bị thu hồi | Order không được ghi LOCKED giả; ghi NEEDS_ATTENTION ở job, không suy T từ danh sách | Ai nhận/giải quyết và thời hạn phản hồi cần ORD-Q07 |
| Retry sau job lỗi, nguồn không đổi và đã commit | Đối soát receipt/outbox, trả revision cũ | Thiết kế transaction/dedupe cần Tech lead review |
| Thiếu default rồi có bản nguồn mới sau hạn | Xử lý ngoại lệ có người, lý do và version; không coi là retry kỹ thuật cùng input | Quyền sửa/gia hạn và cơ chế xử lý cần ORD-Q07/12 |
| Nhiều cấp deadline có giá trị khác nhau | Đề xuất cấu hình duy nhất được resolve và hiển thị trước khi nhận lựa chọn; không để client tự chọn cấp | Thứ tự override khách/điểm/ca còn chờ |

Tách ba sự kiện: **đến hạn nhận lựa chọn**, **khóa thành công snapshot order**, **kế hoạch sẵn sàng**. Chúng không nhất thiết cùng thời điểm khi worker có lỗi. Lỗi plan sau commit không mở lại order.

**Tác động:** FEAT-039/040/041; PORT-LOCK/API-ORD-004/005/022; job outcome, deadline snapshot, outbox; UC010–012; UI09/10. **CHỜ Q-16/ORD-Q07/08/12 và O-06.**

## DR-04 — Kế hoạch có phiên bản và bếp nhận bản mới

**Đề xuất:** mỗi kế hoạch theo bếp/ngày/ca chứa manifest nguồn: đúng một order revision hiện hành cho mỗi order thuộc phạm vi. Dòng món gộp theo dish+recipe+portion+unit; bản cũ bất biến. Không cộng MAIN với món kèm thành tổng suất.

| Tình huống synthetic | Expected đề xuất |
| :--- | :--- |
| A rev1 góp60, B rev1 góp40 suất cùng món | Plan1=100, nguồn[A1,B1] |
| A rev2 tăng5 | Plan2=105, nguồn[A2,B1]; không cộng A1+A2 |
| B rev2 giảm3; event đến cùng A2 | Plan kế tiếp=102, nguồn[A2,B2]; không mất delta của A hoặc B |
| Event A1 đến muộn | Không hồi lui đóng góp A2 |
| A đã khóa, B còn NEEDS_ATTENTION | Có thể tính bản xem trước nhưng phải hiện thiếu B; không gắn nhãn đủ toàn bếp chỉ vì A thành công |
| Bếp đã xem Plan1, hệ thống có Plan2 | Hiện bản mới và delta; không ghi bếp đã nhận nếu chỉ publish thành công |

**Đề xuất vận hành:** bếp xác nhận đã nhận theo `planId+revisionNo`; bản in có version/thời điểm và dấu bản cũ khi xem lại. Acknowledgement không phải duyệt ngoại lệ và không đồng nghĩa đã bắt đầu sản xuất. Phát hành kế hoạch **không tự chuyển** order sang IN_PRODUCTION; transition đó chờ người/quyền/sự kiện ORD-Q14.

Chưa xác định scope nào đã đủ nguồn để được phát hành chính thức: cần tập order dự kiến từ lịch phục vụ và cách ghi bữa hủy/T=0; không lấy số order đã khóa làm mẫu số độ đủ. Khi đổi cơ sở phục vụ, kế hoạch cũ và mới cần cùng một quy trình chuyển đóng góp có kiểm soát, không chỉ ghi tăng ở bếp mới.

**Tác động:** FEAT-034/040/041/048; API-ORD-020/025, source manifest/completeness/acknowledgement delta; UC005/011/012/019, UI09/10/13; ORD-Q03/08/10/13/14. Các trường/endpoint acknowledgement **chưa thêm vào catalog hoặc DBML**.

## Kết luận review và thứ tự chốt

1. Xác nhận cách liên kết danh sách và chứng minh người dùng sở hữu membership; chốt scope R6. E6-EVID-001 không đủ quyết định credential.
2. Chốt C có danh tính hay gộp, chuyển C→S và chính sách S+C vượt T sau lần gửi tổng.
3. Chốt hạn/override, người xử lý thiếu dữ liệu sau hạn và người duyệt ngoại lệ.
4. Chốt điều kiện kế hoạch đủ nguồn, bếp xác nhận bản mới và sự kiện bắt đầu sản xuất.

Mỗi DR cần: phương án được chọn; ngoại lệ; ví dụ; người/ngày/nguồn xác nhận. Sau đó mới cập nhật schema/API/UC/AC và chuyển test từ BLOCKED sang NOT RUN. Không mở E7–E13 trong đợt này. Quy tắc VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03 giữ nguyên.

## Phản hồi người dùng E6-EVID-002 — 11/11/2026

Nguồn: trả lời trực tiếp ba câu hỏi review trong chat. Người dùng chọn **“Chưa chốt, giữ câu hỏi mở”** cho cả ba nội dung:

| Nội dung | Mã liên quan | Trạng thái sau phản hồi |
| :--- | :--- | :--- |
| Người đặt tổng thuộc một công ty hay được quản lý nhiều công ty | DR-01 / ORD-Q11 | CHỜ XÁC NHẬN; chưa chọn phạm vi |
| Người được chọn hộ quay lại tự chọn trước hạn có chuyển C→S, giữ T hay không | DR-02 / ORD-Q06 | CHỜ XÁC NHẬN; chưa duyệt cơ chế chuyển nguồn |
| Khi S+C bằng T đã gửi, chặn lựa chọn mới hay nhận rồi yêu cầu chốt lại T | DR-02 / ORD-Q06 | CHỜ XÁC NHẬN; chưa chọn chính sách vượt tổng |

Đây là xác nhận **tiếp tục để mở**, không phải phê duyệt phương án khuyến nghị hoặc bác bỏ vĩnh viễn phương án khác. Không áp mặc định một công ty, tự chuyển C→S hoặc tự chặn/nhận vượt T trong schema/API. Các ca phụ thuộc giữ BLOCKED. E6-EVID-001 về có danh sách và người quản lý xác nhận vẫn có hiệu lực, nhưng không đóng cơ chế identity. Không hỏi lại ba nội dung này khi chưa có yêu cầu chốt hoặc thông tin mới.
