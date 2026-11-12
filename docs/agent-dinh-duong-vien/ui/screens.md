# Màn hình E9

Draft · 12/11/2026 · Chỉ tài liệu; dữ liệu minh họa synthetic; chưa duyệt/chưa chạy sản phẩm.

| UI | Tên | FR code trong AIN | Nội dung/trạng thái |
| :--- | :--- | :--- | :--- |
| UI-AIN-01 | Yêu cầu thực đơn | SESS/GEN | Loại suất, số suất, khẩu vị/kiêng theo danh mục; nhắc không nhập sức khỏe; consent/identity chưa chốt; input sai/mơ hồ/policyclosed |
| UI-AIN-02 | Xem và giải thích | CHK/EXPL | Món/định lượng/4 chỉ số có nguồn, nhãn ước tính; bảng kiểm; missing/stale/không đạt; giá chưa mở |
| UI-AIN-03 | Chỉnh và kiểm lại | EDIT | Ngày/vị trí/món, baseRevision; diff; kết quả E2 cho bản mới; conflict/vi phạm cứng không VALID |
| UI-AIN-04 | Gửi nháp và trạng thái | SEND/STAT | Xác nhận đề xuất, nguồn/contact/consent chờ duyệt; nơi nhận chưa chốt; receipt mock không thật |
| UI-AIN-05 | Quản trị hạn mức/ngân sách | CONF/LOG | Nhóm/đơn vị/trần ngày chưa chọn; confirmed/reserved/unknown; quyền/duyệt/version conflict; không con số mặc định |
| UI-AIN-06 | Hết lượt / tạm chặn | LIMT | Phân biệt hiển thị an toàn hết lượt/budget unknown; không số trần cho khách, không nút đổi identity |
| UI-AIN-07 | Không khả dụng / ranh giới an toàn | GATE/SAFE/MED | Gate 063 đóng, từ chối nội bộ, lời nhắc bệnh lý chỉ placeholder chờ xác nhận; không form health |

[Wireframe7 màn](../html-wireframe/agent-workbench.html), [user flow](user-flow.md). Mock tĩnh có điều hướng/scenario selector để review, không gọi AI/backend và không lưu trạng thái hoặc thông tin nhập. Mọi tên món/số minh họa ghi synthetic. Các nút hành động nghiệp vụ disabled; không mô phỏng lưu/gửi thành công. UI05 chỉ màn đề xuất, không tự trao quyền PER-08.
