# Nghiệp vụ kế toán giá mua, hóa đơn và chiết khấu

Phiên bản 0.2.0 · 11/11/2026 · Draft thiết kế theo trao đổi người dùng.

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | BA | Liên kết API/schema/wireframe/backlog; làm rõ đơn hiện có một loại suất; giữ10 câuCK. |
| 0.1.1 | 2026-11-11 | BA | Theo yêu cầu người dùng, đặt câu hỏi chiết khấu có mã và đánh dấu Chờ xác nhận; không tự chọn phương án |
| 0.1.0 | 2026-11-11 | BA | Ghi nhận giá mua gồm VAT vào cost; tách yêu cầu hóa đơn và chiết khấu riêng theo đơn |

## 1. Thông tin đã được người dùng xác nhận

Nguồn: trao đổi trực tiếp trong phiên ngày 11/11/2026; chưa có bảng số thực tế hoặc chứng từ đính kèm.

| Mã xác nhận | Nội dung | Hệ quả thiết kế |
| :--- | :--- | :--- |
| ACC-CONF-01 | Giá mua nguyên liệu có lúc ghi VAT, có lúc không | Phải nhận diện cách báo giá, không coi mọi giá nhập cùng một kiểu |
| ACC-CONF-02 | Cost nguyên liệu dùng cả tiền VAT phải trả NCC | Giá dùng tính cost là giá mua có VAT phải trả; giá báo chưa VAT phải quy đổi, giá đã gồm VAT không cộng lần hai |
| ACC-CONF-03 | Khách “không lấy VAT” là không yêu cầu hóa đơn | Lưu nhu cầu hóa đơn riêng; không suy ra thuế suất0 hoặc tự thay công thức doanh thu |
| ACC-CONF-04 | Chiết khấu dành cho khách mua suất ăn, theo % hoặc tiền cố định trên suất, ghi theo đơn | Một khoản chiết khấu có tham chiếu đơn, khách và cách tính |
| ACC-CONF-05 | Khách vẫn trả đủ giá suất40000; chiết khấu ghi nhận riêng | Không trừ khoản chiết khấu này khỏi số tiền phải trả trên đơn; không tự giảm đơn giá suất |

Đã xác nhận nguyên tắc nghiệp vụ trên, chưa đồng nghĩa đã duyệt schema, API, người duyệt hoặc cách thanh toán chiết khấu. Các ví dụ VAT8% dưới đây chỉ là số thử công thức, không phải thuế suất được chọn cho hoạt động thực tế.

## 2. Giá mua và giá tính cost

Kế toán chọn nguyên liệu, NCC, cơ sở, ngày hiệu lực và đơn vị mua trước khi nhập giá. Các quy tắc giá theo ngày/cơ sở, không sửa giá đã hiệu lực và chứng từ giữ theo [SRS](../srs/spec.md).

| Cách ghi giá | Đầu vào tối thiểu | Giá đưa vào cost | Khi chưa đủ dữ liệu |
| :--- | :--- | :--- | :--- |
| Đã gồm VAT | Giá tổng phải trả trên một đơn vị mua; nguồn báo giá | Giữ nguyên giá tổng | Có thể biết giá cost dù chưa tách được tiền thuế; không tự suy ra giá trước VAT |
| Chưa gồm VAT | Giá trước VAT và mức VAT áp dụng đã xác nhận hoặc số VAT trên đơn vị được xác nhận | Giá trước VAT + VAT phải trả | Chưa biết VAT phải trả thì chưa xác định được giá cost, không coi VAT=0 |
| NCC xác nhận không cộng thêm khoản VAT | Giá cuối cùng phải trả, nguồn xác nhận | Giá cuối cùng phải trả | Ghi nhận mô tả nguồn; không tự gán một phân loại thuế pháp lý |
| Chưa rõ cách ghi | Giá báo và chứng từ/ghi chú | Chưa dùng làm giá tham chiếu | Kế toán làm rõ số cuối phải trả trước khi nhập giá hiệu lực |

**Đề xuất dữ liệu:** `quotedUnitPrice`, `priceBasis` (INCLUSIVE / EXCLUSIVE / FINAL_AMOUNT_CONFIRMED / UNKNOWN), `vatRatePct` hoặc `vatUnitAmount`, `effectiveCostUnitPrice`, nguồn/chứng từ, người xác nhận, thời điểm. Tên trường chưa phải API production. Không cho client tự gửi một giá tính cost không khớp số được quy đổi ở server.

Ví dụ: báo giá100000đ/kg chưa VAT, VAT thử8% → giá cost108000đ/kg. Báo giá108000đ/kg đã gồm VAT → giá cost vẫn108000đ/kg. Với70g, cost dòng7560đ ở cả hai trường hợp. Giá cuối100000đ/kg được NCC xác nhận không cộng thêm khoản VAT → cost dòng7000đ; nhãn “không lấy hóa đơn” một mình không đủ chứng minh số cuối này.

**Cần chốt trước migration:** giá quy đổi có phần lẻ xử lý ra sao vì SRS đang lưu giá nhập nguyên đồng; giới hạn và làm tròn VAT; lấy VAT theo báo giá/chứng từ nào khi khác nhau; xử lý vận chuyển/phụ phí có phân bổ vào cost hay không. Không tự gộp các khoản này vào giá chuẩn.

## 3. Khách hàng và yêu cầu hóa đơn

Hồ sơ/thỏa thuận lưu `invoiceRequested` riêng với `salePriceBasis`, mức VAT, giá suất và ngày hiệu lực. Một đơn chụp điều kiện của đơn đó; sửa nhu cầu hóa đơn cho tương lai không làm thay số liệu lịch sử.

- `invoiceRequested=false` không có nghĩa `vatRatePct=0`.
- Giá suất40000 là số theo thỏa thuận cần biết đã gồm VAT hay chưa. Trường hợp đã gồm VAT mới có thể chia `40000/(1+VAT%)` theo công thức hiện tại.
- Nếu giá thỏa thuận chưa VAT, cách cộng VAT vào số khách phải trả cần cấu hình được xác nhận cho hợp đồng; không dùng cờ hóa đơn làm công tắc cộng/trừ.
- Thiếu cách ghi giá hoặc mức VAT cần thiết: đánh dấu chưa xác định doanh thu dùng tính cost; không trả kết quả đạt giả.

Tài liệu này thiết kế dữ liệu quản trị. Nó không quyết định nghĩa vụ hóa đơn hoặc cách hạch toán thuế.

## 4. Ghi nhận chiết khấu riêng theo đơn

Luồng nghiệp vụ: xác định đơn và khách → nhập điều kiện chiết khấu → tính khoản riêng → người có thẩm quyền xác nhận theo quy trình sẽ chốt → lưu liên kết với đơn. Đơn vẫn giữ số suất, đơn giá và số phải trả đầy đủ. Thanh toán/chi trả/bù trừ khoản riêng là bước khác, chưa được người dùng mô tả.

| Nội dung | Quy tắc thiết kế |
| :--- | :--- |
| Hai cách tính đã xác nhận | Theo % hoặc số tiền cố định mỗi suất |
| Phạm vi | Theo từng đơn; mô hình hiện tại một loại suất/điểm/ngày/ca; số suất đủ điều kiện chờ CK-Q02, không dùng dòng chọn món làm dòng doanh thu |
| Công thức tiền/suất | Số suất đủ điều kiện × mức tiền trên suất |
| Công thức % đề xuất | Giá trị tương ứng số suất đủ điều kiện của đơn × tỷ lệ%; cơ sở tiền trước/sau VAT còn cần xác nhận |
| Kết quả | Khoản chiết khấu riêng; không tự ghi giảm `order.total`, `unitPrice` hoặc `amountDue` |
| Không có chiết khấu | Khoản riêng bằng0 hoặc không phát sinh bản ghi theo thiết kế kỹ thuật sẽ chốt; không làm thay số phải trả |
| Không cộng dồn tự động | Hai cách tính cho cùng điều kiện không được tự cộng; trường hợp nhiều chương trình cần quyết định riêng |
| Sửa/hủy đơn | Không xóa dấu vết; đánh dấu khoản liên quan cần rà lại, không tự trả tiền hoặc tự nhân số chiết khấu mới |
| Trạng thái | Đề xuất DRAFT → CONFIRMED / CANCELLED; chưa xác định người có quyền xác nhận; không dùng trạng thái PAID khi chỉ ghi nhận |

Ví dụ dùng cơ sở % **giả định là giá40000 trên đơn**:100 suất ×40000 =4000000đ khách phải trả. Khoản riêng5% =200000đ; hoặc2000đ/suất ×100 =200000đ. Hai trường hợp đều giữ phải trả4000000đ. Con số3800000đ không phải số phải trả của đơn trong nghiệp vụ đã xác nhận. Trạng thái khoản200000đ chưa cho biết đã chi trả hay chưa.

## 5. Ba số cần hiển thị riêng

| Số liệu | Ý nghĩa | Không được suy diễn |
| :--- | :--- | :--- |
| Tiền phải trả của đơn | Số suất × giá và điều kiện VAT đã xác định, trước khoản chiết khấu riêng này | Không tự giảm theo khoản chiết khấu riêng |
| Chiết khấu đã ghi nhận | Cam kết/khoản riêng theo đơn, trạng thái rõ | Không bằng số đã trả/bù trừ nếu chưa có giao dịch xử lý |
| Chiết khấu đã xử lý thanh toán | Chỉ có khi phân hệ sau ghi chứng cứ xử lý | Chưa thuộc chức năng Cost R3 hiện có |

Cost% thực đơn hiện lấy định mức loại suất làm mẫu số chưa VAT. Thông tin người dùng về chiết khấu **chưa quyết định** có lập thêm chỉ số lợi nhuận/doanh thu sau chiết khấu hay không. Không lấy khoản riêng trừ vào mẫu số kiểm52% hoặc cộng vào cost nguyên liệu một cách ngầm định. Nếu cần chỉ số sau chiết khấu, đặt tên khác và chốt công thức riêng.

## 6. Điểm còn cần quyết định

### 6.1 Câu hỏi nghiệp vụ chiết khấu — CHỜ XÁC NHẬN

Theo yêu cầu người dùng, các câu hỏi được lưu tại đây để trả lời sau. **Chưa chọn phương án, chưa gán mặc định và chưa coi là quy tắc đã duyệt.** Các lựa chọn nêu trong câu hỏi chỉ giúp làm rõ nội dung cần trả lời.

Nguyên tắc đã xác nhận vẫn giữ: chiết khấu cho khách theo % hoặc tiền cố định/suất, ghi riêng theo đơn; khách vẫn phải trả đủ giá suất trên đơn. Hỏi về chi trả/bù trừ dưới đây không cho phép tự giảm tiền phải trả của đơn gốc.

| Mã câu hỏi | Câu hỏi cần trả lời | Ảnh hưởng tới thiết kế | Người cần xác nhận (vai trò đề xuất) | Trạng thái / trả lời |
| :--- | :--- | :--- | :--- | :--- |
| CK-Q01 | Chiết khấu % tính trên tiền suất **đã gồm VAT hay chưa VAT**? Cơ sở tính có bao gồm khoản phụ thu nào không? | Công thức và số tiền chiết khấu | Kế toán, người phụ trách thỏa thuận khách | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q02 | Khoản chiết khấu áp dụng cho mọi suất trong đơn hay chỉ một số loại suất/dòng? Số suất tính theo đặt hàng, giao thực tế hay số được khách xác nhận? | Dòng đủ điều kiện, số lượng và thời điểm tính | Kế toán, vận hành, người phụ trách khách | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q03 | Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào? | Kết quả số và ca kiểm tra biên | Kế toán | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q04 | Ai được lập/sửa khoản chiết khấu? Ai được duyệt; có phân cấp theo số tiền hoặc tỷ lệ không? Người lập có được tự duyệt không, ai thay khi người duyệt vắng? | Ma trận quyền, quy trình duyệt và nhật ký | Giám đốc, kế toán | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q05 | Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai? | Cách xử lý khoản riêng, đối tượng và liên kết thanh toán | Kế toán, người phụ trách thỏa thuận khách | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q06 | Khoản chiết khấu được xác nhận và xử lý vào lúc nào: khi chốt đơn, giao xong, khách thanh toán hay cuối kỳ? Có xử lý một phần không; cần chứng từ gì để ghi đã xử lý? | Trạng thái, ngày ghi nhận, số còn chưa xử lý và chứng từ | Kế toán | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q07 | Nếu đơn đổi số suất, giá hoặc loại suất khi chiết khấu chưa duyệt/đã duyệt nhưng chưa xử lý, có tính lại tự động không? Có phải duyệt lại, và giữ phiên bản cũ thế nào? | Điều chỉnh khoản riêng khi sửa đơn | Kế toán, vận hành, người duyệt | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q08 | Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không? | Hủy/điều chỉnh, lịch sử và quyền thao tác | Kế toán, người duyệt | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q09 | Nếu chiết khấu đã chi trả/bù trừ rồi đơn mới đổi hoặc hủy, xử lý phần chênh lệch bằng thu hồi, bù kỳ sau hay khoản điều chỉnh riêng? Ai duyệt và cần chứng từ nào? | Khoản điều chỉnh sau xử lý; không xóa dấu vết giao dịch cũ | Kế toán, Giám đốc | **CHỜ XÁC NHẬN** — chưa trả lời |
| CK-Q10 | Một đơn có được hưởng đồng thời chiết khấu % và tiền/suất hoặc nhiều chương trình không? Nếu có, cộng dồn hay ưu tiên chương trình nào; có mức trần không? | Chống tính trùng, thứ tự áp dụng và giới hạn | Người phụ trách thỏa thuận khách, kế toán, Giám đốc | **CHỜ XÁC NHẬN** — chưa trả lời |

Khi có câu trả lời, ghi cho từng mã: **nội dung quyết định, ví dụ đầu vào → kết quả, người xác nhận, ngày và nguồn xác nhận**. Sau đó mới cập nhật quy tắc, API, mô hình dữ liệu, luồng và tiêu chí nghiệm thu liên quan. Không đóng câu hỏi chỉ vì đã có phương án đề xuất trong tài liệu.

### 6.2 Các điểm khác còn mở

1. Giá suất khi khách không yêu cầu hóa đơn có cách ghi VAT thế nào theo thỏa thuận; không suy ra từ cờ hóa đơn.
2. Có cần chỉ số lợi nhuận sau chiết khấu; nếu có thì giữ riêng với cost nguyên liệu và ngưỡng thực đơn.
3. Tiêu chí đối soát thống nhất giữa epic và SRS; xem [CR](../cr/CR-COST-2026-001.md).

Phần quyết định chưa có câu trả lời không cản việc đặc tả giá mua gồm VAT và nguyên tắc giữ nguyên tiền phải trả của đơn; nhưng chưa đủ để tự động chi trả chiết khấu hay phát hành hợp đồng API cuối.

## 7. Thiết kế đã đồng bộ

[API v0.2.0](../api/accounting-contract.md) · [ERD/DBML v0.4.0](../../nen-tang/srs/erd.md) · [4 màn kế toán](../html-wireframe/accounting-workbench.html) · [6 story/18 ca thiết kế](../userstories/accounting-backlog.md). Tên trạng thái/quyền là thiết kế có gate, chưa duyệt nghiệp vụ. Chuẩn hóa giá phần lẻ chờ rounding; khoản riêng chỉ draft, không tự cấp quyền chi trả.
