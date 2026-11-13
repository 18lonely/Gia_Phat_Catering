# Delta món và định lượng: ranh giới hợp đồng review

11/11/2026 · Draft BA. Liên quan E6-RV-07/04/05, FR-ORD-CHG-001, FR-PLAN-MEAL-001, UC-ORD-012/019, API-ORD-005/021/022/025, UI-ORD-10/13; không thay26route hoặc schema65bảng. [Mapping](data-mapping.md) · [Delta data](../srs/data-dictionary.md).

## Điều kiện dùng ChangeInput hiện tại

`deltaByDish:[{dishId,delta}]` chỉ đủ khi mỗi dishId trong baseOrderRevisionId ánh xạ đúng một dòng MAIN có recipe/portion/role/unit xác định. Đây là điều kiện diễn giải của hợp đồng nháp, không cam kết mọi order đáp ứng điều kiện đó. Server resolve từ snapshot baseline, không từ recipe đang có hiệu lực ở hiện tại; nếu snapshot không đủ đơn vị/định lượng thì không được suy từ tên món.

| Đầu vào / tình huống synthetic | Xử lý có thể xác định độc lập | Gap còn lại |
| :--- | :--- | :--- |
| Một dòng dish A / recipe R1 / STD / MAIN / suất, qty60; delta+5 | Khi policy duyệt cho phép: dòng đó thành65; snapshot60 bất biến | Quyền/ngưỡng approve ORD-Q08/O-06 chưa chốt |
| Cùng A có R1/STD và R2/LARGE; delta+5 | Payload không chỉ được dòng đích; không chọn dòng đầu, chia đều hoặc áp+5 vào cả hai | Contract ghi mở rộng BLOCKED ORD-Q10; chưa tự thêm revisionLineId vào request |
| Delta A nhưng A không có trong baseline | Không chọn recipe hiện hành hoặc tự tạo dòng không provenance | Quy trình thêm món mới sau khóa và nguồn hợp lệ cần ORD-Q04/08/12 |
| Delta-61 trên dòng60 | Kết quả âm, không ghi revision/audit thành công/outbox | ERR-ORD-422-02 đã có; không giảm dòng khác để bù |
| Cùng dish/recipe/portion nhưng role/unit khác | Không cộng số “suất” với “g”; không lấy tổng mọi thành phần làm totalServings | Mapping unit, lượng thập phân món kèm và unique key cần ORD-Q10/O-02 |
| BaseOrderRevision đã cũ hoặc thuộc order khác | Không áp delta lên bản mới tự động; stale409-01; sai scope404 theo quyền | Không tự sửa baseVersion hoặc key rồi gửi lại |

Với trường hợp hợp đồng không biểu diễn được, giữ thao tác BLOCKED ở cổng capability/configuration; không tạo kết quả APPROVED giả. Nếu adapter được triển khai theo phương án này, 503 POLICY_UNCONFIRMED dùng khi chưa cấu hình hợp đồng; 422-04 chỉ dùng khi dữ liệu không khớp context đã xác định. Reason cụ thể cho ambiguous line chưa freeze; không tuyên bố đã có mã lỗi mới.

## Hai phương án cần Tech lead/BA review, chưa chọn

| Phương án | Request / ràng buộc đề xuất | Đánh đổi |
| :--- | :--- | :--- |
| Tham chiếu dòng bất biến | deltaLines[{baseRevisionLineId,delta}], kiểm dòng thuộc baseline/order/scope | Tránh client tự chọn recipe nhưng cần DTO trả lineId, xử lý món mới riêng |
| Khóa ngữ nghĩa đầy đủ | deltaLines[{dishId,recipeId,portionCode,role,unit,delta}] đối chiếu snapshot | Dễ đọc diff nhưng payload lớn, phải khóa đơn vị và chống key giả; không tự quy đổi |

Không ghép một phần hai phương án vào ChangeInput hiện tại. Lựa chọn phải cập nhật đồng bộ ChangeRequest, DecisionReceipt, order_revision_lines, plan delta, UI và AC trước freeze. Không suy mở nhiều MAIN hoặc cơ cấu mới chỉ từ khả năng biểu diễn của payload.

## Delta kế hoạch và nghĩa READY

Plan delta là so hai snapshot theo khóa (dish,recipe,portion,role,unit), không chỉ dishId. Đổi recipe/portion phải biểu diễn giảm dòng cũ và tăng dòng mới, không triệt tiêu thành0 chỉ vì tổng suất bằng nhau. Dòng mất khỏi bản mới có delta âm; dòng mới có delta dương. Bản cũ, source manifest và đơn vị phải còn đọc được.

PlanRevision.delta hiện chưa mang role/unit, OrderRevision.lines chưa có unit và id dòng; đây là gap hợp đồng, không chứng minh fields tồn tại trong DB. `DecisionReceipt.planStatus=READY` chỉ nên được diễn giải là kết quả tổng hợp đã có, không chứng minh completeness/publish/ack/start; phải gắn đúng revision nguồn. Định nghĩa READY chi tiết và DTO tham chiếu plan cần ORD-Q14/Tech lead; chưa thêm trường vào catalog. Khi chưa có bằng chứng nguồn đã được phản ánh, trả PENDING theo thiết kế hiện tại.

## Traceability và ca liên quan

AC-E6-012-2/3 và TC-E6-012-2/3 kiểm quyền/stale; AC-E6-019-3, TC-E6-INV-08/11 kiểm thay nguồn và không gộp khác định lượng. Các điều kiện ambiguous/missing-line là tiêu chí review contract bổ sung, **chưa tính thành test case mới** và chưa có Actual/Evidence. [Bộ evidence](../test/evidence-protocol.md) quy định chứng cứ cần thu khi có môi trường.
