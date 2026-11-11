# Khóa, ngoại lệ và vòng đời kế hoạch — phương án review

11/11/2026 · Draft. Phân rã FR-ORD-DEF-001, FR-ORD-LOCK-001, FR-ORD-CHG-001, FR-PLAN-MEAL-001; không bổ sung quyền hoặc API đã duyệt. [Mapping](../api/data-mapping.md) · [Câu hỏi](../review/questions.md).

## Nguồn đầu vào và kết quả

| Bước / actor đề xuất | Đầu vào / guard | Output, dữ liệu và lỗi | Tiêu chí kiểm / gate |
| :--- | :--- | :--- | :--- |
| Resolve hạn / service | point/date/shift, timezone, deadline source/version; cùng scope lịch | Instant UTC và provenance; thiếu cấu hình →503 POLICY_UNCONFIRMED, không lấy15:00 mặc định | Clock server; override và biên bằng hạn BLOCKED ORD-Q07/12/Q-16 |
| Khóa / scheduler | T đã gửi; menu PUBLISHED, default, quota, recipe/price snapshot; counter đối soát selection; token nguồn không stale | Revision+lines+audit+receipt+outbox nguyên tử; order LOCKED; plan có thể PENDING | Không trả plan v1 khi chưa tạo; retry không tạo revision đôi |
| Thiếu nguồn / scheduler | T=null, default thiếu, nguồn thu hồi hoặc counter lệch | Job NEEDS_ATTENTION kèm reason và source versions; order giữ trạng thái cũ; không coi đã khóa | ERR-ORD-422-03 cho thiếu nguồn; stale409-01; counter lệch ghi lỗi vận hành, không tự sửa counter rồi khóa; mã reason cụ thể chưa freeze |
| Sửa nguồn sau hạn / vận hành được cấp quyền | Quyết định xử lý có evidence, actor, lý do, version cũ/mới; quyền/nguồn hợp lệ | Thao tác nghiệp vụ mới có tham chiếu job cũ; không dùng lại eventKey cũ với input khác | BLOCKED ORD-Q07/12/O-06; không lấy nút mock làm bằng chứng được gia hạn |
| Retry kỹ thuật / worker | Cùng operation/source hash, đã commit hoặc rollback xác định | Commit rồi trả revision cũ; chưa commit thử lại với guard hiện tại; outbox retry riêng | Không mở lại order; receipt/transaction persistence vẫn cần Tech lead |
| Ngoại lệ sau khóa / người đề nghị và người duyệt | baseOrderRevisionId, baseVersion, delta và reason; approver khác creator/last editor | Reject không tạo revision; approve stale409-01; approved mới tạo revision/outbox | Ngưỡng/quyền/khi đã sản xuất BLOCKED ORD-Q08/Q-16/O-06 |

## Completeness không suy từ số order đã khóa

Tập nguồn kỳ vọng E được lập từ lịch phục vụ hiệu lực của bếp/ngày/ca, có source/version và thời điểm chụp. Khóa phần tử là (servicePointId,serviceDate,shift), kể cả chưa có order. I là tập nguồn đã có revision hợp lệ; M=E\I. X là phần bị loại có căn cứ (nếu policy hủy/zero được duyệt); không tự loại T=0, điểm thiếu order hoặc điểm có lỗi. Đối soát E=I∪M∪X với ba tập rời nhau; nguồn ngoài E phải được điều tra, không âm thầm cộng vào.

Nếu nguồn E chưa xác định: completeness=UNKNOWN, expectedCount không được suy bằng includedCount. Nếu M khác rỗng: INCOMPLETE; đây là nhãn logic review, chưa enum API được duyệt. Trường hợp E rỗng không tự suy bữa đã hủy hoặc được publish. Snapshot manifest ghi E/sourceVersion, I/orderRevisionId, M/reason, X/evidence; không chứa tên người ăn. Thay lịch/đổi bếp phải rà cả scope cũ và mới; chưa tự chuyển đóng góp giữa bếp theo một event đơn lẻ. ORD-Q03/07/13/14 còn chặn định nghĩa nguồn cuối.

## Tách build, publish, ack và start-production

| Sự kiện | Actor / guard đề xuất | Tác động đề xuất | Điều chưa chốt |
| :--- | :--- | :--- | :--- |
| Build preview | Worker có scope, revision nguồn đã commit | Snapshot kế hoạch có manifest và missing; bản cũ bất biến; không tự coi phát hành | Chuẩn hóa source rows và phép quy đổi ORD-Q10 |
| Publish | Vai trò phát hành chưa xác nhận; manifest/current revisions kiểm lại | Ghi publishedAt và revision được phát hành; nếu cho phép partial phải có quyết định/nhãn explicit | Chặn policy khi chưa xác định điều kiện đủ hoặc partial; ORD-Q14; không thêm endpoint |
| Acknowledge | Bếp có quyền scope, chỉ rõ planId+revisionNo | Bằng chứng nhận đúng phiên bản, actor/time; xem GET/in thành công không là ack | ORD-Q14 quyết vai trò/thu hồi/quy trình; chưa persistence/route |
| Start production | Actor/sự kiện vận hành chưa xác nhận, chỉ rõ revision và scope | Transition riêng được audit, không phát sinh do publish/ack | ORD-Q14/O-06; chưa API và chưa bật transition |

Bếp đang xem revision cũ phải thấy nhãn bản cũ và nguồn bản mới; UI không gắn “đã nhận bản mới” cho ack cũ. Quyết định buộc nhận lại khi revision đổi còn mở. Lỗi publish/ack không sửa snapshot order. Tiêu chí độc lập: không giả đủ nguồn, không cộng hai revision cùng order, không biến đọc/publish thành bắt đầu sản xuất. Ca policy vẫn BLOCKED, ca invariant chỉ NOT RUN cho tới có môi trường.
