# Bàn giao E6 — review delta và evidence

11/11/2026 · BA draft. Tiếp nối [handoff độc lập](independent-handoff.md); không ghi đè snapshot cũ. [Báo cáo/file thay đổi](../validation/contract-report.md) · [Preview](../preview.html).

Đã rà alias ERD/từ điển và đồng bộ tên logic delta; giữ cột DB hiện hữu. [Review delta](../api/delta-contract-review.md) chỉ rõ dish-only không xác định được dòng khi có nhiều recipe/portion; so sánh2phương án chưa chọn, không thêm route/field vào catalog. Làm rõ READY không chứng minh publish/ack/start; gap unit/id dòng vẫn còn.

[Bộ evidence](../test/evidence-protocol.md) đưa mẫu run và tiêu chí chứng cứ adapter/receipt/manifest/delta; ghi rõ giới hạn UI06/09/10/13 hiện có. [Fixture delta synthetic](../test/fixtures/delta-synthetic.json) minh họa cùng tổng100 nhưng đổi recipe có-60/+60. Sửa mã finding E6-RV-xx trong12INV; không thay trạng thái test. Có checker tài liệu tái chạy được, không phải test backend.

Tiến độ không tăng số feature:40/78thiết kế nháp; E6 có17/19thiết kế có điều kiện,19/19dòng RTM;0/8RV xác nhận đóng.99mô tả ca có overlap, không thêm ca:57theoAC (29NOT RUN/28BLOCKED),10gốc,12hệ thống,8DR BLOCKED,12INV NOT RUN;0backend/UAT. Giữ26HTTP/2port,13màn,65bảng. E6-EVID-001/002 không đổi; không hỏi lại hoặc tự chọn ba policy.

## Chặn

Cần quyết định/thiết kế được review cho delta line identity, món mới sau khóa, unit/role và lượng món kèm; nguồn kỳ vọng/publish/ack/start; identity/credential; receipt/summary persistence. Gap được mô tả không đồng nghĩa được đóng hoặc schema sẵn sàng build. O-02/O-03, CK/DATA-COST và các ORD-Q giữ nguyên.

## Việc tiếp theo có thể làm độc lập

Rà response/error allowlist và provenance nutrition/menu qua adapter E6 với E1/E2/E4; phân biệt thiếu nguồn với ngoài scope và danh sách rỗng hợp lệ. Chuẩn bị bảng hợp đồng lỗi giữa các miền theo envelope hiện có, không tự chốt E1-Q01. Có thể rà request validation từng route theo catalog hiện tại. Nếu sửa mock cho async/version thì phải chạy UI và xem ảnh; phiên này chỉ ghi giới hạn, chưa sửa mock. Chưa backend/migration và chưa E7–E13.
