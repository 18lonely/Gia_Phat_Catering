# Bàn giao E6: sổ gap và hiện diện DTO

11/11/2026 · BA draft; tiếp nối [adapter handoff](adapter-handoff.md), không thay snapshot cũ. [Báo cáo/file thay đổi](../validation/dto-report.md) · [Preview](../preview.html).

[Sổ gap hiện hành](contract-gap-register.md) gom14nhóm từ review trước, nêu căn cứ/gate, vai trò cần review, artifact bị ảnh hưởng và evidence đóng. Không gán người/ngày, không tạo14câu hỏi mới. [Ma trận DTO](../api/dto-presence-review.md) rà14request+20response, phân biệt required/optional/conditional/null/default. API được sửa quy ước hiện diện và ghi rõ qrId nullable như mô tả cũ, không đổi endpoint hay tự chọn branch chưa rõ.

## Tiến độ

34/34DTO có dòng rà hiện diện;14/14nhóm gap có vai trò/điều kiện đóng,0/14được phê duyệt đóng. Đây là độ phủ review tài liệu, không34DTO sẵn sàng build.40/78feature thiết kế nháp;17/19E6 có điều kiện;19/19RTM;0/8RV đóng.99mô tả ca overlap,0backend/UAT;57AC giữ29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED.26route/2port,65bảng,13màn không đổi; E6-EVID-001/002 và các gate Cost/O-02/O-03 giữ nguyên.

## Tiếp theo

Dùng sổ gap làm đầu mối duy nhất cập nhật trạng thái; không tạo thêm sổ song song hoặc lặp lại review đã có. Phần độc lập tiếp theo: rà actor/trigger/hậu điều kiện các UC còn dùng template thao tác ghi cho GET/service job; sửa có căn cứ theo catalog và nối về gap gốc. Nếu cập nhật DTO theo quyết định mới thì đồng bộ type/UC/UI/AC và ghi evidence, không đổi các nhánh đang mở. Chưa backend/migration/E7–E13; không hỏi lại scope/C→S/vượtT.
