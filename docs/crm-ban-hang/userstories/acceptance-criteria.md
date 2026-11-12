---
id: DOC-E10-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: 48 tiêu chí Given / When / Then
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# 48 tiêu chí Given / When / Then

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

| AC | Story | FR | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AC-CRM-001-01 | US-CRM-001 | FR-CUS-VIEW-001 | nguồn order và doanh thu đã được xác nhận cho khách A | mở hồ sơ A trong kỳ được phép | hiện đúng nguồn và phiên bản; tổng doanh thu có nhãn phạm vi, không tự tính từ số giao |
| AC-CRM-001-02 | US-CRM-001 | FR-CUS-VIEW-001 | nguồn doanh thu hoặc phản hồi chưa có | mở hồ sơ A | nhóm tương ứng ghi CHƯA CÓ NGUỒN; giá trị null, không 0; không mở chức năng phản hồi E12 |
| AC-CRM-001-03 | US-CRM-001 | FR-CUS-VIEW-001 | người dùng chỉ có phạm vi khách A | đổi mã hồ sơ sang khách B | trả ERR-CRM-404-01; không lộ liên hệ hoặc tổng tiền của B |
| AC-CRM-002-01 | US-CRM-002 | FR-CUS-CONT-001 | danh mục trường và quyền lưu liên hệ đã được duyệt | ghi đầu mối A từ nguồn xác minh | tạo đúng một bản nháp liên hệ và audit, không tạo users hoặc service_points |
| AC-CRM-002-02 | US-CRM-002 | FR-CUS-CONT-001 | yêu cầu chứa role quản trị hoặc customerId ngoài phạm vi | gửi nháp liên hệ | từ chối trường lạ hoặc phạm vi; không cấp quyền đặt món |
| AC-CRM-002-03 | US-CRM-002 | FR-CUS-CONT-001 | quyết định thời gian lưu và xử lý xóa chưa có | yêu cầu lưu hoặc xóa thông tin liên hệ thật | giữ BLOCKED E10-Q01; không dùng thời gian lưu audit làm thời gian lưu liên hệ |
| AC-CRM-003-01 | US-CRM-003 | FR-CUS-LEAD-001 | hai bên đã duyệt trường bàn giao, consent và đầu nhận | nhận đề xuất từ PORT-AIN-HANDOFF hoặc PORT-PUB-LEAD-HANDOFF | receipt gắn đúng nguồn và hash sau ghi bền vững; trạng thái chờ người thật phân loại |
| AC-CRM-003-02 | US-CRM-003 | FR-CUS-LEAD-001 | đầu nhận hoặc consent chưa được duyệt | nhận đề xuất thật | trả ERR-CRM-503-01; không báo đã vào CRM và không tự tạo customers |
| AC-CRM-003-03 | US-CRM-003 | FR-CUS-LEAD-001 | phiếu đã lưu nhưng mất phản hồi | nhận lại cùng nguồn, revision và nội dung | trả receipt cũ theo quyền hiện tại; khác hash cùng định danh trả ERR-CRM-409-02 |
| AC-CRM-004-01 | US-CRM-004 | FR-CUS-DUP-001 | tiêu chí phát hiện đã được duyệt và cặp hồ sơ thuộc quyền | rà cặp nghi trùng và lập đề nghị | lưu tiêu chí phiên bản, bằng chứng và lựa chọn từng trường; chưa thay mã khách |
| AC-CRM-004-02 | US-CRM-004 | FR-CUS-DUP-001 | chưa chốt tiêu chí phát hiện trùng | yêu cầu quét tự động | BLOCKED E10-Q02; không tự chọn số điện thoại, tên hoặc mã số thuế làm khóa gộp |
| AC-CRM-004-03 | US-CRM-004 | FR-CUS-DUP-001 | hai khách khác nhau dùng chung một đầu mối | đánh giá cặp theo tiêu chí chính thức | kết quả theo bộ tiêu chí được duyệt; không có quy tắc mặc định coi chung đầu mối là trùng |
| AC-CRM-005-01 | US-CRM-005 | FR-CUS-MRG-001 | đề nghị đủ bằng chứng, nguồn và người duyệt được chỉ định | duyệt gộp đúng phiên bản | ghi gộp cùng audit và ảnh trước; vẫn truy được nguồn order, hợp đồng và doanh thu cũ |
| AC-CRM-005-02 | US-CRM-005 | FR-CUS-MRG-001 | người lập đề nghị tự duyệt hoặc chưa có quyền duyệt | gửi quyết định gộp | ERR-CRM-403-01 hoặc ERR-CRM-503-01; không thay ánh xạ khách |
| AC-CRM-005-03 | US-CRM-005 | FR-CUS-MRG-001 | một hồ sơ đổi version sau khi người duyệt mở diff | xác nhận gộp bằng version cũ | ERR-CRM-409-01; tải lại diff, không ghi đè thay đổi mới |
| AC-CRM-006-01 | US-CRM-006 | FR-CUS-UNDO-001 | người duyệt và phương án khôi phục đã được duyệt, không có xung đột mới | xác nhận hoàn tác lần gộp | khôi phục liên kết theo ảnh trước, ghi sự kiện bù; audit gộp còn nguyên |
| AC-CRM-006-02 | US-CRM-006 | FR-CUS-UNDO-001 | thiếu ảnh trước gộp hoặc có tham chiếu mới chưa có phương án | yêu cầu hoàn tác | ERR-CRM-422-01 hoặc BLOCKED E10-Q04; không khôi phục một phần |
| AC-CRM-006-03 | US-CRM-006 | FR-CUS-UNDO-001 | đã phát sinh order và hợp đồng mới sau gộp | lập phương án hoàn tác | phân bổ theo quyết định được duyệt; không tự chuyển toàn bộ giao dịch mới về một khách |
| AC-CRM-007-01 | US-CRM-007 | FR-CUS-LIFE-001 | ma trận và người có quyền đã được duyệt, có bằng chứng chuyển | đề nghị đổi từ PAUSED sang REACTIVATED | ghi trạng thái và evidence theo ma trận, giữ lịch sử trạng thái cũ |
| AC-CRM-007-02 | US-CRM-007 | FR-CUS-LIFE-001 | không có order vào ngày không nằm trong lịch phục vụ | xem vòng đời khách | không tự chuyển CHURNED hoặc AT_RISK chỉ từ sự vắng mặt đó |
| AC-CRM-007-03 | US-CRM-007 | FR-CUS-LIFE-001 | khách có nhiều điểm với lịch phục vụ khác nhau | tổng hợp vòng đời khách | áp đúng quy tắc tổng hợp đã được duyệt; chưa có quy tắc thì BLOCKED E10-Q05 |
| AC-CRM-008-01 | US-CRM-008 | FR-CUS-RISK-001 | lịch ngoại lệ, ngưỡng và nguồn sự kiện đã được duyệt | đọc tín hiệu của khách A | giải thích bằng các kỳ phục vụ đủ điều kiện và nguồn, không dùng số ngày lịch đơn thuần |
| AC-CRM-008-02 | US-CRM-008 | FR-CUS-RISK-001 | lịch thiếu hoặc dữ liệu giao nhận chưa xác nhận | xem tín hiệu | hiện CHƯA ĐỦ DỮ LIỆU và nguyên nhân, không chấm rủi ro thấp hoặc cao giả |
| AC-CRM-008-03 | US-CRM-008 | FR-CUS-RISK-001 | cùng dữ liệu được đọc lại hai lần | GET tín hiệu | không sinh thêm cảnh báo, không đổi vòng đời, giữ cùng evaluationRef |
| AC-CRM-009-01 | US-CRM-009 | FR-SALE-OPP-001 | giai đoạn, chủ cơ hội và định nghĩa chuyển đã được duyệt | ghi sự kiện chuyển cơ hội | lưu nguồn, thời điểm và stage đúng ma trận; bảng phễu không đếm trùng do nhiều phiên bản báo giá |
| AC-CRM-009-02 | US-CRM-009 | FR-SALE-OPP-001 | chỉ có báo giá đã gửi, chưa có bằng chứng thắng | đề nghị ghi WON | ERR-CRM-422-01; không tự suy thắng từ việc gửi báo giá |
| AC-CRM-009-03 | US-CRM-009 | FR-SALE-OPP-001 | mẫu số cơ hội của kỳ bằng 0 | xem tỷ lệ chuyển đổi | hiện chưa có cơ sở tính, tỷ lệ null; không chia 0 hoặc hiển thị 100% |
| AC-CRM-010-01 | US-CRM-010 | FR-SALE-QUOT-001 | chính sách báo giá và giá/VAT đã được duyệt | soạn revision mới từ báo giá đã phát hành | revision mới ở DRAFT, bản cũ và bằng chứng phát hành không đổi |
| AC-CRM-010-02 | US-CRM-010 | FR-SALE-QUOT-001 | client gửi approvedBy, margin hoặc số tổng để ép kết quả | lưu báo giá | từ chối trường ngoài hợp đồng; không tin tổng hay người duyệt client |
| AC-CRM-010-03 | US-CRM-010 | FR-SALE-QUOT-001 | hai người cùng sửa baseRevision | lưu bản thứ hai sau khi bản thứ nhất đã ghi | ERR-CRM-409-01; không mất diff và không ghi đè revision |
| AC-CRM-011-01 | US-CRM-011 | FR-SALE-MENU-001 | nguồn MENU và quyền đưa cho khách đã được xác nhận | gắn thực đơn vào revision báo giá | lưu menuRevision và hash, khách chỉ thấy projection được phép của bản đính kèm |
| AC-CRM-011-02 | US-CRM-011 | FR-SALE-MENU-001 | nguồn thực đơn bị thu hồi hoặc chỉ có nháp E9 chưa duyệt | đính kèm để phát hành báo giá | ERR-CRM-422-01 hoặc BLOCKED theo nguồn; không tự công bố MENU |
| AC-CRM-011-03 | US-CRM-011 | FR-SALE-MENU-001 | MENU có bản mới sau khi báo giá đã phát hành | mở lại báo giá cũ | giữ đúng bản đính kèm cũ và cảnh báo nguồn; muốn thay phải tạo revision mới |
| AC-CRM-012-01 | US-CRM-012 | FR-SALE-SAFE-001 | báo giá được duyệt và nguồn còn hợp lệ | tạo bản phát hành cho khách A | chỉ có mã/phiên bản, giá bán được duyệt, điều kiện và thực đơn an toàn; không cost hoặc margin |
| AC-CRM-012-02 | US-CRM-012 | FR-SALE-SAFE-001 | dữ liệu lồng nhau hoặc lỗi chứa purchasePrice, costAmount hoặc margin | tạo projection khách | loại theo allowlist trước lưu/xuất, không có trường nhạy cảm trong JSON, HTML, metadata, lỗi hoặc cache |
| AC-CRM-012-03 | US-CRM-012 | FR-SALE-SAFE-001 | khách B hoặc tài khoản AIN truy bản dành cho A | đọc bản phát hành | ERR-CRM-404-01 hoặc ERR-CRM-403-01; không trả bản nội bộ và không nâng quyền dịch vụ |
| AC-CRM-013-01 | US-CRM-013 | FR-SALE-CONT-001 | khách chấp thuận đúng revision và bằng chứng được duyệt | lập hợp đồng từ báo giá | hợp đồng DRAFT giữ quoteRevision/hash và evidence, không tự ACTIVE |
| AC-CRM-013-02 | US-CRM-013 | FR-SALE-CONT-001 | bằng chứng thuộc revision cũ nhưng yêu cầu lấy giá revision mới | lập hợp đồng | ERR-CRM-409-01; yêu cầu đối chiếu lại, không đổi giá khách đã nhận |
| AC-CRM-013-03 | US-CRM-013 | FR-SALE-CONT-001 | chỉ có lượt mở báo giá, không có bằng chứng chấp thuận | lập hợp đồng theo luồng báo giá đã chấp thuận | ERR-CRM-422-01; không coi lượt xem là ký hoặc chấp thuận |
| AC-CRM-014-01 | US-CRM-014 | FR-SALE-ACTV-001 | quy ước hiệu lực và quyền duyệt đã được chốt, có bằng chứng ký | kích hoạt bộ giá không chồng lấn | mỗi customer + mealType + ngày áp dụng có tối đa một giá ACTIVE; dữ liệu và audit cùng giao dịch |
| AC-CRM-014-02 | US-CRM-014 | FR-SALE-ACTV-001 | hai bộ giá cùng khách và loại suất có phần giao nhau | kích hoạt bộ thứ hai | ERR-CRM-409-03; không ACTIVE một phần và không chọn giá theo bản ghi mới nhất |
| AC-CRM-014-03 | US-CRM-014 | FR-SALE-ACTV-001 | hai bộ giá liền kề đúng ngày kết thúc/bắt đầu | kiểm tra hiệu lực tại ranh giới | kết quả theo quy ước biên đã duyệt E10-Q11; trước quyết định thì BLOCKED |
| AC-CRM-015-01 | US-CRM-015 | FR-SALE-AMND-001 | có chính sách phụ lục và thời điểm hiệu lực được duyệt | lập phụ lục giá cho kỳ tới | lưu bản nháp có predecessor và diff; giá cũ vẫn được truy nguyên |
| AC-CRM-015-02 | US-CRM-015 | FR-SALE-AMND-001 | người dùng đòi sửa trực tiếp bản giá đã dùng cho order | gửi phụ lục kèm lệnh ghi đè lịch sử | ERR-CRM-422-01; không sửa snapshot và không tự mở kỳ khóa E7 |
| AC-CRM-015-03 | US-CRM-015 | FR-SALE-AMND-001 | gửi lại cùng khóa và cùng nội dung phụ lục | lưu lại sau mất phản hồi | trả cùng phụ lục, không tạo hai chuỗi thay thế |
| AC-CRM-016-01 | US-CRM-016 | FR-SALE-PRIC-001 | đúng một bộ giá hợp lệ cho khách, loại suất và ngày | tra giá theo ngày phục vụ | trả giá và căn cứ thuế cùng nguồn hợp đồng/phụ lục; GET không ghi order |
| AC-CRM-016-02 | US-CRM-016 | FR-SALE-PRIC-001 | không có hoặc có hơn một giá khớp, VAT cần thiết chưa rõ | tra giá | UNRESOLVED hoặc ERR-CRM-409-03; không lấy giá 0 hoặc tự chọn giá mới nhất |
| AC-CRM-016-03 | US-CRM-016 | FR-SALE-PRIC-001 | đơn lịch sử đã có pricingSnapshot và sau đó có phụ lục mới | xem hồ sơ đơn cũ | vẫn dùng snapshot đúng order/version từ E6/Cost; không thay bằng kết quả tra giá hiện tại |

Mỗi story có đúng ba AC: thành công có điều kiện, lỗi nghiệp vụ, biên/quyền. Mỗi AC chỉ một ca chức năng tại [ca kiểm](../test/test-cases.md).
