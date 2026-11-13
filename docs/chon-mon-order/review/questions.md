---
id: DOC-CHON-MON-ORDER-REVIEW-QUESTIONS
title: Câu hỏi E6
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Câu hỏi E6

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

| Mã | Câu hỏi | Vai trò | Tác động | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| ORD-Q01 | Định danh duy nhất người ăn có tài khoản/QR bằng gì; xử lý nhiều thiết bị/QR chia sẻ và account trùng ra sao? | Gia Phát, BA | FEAT-030–032; không thể chống trùng người chỉ bằng cookie/IP | CHỜ XÁC NHẬN |
| ORD-Q02 | Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa? | Người đặt tổng, BA | FEAT-033; không xóa lịch sử | CHỜ XÁC NHẬN |
| ORD-Q03 | Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order? | Vận hành | FEAT-034/048 | CHỜ XÁC NHẬN |
| ORD-Q04 | Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào? | Người phụ trách khách, DDV | FEAT-035/036 | CHỜ XÁC NHẬN |
| ORD-Q05 | Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào? | Người đặt tổng, BA | FEAT-037 | CHỜ XÁC NHẬN |
| ORD-Q06 | T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món? | Người đặt tổng, DDV | FEAT-038/039/042; giữ đề xuất không xóa tự động | CHỜ XÁC NHẬN |
| ORD-Q07 | Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao? | Vận hành, Giám đốc | FEAT-039/040; không mặc định tổng bằng số người đăng ký | CHỜ XÁC NHẬN |
| ORD-Q08 | Ngưỡng đổi sau chốt, vai trò duyệt, delta âm và khi bếp đã sản xuất xử lý thế nào? | Giám đốc, bếp trưởng | Q-16/O-06; FEAT-041 | CHỜ XÁC NHẬN |
| ORD-Q09 | Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi? | Người đặt tổng | FEAT-044 | CHỜ XÁC NHẬN |
| ORD-Q10 | R6 luôn1MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao? | DDV, bếp trưởng | D-04/D-20, O-02; schema selection một dishId cần review | CHỜ XÁC NHẬN |

Ghi quyết định,ví dụ,người/ngày/nguồn rồi cập nhật FR/API/schema/AC. Chưa có trả lời thay stakeholder. O-03 vẫn chặn thiết kế thu thập/gợi ý sức khỏe; Q-14 vẫn chờ kênh nhắc.

## Câu hỏi phát hiện khi hoàn thiện E6: tất cả CHỜ XÁC NHẬN

| Mã | Câu hỏi | Vai trò cần xác nhận | Tác động | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| ORD-Q11 | Người đặt tổng có thể quản lý nhiều khách/điểm không; role customer scope và audit QR guest/service lưu thế nào khi user_roles/sessions/audit_logs hiện yêu cầu user? | Gia Phát, Tech lead | FEAT-030–033; schema danh tính, TTL/rate limit và phân quyền | CHỜ XÁC NHẬN |
| ORD-Q12 | MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn? | DDV, vận hành | FEAT-036/039/040/048; không tự sửa lịch sử hay phát hành plan mới | CHỜ XÁC NHẬN |
| ORD-Q13 | Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày? | Người đặt tổng, BA | Unique eater/date/shift và UI hủy/zero order chưa có write contract | CHỜ XÁC NHẬN |
| ORD-Q14 | Bếp phải xác nhận nhận phiên bản kế hoạch mới không; ai phát hành/cho IN_PRODUCTION và xử lý bản in cũ? | Bếp trưởng, vận hành | FEAT-048/041; chưa tự tạo endpoint acknowledge/production-start | CHỜ XÁC NHẬN |
| ORD-Q15 | Nếu mở O-03: consent/version, rút đồng ý, thời hạn xóa/lưu log, phạm vi bệnh lý và tiêu chí gợi ý cụ thể? | Chủ sản phẩm, phụ trách dữ liệu | FEAT-046/047; chưa schema/API sức khỏe mới | CHỜ XÁC NHẬN |

ORD-Q01–10 giữ nguyên; không câu nào được đóng trong phiên này. Các câu mới không thay Q-14/Q-16/O-02/O-03/O-06 hoặc E1-Q01/02/04. Phiếu quyết định cần: mã, phương án được chọn, ví dụ, người xác nhận, ngày và nguồn bằng chứng; sau đó sửa đồng bộ FR/UC/API/data/UI/AC/test.


## Review quyết định ngày 11/11/2026

Nguồn E6-EVID-001: người dùng trả lời trực tiếp **“Có danh sách và người quản lý xác nhận”**. Đã xác nhận đầu vào danh sách và khả năng quản lý xác nhận; chưa chốt credential, mã duy nhất, account/guest binding. ORD-Q01 tiếp tục **CHỜ XÁC NHẬN phần cơ chế**, không đánh dấu đóng toàn bộ.

[Bảng DR-01–04](decision-review.md) · [8 phát hiện](decision-findings.md) · [8 ca review](../test/decision-review-cases.md).

Bổ sung nội dung cần trả lời trong mã gốc, không tạo số câu hỏi trùng:

- ORD-Q06: người được nhập hộ rồi tự chọn có chuyển C→S không; C bắt buộc theo danh tính hay cho gộp; khi S+C vượt T đã gửi thì chặn lựa chọn mới hay buộc chốt lại tổng?
- ORD-Q07/12: quyền xử lý nguồn mới sau hạn khác retry kỹ thuật ra sao?
- ORD-Q14: định nghĩa plan đủ nguồn, xác nhận bếp nhận version và sự kiện bắt đầu sản xuất; publish không tự chứng minh IN_PRODUCTION.

Các phương án khuyến nghị trong DR đều CHỜ XÁC NHẬN. ORD-Q02–15 và Q-16/O-06 không được đóng bởi việc review tài liệu.


## Phản hồi người dùng E6-EVID-002 ngày 11/11/2026

Nguồn: trả lời trực tiếp ba câu hỏi review trong chat. Người dùng chọn **“Chưa chốt, giữ câu hỏi mở”** cho cả ba nội dung:

| Nội dung | Mã liên quan | Trạng thái sau phản hồi |
| :--- | :--- | :--- |
| Người đặt tổng thuộc một công ty hay được quản lý nhiều công ty | DR-01 / ORD-Q11 | CHỜ XÁC NHẬN; chưa chọn phạm vi |
| Người được chọn hộ quay lại tự chọn trước hạn có chuyển C→S, giữ T hay không | DR-02 / ORD-Q06 | CHỜ XÁC NHẬN; chưa duyệt cơ chế chuyển nguồn |
| Khi S+C bằng T đã gửi, chặn lựa chọn mới hay nhận rồi yêu cầu chốt lại T | DR-02 / ORD-Q06 | CHỜ XÁC NHẬN; chưa chọn chính sách vượt tổng |

Đây là xác nhận **tiếp tục để mở**, không phải phê duyệt phương án khuyến nghị hoặc bác bỏ vĩnh viễn phương án khác. Không áp mặc định một công ty, tự chuyển C→S hoặc tự chặn/nhận vượt T trong schema/API. Các ca phụ thuộc giữ BLOCKED. E6-EVID-001 về có danh sách và người quản lý xác nhận vẫn có hiệu lực, nhưng không đóng cơ chế identity. Không hỏi lại ba nội dung này khi chưa có yêu cầu chốt hoặc thông tin mới.
