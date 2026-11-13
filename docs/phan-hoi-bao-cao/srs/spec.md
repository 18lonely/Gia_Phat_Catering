---
id: DOC-E12-SRS-SPEC-MD
title: "SRS E12: Phản hồi và báo cáo"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# SRS E12: Phản hồi và báo cáo

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## 1. Giới thiệu

Đặc tả theo IEEE 830/29148, đúng [9 feature](../epic-spec.md). Provenance là căn cứ truy về hệ thống nguồn, bản ghi/phiên bản, phạm vi và thời điểm. Receipt là bằng chứng tiếp nhận, không đồng nghĩa duyệt/hoàn tất.

## 2. Tổng quan

Web desktop/mobile, quyền theo chủ thể × cơ sở × khách × trường dữ liệu. E1 giữ xác thực, scope, audit. E12 chỉ nhận dữ liệu đủ căn cứ từ E2/E3/E4/E5/E6/E7/E9/E10/E11; chưa có nguồn thì chỉ mô tả cổng thiếu, không tự bổ sung producer. [Phụ thuộc](../review/dependencies.md).

## 3.1 Yêu cầu chức năng

| FR / Feature | Tên / Actor | Ưu tiên | Input | Xử lý | Output | BR / ERR | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-FB-RATE-001 / FEAT-079 | Gửi đánh giá bữa ăn (PER-02, PER-03, PER-04, PER-05) | P1 | mealRef, ratingScaleRef, ratingValue, sourceScope | Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn. | Đánh giá có receipt và trạng thái tiếp nhận | BR-FBR-001; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q01/02; E6 CG01/08 |
| FR-FB-CASE-001 / FEAT-079 | Tiếp nhận và theo dõi khiếu nại (PER-02, PER-03, PER-04, PER-05) | P1 | mealRef, complaintCategoryRef, nội dung về bữa, caseVersion | Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn. | Hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách | BR-FBR-002; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q02/03; E6 CG01/08; E7-Q02 |
| FR-FB-SELR-001 / FEAT-080 | Xem tỷ lệ được chọn theo món (PER-05) | P1 | ngày, khách, điểm, ca, dishRef, selectionSourceRef | Chỉ lấy lựa chọn thật của người ăn từ E6; phân biệt tự chọn với gán mặc định, nhập tổng và sản xuất. Chưa có mẫu số hoặc provenance đủ thì tỷ lệ null, không tự chọn trong ba mẫu số. | Số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định | BR-FBR-003; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q04; E6 CG01–14, ORD-Q01–15, E6-EVID-001/002 |
| FR-FB-PROP-001 / FEAT-080 | Lập đề xuất cải tiến thực đơn từ phản hồi (PER-05) | P1 | dishMetricRefs, feedbackRefs, menuRef, revision, ghi chú đề xuất | Người dùng đọc dữ liệu có nguồn, tự chọn món cần rà; thiếu mẫu số không xếp hạng tỷ lệ. Lưu đề xuất nháp riêng, không tự đổi MENU; thay món hoặc định lượng phải qua E2, dị ứng và E3. | Đề xuất nháp cùng căn cứ và điều kiện kiểm lại | BR-FBR-004; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q04/05; DL-01; O-02 |
| FR-RPT-ROLE-001 / FEAT-081 | Xem dashboard theo bốn vai trò (PER-05, PER-06, PER-07, PER-08) | P1 | roleView, dateRange, customerRef, kitchenRef | Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn. | Bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng | BR-FBR-005; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q06/07/08; E7-Q03/04; E10-Q07; E11-Q07/08 |
| FR-RPT-CPCT-001 / FEAT-081 | Đọc cost % ngày và theo khách: PER-05, PER-06, PER-07, PER-08 theo quyền riêng | P1 | date, customerRef, kitchenRef, costResultRef | Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13. | Cost % ngày có nguồn E3; ô theo khách chưa xác định khi thiếu công thức | BR-FBR-006; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q07/08; O-01; DATA-COST-Q01–06; E11-Q07/08 |
| FR-AIO-PRRV-001 / FEAT-082 | Yêu cầu rà soát thực đơn khi giá đổi (PER-05, PER-08) | P1 | priceChangeRef, menuRef, menuRevision, scope | Chỉ đọc sự kiện giá E3 và thực đơn được phép; diễn giải ảnh hưởng và đề xuất đổi món hoặc định lượng có nguồn. Không ghi giá, công thức hay thực đơn. Không tự tính tiền. | Đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn | BR-FBR-007; ERR-FBR-422-01; lỗi chung theo điều kiện | AIO-Q01–06; E12-Q09; O-01/O-02 |
| FR-AIO-RCHK-001 / FEAT-082 | Kiểm lại đề xuất đổi món hoặc định lượng (PER-05, PER-08) | P1 | candidateRef, candidateRevision, menuSourceRef | Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO. | Bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật | BR-FBR-008; ERR-FBR-422-01; lỗi chung theo điều kiện | AIO-Q02/05/06; DL-01; E11-Q15; E12-Q09 |
| FR-AIO-ESTR-001 / FEAT-083 | Diễn giải dự toán có nguồn (PER-07) | P1 | estimateRef, estimateRevision, date, kitchenRef | Chỉ đọc dự toán E3 trong scope; giữ lượng mua, đơn vị, giá gồm VAT, khoản khoán và tổng từ hệ thống; AI chỉ giải thích, không tạo con số. | Nháp diễn giải dự toán chờ người thật rà | BR-FBR-009; ERR-FBR-422-01; lỗi chung theo điều kiện | AIO-Q01–06; E12-Q09; DATA-COST-Q01–06 |
| FR-AIO-DEMR-001 / FEAT-083 | Diễn giải nhu cầu nguyên liệu (PER-07) | P1 | demandRef, planRevisionRef, estimateRef | Đọc nhu cầu E11 và revision nguồn; phân biệt nhu cầu gộp với mua ròng. Chưa chốt trừ tồn/dự phòng thì không đề xuất lượng mua ròng; không tạo đơn mua hoặc chọn NCC. | Nháp diễn giải nhu cầu với thiếu nguồn rõ ràng | BR-FBR-010; ERR-FBR-422-01; lỗi chung theo điều kiện | E11-Q01/03/13; E6 CG06; AIO-Q01–06 |
| FR-AIO-PDEV-001 / FEAT-083 | Giải thích cảnh báo giá lệch (PER-07) | P1 | comparisonRef, priceSourceRefs, alertPolicyRef | Đọc so sánh E3/E11 cùng đơn vị, VAT, thời điểm và scope. Ngưỡng giá lệch chờ E12-Q10; không mượn BO-02 hoặc sai số NFR làm ngưỡng giá. | Nháp giải thích; cảnh báo chính thức chưa xác định | BR-FBR-011; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q10; E11-Q07/08/14; AIO-Q01–06 |
| FR-AIO-CRMS-001 / FEAT-084 | Tóm tắt khách và đề xuất nhắc việc (PER-05, PER-08) | P1 | customerRef, timeRange, CRM sourceRefs | Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ. | Nháp tóm tắt và danh sách việc cần người thật rà | BR-FBR-012; ERR-FBR-422-01; lỗi chung theo điều kiện | E10-Q01/05/06/13; AIO-Q01–06; E12-Q11 |
| FR-AIO-CRMQ-001 / FEAT-084 | Soạn nội dung báo giá nháp để review (PER-05, PER-08) | P1 | customerRef, quoteRevisionRef, menuRef, nguồn giá được phép | Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này. | Nháp báo giá có nguồn và nhãn chưa phát hành | BR-FBR-013; ERR-FBR-422-01; lỗi chung theo điều kiện | E10-Q08/09/13/15; AIO-Q01–06; E12-Q11 |
| FR-AIO-DQA-001 / FEAT-085 | Hỏi đáp số liệu theo quyền (PER-07, PER-08) | P2 | câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef | Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược. | Câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu | BR-FBR-014; ERR-FBR-422-01; lỗi chung theo điều kiện | AIO-Q01–06; E12-Q06/07/08/12; E10-Q15 |
| FR-NUTR-GRPT-001 / FEAT-086 | Lập mục tiêu dinh dưỡng nhóm (PER-05) | P1 | groupRef phi y tế, mục tiêu có sourceRef, effectiveRange, version | Chỉ mục tiêu cấp nhóm người ăn; không danh sách bệnh lý, hồ sơ cá nhân hoặc suy nhóm từ sức khỏe. Nguồn chỉ số/công thức/ngưỡng chờ NUTR-Q01–04; chưa có thì chỉ nháp thiếu căn cứ, không kích hoạt. | Mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu | BR-FBR-015; ERR-FBR-422-01; lỗi chung theo điều kiện | NUTR-Q01–04; E12-Q13/14 |
| FR-NUTR-GRPC-001 / FEAT-086 | Kiểm thực đơn theo mục tiêu nhóm (PER-05) | P1 | groupTargetRef, targetVersion, menuRevision, nutritionCalculationRefs | Đọc bản tính E4 cho tổ hợp suất có nguồn và mục tiêu được duyệt; thiếu công thức/ngưỡng thì chưa đánh giá. Không tự đặt mức kcal hoặc đổi kết quả thành cổng công bố MENU. | So sánh có phiên bản hoặc chưa xác định | BR-FBR-016; ERR-FBR-422-01; lỗi chung theo điều kiện | NUTR-Q01–04; E12-Q13/14; DL-01 |
| FR-NUTR-DCON-001 / FEAT-087 | Đồng ý dùng nhật ký bữa đã ăn (PER-03) | P2 | consentPolicyRef, explicitAgreement | Tự nguyện, không chọn sẵn; nội dung chỉ bữa đã ăn và giá trị của suất. Không gọi FEAT-046/047; từ chối không ảnh hưởng chọn món. Chủ thể lấy từ phiên server; chi tiết identity E6 chưa chốt thì chặn nhận thật. | Đồng ý có phiên bản hoặc nhật ký chưa bật | BR-FBR-017; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q15/16; E6 CG01/08; E1 NFR-PRIV-001 |
| FR-NUTR-DREC-001 / FEAT-087 | Ghi bữa đã ăn vào nhật ký (PER-03) | P2 | consentRef, consumedMealRef, consumedAt, mealNutritionSnapshotRef | Chỉ nhận bữa đã ăn theo bằng chứng/chính sách E12-Q17; lựa chọn/order/giao nhận không tự chứng minh cá nhân đã ăn. Lưu liên kết tổ hợp và 4 giá trị E4, nhãn ước tính; không trường text sức khỏe, không suy lượng hấp thu. | Bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng | BR-FBR-018; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q15/17; NUTR-Q01–04; E6 CG01/08/10 |
| FR-NUTR-DVIW-001 / FEAT-087 | Xem nhật ký dinh dưỡng của mình (PER-03) | P2 | dateRange; subject từ phiên | Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân. | Danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực | BR-FBR-019; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q15/16; E6 CG01/08; NUTR-Q03/04 |
| FR-NUTR-DDEL-001 / FEAT-087 | Yêu cầu xóa nhật ký và rút đồng ý (PER-03) | P2 | consentRef, diaryScope, explicitDeleteConfirmation | Xác thực chủ thể, cho xóa dữ liệu của mình theo nền ≤ 72 giờ; không xóa giao dịch nguồn E6/E7. Cơ chế bản sao/retention chờ Q16; receipt chỉ xác nhận nhận yêu cầu, không báo đã xóa khi chưa có evidence. | Receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút | BR-FBR-020; ERR-FBR-422-01; lỗi chung theo điều kiện | E12-Q15/16; E1 NFR-PRIV-001 |

Mọi FR chịu kiểm quyền/scope và ma trận lỗi chung; GET chỉ đọc, không chạy công cụ ghi hoặc tạo bản tính ẩn. Nhánh phụ thuộc gate giữ BLOCKED, không coi đề xuất là chính sách đã chọn.

## 3.2 Quy tắc nghiệp vụ

| BR | KHI | THÌ | Ngoại lệ |
| :--- | :--- | :--- | :--- |
| BR-FBR-001 | Gửi đánh giá bữa ăn | Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-002 | Tiếp nhận và theo dõi khiếu nại | Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-003 | Xem tỷ lệ được chọn theo món | Chỉ lấy lựa chọn thật của người ăn từ E6; phân biệt tự chọn với gán mặc định, nhập tổng và sản xuất. Chưa có mẫu số hoặc provenance đủ thì tỷ lệ null, không tự chọn trong ba mẫu số. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-004 | Lập đề xuất cải tiến thực đơn từ phản hồi | Người dùng đọc dữ liệu có nguồn, tự chọn món cần rà; thiếu mẫu số không xếp hạng tỷ lệ. Lưu đề xuất nháp riêng, không tự đổi MENU; thay món hoặc định lượng phải qua E2, dị ứng và E3. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-005 | Xem dashboard theo bốn vai trò | Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-006 | Đọc cost % ngày và theo khách | Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-007 | Yêu cầu rà soát thực đơn khi giá đổi | Chỉ đọc sự kiện giá E3 và thực đơn được phép; diễn giải ảnh hưởng và đề xuất đổi món hoặc định lượng có nguồn. Không ghi giá, công thức hay thực đơn. Không tự tính tiền. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-008 | Kiểm lại đề xuất đổi món hoặc định lượng | Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-009 | Diễn giải dự toán có nguồn | Chỉ đọc dự toán E3 trong scope; giữ lượng mua, đơn vị, giá gồm VAT, khoản khoán và tổng từ hệ thống; AI chỉ giải thích, không tạo con số. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-010 | Diễn giải nhu cầu nguyên liệu | Đọc nhu cầu E11 và revision nguồn; phân biệt nhu cầu gộp với mua ròng. Chưa chốt trừ tồn/dự phòng thì không đề xuất lượng mua ròng; không tạo đơn mua hoặc chọn NCC. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-011 | Giải thích cảnh báo giá lệch | Đọc so sánh E3/E11 cùng đơn vị, VAT, thời điểm và scope. Ngưỡng giá lệch chờ E12-Q10; không mượn BO-02 hoặc sai số NFR làm ngưỡng giá. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-012 | Tóm tắt khách và đề xuất nhắc việc | Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-013 | Soạn nội dung báo giá nháp để review | Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-014 | Hỏi đáp số liệu theo quyền | Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-015 | Lập mục tiêu dinh dưỡng nhóm | Chỉ mục tiêu cấp nhóm người ăn; không danh sách bệnh lý, hồ sơ cá nhân hoặc suy nhóm từ sức khỏe. Nguồn chỉ số/công thức/ngưỡng chờ NUTR-Q01–04; chưa có thì chỉ nháp thiếu căn cứ, không kích hoạt. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-016 | Kiểm thực đơn theo mục tiêu nhóm | Đọc bản tính E4 cho tổ hợp suất có nguồn và mục tiêu được duyệt; thiếu công thức/ngưỡng thì chưa đánh giá. Không tự đặt mức kcal hoặc đổi kết quả thành cổng công bố MENU. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-017 | Đồng ý dùng nhật ký bữa đã ăn | Tự nguyện, không chọn sẵn; nội dung chỉ bữa đã ăn và giá trị của suất. Không gọi FEAT-046/047; từ chối không ảnh hưởng chọn món. Chủ thể lấy từ phiên server; chi tiết identity E6 chưa chốt thì chặn nhận thật. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-018 | Ghi bữa đã ăn vào nhật ký | Chỉ nhận bữa đã ăn theo bằng chứng/chính sách E12-Q17; lựa chọn/order/giao nhận không tự chứng minh cá nhân đã ăn. Lưu liên kết tổ hợp và 4 giá trị E4, nhãn ước tính; không trường text sức khỏe, không suy lượng hấp thu. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-019 | Xem nhật ký dinh dưỡng của mình | Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân. | Không; thiếu căn cứ giữ BLOCKED |
| BR-FBR-020 | Yêu cầu xóa nhật ký và rút đồng ý | Xác thực chủ thể, cho xóa dữ liệu của mình theo nền ≤ 72 giờ; không xóa giao dịch nguồn E6/E7. Cơ chế bản sao/retention chờ Q16; receipt chỉ xác nhận nhận yêu cầu, không báo đã xóa khi chưa có evidence. | Không; thiếu căn cứ giữ BLOCKED |

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm số phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02 ≤ 3 điểm phần trăm là mục tiêu R11, không phải sai số tính toán. FR-MENU-RCP-007 chặn O-02; FEAT-046/047/063 chặn O-03.

## 3.3 Giao diện ngoài và an toàn AI

[API](../api/api-spec.md), [mapping](../api/data-mapping.md), [màn](../ui/screens.md). Các công cụ là port chỉ đọc/kiểm thuần, chặn quyền tại registry/API/service/DB theo giao quyền E5 và BR-SEC-009. Không cấp SQL/URL tùy ý, công cụ ghi, duyệt hay gửi. Nội dung CRM và câu hỏi là dữ liệu không đáng tin; không trở thành quyền hoặc chỉ dẫn hệ thống. Lọc trước bộ diễn giải và trước trả ra UI, lỗi, cache, log. Đầu ra của cả FEAT-082–085 luôn là đề xuất nháp chờ người thật duyệt; quyết định review không thực hiện thay đổi nghiệp vụ. Không mô tả system prompt, nhà cung cấp hoặc model.

## 3.4 Yêu cầu phi chức năng

| Mã | Tiêu chí đo / kiểm | Gate |
| :--- | :--- | :--- |
| NFR-FBR-001 | 0 lần đọc chéo khách/cơ sở/chủ thể hoặc lộ cost/biên lợi nhuận ngoài quyền qua API/tool/DB/UI/lỗi/log/cache; thử thu hồi quyền giữa lượt | E12-Q07/12/18; E1 |
| NFR-FBR-002 | 100% số hiển thị có nguồn, revision, asOf, phạm vi, định nghĩa; thiếu khác 0; không cộng trộn cơ sở đo | E12-Q04/06/08; nguồn chưa freeze |
| NFR-FBR-003 | 100% thay đổi E12 có actor/thời điểm/trước-sau/lý do và receipt; retry không ghi trùng | E12-Q18; E1-Q01–05 |
| NFR-FBR-004 | 0 trường sức khỏe hoặc gợi ý cá nhân trong nhật ký; đồng ý trước ghi; xóa được ≤ 72 giờ theo NFR-PRIV-001 | E12-Q15/16/17; không đặt retention |
| NFR-FBR-005 | Kế thừa 1000 người đồng thời, p95 API đọc ≤ 300 ms và ghi ≤ 800 ms của nền; AI ngoài luồng web, không tự áp deadline E5 cho mọi loại trả lời | Profile E12-Q18; AIO-Q01–06 |
| NFR-FBR-006 | Ở 1440 / 390 / 360 px mọi màn đọc được, không tràn ngang trang; nhãn và focus bàn phím; mục tiêu WCAG 2.1 AA theo nền | Kiểm mock riêng, chưa audit đầy đủ |
| NFR-FBR-007 | Đối chiếu nguồn cost theo NFR-COST-002; 10 món và 10 ngày của kế toán, sai số ≤ 1 đ và ≤ 0,01 điểm phần trăm | DATA-COST-Q01–06; không thay BO-02 |


## 3.5 Lỗi và 4. Phụ lục

[Ma trận lỗi](error-matrix.md) · [Từ điển](data-dictionary.md) · [Trạng thái](states.md) · [RTM](../test/traceability.md). Schema chung giữ 65 bảng; delta chỉ đề xuất.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp producer đang chờ. Chỉ ghi điều kiện nhận dữ liệu của E12 và tiếp tục phần độc lập.
