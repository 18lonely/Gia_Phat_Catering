# Sổ quyết định cần review Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft; O-01 được xác nhận một phần trong phiên, các chi tiết còn lại chờ review.

Mỗi dòng giữ nguyên mã điểm mở của nguồn. Phương án dưới đây là đề xuất thảo luận, không sửa SRS, không cấu hình hệ thống và không thay chữ ký chủ sở hữu. Danh sách test chỉ lấy mã xuất hiện trực tiếp trong gate, không phải toàn bộ tác động gián tiếp. Không cộng số test giữa các điểm vì một ca có thể phụ thuộc nhiều quyết định.

Thứ tự phiên review đề xuất: (1) kế toán/Giám đốc chốt O-01, E3-Q1/Q2/Q4/Q14/Q15/Q16; (2) BA/Tech lead chốt FLOW-Q01–Q07 và QA-Q01; (3) xử lý agent/P1/P2 theo release. Mốc ngày họp, tên người phụ trách cụ thể và thời hạn chưa được ấn định.

| Mã | Câu hỏi | Chủ sở hữu theo tài liệu | Trạng thái |
| :--- | :--- | :--- | :--- |
| [O-01](#o-01) | Thành phần cost; khoản khoán; VAT; giá nhập có gồm VAT đầu vào | Kế toán | PARTIALLY_CONFIRMED |
| [E3-Q1](#e3-q1) | Cost phần món chính | Giám đốc, kế toán | OPEN |
| [E3-Q2](#e3-q2) | Định lượng sống đã gồm xương, vỏ chưa | Người soạn docx, bếp trưởng | OPEN |
| [E3-Q3](#e3-q3) | Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào | Kế toán | OPEN |
| [E3-Q4](#e3-q4) | Giá nào là giá tham chiếu | Kế toán | OPEN |
| [E3-Q5](#e3-q5) | Tần suất cập nhật giá thực tế | Kế toán | OPEN |
| [E3-Q6](#e3-q6) | Giá nhập có cần duyệt | Giám đốc | OPEN |
| [E3-Q7](#e3-q7) | Định nghĩa cost cao / thấp | Người soạn docx | OPEN |
| [E3-Q8](#e3-q8) | Nguồn số suất trước khi có order | Dinh dưỡng viên | OPEN |
| [E3-Q9](#e3-q9) | Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ | Giám đốc | OPEN |
| [E3-Q10](#e3-q10) | Chặn chuyển bếp | Giám đốc | OPEN |
| [E3-Q11](#e3-q11) | Bếp trưởng có xem giá và cost | Giám đốc | OPEN |
| [E2-Q1](#e2-q1) | Giá món dùng để làm gì khi công ty đã đặt định mức | Dinh dưỡng viên, Giám đốc | OPEN |
| [DL-01](#dl-01) | Loại và con số của các quy tắc cost | Người soạn docx, kế toán | OPEN |
| [E3-Q12](#e3-q12) | Khi tính `BINH_QUAN` hoặc `DAT_NHAT`, món chính Healthy (thường rẻ hơn) có được tính vào không | Giám đốc | OPEN |
| [E3-Q13](#e3-q13) | Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không | Kế toán | OPEN |
| [E3-Q14](#e3-q14) | FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không? | Kế toán | OPEN |
| [E3-Q15](#e3-q15) | Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick | Dinh dưỡng viên | OPEN |
| [E3-Q16](#e3-q16) | Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá? | Giám đốc, kế toán | OPEN |
| [FLOW-COST-Q01](#flow-cost-q01) | Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào? | Kế toán | OPEN |
| [FLOW-COST-Q02](#flow-cost-q02) | Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào? | Tech lead và BA | OPEN |
| [FLOW-COST-Q03](#flow-cost-q03) | Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào? | BA, kế toán, Tech lead | OPEN |
| [FLOW-COST-Q04](#flow-cost-q04) | Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào? | Kế toán, UX/BA | OPEN |
| [FLOW-COST-Q05](#flow-cost-q05) | Ai được đọc danh sách/chi tiết khoản khoán? | Giám đốc, BA | OPEN |
| [FLOW-COST-Q06](#flow-cost-q06) | Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào? | Giám đốc, kế toán | OPEN |
| [FLOW-COST-Q07](#flow-cost-q07) | Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ? | Kế toán, dinh dưỡng viên | OPEN |
| [FLOW-COST-Q08](#flow-cost-q08) | Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao? | Giám đốc, dinh dưỡng viên | OPEN |
| [FLOW-COST-Q09](#flow-cost-q09) | Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không? | BA, chủ sản phẩm/AI lead | OPEN |
| [FLOW-COST-Q10](#flow-cost-q10) | Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào? | Giám đốc, kế toán | OPEN |
| [O-06](#o-06) | Ai duyệt và ai thay khi vắng? | Giám đốc | OPEN |
| [E2-Q5](#e2-q5) | Nguồn khoảng định lượng chuẩn và mức chất độn? | Dinh dưỡng viên, Giám đốc | OPEN |
| [QA-COST-Q01](#qa-cost-q01) | NCC tồn tại INACTIVE trả 404-01 hay 422-02? | BA, Tech lead | OPEN |

<a id="o-01"></a>

## O-01

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Người dùng xác nhận 11/11/2026: cost nguyên liệu gồm VAT phải trả; khách không lấy VAT là không yêu cầu hóa đơn. Chi tiết ACC-CONF-01 đến05 tại accounting/business-rules.md. VAT cụ thể/thành phần khoán/cơ sở doanh thu còn mở..
- Hiện tại theo nguồn: Cờ "tính vào cost" từng nguyên liệu + khoản khoán + `VAT_PCT`; Cost gồm VAT phải trả theo ACC-CONF-02; giá báo chưa VAT cần chuẩn hóa trước khi tính, xem bổ sung kế toán
- Đề xuất để review: Chốt riêng VAT bán ra, thành phần cost, khoản khoán và cách hiểu giá nhập; yêu cầu bảng kế toán làm nguồn.
- Đánh đổi/cần làm rõ: Không lấy VAT8% của mẫu làm mặc định; thiếu VAT vẫn chặn tính%.
- Sau quyết định phải cập nhật: SRS3.3, params SYS, seed dữ liệu, fixture kế toán.
- Test bị chặn có gate nêu đích danh: TC-COST-010-06, TC-COST-015-01.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q1"></a>

## E3-Q1

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Tham số, mặc định `DAT_NHAT`
- Đề xuất để review: Cân nhắc DAT_NHAT giai đoạn đầu; so với BINH_QUAN/MAC_DINH trên10 ngày thực tế trước khi chọn.
- Đánh đổi/cần làm rõ: DAT_NHAT thận trọng nhưng có thể cao hơn cơ cấu chọn thực tế.
- Sau quyết định phải cập nhật: BR-CALC-004, tham số, AC-COST-015-04.
- Test bị chặn có gate nêu đích danh: TC-COST-015-04.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q2"></a>

## E3-Q2

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Tham số, mặc định `KHONG`
- Đề xuất để review: Xác nhận định lượng sống là trước hay sau loại xương/vỏ; chỉ áp hao hụt một lần.
- Đánh đổi/cần làm rõ: Áp hai lần sẽ tăng lượng mua sai; tắt hao hụt khi định lượng đã bao gồm phần bỏ.
- Sau quyết định phải cập nhật: SRS3.3.1/3.3.4 và dữ liệu công thức.
- Test bị chặn có gate nêu đích danh: TC-COST-010-05.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q3"></a>

## E3-Q3

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Kiểm theo từng cơ sở, phải đạt ở mọi cơ sở
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q4"></a>

## E3-Q4

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Kế toán đánh dấu
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-003-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q5"></a>

## E3-Q5

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Ngưỡng giá cũ là tham số
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q6"></a>

## E3-Q6

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không có bước duyệt; chỉ hỏi xác nhận khi lệch bất thường
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q7"></a>

## E3-Q7

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Dùng nhóm cost gắn tay ở E2
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-014-01, TC-COST-014-02, TC-COST-014-03, TC-COST-020-01.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q8"></a>

## E3-Q8

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Nhập tay theo từng món chính
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q9"></a>

## E3-Q9

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Chặn tuyệt đối khi ở chế độ `CHAN`; có chế độ `CANH_BAO`
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q10"></a>

## E3-Q10

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Chưa hiện thực
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q11"></a>

## E3-Q11

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không; chỉ xem dự toán dạng số lượng
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-021-05, TC-COST-024-02, TC-COST-024-03, TC-COST-025-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e2-q1"></a>

## E2-Q1

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Mẫu số của cost % là ngưỡng giá loại suất
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-015-01.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="dl-01"></a>

## DL-01

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Loại ghi "chờ DL-01"
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-007-03, TC-COST-020-01.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q12"></a>

## E3-Q12

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Có, tính mọi món chính của ngày
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-015-04.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q13"></a>

## E3-Q13

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: 7 ngày; không tính lại bản chụp, chỉ ảnh hưởng lần tính sau
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-002-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q14"></a>

## E3-Q14

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Chưa cho phép thay đổi hồi tố cờ trên giá đã hiệu lực; snapshot cũ giữ bất biến. Cần quyết định trước khi triển khai thao tác này
- Đề xuất để review: Giữ giá đã hiệu lực bất biến, chỉ đổi tham chiếu tương lai; nếu cần hồi tố phải thiết kế nghiệp vụ riêng.
- Đánh đổi/cần làm rõ: Dễ kiểm toán nhưng kế toán không sửa cờ lịch sử trực tiếp.
- Sau quyết định phải cập nhật: BR-PRC-004/005, API-COST-008, UC-COST-002.
- Test bị chặn có gate nêu đích danh: TC-COST-003-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q15"></a>

## E3-Q15

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Mô hình theo BR-EST-001; tổng lượt chọn phải chia hết cho main_pick. MVP main_pick=1 không bị ảnh hưởng; cần chốt trước khi mở main_pick>1
- Đề xuất để review: R3 giới hạn K=1; chỉ mở K>1 khi xác nhận tổng lượt chọn chia hết K và cách xử lý phần dư.
- Đánh đổi/cần làm rõ: Giảm rủi ro suy ra sai số suất; hạn chế loại suất nhiều món chính.
- Sau quyết định phải cập nhật: BR-EST-001, API EstimateInput, TC-COST-022-04.
- Test bị chặn có gate nêu đích danh: TC-COST-022-04.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e3-q16"></a>

## E3-Q16

- Nguồn: [srs/spec.md](../srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Lưu cả cơ sở, ngày tính và thời điểm lập, chưa suy ra quyền dùng chéo cơ sở. Cần xác nhận bộ lọc hiệu lực trước triển khai
- Đề xuất để review: Cân nhắc cùng món/cỡ/cơ sở, ngày lập đến ngày phục vụ <=N ngày; chốt riêng công thức đổi có làm hết hiệu lực không.
- Đánh đổi/cần làm rõ: Không tái dùng bảng khác cơ sở nếu chưa có quy tắc; tăng số bảng cần duyệt.
- Sau quyết định phải cập nhật: BR-CALC-007, bộ lọc bảng, test89/90/91ngày.
- Test bị chặn có gate nêu đích danh: TC-COST-013-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q01"></a>

## FLOW-COST-Q01

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không tự chọn NCC; luồng còn chờ phương án để giữ đúng một tham chiếu
- Đề xuất để review: Yêu cầu chọn giá thay thế trong cùng giao dịch hủy, nếu còn báo giá khác cùng nhóm.
- Đánh đổi/cần làm rõ: Không tự chọn NCC; lỗi ở một bước rollback cả hai thay đổi.
- Sau quyết định phải cập nhật: API hủy/tham chiếu, unique constraint, UC-COST-002.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q02"></a>

## FLOW-COST-Q02

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: API v0.1.0 kế thừa TTL 24h từ SYS, đề xuất scope key/hash/đối soát; chờ Tech lead review, chưa triển khai
- Đề xuất để review: Review phương án API hiện có: key/hash theo actor/method/path, TTL24h, đối soát, commit nguyên tử.
- Đánh đổi/cần làm rõ: Cần kho bền vững và migration; retry không được vượt quyền hiện tại.
- Sau quyết định phải cập nhật: API mục2/7, schema request store, test concurrency.
- Test bị chặn có gate nêu đích danh: TC-COST-004-03, TC-COST-004-05, TC-COST-015-05, TC-COST-018-01, TC-COST-018-03, TC-COST-023-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q03"></a>

## FLOW-COST-Q03

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không dùng cost_alerts có menu_day_id bắt buộc để giả lưu cảnh báo nguyên liệu; cần đặc tả lưu trữ riêng hoặc mở rộng notifications
- Đề xuất để review: Tạo thiết kế cảnh báo nguyên liệu riêng, không dùng cost_alerts bắt buộc menu_day_id.
- Đánh đổi/cần làm rõ: Chốt khóa chống trùng theo nguyên liệu hay nguyên liệu/cơ sở trước thiết kế bảng.
- Sau quyết định phải cập nhật: SRS PRC009, schema, worker giá cũ, thông báo NCC ngừng.
- Test bị chặn có gate nêu đích danh: TC-COST-001-03, TC-COST-007-02.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q04"></a>

## FLOW-COST-Q04

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không chia 0; đề xuất hiện không áp dụng, chờ xác nhận
- Đề xuất để review: Hiện dấu — và ghi Không áp dụng khi mẫu số0; giữ delta tiền nếu tính được.
- Đánh đổi/cần làm rõ: Không trả Infinity/NaN, không biến delta% thành0 gây hiểu nhầm.
- Sau quyết định phải cập nhật: API Decimal nullable, bảng phân rã/so sánh, AC.
- Test bị chặn có gate nêu đích danh: TC-COST-010-08, TC-COST-011-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q05"></a>

## FLOW-COST-Q05

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không suy ra mọi người xem cost được đọc danh mục quản trị khoản khoán
- Đề xuất để review: Xác nhận ma trận đọc danh mục quản trị riêng với quyền xem khoản trong phân rã cost.
- Đánh đổi/cần làm rõ: Cần phân biệt số liệu người xem cost được biết với quyền xem đề nghị quản trị.
- Sau quyết định phải cập nhật: SRS2.2, API khoản khoán, wireframe11.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q06"></a>

## FLOW-COST-Q06

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Luồng thành công giả định dữ liệu không đổi; nhánh thay đổi chưa đủ nghiệm thu
- Đề xuất để review: Cân nhắc kiểm lại tại duyệt cuối; nếu đủ điều kiện thì chụp bộ vừa kiểm cùng transaction.
- Đánh đổi/cần làm rõ: Khi mới vượt ở CHAN cần trả lại hoặc giữ PENDING? phải chốt trạng thái; không tự chuyển.
- Sau quyết định phải cập nhật: MENU/SRS Cost, transaction approve, snapshot, TC-COST-018-02.
- Test bị chặn có gate nêu đích danh: TC-COST-018-02.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q07"></a>

## FLOW-COST-Q07

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không tự chốt; mỗi bản ngày nguyên tử, trạng thái cả batch còn mở
- Đề xuất để review: Cân nhắc all-or-nothing cho cả batch tuần; trả lỗi theo ngày, không ghi ngày hợp lệ khi có lỗi.
- Đánh đổi/cần làm rõ: Dễ đối soát/retry nhưng phải sửa mọi ngày lỗi trước khi có kết quả tuần.
- Sau quyết định phải cập nhật: API batch success/error, transaction, version/batch key, UC012.
- Test bị chặn có gate nêu đích danh: TC-COST-023-01, TC-COST-023-02, TC-COST-023-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q08"></a>

## FLOW-COST-Q08

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Giữ điều kiện đã có: chuyển đạt → vượt; không tự đặt ngưỡng tăng mới
- Đề xuất để review: Tách hai tình huống: vốn vượt khi duyệt và phục hồi rồi vượt lại; xác định có mở cảnh báo mới hay cập nhật lịch sử.
- Đánh đổi/cần làm rõ: Không dùng mức tăng tùy ý để phát thông báo; cần tránh lặp cảnh báo đang mở.
- Sau quyết định phải cập nhật: SRS ALR001/002, state/worker và test P1.
- Test bị chặn có gate nêu đích danh: TC-COST-026-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q09"></a>

## FLOW-COST-Q09

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Không trả DAT; nhánh còn chờ quy tắc tổng hợp
- Đề xuất để review: Cân nhắc KHONG_XAC_DINH ưu tiên khi bất kỳ ngày/cơ sở không tính được, kể cả thiếu VAT.
- Đánh đổi/cần làm rõ: Tránh kết luận toàn bộ đã đánh giá, nhưng che mất một vi phạm đã chắc chắn; PO phải chọn.
- Sau quyết định phải cập nhật: BR-CALC-011, budget contract, quota/log, TC-COST-021-04.
- Test bị chặn có gate nêu đích danh: TC-COST-021-04.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="flow-cost-q10"></a>

## FLOW-COST-Q10

- Nguồn: [ui/user-flow.md](../ui/user-flow.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Đánh dấu đề xuất; không cấp quyền hoặc nâng P2 thành bắt buộc
- Đề xuất để review: Giữ P2; chốt vai trò, phạm vi cơ sở, trạng thái thực đơn và cửa sổ ngày trước khi mở.
- Đánh đổi/cần làm rõ: Không tăng phạm vi R3 để hoàn tất một màn mẫu.
- Sau quyết định phải cập nhật: API simulation, role matrix, US-COST-028.
- Test bị chặn có gate nêu đích danh: TC-COST-028-01, TC-COST-028-02, TC-COST-028-03.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="o-06"></a>

## O-06

- Nguồn: [../nen-tang/srs/spec.md](../../nen-tang/srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Giữ phân tách người tạo/người sửa cuối và người duyệt
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="e2-q5"></a>

## E2-Q5

- Nguồn: [../thuc-don-dinh-luong/srs/spec.md](../../thuc-don-dinh-luong/srs/spec.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Test dùng ngưỡng fixture, chưa làm cấu hình thật
- Đề xuất để review: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.
- Đánh đổi/cần làm rõ: Chưa có bằng chứng để tự quyết thay nghiệp vụ.
- Sau quyết định phải cập nhật: SRS, use case, API và AC bị ảnh hưởng.
- Test bị chặn có gate nêu đích danh: TC-COST-020-04.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.

<a id="qa-cost-q01"></a>

## QA-COST-Q01

- Nguồn: [validation/backlog-report.md](../validation/backlog-report.md).
- Thông tin xác nhận bổ sung: Chưa có xác nhận mới trong đợt kế toán.
- Hiện tại theo nguồn: Cả hai mô tả trùng điều kiện, chưa đổi mã lỗi
- Đề xuất để review: Cân nhắc422-02 khi NCC tồn tại nhưng INACTIVE;404-01 chỉ tham chiếu không tồn tại hoặc nguyên liệu không dùng.
- Đánh đổi/cần làm rõ: Phải sửa câu chữ404-01 và đồng bộ các client; ngoài phạm vi vẫn dùng404 theo SYS.
- Sau quyết định phải cập nhật: SRS ma trận lỗi, API và TC-COST-002-06.
- Test bị chặn có gate nêu đích danh: TC-COST-002-06.
- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.
