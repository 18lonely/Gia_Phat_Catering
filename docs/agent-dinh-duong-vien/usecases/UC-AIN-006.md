---
id: DOC-E9-USECASES-UC-AIN-006-MD
title: "UC-AIN-006: Gửi đề xuất về Gia Phát"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-006: Gửi đề xuất về Gia Phát

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02). Bên quan tâm: Gia Phát cần bản đề xuất đúng nguồn để người thật review; khách cần bằng chứng tiếp nhận.
Truy vết: FR-AIN-SEND-001 / FEAT-062 / US-AIN-006.

Trigger: Khách hài lòng với nháp đã kiểm và xác nhận gửi phương án cho Gia Phát xem xét.

Tiền điều kiện (nghiệp vụ): Candidate thuộc chủ thể, có evidence kiểm còn hiệu lực; khách có thông tin liên hệ tối thiểu và consent theo nội dung được duyệt.
Tiền điều kiện (gate còn mở): E9-Q06, E9-Q10, E9-Q13 chưa chốt đầu nhận, consent và receipt/ghi bền vững. O-03 vẫn đóng đối với sức khỏe.

Luồng chính:
1. Khách rà candidateRef/revision tại UI-AIN-04, nguồn kênh và thông tin liên hệ được phép gửi.
2. Khách thể hiện consent và xác nhận lệnh gửi; ứng dụng nhận clientConfirmation, không để model tự gửi.
3. Hệ thống kiểm lại quyền sở hữu, revision/hash và evidence hiện hành, cùng policy nơi lưu/đầu nhận.
4. Hệ thống ghi proposal, nguồn, revision và receipt bền vững theo key/body của lệnh.
5. Hệ thống chỉ trả mã tiếp nhận sau khi xác định đã lưu; trạng thái là CHỜ XEM XÉT bởi người thật.
6. Ứng dụng chuyển qua port tối thiểu khi có đầu nhận được duyệt, theo dõi receipt bàn giao riêng; không gọi applyDraft.

Hậu điều kiện thành công: Có đề xuất và receipt tiếp nhận bền vững; việc áp dụng vẫn chờ người thật, chưa tạo menus/order/báo giá.
Bảo đảm tối thiểu: Không ACK giả, không coi receipt là duyệt hoặc đã vào CRM, không thu dữ liệu sức khỏe hoặc gửi candidate tùy ý ngoài quyền.

Extensions:
- 3a. Chưa chọn nơi lưu/đầu nhận: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q06; không báo tiếp nhận thành công.
- 3b. Revision/nguồn/evidence thay đổi: hệ thống trả ERR-AIN-409-01, yêu cầu kiểm lại; chưa gửi nháp đó.
- 4a. Đã lưu nhưng mất phản hồi hoặc nhận lại cùng key/body: hệ thống đối soát và trả cùng proposal/receipt theo quyền hiện tại; không tạo lead/đề xuất trùng.
- 4b. Cùng key khác body: hệ thống trả ERR-AIN-409-02; giữ yêu cầu gốc, không ghi đề xuất mới.
- 4c. Lỗi ghi chưa xác định kết quả: hệ thống báo ERR-AIN-500-01; khách giữ key để đối soát, chưa coi đã tiếp nhận.
- 6a. Chưa có receipt bàn giao: hệ thống giữ trạng thái chờ/lỗi có căn cứ; proposal đã lưu không bị xóa và không được coi đã duyệt.

## Giao tiếp và kiểm

API-AIN-006: POST /v1/nutrition-agent/proposals; UI-AIN-04. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
