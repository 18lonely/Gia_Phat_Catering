---
id: DOC-E12-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## AC-FBR-001-1 — Thành công có điều kiện

US-FBR-001 · FR-FB-RATE-001 · BR-FBR-001

```gherkin
Scenario: Gửi đánh giá bữa ăn — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q01/02; E6 CG01/08
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện gửi đánh giá bữa ăn
  Then Đánh giá có receipt và trạng thái tiếp nhận; Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn.
```

## AC-FBR-001-2 — Lỗi nghiệp vụ

US-FBR-001 · FR-FB-RATE-001 · BR-FBR-001

```gherkin
Scenario: Gửi đánh giá bữa ăn — Lỗi nghiệp vụ
  Given Giá trị ngoài thang đã duyệt
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện gửi đánh giá bữa ăn
  Then Từ chối giá trị, không ghi đánh giá
```

## AC-FBR-001-3 — Biên và bảo mật

US-FBR-001 · FR-FB-RATE-001 · BR-FBR-001

```gherkin
Scenario: Gửi đánh giá bữa ăn — Biên và bảo mật
  Given Gửi lại cùng yêu cầu sau mất phản hồi
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện gửi đánh giá bữa ăn
  Then Chỉ một đánh giá theo receipt; chính sách số lần đánh giá vẫn chờ Q02
```

## AC-FBR-002-1 — Thành công có điều kiện

US-FBR-002 · FR-FB-CASE-001 · BR-FBR-002

```gherkin
Scenario: Tiếp nhận và theo dõi khiếu nại — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q02/03; E6 CG01/08; E7-Q02
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tiếp nhận và theo dõi khiếu nại
  Then Hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách; Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn.
```

## AC-FBR-002-2 — Lỗi nghiệp vụ

US-FBR-002 · FR-FB-CASE-001 · BR-FBR-002

```gherkin
Scenario: Tiếp nhận và theo dõi khiếu nại — Lỗi nghiệp vụ
  Given Yêu cầu đóng hồ sơ khi thiếu chính sách xử lý
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tiếp nhận và theo dõi khiếu nại
  Then Giữ hồ sơ chưa kết thúc; báo thiếu chính sách
```

## AC-FBR-002-3 — Biên và bảo mật

US-FBR-002 · FR-FB-CASE-001 · BR-FBR-002

```gherkin
Scenario: Tiếp nhận và theo dõi khiếu nại — Biên và bảo mật
  Given Khách gửi nội dung trùng nhưng chưa có receipt xác định
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tiếp nhận và theo dõi khiếu nại
  Then Không tự gộp hoặc xóa; nêu cần rà trùng theo Q02
```

## AC-FBR-003-1 — Thành công có điều kiện

US-FBR-003 · FR-FB-SELR-001 · BR-FBR-003

```gherkin
Scenario: Xem tỷ lệ được chọn theo món — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q04; E6 CG01–14, ORD-Q01–15, E6-EVID-001/002
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem tỷ lệ được chọn theo món
  Then Số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định; Chỉ lấy lựa chọn thật của người ăn từ E6; phân biệt tự chọn với gán mặc định, nhập tổng và sản xuất. Chưa có mẫu số hoặc provenance đủ thì tỷ lệ null, không tự chọn trong ba mẫu số.
```

## AC-FBR-003-2 — Lỗi nghiệp vụ

US-FBR-003 · FR-FB-SELR-001 · BR-FBR-003

```gherkin
Scenario: Xem tỷ lệ được chọn theo món — Lỗi nghiệp vụ
  Given Nguồn chỉ có số suất sản xuất
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem tỷ lệ được chọn theo món
  Then Không tính hoặc suy tỷ lệ được chọn
```

## AC-FBR-003-3 — Biên và bảo mật

US-FBR-003 · FR-FB-SELR-001 · BR-FBR-003

```gherkin
Scenario: Xem tỷ lệ được chọn theo món — Biên và bảo mật
  Given Mẫu số thiếu hoặc bằng 0
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem tỷ lệ được chọn theo món
  Then Trả null cùng lý do; không trả 0 % hoặc chia cho 0
```

## AC-FBR-004-1 — Thành công có điều kiện

US-FBR-004 · FR-FB-PROP-001 · BR-FBR-004

```gherkin
Scenario: Lập đề xuất cải tiến thực đơn từ phản hồi — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q04/05; DL-01; O-02
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập đề xuất cải tiến thực đơn từ phản hồi
  Then Đề xuất nháp cùng căn cứ và điều kiện kiểm lại; Người dùng đọc dữ liệu có nguồn, tự chọn món cần rà; thiếu mẫu số không xếp hạng tỷ lệ. Lưu đề xuất nháp riêng, không tự đổi MENU; thay món hoặc định lượng phải qua E2, dị ứng và E3.
```

## AC-FBR-004-2 — Lỗi nghiệp vụ

US-FBR-004 · FR-FB-PROP-001 · BR-FBR-004

```gherkin
Scenario: Lập đề xuất cải tiến thực đơn từ phản hồi — Lỗi nghiệp vụ
  Given Không có tỷ lệ nhưng yêu cầu xếp hạng món ít được chọn
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập đề xuất cải tiến thực đơn từ phản hồi
  Then Không xếp hạng; ghi thiếu mẫu số
```

## AC-FBR-004-3 — Biên và bảo mật

US-FBR-004 · FR-FB-PROP-001 · BR-FBR-004

```gherkin
Scenario: Lập đề xuất cải tiến thực đơn từ phản hồi — Biên và bảo mật
  Given Nguồn phản hồi thay đổi sau khi lập nháp
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập đề xuất cải tiến thực đơn từ phản hồi
  Then Đánh dấu cần rà lại, không dùng bằng chứng cũ để chuyển duyệt
```

## AC-FBR-005-1 — Thành công có điều kiện

US-FBR-005 · FR-RPT-ROLE-001 · BR-FBR-005

```gherkin
Scenario: Xem dashboard theo bốn vai trò — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q06/07/08; E7-Q03/04; E10-Q07; E11-Q07/08
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem dashboard theo bốn vai trò
  Then Bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng; Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn.
```

## AC-FBR-005-2 — Lỗi nghiệp vụ

US-FBR-005 · FR-RPT-ROLE-001 · BR-FBR-005

```gherkin
Scenario: Xem dashboard theo bốn vai trò — Lỗi nghiệp vụ
  Given Đổi roleView thành giám đốc khi không có quyền
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem dashboard theo bốn vai trò
  Then Từ chối; roleView không cấp thêm quyền
```

## AC-FBR-005-3 — Biên và bảo mật

US-FBR-005 · FR-RPT-ROLE-001 · BR-FBR-005

```gherkin
Scenario: Xem dashboard theo bốn vai trò — Biên và bảo mật
  Given Một nguồn lỗi trong nhiều chỉ số
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem dashboard theo bốn vai trò
  Then Ô lỗi hiện thiếu nguồn, ô độc lập vẫn có nguồn; không cộng thiếu như 0
```

## AC-FBR-006-1 — Thành công có điều kiện

US-FBR-006 · FR-RPT-CPCT-001 · BR-FBR-006

```gherkin
Scenario: Đọc cost % ngày và theo khách — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q07/08; O-01; DATA-COST-Q01–06; E11-Q07/08
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đọc cost % ngày và theo khách
  Then Cost % ngày có nguồn E3; ô theo khách chưa xác định khi thiếu công thức; Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13.
```

## AC-FBR-006-2 — Lỗi nghiệp vụ

US-FBR-006 · FR-RPT-CPCT-001 · BR-FBR-006

```gherkin
Scenario: Đọc cost % ngày và theo khách — Lỗi nghiệp vụ
  Given Không có cost.cost.read
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đọc cost % ngày và theo khách
  Then Loại số cost khỏi API, UI, lỗi, log và cache
```

## AC-FBR-006-3 — Biên và bảo mật

US-FBR-006 · FR-RPT-CPCT-001 · BR-FBR-006

```gherkin
Scenario: Đọc cost % ngày và theo khách — Biên và bảo mật
  Given Khách có nhiều loại suất hoặc ngày không doanh thu
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đọc cost % ngày và theo khách
  Then Không bình quân tỷ lệ hay dùng số giao làm mẫu số; giữ chưa xác định
```

## AC-FBR-007-1 — Thành công có điều kiện

US-FBR-007 · FR-AIO-PRRV-001 · BR-FBR-007

```gherkin
Scenario: Yêu cầu rà soát thực đơn khi giá đổi — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho AIO-Q01–06; E12-Q09; O-01/O-02
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu rà soát thực đơn khi giá đổi
  Then Đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn; Chỉ đọc sự kiện giá E3 và thực đơn được phép; diễn giải ảnh hưởng và đề xuất đổi món hoặc định lượng có nguồn. Không ghi giá, công thức hay thực đơn. Không tự tính tiền.
```

## AC-FBR-007-2 — Lỗi nghiệp vụ

US-FBR-007 · FR-AIO-PRRV-001 · BR-FBR-007

```gherkin
Scenario: Yêu cầu rà soát thực đơn khi giá đổi — Lỗi nghiệp vụ
  Given Sự kiện giá không có VAT phải trả xác định
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu rà soát thực đơn khi giá đổi
  Then Không đưa số cost hay phương án đạt; báo thiếu nguồn
```

## AC-FBR-007-3 — Biên và bảo mật

US-FBR-007 · FR-AIO-PRRV-001 · BR-FBR-007

```gherkin
Scenario: Yêu cầu rà soát thực đơn khi giá đổi — Biên và bảo mật
  Given Giá hoặc menu đổi trong lúc rà
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu rà soát thực đơn khi giá đổi
  Then Kết quả gắn revision cũ và cần rà lại; không tự áp dụng
```

## AC-FBR-008-1 — Thành công có điều kiện

US-FBR-008 · FR-AIO-RCHK-001 · BR-FBR-008

```gherkin
Scenario: Kiểm lại đề xuất đổi món hoặc định lượng — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho AIO-Q02/05/06; DL-01; E11-Q15; E12-Q09
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm lại đề xuất đổi món hoặc định lượng
  Then Bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật; Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO.
```

## AC-FBR-008-2 — Lỗi nghiệp vụ

US-FBR-008 · FR-AIO-RCHK-001 · BR-FBR-008

```gherkin
Scenario: Kiểm lại đề xuất đổi món hoặc định lượng — Lỗi nghiệp vụ
  Given Một lần thay định lượng không chạy lại kiểm dị ứng/E2/E3
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm lại đề xuất đổi món hoặc định lượng
  Then Chặn nhãn sẵn sàng review; nêu kiểm còn thiếu
```

## AC-FBR-008-3 — Biên và bảo mật

US-FBR-008 · FR-AIO-RCHK-001 · BR-FBR-008

```gherkin
Scenario: Kiểm lại đề xuất đổi món hoặc định lượng — Biên và bảo mật
  Given Nguồn kiểm khác hash ứng viên
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm lại đề xuất đổi món hoặc định lượng
  Then Từ chối ghép kết quả; yêu cầu kiểm lại cùng revision
```

## AC-FBR-009-1 — Thành công có điều kiện

US-FBR-009 · FR-AIO-ESTR-001 · BR-FBR-009

```gherkin
Scenario: Diễn giải dự toán có nguồn — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho AIO-Q01–06; E12-Q09; DATA-COST-Q01–06
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải dự toán có nguồn
  Then Nháp diễn giải dự toán chờ người thật rà; Chỉ đọc dự toán E3 trong scope; giữ lượng mua, đơn vị, giá gồm VAT, khoản khoán và tổng từ hệ thống; AI chỉ giải thích, không tạo con số.
```

## AC-FBR-009-2 — Lỗi nghiệp vụ

US-FBR-009 · FR-AIO-ESTR-001 · BR-FBR-009

```gherkin
Scenario: Diễn giải dự toán có nguồn — Lỗi nghiệp vụ
  Given Dòng dự toán thiếu nguồn giá
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải dự toán có nguồn
  Then Không bịa giá hoặc tổng hoàn tất
```

## AC-FBR-009-3 — Biên và bảo mật

US-FBR-009 · FR-AIO-ESTR-001 · BR-FBR-009

```gherkin
Scenario: Diễn giải dự toán có nguồn — Biên và bảo mật
  Given Hao hụt đã nằm trong lượng E3
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải dự toán có nguồn
  Then Giữ lượng nguồn; không áp hao hụt thêm lần nữa
```

## AC-FBR-010-1 — Thành công có điều kiện

US-FBR-010 · FR-AIO-DEMR-001 · BR-FBR-010

```gherkin
Scenario: Diễn giải nhu cầu nguyên liệu — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E11-Q01/03/13; E6 CG06; AIO-Q01–06
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải nhu cầu nguyên liệu
  Then Nháp diễn giải nhu cầu với thiếu nguồn rõ ràng; Đọc nhu cầu E11 và revision nguồn; phân biệt nhu cầu gộp với mua ròng. Chưa chốt trừ tồn/dự phòng thì không đề xuất lượng mua ròng; không tạo đơn mua hoặc chọn NCC.
```

## AC-FBR-010-2 — Lỗi nghiệp vụ

US-FBR-010 · FR-AIO-DEMR-001 · BR-FBR-010

```gherkin
Scenario: Diễn giải nhu cầu nguyên liệu — Lỗi nghiệp vụ
  Given Chỉ có kế hoạch thiếu revision hoặc nguồn chưa đủ
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải nhu cầu nguyên liệu
  Then Giữ BLOCKED_DATA, không kết luận đủ để mua
```

## AC-FBR-010-3 — Biên và bảo mật

US-FBR-010 · FR-AIO-DEMR-001 · BR-FBR-010

```gherkin
Scenario: Diễn giải nhu cầu nguyên liệu — Biên và bảo mật
  Given Yêu cầu trừ tồn khi chính sách chưa chốt
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện diễn giải nhu cầu nguyên liệu
  Then Không trừ; giữ nhu cầu gộp và tham chiếu E11-Q01
```

## AC-FBR-011-1 — Thành công có điều kiện

US-FBR-011 · FR-AIO-PDEV-001 · BR-FBR-011

```gherkin
Scenario: Giải thích cảnh báo giá lệch — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q10; E11-Q07/08/14; AIO-Q01–06
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện giải thích cảnh báo giá lệch
  Then Nháp giải thích; cảnh báo chính thức chưa xác định; Đọc so sánh E3/E11 cùng đơn vị, VAT, thời điểm và scope. Ngưỡng giá lệch chờ E12-Q10; không mượn BO-02 hoặc sai số NFR làm ngưỡng giá.
```

## AC-FBR-011-2 — Lỗi nghiệp vụ

US-FBR-011 · FR-AIO-PDEV-001 · BR-FBR-011

```gherkin
Scenario: Giải thích cảnh báo giá lệch — Lỗi nghiệp vụ
  Given Không có ngưỡng cảnh báo được duyệt
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện giải thích cảnh báo giá lệch
  Then Không gán cảnh báo đạt/vượt
```

## AC-FBR-011-3 — Biên và bảo mật

US-FBR-011 · FR-AIO-PDEV-001 · BR-FBR-011

```gherkin
Scenario: Giải thích cảnh báo giá lệch — Biên và bảo mật
  Given Hai giá khác đơn vị hoặc cách ghi VAT
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện giải thích cảnh báo giá lệch
  Then Không so trực tiếp; chờ nguồn quy đổi E3
```

## AC-FBR-012-1 — Thành công có điều kiện

US-FBR-012 · FR-AIO-CRMS-001 · BR-FBR-012

```gherkin
Scenario: Tóm tắt khách và đề xuất nhắc việc — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E10-Q01/05/06/13; AIO-Q01–06; E12-Q11
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tóm tắt khách và đề xuất nhắc việc
  Then Nháp tóm tắt và danh sách việc cần người thật rà; Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ.
```

## AC-FBR-012-2 — Lỗi nghiệp vụ

US-FBR-012 · FR-AIO-CRMS-001 · BR-FBR-012

```gherkin
Scenario: Tóm tắt khách và đề xuất nhắc việc — Lỗi nghiệp vụ
  Given Văn bản CRM yêu cầu đọc khách ngoài scope
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tóm tắt khách và đề xuất nhắc việc
  Then Coi là dữ liệu, chặn tại công cụ/DB trước lấy dữ liệu
```

## AC-FBR-012-3 — Biên và bảo mật

US-FBR-012 · FR-AIO-CRMS-001 · BR-FBR-012

```gherkin
Scenario: Tóm tắt khách và đề xuất nhắc việc — Biên và bảo mật
  Given Nguồn phản hồi mới chưa sẵn sàng
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện tóm tắt khách và đề xuất nhắc việc
  Then Ghi thiếu nguồn; không bịa khiếu nại hoặc nguy cơ rời
```

## AC-FBR-013-1 — Thành công có điều kiện

US-FBR-013 · FR-AIO-CRMQ-001 · BR-FBR-013

```gherkin
Scenario: Soạn nội dung báo giá nháp để review — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E10-Q08/09/13/15; AIO-Q01–06; E12-Q11
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện soạn nội dung báo giá nháp để review
  Then Nháp báo giá có nguồn và nhãn chưa phát hành; Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này.
```

## AC-FBR-013-2 — Lỗi nghiệp vụ

US-FBR-013 · FR-AIO-CRMQ-001 · BR-FBR-013

```gherkin
Scenario: Soạn nội dung báo giá nháp để review — Lỗi nghiệp vụ
  Given Yêu cầu gửi báo giá hoặc sửa giá hợp đồng
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện soạn nội dung báo giá nháp để review
  Then Từ chối hành động ghi/gửi; chỉ trả nháp
```

## AC-FBR-013-3 — Biên và bảo mật

US-FBR-013 · FR-AIO-CRMQ-001 · BR-FBR-013

```gherkin
Scenario: Soạn nội dung báo giá nháp để review — Biên và bảo mật
  Given Báo giá nguồn đã có revision mới
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện soạn nội dung báo giá nháp để review
  Then Ghi cũ nguồn và yêu cầu review; không thay snapshot cũ
```

## AC-FBR-014-1 — Thành công có điều kiện

US-FBR-014 · FR-AIO-DQA-001 · BR-FBR-014

```gherkin
Scenario: Hỏi đáp số liệu theo quyền — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho AIO-Q01–06; E12-Q06/07/08/12; E10-Q15
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện hỏi đáp số liệu theo quyền
  Then Câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu; Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược.
```

## AC-FBR-014-2 — Lỗi nghiệp vụ

US-FBR-014 · FR-AIO-DQA-001 · BR-FBR-014

```gherkin
Scenario: Hỏi đáp số liệu theo quyền — Lỗi nghiệp vụ
  Given Câu hỏi yêu cầu cập nhật doanh thu hoặc dò cost ngoài quyền
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện hỏi đáp số liệu theo quyền
  Then Không có công cụ ghi; từ chối dữ liệu cấm trước khi đưa vào bộ diễn giải
```

## AC-FBR-014-3 — Biên và bảo mật

US-FBR-014 · FR-AIO-DQA-001 · BR-FBR-014

```gherkin
Scenario: Hỏi đáp số liệu theo quyền — Biên và bảo mật
  Given Quyền bị thu hồi giữa hai lần gọi công cụ
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện hỏi đáp số liệu theo quyền
  Then Lần gọi sau và kết quả cuối bị chặn; không dùng cache quyền cũ
```

## AC-FBR-015-1 — Thành công có điều kiện

US-FBR-015 · FR-NUTR-GRPT-001 · BR-FBR-015

```gherkin
Scenario: Lập mục tiêu dinh dưỡng nhóm — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho NUTR-Q01–04; E12-Q13/14
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập mục tiêu dinh dưỡng nhóm
  Then Mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu; Chỉ mục tiêu cấp nhóm người ăn; không danh sách bệnh lý, hồ sơ cá nhân hoặc suy nhóm từ sức khỏe. Nguồn chỉ số/công thức/ngưỡng chờ NUTR-Q01–04; chưa có thì chỉ nháp thiếu căn cứ, không kích hoạt.
```

## AC-FBR-015-2 — Lỗi nghiệp vụ

US-FBR-015 · FR-NUTR-GRPT-001 · BR-FBR-015

```gherkin
Scenario: Lập mục tiêu dinh dưỡng nhóm — Lỗi nghiệp vụ
  Given Yêu cầu đặt mục tiêu cho một người theo bệnh lý
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập mục tiêu dinh dưỡng nhóm
  Then Từ chối ngoài phạm vi; không lưu hồ sơ
```

## AC-FBR-015-3 — Biên và bảo mật

US-FBR-015 · FR-NUTR-GRPT-001 · BR-FBR-015

```gherkin
Scenario: Lập mục tiêu dinh dưỡng nhóm — Biên và bảo mật
  Given Hai mục tiêu trùng khoảng nhóm khi chưa có policy ưu tiên
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện lập mục tiêu dinh dưỡng nhóm
  Then Không tự chọn mục tiêu mới nhất; giữ xung đột chờ Q14
```

## AC-FBR-016-1 — Thành công có điều kiện

US-FBR-016 · FR-NUTR-GRPC-001 · BR-FBR-016

```gherkin
Scenario: Kiểm thực đơn theo mục tiêu nhóm — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho NUTR-Q01–04; E12-Q13/14; DL-01
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm thực đơn theo mục tiêu nhóm
  Then So sánh có phiên bản hoặc chưa xác định; Đọc bản tính E4 cho tổ hợp suất có nguồn và mục tiêu được duyệt; thiếu công thức/ngưỡng thì chưa đánh giá. Không tự đặt mức kcal hoặc đổi kết quả thành cổng công bố MENU.
```

## AC-FBR-016-2 — Lỗi nghiệp vụ

US-FBR-016 · FR-NUTR-GRPC-001 · BR-FBR-016

```gherkin
Scenario: Kiểm thực đơn theo mục tiêu nhóm — Lỗi nghiệp vụ
  Given Không có nguồn/ngưỡng đã duyệt
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm thực đơn theo mục tiêu nhóm
  Then Không kết luận đạt dinh dưỡng
```

## AC-FBR-016-3 — Biên và bảo mật

US-FBR-016 · FR-NUTR-GRPC-001 · BR-FBR-016

```gherkin
Scenario: Kiểm thực đơn theo mục tiêu nhóm — Biên và bảo mật
  Given Một thành phần suất thiếu giá trị dinh dưỡng
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện kiểm thực đơn theo mục tiêu nhóm
  Then Giữ totals=null theo E4; không so tổng một phần như đầy đủ
```

## AC-FBR-017-1 — Thành công có điều kiện

US-FBR-017 · FR-NUTR-DCON-001 · BR-FBR-017

```gherkin
Scenario: Đồng ý dùng nhật ký bữa đã ăn — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q15/16; E6 CG01/08; E1 NFR-PRIV-001
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đồng ý dùng nhật ký bữa đã ăn
  Then Đồng ý có phiên bản hoặc nhật ký chưa bật; Tự nguyện, không chọn sẵn; nội dung chỉ bữa đã ăn và giá trị của suất. Không gọi FEAT-046/047; từ chối không ảnh hưởng chọn món. Chủ thể lấy từ phiên server; chi tiết identity E6 chưa chốt thì chặn nhận thật.
```

## AC-FBR-017-2 — Lỗi nghiệp vụ

US-FBR-017 · FR-NUTR-DCON-001 · BR-FBR-017

```gherkin
Scenario: Đồng ý dùng nhật ký bữa đã ăn — Lỗi nghiệp vụ
  Given Không đánh dấu đồng ý mà gửi yêu cầu bật
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đồng ý dùng nhật ký bữa đã ăn
  Then Không bật, không ghi bữa hoặc dinh dưỡng cá nhân
```

## AC-FBR-017-3 — Biên và bảo mật

US-FBR-017 · FR-NUTR-DCON-001 · BR-FBR-017

```gherkin
Scenario: Đồng ý dùng nhật ký bữa đã ăn — Biên và bảo mật
  Given Rút đồng ý sau khi đã có bữa
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện đồng ý dùng nhật ký bữa đã ăn
  Then Dừng ghi thêm; cho yêu cầu xóa riêng, không mở hồ sơ sức khỏe
```

## AC-FBR-018-1 — Thành công có điều kiện

US-FBR-018 · FR-NUTR-DREC-001 · BR-FBR-018

```gherkin
Scenario: Ghi bữa đã ăn vào nhật ký — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q15/17; NUTR-Q01–04; E6 CG01/08/10
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện ghi bữa đã ăn vào nhật ký
  Then Bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng; Chỉ nhận bữa đã ăn theo bằng chứng/chính sách E12-Q17; lựa chọn/order/giao nhận không tự chứng minh cá nhân đã ăn. Lưu liên kết tổ hợp và 4 giá trị E4, nhãn ước tính; không trường text sức khỏe, không suy lượng hấp thu.
```

## AC-FBR-018-2 — Lỗi nghiệp vụ

US-FBR-018 · FR-NUTR-DREC-001 · BR-FBR-018

```gherkin
Scenario: Ghi bữa đã ăn vào nhật ký — Lỗi nghiệp vụ
  Given Chỉ có lựa chọn cho ngày mai
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện ghi bữa đã ăn vào nhật ký
  Then Không ghi thành bữa đã ăn
```

## AC-FBR-018-3 — Biên và bảo mật

US-FBR-018 · FR-NUTR-DREC-001 · BR-FBR-018

```gherkin
Scenario: Ghi bữa đã ăn vào nhật ký — Biên và bảo mật
  Given Bữa đã ăn nhưng snapshot thiếu một chỉ số
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện ghi bữa đã ăn vào nhật ký
  Then Không bịa số; hiển thị thiếu nguồn, không coi đủ dinh dưỡng
```

## AC-FBR-019-1 — Thành công có điều kiện

US-FBR-019 · FR-NUTR-DVIW-001 · BR-FBR-019

```gherkin
Scenario: Xem nhật ký dinh dưỡng của mình — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q15/16; E6 CG01/08; NUTR-Q03/04
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem nhật ký dinh dưỡng của mình
  Then Danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực; Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân.
```

## AC-FBR-019-2 — Lỗi nghiệp vụ

US-FBR-019 · FR-NUTR-DVIW-001 · BR-FBR-019

```gherkin
Scenario: Xem nhật ký dinh dưỡng của mình — Lỗi nghiệp vụ
  Given Sửa subjectRef sang người khác
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem nhật ký dinh dưỡng của mình
  Then Không trả bữa hoặc tiết lộ tồn tại của nhật ký khác
```

## AC-FBR-019-3 — Biên và bảo mật

US-FBR-019 · FR-NUTR-DVIW-001 · BR-FBR-019

```gherkin
Scenario: Xem nhật ký dinh dưỡng của mình — Biên và bảo mật
  Given Nguồn dinh dưỡng đổi sau ngày ăn
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện xem nhật ký dinh dưỡng của mình
  Then Giữ snapshot lịch sử và nhãn nguồn cũ, không viết lại
```

## AC-FBR-020-1 — Thành công có điều kiện

US-FBR-020 · FR-NUTR-DDEL-001 · BR-FBR-020

```gherkin
Scenario: Yêu cầu xóa nhật ký và rút đồng ý — Thành công có điều kiện
  Given đã có quyết định và dữ liệu đúng phiên bản cho E12-Q15/16; E1 NFR-PRIV-001
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu xóa nhật ký và rút đồng ý
  Then Receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút; Xác thực chủ thể, cho xóa dữ liệu của mình theo nền ≤ 72 giờ; không xóa giao dịch nguồn E6/E7. Cơ chế bản sao/retention chờ Q16; receipt chỉ xác nhận nhận yêu cầu, không báo đã xóa khi chưa có evidence.
```

## AC-FBR-020-2 — Lỗi nghiệp vụ

US-FBR-020 · FR-NUTR-DDEL-001 · BR-FBR-020

```gherkin
Scenario: Yêu cầu xóa nhật ký và rút đồng ý — Lỗi nghiệp vụ
  Given Yêu cầu xóa nhật ký của người khác
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu xóa nhật ký và rút đồng ý
  Then Từ chối trước khi ghi yêu cầu
```

## AC-FBR-020-3 — Biên và bảo mật

US-FBR-020 · FR-NUTR-DDEL-001 · BR-FBR-020

```gherkin
Scenario: Yêu cầu xóa nhật ký và rút đồng ý — Biên và bảo mật
  Given Gửi lặp khi yêu cầu xóa đang xử lý
  And chủ thể được xác thực trong scope kiểm thử, trừ ca cố tình vượt quyền
  When người dùng thực hiện yêu cầu xóa nhật ký và rút đồng ý
  Then Trả cùng receipt theo quyền hiện tại, không tuyên bố hoàn tất sớm
```

