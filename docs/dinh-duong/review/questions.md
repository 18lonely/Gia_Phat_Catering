# Sổ câu hỏi — NUTR

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Không có người/ngày ký thay stakeholder. Đề xuất kỹ thuật không đóng điểm mở nghiệp vụ.

| Mã | Câu hỏi | Vai trò cần trả lời | Tác động | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| NUTR-Q01 | Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu? | Dinh dưỡng viên, Giám đốc | FEAT-019; nguồn D-17/DL-07; quyền ghi đề xuất, chưa có workflow duyệt riêng | CHỜ XÁC NHẬN |
| NUTR-Q02 | qty_std là gram sống còn xương/vỏ hay gram phần ăn được? Xác nhận edible_pct và quy đổi theo từng nguyên liệu để không trừ hai lần. | Dinh dưỡng viên, bếp trưởng | FR-NUTR-CALC-001; công thức khung kế thừa ERD, chưa nghiệm thu dữ liệu | CHỜ XÁC NHẬN |
| NUTR-Q03 | Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi? | Dinh dưỡng viên | FR-NUTR-CALC-002; đề xuất tổ hợp tường minh, không sao chép cách chọn món đắt nhất Cost | CHỜ XÁC NHẬN |
| NUTR-Q04 | Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost. | Dinh dưỡng viên, QA | NFR-NUTR-001; chưa có ngưỡng nghiệm thu được duyệt | CHỜ XÁC NHẬN |
| DATA-NUTR-Q01 | Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp. | Dinh dưỡng viên | DL-03/05/07, nghiệm thu R4; chưa có dữ liệu thật trong gói | CHỜ XÁC NHẬN |

Khi trả lời: ghi lựa chọn, ví dụ/ca biên, người xác nhận, ngày, nguồn và phiên bản tài liệu; cập nhật SRS/API/ERD/UI/AC/test rồi mới đóng. Ca BLOCKED chuyển NOT RUN khi đủ đầu vào, không tự chuyển PASS. Các ca kỹ thuật dùng fixture giả định có thể chuẩn bị độc lập.
