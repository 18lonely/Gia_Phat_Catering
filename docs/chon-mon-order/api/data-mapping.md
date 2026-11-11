# Mapping consistency E6 — bổ sung review 11/11/2026

Draft; thiết kế logic chưa freeze/persistence. Bổ sung [API](api-spec.md), [delta](../srs/data-dictionary.md) và [quy tắc](../srs/operational-rules.md); không thêm endpoint. E6-EVID-001/002 giữ nguyên.

| UI / nghiệp vụ | API / token | Dữ liệu logic, scope, điều kiện thay đổi | Giới hạn |
| :--- | :--- | :--- | :--- |
| UI06 lựa chọn cá nhân | Selection.version → SelectionInput.version | meal_selections.version; một selection; tạo=0, cập nhật dùng version hiện tại | Không thay summary token; identity binding vẫn ORD-Q01 |
| UI08/11 tổng vừa đọc | Summary.version → SubmissionInput.summaryVersion | Token snapshot theo point/date/shift; selection, C/T, counts hoặc nguồn quyết định chốt thay đổi thì token phải đổi cùng giao dịch | Kho token/CAS chưa có trong DBML; không dùng orders.version thay thế; RV04 chưa đóng |
| UI08 order đang sửa | OrderReceipt.version → SubmissionInput.version | orders.version; 0 chỉ khi tạo order, tổng chưa gửi là null không phải 0 | Summary có thể đổi mà order version không đổi |
| UI10 đề nghị đổi | ChangeInput.baseVersion + baseOrderRevisionId | orders.version và order_revisions.id cùng order; kiểm lại khi duyệt | DecisionInput.version là version đề nghị; không phải order version |
| UI09/10 snapshot khóa | OrderRevision.revisionId/revisionNo/orderVersion | revisionNo tăng trong một order; orderVersion là version order chụp lúc tạo revision; bản cũ bất biến | Hai số không cần bằng nhau; pricing_snapshot cùng order/version |
| UI13 kế hoạch | planId + revisionNo; sources[].revisionId | production_plan_revisions theo kitchen/date/shift; mỗi order đúng một revision hiệu lực | plan revision không bằng order revision; GET không phải ack |
| UI06 nguồn đang chọn | menuVersion/quotaVersion; deadlineVersion trong AvailableMeals | Snapshot nguồn và deadline theo scope; ghi kiểm lại nguồn server, không tin client cache | SelectionInput chưa có deadlineVersion: server resolve lại; không tự thêm field vào request |
| UI09 độ đủ nguồn | Delta review: expected scope version + included/missing source keys | Tập kỳ vọng từ lịch hiệu lực; trước khi có order dùng point/date/shift, không dùng orderId rỗng làm khóa | Chưa có wire DTO completeness hoặc persistence được duyệt; xem lifecycle |

## Thứ tự ghi và retry đề xuất

1. Xác thực và authorize theo scope hiện tại; tra receipt bằng principal/operation/key. Receipt không được dùng để vượt quyền mới bị thu hồi.
2. Cùng key, cùng body đã commit: trả receipt/resource đã ghi theo quyền hiện tại, không chạy lại guard version như thao tác mới, không tăng version/counter/revision. Không trả lại secret QR/credential. Khác body: ERR-ORD-409-02. IN_PROGRESS: lỗi cùng mã, Retry-After; không đổi key.
3. Khi chưa commit: khóa/CAS scope, kiểm version, nguồn và deadline theo policy được duyệt; ghi dữ liệu, audit thành công, receipt, outbox nguyên tử. Lỗi trước commit không có kết quả thành công một phần. Log lỗi vận hành có thể tồn tại, không được mang nhãn audit thành công.
4. Mất response chỉ là UNKNOWN với client. Retry cùng key/body để đối soát; không tự gửi thao tác mới. Catalog chưa có endpoint GET receipt theo requestId; requestId phục vụ tra cứu vận hành có quyền, không hứa một route chưa thiết kế. Nếu receipt hết retention, phải đối soát resource/domain identity trước gửi mới; retention E1-Q02 chưa chốt.
5. Order đã commit nhưng worker plan lỗi: order vẫn LOCKED, outbox pending/retry; không hứa plan READY. Replay event cũ không thay nguồn mới hơn, không tạo revision kế hoạch chỉ do retry.

## Delta kiểu dữ liệu cần review

OrderReceipt.summaryVersion đề xuất là token **sau commit**; Summary.version đọc trước ghi là token kiểm điều kiện. Không tái dùng token đầu vào cho lần sửa kế tiếp. Submission lỗi stale không thay order/summary/counter. Remaining=null khi total=null; giá trị remaining âm trong mô hình đề xuất phải hiển thị cần xử lý, không clamp thành0 để che xung đột; quyết định nhận/chặn vượt T vẫn ORD-Q06.

PlanRevision.delta hiện thiếu role/unit trong khi dòng snapshot có role/unit; delta nên đối chiếu theo dish+recipe+portion+role+unit, không cộng khác đơn vị. Đây là yêu cầu review DTO/khóa delta, chưa tự đổi unique DB hoặc quy tắc quy đổi ORD-Q10/O-02. PlanSummary.sourceOrderCount chỉ là số nguồn đã gồm; không phải mẫu số đủ nguồn. publishedAt cần nullable cho bản chưa phát hành hoặc chỉ trả bản phát hành; lựa chọn wire contract này giữ ORD-Q14, chưa freeze.

## Ranh giới delta theo dòng

[Review delta món/recipe/portion](delta-contract-review.md) phân biệt payload hiện tại và phương án chưa chọn. deltaByDish không đủ nếu một món ánh xạ nhiều dòng; READY không đồng nghĩa publish/ack/start. Không đổi catalog hoặc thêm trường giả đã duyệt.
