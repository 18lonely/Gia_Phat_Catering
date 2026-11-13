# Test Checklist: Epic E2 · Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `42-test-checklist.md` · BA-Kit v1.0 |
| Phiên bản | 0.1.0 |
| Trạng thái | Draft: chờ QA và BA rà độ phủ trước khi viết test case chi tiết |
| Ngày | 2026-11-11 |
| Căn cứ | [SRS epic v0.2.0](../srs/spec.md) · [Backlog v0.1.0](../userstories/backlog.md) · [Tiêu chí nghiệm thu v0.1.0](../userstories/acceptance-criteria.md) · [User-flow v0.1.0](../ui/user-flow.md) · [SRS nền tảng](../../nen-tang/srs/spec.md) |

## 1. Thông tin tổng quan

Tài liệu liệt kê **những gì cần kiểm thử** cho đợt R2, ở mức đề mục, để BA và QA thống nhất độ phủ trước khi viết test case chi tiết (`/test-cases`). Nó không lặp lại 239 kịch bản nghiệm thu; nhóm chức năng dẫn về mã `AC-MENU-…`, các nhóm còn lại bổ sung những thứ tiêu chí nghiệm thu không phủ: giao diện, phân quyền, hiệu năng, dữ liệu biên, toàn vẹn dữ liệu, tích hợp.

Cách dùng: mỗi dòng có ô ☐. Khi rà, đánh ☑ nếu đồng ý kiểm, gạch nếu bỏ, và ghi thêm dòng còn thiếu.

**Chưa có đội QA và đội phát triển** ([O-04]): ai chạy, bằng công cụ gì, tự động hoá đến đâu chưa được quyết. Mục 9 và 10 là đề xuất.

### Tổng quan độ phủ

| Nhóm | Mã | Số đề mục | Ghi chú |
| :--- | :--- | :---: | :--- |
| Chức năng theo story | `CL-F` | 53 | Dẫn về 239 kịch bản nghiệm thu |
| Bộ kiểm quy tắc: từng quy tắc | `CL-R` | 35 | **Chờ DL-01**: chưa có con số để viết ca kiểm |
| Phân quyền và bảo mật | `CL-S` | 22 | |
| Giao diện và trạng thái màn hình | `CL-U` | 24 | |
| Dữ liệu biên | `CL-B` | 26 | |
| Toàn vẹn dữ liệu và đồng thời | `CL-D` | 16 | |
| Hiệu năng | `CL-P` | 9 | |
| Tích hợp với phân hệ khác | `CL-I` | 9 | |
| Nhập bảng tính: ma trận lỗi theo cột | `CL-X` | 14 | |

---

## 2. Chức năng theo story: `CL-F`

Mỗi dòng là một story; kiểm thử chức năng của story đó là chạy các kịch bản nghiệm thu đã liệt kê. Cột H / E / B là số kịch bản thuận lợi / lỗi / biên. Cột "Chờ" lấy từ thẻ `@blocked` của các kịch bản.

| Mã | Story | Tên | Lát | Ưu tiên | H | E | B | Kịch bản | Chờ | ☐ |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| `CL-F-01` | `US-MENU-01` | Tạo và sửa nguyên liệu | R2.1 | P0 | 2 | 3 | 2 | `AC-MENU-01-1` → `7` |  | ☐ |
| `CL-F-02` | `US-MENU-02` | Ngừng dùng nguyên liệu | R2.1 | P0 | 1 | 1 | 1 | `AC-MENU-02-1` → `3` |  | ☐ |
| `CL-F-03` | `US-MENU-03` | Tìm và lọc nguyên liệu | R2.1 | P0 | 1 | 1 | 2 | `AC-MENU-03-1` → `4` |  | ☐ |
| `CL-F-04` | `US-MENU-04` | Quản lý nhóm nguyên liệu | R2.1 | P0 | 1 | 1 | 1 | `AC-MENU-04-1` → `3` | H-3 | ☐ |
| `CL-F-05` | `US-MENU-05` | Khai mùa vụ | R2.1 | P1 | 1 | 1 | 1 | `AC-MENU-05-1` → `3` |  | ☐ |
| `CL-F-06` | `US-MENU-06` | Quản lý phương pháp chế biến | R2.1 | P0 | 1 | 1 | 1 | `AC-MENU-06-1` → `3` | H-1, H-8 | ☐ |
| `CL-F-07` | `US-MENU-07` | Tạo món nháp | R2.1 | P0 | 1 | 3 | 2 | `AC-MENU-07-1` → `6` |  | ☐ |
| `CL-F-08` | `US-MENU-08` | Khai cặp món kỵ nhau | R2.1 | P0 | 1 | 1 | 1 | `AC-MENU-08-1` → `3` | H-4 | ☐ |
| `CL-F-09` | `US-MENU-09` | Tìm và lọc món | R2.1 | P0 | 1 | 1 | 1 | `AC-MENU-09-1` → `3` |  | ☐ |
| `CL-F-10` | `US-MENU-10` | Gửi duyệt món | R2.1 | P0 | 1 | 1 | 2 | `AC-MENU-10-1` → `4` |  | ☐ |
| `CL-F-11` | `US-MENU-11` | Duyệt hoặc trả lại món | R2.1 | P0 | 2 | 3 | 1 | `AC-MENU-11-1` → `6` | O-06 | ☐ |
| `CL-F-12` | `US-MENU-12` | Tải mẫu và kiểm tệp nhập | R2.1 | P0 | 1 | 2 | 3 | `AC-MENU-12-1` → `6` |  | ☐ |
| `CL-F-13` | `US-MENU-13` | Nhập tệp đã kiểm sạch | R2.1 | P0 | 2 | 1 | 1 | `AC-MENU-13-1` → `4` | E2-Q10 | ☐ |
| `CL-F-14` | `US-MENU-14` | Lập công thức nháp | R2.2 | P0 | 1 | 4 | 2 | `AC-MENU-14-1` → `7` | E2-Q5, O-02 | ☐ |
| `CL-F-15` | `US-MENU-15` | Tạo nguyên liệu trong lúc soạn công thức | R2.2 | P0 | 1 | 1 | 1 | `AC-MENU-15-1` → `3` |  | ☐ |
| `CL-F-16` | `US-MENU-16` | Duyệt hoặc trả lại công thức | R2.2 | P0 | 2 | 2 | 1 | `AC-MENU-16-1` → `5` | O-06 | ☐ |
| `CL-F-17` | `US-MENU-17` | Tạo phiên bản công thức mới | R2.2 | P0 | 1 | 1 | 2 | `AC-MENU-17-1` → `4` |  | ☐ |
| `CL-F-18` | `US-MENU-18` | Lấy đúng công thức hiệu lực theo ngày | R2.2 | P0 | 1 | 1 | 1 | `AC-MENU-18-1` → `3` |  | ☐ |
| `CL-F-19` | `US-MENU-19` | So sánh hai phiên bản công thức | R2.2 | P1 | 1 | 1 | 1 | `AC-MENU-19-1` → `3` |  | ☐ |
| `CL-F-20` | `US-MENU-20` | Đặt giá bán | R2.2 | P0 | 1 | 3 | 1 | `AC-MENU-20-1` → `5` | E2-Q1 | ☐ |
| `CL-F-21` | `US-MENU-21` | Duyệt giá bán và lấy giá hiệu lực | R2.2 | P0 | 1 | 2 | 2 | `AC-MENU-21-1` → `5` | E2-Q7, O-06 | ☐ |
| `CL-F-22` | `US-MENU-22` | Lịch sử giá bán | R2.2 | P1 | 1 | 1 | 1 | `AC-MENU-22-1` → `3` |  | ☐ |
| `CL-F-23` | `US-MENU-23` | Tạo loại suất | R2.2 | P0 | 1 | 1 | 2 | `AC-MENU-23-1` → `4` |  | ☐ |
| `CL-F-24` | `US-MENU-24` | Khoá cơ cấu loại suất | R2.2 | P0 | 1 | 1 | 2 | `AC-MENU-24-1` → `4` |  | ☐ |
| `CL-F-25` | `US-MENU-25` | Đánh dấu loại suất công khai | R2.2 | P1 | 1 | 1 | 1 | `AC-MENU-25-1` → `3` |  | ☐ |
| `CL-F-26` | `US-MENU-26` | Đề nghị sửa thuộc tính món đang dùng | R2.2 | P0 | 2 | 2 | 2 | `AC-MENU-26-1` → `6` |  | ☐ |
| `CL-F-27` | `US-MENU-27` | Duyệt đề nghị thay đổi | R2.2 | P0 | 1 | 1 | 3 | `AC-MENU-27-1` → `5` | O-06 | ☐ |
| `CL-F-28` | `US-MENU-28` | Ngừng dùng món | R2.2 | P0 | 1 | 1 | 2 | `AC-MENU-28-1` → `4` |  | ☐ |
| `CL-F-29` | `US-MENU-29` | Ảnh món | R2.2 | P1 | 1 | 1 | 2 | `AC-MENU-29-1` → `4` |  | ☐ |
| `CL-F-30` | `US-MENU-30` | Nhập công thức và giá bán từ bảng tính | R2.2 | P0 | 2 | 2 | 1 | `AC-MENU-30-1` → `5` | O-02 | ☐ |
| `CL-F-31` | `US-MENU-31` | Tạo thực đơn tuần | R2.3 | P0 | 1 | 2 | 2 | `AC-MENU-31-1` → `5` | E2-Q3, E2-Q4 | ☐ |
| `CL-F-32` | `US-MENU-32` | Xếp món vào ô | R2.3 | P0 | 1 | 3 | 3 | `AC-MENU-32-1` → `7` |  | ☐ |
| `CL-F-33` | `US-MENU-33` | Chọn món mặc định | R2.3 | P0 | 1 | 1 | 2 | `AC-MENU-33-1` → `4` |  | ☐ |
| `CL-F-34` | `US-MENU-34` | Xem danh sách và chi tiết thực đơn | R2.3 | P0 | 2 | 1 | 1 | `AC-MENU-34-1` → `4` |  | ☐ |
| `CL-F-35` | `US-MENU-35` | Huỷ thực đơn nháp | R2.3 | P0 | 1 | 2 | 1 | `AC-MENU-35-1` → `4` |  | ☐ |
| `CL-F-36` | `US-MENU-36` | Kiểm quy tắc cấp ngày | R2.3 | P0 | 1 | 1 | 5 | `AC-MENU-36-1` → `7` |  | ☐ |
| `CL-F-37` | `US-MENU-37` | Kiểm quy tắc cấp tuần | R2.3 | P0 | 1 | 1 | 3 | `AC-MENU-37-1` → `5` | DL-01, E2-Q2, H-2 | ☐ |
| `CL-F-38` | `US-MENU-38` | Điểm quy tắc và trạng thái "đã kiểm" | R2.3 | P0 | 2 | 1 | 3 | `AC-MENU-38-1` → `6` | DL-01 | ☐ |
| `CL-F-39` | `US-MENU-39` | Kiểm ngưỡng giá suất | R2.3 | P0 | 1 | 1 | 2 | `AC-MENU-39-1` → `4` | E2-Q1 | ☐ |
| `CL-F-40` | `US-MENU-40` | Lý do chấp nhận cho cảnh báo mức nặng | R2.3 | P0 | 1 | 1 | 2 | `AC-MENU-40-1` → `4` |  | ☐ |
| `CL-F-41` | `US-MENU-41` | Kiểm thực đơn chưa lưu | R2.3 | P0 | 1 | 2 | 1 | `AC-MENU-41-1` → `4` |  | ☐ |
| `CL-F-42` | `US-MENU-42` | Xem danh mục quy tắc | R2.3 | P0 | 1 | 1 | 1 | `AC-MENU-42-1` → `3` | DL-01 | ☐ |
| `CL-F-43` | `US-MENU-43` | Đề nghị sửa quy tắc | R2.3 | P0 | 2 | 2 | 2 | `AC-MENU-43-1` → `6` | E2-Q11 | ☐ |
| `CL-F-44` | `US-MENU-44` | Gửi duyệt thực đơn | R2.4 | P0 | 1 | 3 | 3 | `AC-MENU-44-1` → `7` | E2-Q6 | ☐ |
| `CL-F-45` | `US-MENU-45` | Duyệt hoặc trả lại thực đơn | R2.4 | P0 | 2 | 2 | 2 | `AC-MENU-45-1` → `6` | O-06 | ☐ |
| `CL-F-46` | `US-MENU-46` | Trang chờ duyệt | R2.4 | P0 | 2 | 1 | 3 | `AC-MENU-46-1` → `6` | E2-Q7, O-06 | ☐ |
| `CL-F-47` | `US-MENU-47` | Thông báo duyệt | R2.4 | P0 | 2 | 1 | 1 | `AC-MENU-47-1` → `4` |  | ☐ |
| `CL-F-48` | `US-MENU-48` | Công bố thực đơn | R2.4 | P0 | 1 | 1 | 2 | `AC-MENU-48-1` → `4` | E2-Q9 | ☐ |
| `CL-F-49` | `US-MENU-49` | Thu hồi và sửa lại | R2.4 | P0 | 1 | 1 | 3 | `AC-MENU-49-1` → `5` | E2-Q8 | ☐ |
| `CL-F-50` | `US-MENU-50` | Hai người duyệt khi điểm thấp | R2.4 | P1 | 1 | 1 | 2 | `AC-MENU-50-1` → `4` | O-06 | ☐ |
| `CL-F-51` | `US-MENU-51` | Sao chép thực đơn | R2.4 | P1 | 1 | 1 | 2 | `AC-MENU-51-1` → `4` |  | ☐ |
| `CL-F-52` | `US-MENU-52` | Lịch sử món đã dùng | R2.4 | P1 | 1 | 1 | 2 | `AC-MENU-52-1` → `4` |  | ☐ |
| `CL-F-53` | `US-MENU-53` | Xuất PDF | R2.4 | P1 | 1 | 1 | 2 | `AC-MENU-53-1` → `4` |  | ☐ |
| | | **Cộng** | | | **65** | **78** | **96** | **239 kịch bản** | | |

---

## 3. Bộ kiểm quy tắc: từng quy tắc (`CL-R`)

Mỗi quy tắc đang bật cần **tối thiểu 4 ca**: (1) đạt, (2) vi phạm, (3) đúng tại giới hạn, (4) vượt giới hạn 1 đơn vị. Quy tắc cấp tuần thêm (5) vi phạm vắt qua ngày nghỉ và (6) biến thể tính theo món gốc, nếu áp dụng. Bảng dưới là khung; cột "Giới hạn" điền khi DL-01 duyệt con số.

| Mã | Quy tắc | Phạm vi | Ca 1–4 | Ca riêng cần thêm | Giới hạn | ☐ |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| `CL-R-01` | `BR-MENU-001` Số món chính | Ngày | ☐ | Loại suất có 2 và 4 món chính đưa ra | Theo loại suất | ☐ |
| `CL-R-02` | `BR-MENU-002` Đúng 1 món Healthy | Ngày | ☐ | 0 món Healthy; 2 món Healthy | Chờ DL-01 | ☐ |
| `CL-R-03` | `BR-MENU-003` Healthy dùng phương pháp ít dầu mỡ | Ngày | ☐ | Món Healthy có phương pháp vừa bị bỏ cờ (không xảy ra được nhờ `BR-CAT-020`: kiểm là không xảy ra) | Không áp dụng | ☐ |
| `CL-R-04` | `BR-MENU-004` Đủ rau và canh | Ngày | ☐ | Loại suất không có canh | Theo loại suất | ☐ |
| `CL-R-05` | `BR-MENU-005` Số món phụ | Ngày | ☐ | Loại suất 0 món phụ | Theo loại suất | ☐ |
| `CL-R-06` | `BR-MENU-010` Món chính không trùng nhóm | Ngày | ☐ | 3 món cùng nhóm → mấy kết quả | Không áp dụng | ☐ |
| `CL-R-07` | `BR-MENU-011` Món phụ trùng nhóm món chính | Ngày | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-08` | `BR-MENU-012` Nhóm nguyên liệu nhiều ngày liền | Tuần | ☐ | Ngày nghỉ ở giữa; có/không dữ liệu tuần trước; thịt lợn nếu có giới hạn riêng | Chờ DL-01, [H-2], [E2-Q2] | ☐ |
| `CL-R-09` | `BR-MENU-013` Món lặp trong tuần | Tuần | ☐ | Biến thể theo món gốc | Chờ DL-01 | ☐ |
| `CL-R-10` | `BR-MENU-015` Số nhóm nguyên liệu tối thiểu | Tuần | ☐ | Tuần chỉ có 2 ngày phục vụ | Chờ DL-01 | ☐ |
| `CL-R-11` | `BR-MENU-016` Rau lặp ngày gần | Tuần | ☐ | Ngày nghỉ ở giữa | Chờ DL-01 | ☐ |
| `CL-R-12` | `BR-MENU-017` Canh lặp ngày gần | Tuần | ☐ | Ngày nghỉ ở giữa | Chờ DL-01 | ☐ |
| `CL-R-13` | `BR-MENU-018` Rau trái mùa | Ngày | ☐ | Mùa vắt qua cuối năm; rau không khai mùa | Không áp dụng | ☐ |
| `CL-R-14` | `BR-MENU-019` Món phụ lặp trong tuần | Tuần | ☐ | Biến thể theo món gốc | Chờ DL-01 | ☐ |
| `CL-R-15` | `BR-MENU-020` Hai món chính cùng phương pháp | Ngày | ☐ | Món Healthy cùng phương pháp với món không Healthy (không tính) | Không áp dụng | ☐ |
| `CL-R-16` | `BR-MENU-021` Món phụ chiên | Ngày | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-17` | `BR-MENU-022` Tổng món chiên | Ngày | ☐ | Rau, canh có phương pháp chiên | Chờ DL-01 | ☐ |
| `CL-R-18` | `BR-MENU-023` Cùng phương pháp | Ngày | ☐ | Rau luộc + món luộc Healthy có tính chung không | Chờ DL-01 | ☐ |
| `CL-R-19` | `BR-MENU-030` Món vị chua | Ngày | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-20` | `BR-MENU-031` Món có sốt | Ngày | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-21` | `BR-MENU-032` Món khô | Ngày | ☐ | Rau khô không tính | Chờ DL-01 | ☐ |
| `CL-R-22` | `BR-MENU-033` Món thanh nhẹ | Ngày | ☐ | Món Healthy có tự là thanh nhẹ không | Chờ DL-01 | ☐ |
| `CL-R-23` | `BR-MENU-034` Cặp kỵ | Ngày | ☐ | Biến thể của món trong cặp; cặp khai ngược thứ tự | Không áp dụng | ☐ |
| `CL-R-24` | `BR-MENU-040` Món cầu kỳ trong ngày | Ngày | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-25` | `BR-MENU-041` Món cầu kỳ trong tuần | Tuần | ☐ | Không áp dụng | Chờ DL-01 | ☐ |
| `CL-R-26` | `BR-MENU-042` Món kém chịu vận chuyển | Ngày | ☐ | R2 chỉ cảnh báo | Không áp dụng | ☐ |
| `CL-R-27` | `BR-MENU-043` Phù hợp bếp lớn | Ngày | ☐ | Không áp dụng | Không áp dụng | ☐ |
| `CL-R-28` | `BR-MENU-044` Nguồn cung không ổn định | Ngày | ☐ | Công thức có 2 nguyên liệu chính, 1 không ổn định | Không áp dụng | ☐ |
| `CL-R-29` | `BR-MENU-050` Đa dạng nguồn đạm | Tuần | ☐ | Nhóm không có nguồn đạm | Chờ DL-01 | ☐ |
| `CL-R-30` | `BR-COST-012` Ngưỡng giá suất | Ngày | ☐ | Giá đổi giữa tuần; món thiếu giá | [E2-Q1] | ☐ |
| `CL-R-31` | `BR-COST-008` Định lượng trong khoảng chuẩn | Khi lưu công thức | ☐ | Không áp dụng | [E2-Q5] | ☐ |
| `CL-R-32` | `BR-COST-009` Chất độn không vượt mức | Khi lưu công thức | ☐ | Không áp dụng | [E2-Q5] | ☐ |
| `CL-R-33` | Điểm quy tắc | Thực đơn | ☐ | Nhiều quy tắc cùng vi phạm một ô; quy tắc ngày vi phạm 6 ngày; sàn 0 | Không áp dụng | ☐ |
| `CL-R-34` | Bật/tắt và đổi loại quy tắc | Danh mục | ☐ | Đổi cứng ↔ mềm; quy tắc tắt không sinh kết quả | Không áp dụng | ☐ |
| `CL-R-35` | Thực đơn mẫu thực tế | Thực đơn | ☐ | Chạy bộ kiểm trên 4 thực đơn tuần gần nhất của Gia Phát; ghi số vi phạm (rủi ro E2-R2) | Cần Gia Phát cung cấp thực đơn | ☐ |

`BR-MENU-014` là cách đếm (phủ ở `CL-R-09`, `14`, `23`); `BR-MENU-051` chưa có định nghĩa ([H-5]).

---

## 4. Phân quyền và bảo mật: `CL-S`

| Mã | Đề mục | Cách kiểm | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :---: |
| `CL-S-01` | Ma trận quyền: mỗi vai trò × mỗi quyền `menu.*` | Với 6 vai trò nội bộ, gọi 1 API đại diện cho từng quyền trong 12 quyền; so với bảng mục 2.2 của SRS (72 tổ hợp) | SRS 2.2 | ☐ |
| `CL-S-02` | Vai trò chỉ xem không thấy nút ghi | Mở 16 màn hình bằng tài khoản bếp trưởng | User-flow mục 2 | ☐ |
| `CL-S-03` | Ẩn nút không thay cho kiểm quyền | Gọi trực tiếp mọi API ghi bằng tài khoản chỉ xem | `ERR-AUTH-403-02` | ☐ |
| `CL-S-04` | Thực đơn chưa công bố không lộ cho vai trò chỉ xem | Danh sách, chi tiết, xuất PDF, tìm kiếm | `ERR-SYS-404-01` | ☐ |
| `CL-S-05` | Giá bán không lộ cho quản lý cơ sở và bếp trưởng | Chi tiết món, API giá, PDF, kết quả kiểm `BR-COST-012` | SRS 2.2 | ☐ |
| `CL-S-06` | Không tự duyệt: theo người tạo | 5 loại nội dung: món, công thức, giá, đề nghị thay đổi, thực đơn | `BR-SEC-008` | ☐ |
| `CL-S-07` | Không tự duyệt: theo người sửa cuối | Người A tạo, người B sửa, B duyệt | `BR-SEC-008` | ☐ |
| `CL-S-08` | Không tự duyệt qua duyệt hàng loạt | Tích chọn mục của chính mình trong lô | `ERR-SYS-403-01` | ☐ |
| `CL-S-09` | Một người không duyệt hai lần cùng vòng | Thực đơn cần 2 người duyệt | `BR-MNU-008` | ☐ |
| `CL-S-10` | Uỷ quyền duyệt | Còn hạn: duyệt được; hết hạn: bị từ chối; uỷ quyền không gồm quyền đó | `FR-AUTH-RBAC-003` | ☐ |
| `CL-S-11` | Người được uỷ quyền cũng không tự duyệt | Người được uỷ là người tạo | `BR-SEC-008` | ☐ |
| `CL-S-12` | Nhật ký thay đổi đầy đủ | Mỗi lệnh tạo, sửa, huỷ, duyệt, trả lại, công bố, thu hồi có 1 bản ghi đủ người, thời điểm, cũ → mới, lý do | `FR-SYS-AUD-001` | ☐ |
| `CL-S-13` | Nhật ký ghi cả hành động của agent | Lệnh kiểm thực đơn chưa lưu ghi tài khoản dịch vụ | `FR-SYS-AUD-001` | ☐ |
| `CL-S-14` | Lý do bắt buộc | Mọi thao tác thuộc `BR-AUD-001` trong epic: trả lại, thu hồi, huỷ thực đơn, tạo phiên bản, đề nghị thay đổi, ngừng dùng | `ERR-SYS-422-01` | ☐ |
| `CL-S-15` | Không có đường xoá cứng | Tìm API và thao tác giao diện xoá hẳn bản ghi | `FR-SYS-AUD-004` | ☐ |
| `CL-S-16` | Chèn mã vào ô văn bản | Tên, mô tả, lý do, ghi chú chứa thẻ HTML và ký tự đặc biệt: hiển thị đúng dạng văn bản | `NFR-SEC-004` | ☐ |
| `CL-S-17` | Chèn truy vấn qua bộ lọc và sắp xếp | Tham số tìm, lọc, phân trang | `NFR-SEC-004` | ☐ |
| `CL-S-18` | Tệp tải lên | Sai loại theo nội dung; đổi đuôi; vượt 10 MB; tên tệp có ký tự đường dẫn | `FR-SYS-FILE-001` | ☐ |
| `CL-S-19` | Tệp bảng tính độc hại | Công thức bảng tính trong ô; tệp nén lồng; tệp hỏng | `FR-MENU-IMP-002` | ☐ |
| `CL-S-20` | Truy cập bằng mã bản ghi của người khác | Đổi mã trên đường dẫn và trong thân yêu cầu | `FR-AUTH-RBAC-001` | ☐ |
| `CL-S-21` | Phiên hết hạn giữa chừng | Đang soạn thực đơn thì phiên hết hạn: không mất dữ liệu đã lưu, quay lại đúng màn hình sau đăng nhập | `ERR-AUTH-401-02` | ☐ |
| `CL-S-22` | Agent phía khách không đọc được giá nhập và cost | R2 chưa có bảng cost; kiểm tài khoản dịch vụ `svc-agent-dinh-duong-vien` không có quyền nào ngoài tra cứu món đã duyệt và kiểm quy tắc | `BR-SEC-010` | ☐ |

---

## 5. Giao diện và trạng thái màn hình: `CL-U`

| Mã | Đề mục | Phạm vi | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :---: |
| `CL-U-01` | Trạng thái bình thường | 16 màn hình | User-flow mục 5 | ☐ |
| `CL-U-02` | Trạng thái rỗng | 9 màn hình có trạng thái rỗng | User-flow mục 5 | ☐ |
| `CL-U-03` | Lọc không ra kết quả | Danh sách nguyên liệu, món, thực đơn | User-flow mục 5 | ☐ |
| `CL-U-04` | Đang tải | Khung xương đúng bố cục, không có vòng xoay toàn trang | User-flow mục 5 | ☐ |
| `CL-U-05` | Lỗi tải | Có nút "Thử lại" và mã yêu cầu | `ERR-SYS-500-01` | ☐ |
| `CL-U-06` | Mất kết nối | Dải thông báo; nút ghi tắt; dữ liệu đang nhập được giữ; tự thử lại | User-flow mục 5 | ☐ |
| `CL-U-07` | Không có quyền / không tìm thấy | Trang riêng cho 403 và 404 | `ERR-AUTH-403-02`, `ERR-SYS-404-01` | ☐ |
| `CL-U-08` | Hiển thị 32 mã lỗi | Mỗi mã `ERR-MENU` hiện đúng thông báo, đúng vị trí | SRS 3.5; user-flow 6.1 | ☐ |
| `CL-U-09` | Ô bị khoá có chú giải | Đơn vị nguyên liệu đang dùng; cơ cấu loại suất đã có thực đơn; món có đề nghị chờ duyệt; công thức không phải nháp | User-flow 6.1 | ☐ |
| `CL-U-10` | Chú giải 12 thuộc tính món | Mỗi thuộc tính có định nghĩa và ví dụ | `NFR-MENU-006` | ☐ |
| `CL-U-11` | Rời form có thay đổi chưa lưu | Hộp xác nhận ở form món, công thức, nguyên liệu, loại suất | User-flow F1-13 | ☐ |
| `CL-U-12` | Ngăn tạo nguyên liệu khi soạn công thức | Mở, lưu, huỷ đều giữ các dòng đã nhập | AC-MENU-15 | ☐ |
| `CL-U-13` | Lưới soạn thực đơn | Số cột theo ngày phục vụ đã chọn; số dòng theo loại suất | AC-MENU-31 | ☐ |
| `CL-U-14` | Tô sáng ô khi bấm vi phạm | Vi phạm cấp ngày và cấp tuần | User-flow F2 | ☐ |
| `CL-U-15` | Bảng kiểm khi đang kiểm | Hiện "đang kiểm", kết quả cũ mờ, nút Gửi duyệt tắt | User-flow F2-17 | ☐ |
| `CL-U-16` | Nhãn trạng thái thực đơn | 6 trạng thái và tiến độ duyệt 0/1, 1/2 | SRS epic-spec 2.2 | ☐ |
| `CL-U-17` | Nút theo trạng thái ở màn xem thực đơn | Công bố · Thu hồi · Xuất PDF · Sửa | User-flow mục 5 | ☐ |
| `CL-U-18` | Bảng so sánh phiên bản công thức | Đổi, thêm, bỏ, không đổi | AC-MENU-19 | ☐ |
| `CL-U-19` | Bảng cũ – mới của đề nghị thay đổi | Món và quy tắc | AC-MENU-26, 43 | ☐ |
| `CL-U-20` | Chiều rộng 360 px | 16 màn hình không cuộn ngang; bảng rộng cuộn trong khung | `NFR-USE-001` | ☐ |
| `CL-U-21` | Lưới thực đơn dưới 768 px | Xem từng ngày; bảng kiểm thành ngăn kéo | User-flow F2-19 | ☐ |
| `CL-U-22` | Thanh nút duyệt trên điện thoại | Luôn thấy nút Duyệt và Trả lại | Wireframe chờ duyệt | ☐ |
| `CL-U-23` | Bàn phím và trình đọc màn hình | Đi hết form món và lưới thực đơn bằng phím; ô có nhãn; tương phản ≥ 4,5:1 | `NFR-USE-002` | ☐ |
| `CL-U-24` | Trình duyệt | Chrome, Safari, Edge, Firefox bản mới nhất và bản trước đó; Chrome và Safari trên điện thoại | SRS nền tảng 2.4 | ☐ |

---

## 6. Dữ liệu biên: `CL-B`

Kiểm tại giá trị biên, ngay dưới và ngay trên biên.

| Mã | Trường | Biên | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :---: |
| `CL-B-01` | Tên nguyên liệu | Rỗng · 1 ký tự · 120 · 121 ký tự · toàn dấu cách · có dấu tiếng Việt và ký tự đặc biệt | ERD 4.1 | ☐ |
| `CL-B-02` | Tên món | Rỗng · 160 · 161 ký tự | ERD 4.2 | ☐ |
| `CL-B-03` | So trùng tên | Khác hoa thường · thừa dấu cách đầu, cuối, giữa · khác dấu ("Ca kho" và "Cá kho" là hai tên) | `BR-CAT-001` | ☐ |
| `CL-B-04` | Hệ số quy đổi | 0 · số âm · 0,0001 · số rất lớn · chữ | `BR-CAT-002` | ☐ |
| `CL-B-05` | Tỷ lệ hao hụt | 0 · 0,01 · 99,99 · 100 · âm · 3 chữ số thập phân | `BR-CAT-003` | ☐ |
| `CL-B-06` | Tháng mùa vụ | 0 · 1 · 12 · 13 · từ tháng lớn đến tháng nhỏ | AC-MENU-05 | ☐ |
| `CL-B-07` | Định lượng | 0 · 0,001 · số có 4 chữ số thập phân · tối thiểu = chuẩn = tối đa · số rất lớn | `BR-CAT-011` | ☐ |
| `CL-B-08` | Số dòng công thức | 0 · 1 · 30 dòng | `BR-CAT-010` | ☐ |
| `CL-B-09` | Ngày hiệu lực công thức | Quá khứ · hôm nay · ngày mai · năm sau · trùng ngày của phiên bản khác | `BR-CAT-014` | ☐ |
| `CL-B-10` | Giá bán | Âm · 0 · 50 · 100 · 22.050 · số rất lớn · số thập phân | `BR-CAT-015` | ☐ |
| `CL-B-11` | Ngày hiệu lực giá | Hôm qua · hôm nay · ngày mai · trùng ngày đã có | `BR-CAT-016` | ☐ |
| `CL-B-12` | Ngưỡng giá loại suất | 0 · 1 · số rất lớn | `BR-CAT-017` | ☐ |
| `CL-B-13` | Số món chính đưa ra / được chọn | 0 · 1 · chọn = đưa ra · chọn > đưa ra | `BR-CAT-017` | ☐ |
| `CL-B-14` | Số món phụ | 0 · 5 · 6 | `BR-CAT-017` | ☐ |
| `CL-B-15` | Loại suất không rau, không canh | Lưới không có dòng rau, canh; quy tắc `BR-MENU-004` không báo | `BR-MNU-002` | ☐ |
| `CL-B-16` | Ngày bắt đầu tuần | Chủ nhật · thứ Hai · thứ Ba · tuần vắt qua cuối tháng, cuối năm | `ERR-MENU-422-13` | ☐ |
| `CL-B-17` | Số ngày phục vụ | 0 · 1 · 6 · 7 ngày | [E2-Q3] | ☐ |
| `CL-B-18` | Tổng giá suất so với ngưỡng | Ngưỡng − 100 · đúng ngưỡng · ngưỡng + 100 | AC-MENU-39 | ☐ |
| `CL-B-19` | Điểm quy tắc | 100 · 80 · 79 · 0 · tổng phạt > 100 | AC-MENU-38, 50 | ☐ |
| `CL-B-20` | Lý do | 9 · 10 · 500 · 501 ký tự · toàn dấu cách | `BR-AUD-001` | ☐ |
| `CL-B-21` | Điểm phạt quy tắc | 0 · 1 · 3 · 4 cho quy tắc mềm; khác 0 cho quy tắc cứng | `BR-MNU-007` | ☐ |
| `CL-B-22` | Tham số quy tắc | 0 · âm · số thập phân cho tham số đếm | `BR-MNU-007` | ☐ |
| `CL-B-23` | Ngày công bố | Ngày phục vụ đầu là hôm qua · hôm nay · ngày mai | `BR-MNU-009` | ☐ |
| `CL-B-24` | Tệp ảnh | 0 byte · 10 MB · 10 MB + 1 byte | `FR-SYS-FILE-001` | ☐ |
| `CL-B-25` | Tệp nhập | 0 dòng · 1 · 2.000 · 2.001 dòng · chỉ có dòng tiêu đề | `FR-MENU-IMP-002` | ☐ |
| `CL-B-26` | Phân trang | Trang 0 · trang cuối · sau trang cuối · cỡ trang 100 · 101 | SRS nền tảng 3.3 | ☐ |

---

## 7. Toàn vẹn dữ liệu và đồng thời: `CL-D`

| Mã | Đề mục | Cách kiểm | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :---: |
| `CL-D-01` | Khoá phiên bản khi hai người sửa một bản ghi | Món, công thức nháp, loại suất, thực đơn | `ERR-SYS-409-02` | ☐ |
| `CL-D-02` | Hai người duyệt cùng một mục cùng lúc | Chỉ 1 quyết định được ghi; người kia nhận thông báo | AC-MENU-46-4 | ☐ |
| `CL-D-03` | Hai người duyệt thực đơn cần 2 người, bấm cùng lúc | Kết quả đúng 2 dòng quyết định, thực đơn `APPROVED` đúng 1 lần | `BR-MNU-008` | ☐ |
| `CL-D-04` | Gửi lặp lệnh tạo | Cùng khoá chống gửi lặp: không sinh bản ghi thứ hai | SRS nền tảng 3.3 | ☐ |
| `CL-D-05` | Tạo hai thực đơn cùng loại suất, cùng tuần, cùng lúc | Chỉ 1 thực đơn được tạo | `BR-MNU-001` | ☐ |
| `CL-D-06` | Hai đề nghị thay đổi cho một món, gửi cùng lúc | Chỉ 1 đề nghị `PENDING` | AC-MENU-26-5 | ☐ |
| `CL-D-07` | Nhập bảng tính: tất cả hoặc không gì cả | Gây lỗi ở dòng cuối khi đang ghi: không dòng nào được lưu | `FR-MENU-IMP-003` | ☐ |
| `CL-D-08` | Một công thức hiệu lực mỗi món mỗi ngày | Với mọi món `ACTIVE` và mọi ngày trong 60 ngày tới: đúng 1 kết quả | `BR-CAT-014` | ☐ |
| `CL-D-09` | Chuyển phiên bản công thức đúng ngày | Tác vụ định giờ chạy đúng ngày hiệu lực; chạy lại lần hai không đổi kết quả; chạy trễ 1 ngày vẫn đúng | AC-MENU-16-2 | ☐ |
| `CL-D-10` | Công thức gắn vào thực đơn là bản chụp | Duyệt phiên bản mới không đổi thực đơn đã gửi duyệt trở đi | AC-MENU-17-3, 45-6 | ☐ |
| `CL-D-11` | Kết quả kiểm đóng băng | Sau gửi duyệt: đổi thuộc tính món, đổi quy tắc, đổi giá không làm đổi kết quả đã lưu | [E2-Q11] | ☐ |
| `CL-D-12` | Đề nghị lỗi thời | Bản ghi gốc đổi sau khi đề nghị được gửi → `STALE` | AC-MENU-27-3 | ☐ |
| `CL-D-13` | Bộ kiểm xác định | Cùng đầu vào chạy 100 lần cho cùng kết quả | `NFR-MENU-005` | ☐ |
| `CL-D-14` | Múi giờ | "Hôm nay", "ngày mai", ngày hiệu lực tính theo giờ Việt Nam: kiểm lúc 23:59 và 00:01; kiểm lúc 06:59 và 07:01 (ranh giới ngày theo UTC) | SRS nền tảng 2.4 | ☐ |
| `CL-D-15` | Huỷ không phải xoá | Bản ghi huỷ còn trong cơ sở dữ liệu và nhật ký, không hiện ở danh sách mặc định, tên được dùng lại | `BR-CAT-001` | ☐ |
| `CL-D-16` | Tham chiếu chéo khi ngừng dùng | Nguyên liệu → công thức; món → thực đơn; nhóm → món; phương pháp → món Healthy | `BR-CAT-005`, `020` | ☐ |

---

## 8. Hiệu năng: `CL-P`

| Mã | Đề mục | Chỉ tiêu | Dữ liệu | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `CL-P-01` | Bộ kiểm trên thực đơn đã lưu | p95 ≤ 2 giây | Thực đơn 6 ngày × 7 món; 50 lần | `NFR-MENU-001` | ☐ |
| `CL-P-02` | Bộ kiểm trên thực đơn chưa lưu, đồng thời | p95 ≤ 2 giây, 0 lỗi | 20 lời gọi cùng lúc | `NFR-MENU-002` | ☐ |
| `CL-P-03` | Bộ kiểm với dữ liệu lịch sử | p95 ≤ 2 giây | Có thực đơn của 52 tuần trước | `NFR-CAP-001` | ☐ |
| `CL-P-04` | Kiểm tệp nhập | ≤ 30 giây; chạy nền nếu > 5 giây | 2.000 dòng | `NFR-MENU-003` | ☐ |
| `CL-P-05` | Danh sách món, nguyên liệu | p95 ≤ 300 ms | 2.000 món, 1.000 nguyên liệu | `NFR-MENU-004` | ☐ |
| `CL-P-06` | Hộp chọn món | p95 ≤ 300 ms, có lịch sử 4 tuần | 500 món chính | `FR-MENU-MNU-006` | ☐ |
| `CL-P-07` | Trang chờ duyệt | p95 ≤ 300 ms | 200 mục chờ | `NFR-PERF-001` | ☐ |
| `CL-P-08` | Duyệt hàng loạt | Hoàn tất ≤ 5 giây | 100 món một lần | [ĐỀ XUẤT] | ☐ |
| `CL-P-09` | Xuất PDF | ≤ 5 giây | Thực đơn 6 ngày | [ĐỀ XUẤT] | ☐ |

`CL-P-08` và `CL-P-09` chưa có chỉ tiêu trong SRS; con số là đề xuất.

---

## 9. Tích hợp với phân hệ khác: `CL-I`

| Mã | Đề mục | Cách kiểm | Tham chiếu | ☐ |
| :--- | :--- | :--- | :--- | :---: |
| `CL-I-01` | Thông báo chờ duyệt và kết quả duyệt | Đúng người nhận, đúng liên kết, gộp theo lần gửi | `BR-MNU-010` | ☐ |
| `CL-I-02` | Tham số `QUY_TAC_DIEM_TOI_THIEU` | Đổi tham số có hiệu lực ở lần gửi duyệt kế tiếp; không đổi thực đơn đang chờ | `FR-SYS-PRM-001` | ☐ |
| `CL-I-03` | Uỷ quyền duyệt của nền tảng | Như `CL-S-10` | `FR-AUTH-RBAC-003` | ☐ |
| `CL-I-04` | Dịch vụ tra cứu món và công thức đã duyệt | Chỉ trả bản ghi `ACTIVE`; không trả nháp, chờ duyệt, ngừng dùng | SRS 2.1 | ☐ |
| `CL-I-05` | Dịch vụ tra cứu thực đơn đã công bố | Chỉ trả `PUBLISHED`; thực đơn thu hồi biến mất ngay | SRS 2.1 | ☐ |
| `CL-I-06` | Dịch vụ kiểm quy tắc cho agent | Cùng kết quả với giao diện | AC-MENU-41-1 | ☐ |
| `CL-I-07` | Sự kiện "thực đơn bị thu hồi" | Phát đúng 1 lần, mang mã thực đơn và lý do | AC-MENU-49-5 | ☐ |
| `CL-I-08` | Chỗ móc ở bước gửi duyệt | Đăng ký một bộ kiểm giả trả "không đạt": gửi duyệt bị chặn; gỡ ra: gửi duyệt được | `FR-MENU-APV-006` | ☐ |
| `CL-I-09` | Tệp đính kèm | Ảnh món lưu qua dịch vụ tệp; liên kết có chữ ký hết hạn sau 15 phút | `FR-SYS-FILE-001` | ☐ |

---

## 10. Nhập bảng tính: ma trận lỗi theo cột (`CL-X`)

Mỗi loại tệp cần một tệp mẫu sạch và một tệp chứa đủ các lỗi dưới đây, mỗi lỗi một dòng.

| Mã | Loại tệp | Lỗi cần có trong tệp kiểm thử | ☐ |
| :--- | :--- | :--- | :---: |
| `CL-X-01` | Mọi loại | Thiếu cột · thừa cột · đổi thứ tự cột · đổi tên cột | ☐ |
| `CL-X-02` | Mọi loại | Dòng trống giữa tệp · ô có dấu cách thừa · ô số ở dạng văn bản · dấu thập phân phẩy và chấm | ☐ |
| `CL-X-03` | Mọi loại | Giá trị liệt kê không hợp lệ (vai trò, loại bảo quản, kết cấu) | ☐ |
| `CL-X-04` | Nguyên liệu | Tên trùng trong tệp · trùng trong hệ thống · nhóm không tồn tại | ☐ |
| `CL-X-05` | Nguyên liệu | Hệ số quy đổi sai · thiếu hao hụt khi có xương/vỏ | ☐ |
| `CL-X-06` | Món | Tên trùng · nhóm hoặc phương pháp không tồn tại · Healthy sai phương pháp · món gốc không tồn tại, khác vai trò | ☐ |
| `CL-X-07` | Món | Món gốc nằm ở dòng sau trong cùng tệp | ☐ |
| `CL-X-08` | Công thức | Món không tồn tại · nguyên liệu không tồn tại · nguyên liệu đã ngừng dùng | ☐ |
| `CL-X-09` | Công thức | Món không có dòng nguyên liệu chính · lặp nguyên liệu trong một món · khoảng định lượng sai · nhóm không khớp | ☐ |
| `CL-X-10` | Công thức | Các dòng của một món không nằm liền nhau | ☐ |
| `CL-X-11` | Giá bán | Món không tồn tại · giá sai bội số · ngày hiệu lực không sau hôm nay · trùng ngày hiệu lực | ☐ |
| `CL-X-12` | Mọi loại | Trạng thái sau nhập: nguyên liệu `ACTIVE`; món, công thức `DRAFT`; giá `PENDING` | ☐ |
| `CL-X-13` | Mọi loại | Nhập hai lần cùng một tệp: lần hai báo trùng toàn bộ | ☐ |
| `CL-X-14` | Mọi loại | Tệp `.xls` cũ · `.csv` · `.xlsx` có nhiều trang tính · có mật khẩu | ☐ |

Cách xử lý của `CL-X-01`, `02`, `07`, `10`, `14` đã được quy định ở `BR-CAT-023` của SRS v0.3.0.

---

## 11. Dữ liệu và môi trường kiểm thử [ĐỀ XUẤT]

| Hạng mục | Nội dung |
| :--- | :--- |
| Bộ dữ liệu nền | 13 nhóm nguyên liệu · 11 phương pháp chế biến · 60 nguyên liệu · 40 món (16 chính, 11 phụ, 6 rau, 7 canh) có công thức và giá hiệu lực · 2 loại suất · thực đơn đã công bố của 4 tuần trước. Dựng được từ dữ liệu mẫu trong ba file wireframe |
| Tài khoản | 2 dinh dưỡng viên · 2 người duyệt · 1 quản lý cơ sở · 1 bếp trưởng · 2 kế toán · 1 tài khoản vừa tạo vừa duyệt · 2 tài khoản dịch vụ agent |
| Ngày hệ thống | Cần chỉnh được "hôm nay" của môi trường thử để kiểm ngày hiệu lực, chuyển phiên bản công thức, công bố |
| Bộ dữ liệu lớn | 2.000 món, 1.000 nguyên liệu, thực đơn 52 tuần: cho nhóm hiệu năng |
| Tệp nhập | 4 tệp sạch + 4 tệp lỗi theo mục 10 + 1 tệp 2.000 dòng + 1 tệp 2.001 dòng |
| Thực đơn thật | 4 thực đơn tuần gần nhất của Gia Phát, cho `CL-R-35`: Gia Phát cung cấp |

## 12. Điều kiện bắt đầu và kết thúc kiểm thử [ĐỀ XUẤT]

| Lát | Bắt đầu khi | Kết thúc khi |
| :--- | :--- | :--- |
| R2.1 | Nền tảng R1 đã nghiệm thu; bộ dữ liệu nền nạp xong | 100% kịch bản của story `01` – `13` đạt; `CL-S-01` → `05` đạt; không còn lỗi mức Critical, High |
| R2.2 | R2.1 kết thúc; [O-02] có câu trả lời | 100% kịch bản của story `14` – `30` đạt; `CL-D-08` → `10` đạt |
| R2.3 | R2.2 kết thúc; DL-01 xong và bảng `CL-R` đã điền giới hạn | 100% kịch bản của story `31` – `43` đạt; mỗi quy tắc đang bật đạt đủ các ca ở `CL-R`; `CL-P-01` → `03` đạt; `CL-R-35` đã chạy và kết quả được dinh dưỡng viên xem |
| R2.4 | R2.3 kết thúc; [O-06] có câu trả lời | 100% kịch bản của story `44` – `53` đạt; toàn bộ `CL-S`, `CL-D`, `CL-I` đạt; `CL-U-20` → `24` đạt; dinh dưỡng viên dựng và công bố được 1 thực đơn thật |

---

## 13. Ma trận truy vết yêu cầu (RTM)

Theo `rules/14`: mỗi yêu cầu chức năng phải có story, tiêu chí nghiệm thu và ít nhất một test case. Cột "Test Case ID" ghi dải mã test case chức năng của từng story (điền ngày 11/11/2026 từ [test-cases.md](test-cases.md)); test case bổ sung của phần B tra theo cột "Nhóm checklist".

| FR ID | Tên yêu cầu chức năng | User Story | Số kịch bản AC | Nhóm checklist | Test Case ID | Trạng thái |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| `FR-MENU-ING-001` | Tạo nguyên liệu | `US-MENU-01`, `US-MENU-15` | 10 | CL-F, CL-B, CL-X | `TC-MENU-0101` → `0107`, `TC-MENU-1501` → `1503` | Sẵn sàng viết test case |
| `FR-MENU-ING-002` | Sửa nguyên liệu | `US-MENU-01` | 7 | CL-F, CL-B, CL-X | `TC-MENU-0101` → `0107` | Sẵn sàng viết test case |
| `FR-MENU-ING-003` | Ngừng dùng / huỷ nguyên liệu | `US-MENU-02` | 3 | CL-F, CL-B, CL-X | `TC-MENU-0201` → `0203` | Sẵn sàng viết test case |
| `FR-MENU-ING-004` | Danh sách và tìm nguyên liệu | `US-MENU-03` | 4 | CL-F, CL-B, CL-X | `TC-MENU-0301` → `0304` | Sẵn sàng viết test case |
| `FR-MENU-ING-005` | Quản lý nhóm nguyên liệu | `US-MENU-04` | 3 | CL-F, CL-B, CL-X | `TC-MENU-0401` → `0403` | Chờ H-3 |
| `FR-MENU-ING-006` | Khai mùa vụ | `US-MENU-05` | 3 | CL-F, CL-B, CL-X | `TC-MENU-0501` → `0503` | Sẵn sàng viết test case |
| `FR-MENU-DISH-001` | Tạo món | `US-MENU-07` | 6 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-0701` → `0706` | Sẵn sàng viết test case |
| `FR-MENU-DISH-002` | Sửa món | `US-MENU-26`, `US-MENU-27` | 11 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-2601` → `2606`, `TC-MENU-2701` → `2705` | Sẵn sàng viết test case |
| `FR-MENU-DISH-003` | Gửi duyệt món | `US-MENU-10` | 4 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-1001` → `1004` | Sẵn sàng viết test case |
| `FR-MENU-DISH-004` | Duyệt / trả lại món | `US-MENU-11`, `US-MENU-46` | 12 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-1101` → `1106`, `TC-MENU-4601` → `4606` | Chờ E2-Q7 |
| `FR-MENU-DISH-005` | Ngừng dùng món | `US-MENU-28` | 4 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-2801` → `2804` | Sẵn sàng viết test case |
| `FR-MENU-DISH-006` | Danh sách và tìm món | `US-MENU-09` | 3 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-0901` → `0903` | Sẵn sàng viết test case |
| `FR-MENU-DISH-007` | Quản lý phương pháp chế biến | `US-MENU-06` | 3 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-0601` → `0603` | Chờ H-1, H-8 |
| `FR-MENU-DISH-008` | Quản lý cặp món kỵ nhau | `US-MENU-08` | 3 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-0801` → `0803` | Chờ H-4 |
| `FR-MENU-DISH-009` | Ảnh món | `US-MENU-29` | 4 | CL-F, CL-S, CL-U, CL-X | `TC-MENU-2901` → `2904` | Sẵn sàng viết test case |
| `FR-MENU-RCP-001` | Tạo công thức | `US-MENU-14` | 7 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1401` → `1407` | Chờ E2-Q5, O-02 |
| `FR-MENU-RCP-002` | Sửa công thức nháp | `US-MENU-14` | 7 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1401` → `1407` | Chờ E2-Q5, O-02 |
| `FR-MENU-RCP-003` | Gửi duyệt, duyệt, trả lại công thức | `US-MENU-16`, `US-MENU-46` | 11 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1601` → `1605`, `TC-MENU-4601` → `4606` | Chờ E2-Q7 |
| `FR-MENU-RCP-004` | Tạo phiên bản mới | `US-MENU-17` | 4 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1701` → `1704` | Sẵn sàng viết test case |
| `FR-MENU-RCP-005` | Lấy công thức hiệu lực | `US-MENU-18` | 3 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1801` → `1803` | Sẵn sàng viết test case |
| `FR-MENU-RCP-006` | So sánh hai phiên bản | `US-MENU-19` | 3 | CL-F, CL-D, CL-B, CL-X | `TC-MENU-1901` → `1903` | Sẵn sàng viết test case |
| `FR-MENU-RCP-007` | Nhiều cỡ định lượng | Chưa có | 0 | Không áp dụng | Chưa có | Chưa thành story: chờ [O-02] |
| `FR-MENU-PRC-001` | Đặt giá bán | `US-MENU-20` | 5 | CL-F, CL-S, CL-B, CL-X | `TC-MENU-2001` → `2005` | Chờ E2-Q1 |
| `FR-MENU-PRC-002` | Duyệt / trả lại giá | `US-MENU-21`, `US-MENU-46` | 11 | CL-F, CL-S, CL-B, CL-X | `TC-MENU-2101` → `2105`, `TC-MENU-4601` → `4606` | Chờ E2-Q7 |
| `FR-MENU-PRC-003` | Lấy giá hiệu lực | `US-MENU-21` | 5 | CL-F, CL-S, CL-B, CL-X | `TC-MENU-2101` → `2105` | Chờ E2-Q7 |
| `FR-MENU-PRC-004` | Lịch sử giá | `US-MENU-22` | 3 | CL-F, CL-S, CL-B, CL-X | `TC-MENU-2201` → `2203` | Sẵn sàng viết test case |
| `FR-MENU-MTY-001` | Tạo loại suất | `US-MENU-23` | 4 | CL-F, CL-B | `TC-MENU-2301` → `2304` | Sẵn sàng viết test case |
| `FR-MENU-MTY-002` | Kích hoạt / ngừng loại suất | `US-MENU-23` | 4 | CL-F, CL-B | `TC-MENU-2301` → `2304` | Sẵn sàng viết test case |
| `FR-MENU-MTY-003` | Sửa loại suất | `US-MENU-24` | 4 | CL-F, CL-B | `TC-MENU-2401` → `2404` | Sẵn sàng viết test case |
| `FR-MENU-MTY-004` | Đánh dấu công khai | `US-MENU-25` | 3 | CL-F, CL-B | `TC-MENU-2501` → `2503` | Sẵn sàng viết test case |
| `FR-MENU-MNU-001` | Tạo thực đơn tuần | `US-MENU-31` | 5 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3101` → `3105` | Chờ E2-Q3, E2-Q4 |
| `FR-MENU-MNU-002` | Xếp món vào ngày | `US-MENU-32` | 7 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3201` → `3207` | Sẵn sàng viết test case |
| `FR-MENU-MNU-003` | Chọn món mặc định | `US-MENU-33` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3301` → `3304` | Sẵn sàng viết test case |
| `FR-MENU-MNU-004` | Kiểm ngưỡng giá suất | `US-MENU-39` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3901` → `3904` | Chờ E2-Q1 |
| `FR-MENU-MNU-005` | Sao chép thực đơn | `US-MENU-51` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-5101` → `5104` | Sẵn sàng viết test case |
| `FR-MENU-MNU-006` | Lịch sử món đã dùng | `US-MENU-52` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-5201` → `5204` | Sẵn sàng viết test case |
| `FR-MENU-MNU-007` | Xem và danh sách thực đơn | `US-MENU-34` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3401` → `3404` | Sẵn sàng viết test case |
| `FR-MENU-MNU-008` | Xuất thực đơn | `US-MENU-53` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-5301` → `5304` | Sẵn sàng viết test case |
| `FR-MENU-MNU-009` | Huỷ thực đơn nháp | `US-MENU-35` | 4 | CL-F, CL-U, CL-P, CL-D | `TC-MENU-3501` → `3504` | Sẵn sàng viết test case |
| `FR-MENU-RUL-001` | Kiểm thực đơn | `US-MENU-36`, `US-MENU-37`, `US-MENU-38` | 18 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-3601` → `3607`, `TC-MENU-3701` → `3705`, `TC-MENU-3801` → `3806` | Chờ DL-01, E2-Q2, H-2 |
| `FR-MENU-RUL-002` | Kiểm thực đơn chưa lưu | `US-MENU-41` | 4 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-4101` → `4104` | Sẵn sàng viết test case |
| `FR-MENU-RUL-003` | Chi tiết vi phạm | `US-MENU-36` | 7 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-3601` → `3607` | Sẵn sàng viết test case |
| `FR-MENU-RUL-004` | Ghi lý do chấp nhận | `US-MENU-40` | 4 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-4001` → `4004` | Sẵn sàng viết test case |
| `FR-MENU-RUL-005` | Danh mục quy tắc | `US-MENU-42` | 3 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-4201` → `4203` | Chờ DL-01 |
| `FR-MENU-RUL-006` | Sửa quy tắc | `US-MENU-27`, `US-MENU-43` | 11 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-2701` → `2705`, `TC-MENU-4301` → `4306` | Chờ E2-Q11 |
| `FR-MENU-RUL-007` | Cần người duyệt thứ hai khi điểm thấp | `US-MENU-50` | 4 | CL-F, CL-R, CL-P, CL-D | `TC-MENU-5001` → `5004` | Sẵn sàng viết test case |
| `FR-MENU-APV-001` | Gửi duyệt thực đơn | `US-MENU-44` | 7 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4401` → `4407` | Chờ E2-Q6 |
| `FR-MENU-APV-002` | Duyệt / trả lại thực đơn | `US-MENU-45`, `US-MENU-46` | 12 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4501` → `4506`, `TC-MENU-4601` → `4606` | Chờ E2-Q7 |
| `FR-MENU-APV-003` | Công bố | `US-MENU-48` | 4 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4801` → `4804` | Chờ E2-Q9 |
| `FR-MENU-APV-004` | Thu hồi | `US-MENU-49` | 5 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4901` → `4905` | Chờ E2-Q8 |
| `FR-MENU-APV-005` | Sửa sau thu hồi | `US-MENU-49` | 5 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4901` → `4905` | Chờ E2-Q8 |
| `FR-MENU-APV-006` | Chỗ móc kiểm cost | `US-MENU-44` | 7 | CL-F, CL-S, CL-D, CL-I | `TC-MENU-4401` → `4407` | Chờ E2-Q6 |
| `FR-MENU-IMP-001` | Tải mẫu | `US-MENU-12`, `US-MENU-30` | 11 | CL-F, CL-X, CL-P, CL-D | `TC-MENU-1201` → `1206`, `TC-MENU-3001` → `3005` | Chờ O-02 |
| `FR-MENU-IMP-002` | Kiểm tệp nhập | `US-MENU-12`, `US-MENU-30` | 11 | CL-F, CL-X, CL-P, CL-D | `TC-MENU-1201` → `1206`, `TC-MENU-3001` → `3005` | Chờ O-02 |
| `FR-MENU-IMP-003` | Thực hiện nhập | `US-MENU-13`, `US-MENU-30` | 9 | CL-F, CL-X, CL-P, CL-D | `TC-MENU-1301` → `1304`, `TC-MENU-3001` → `3005` | Chờ E2-Q10, O-02 |

Tổng: 55 yêu cầu chức năng · 30 sẵn sàng viết test case · 24 chờ điểm mở nghiệp vụ · 1 chưa thành story. Yêu cầu chỉ chờ [O-06] (ai là người duyệt) được tính là sẵn sàng, vì test case viết được với tài khoản kiểm thử.

`FR-SYS-NTF-001` (thông báo, thuộc epic nền tảng) được kiểm trong epic này qua `US-MENU-47` và `CL-I-01`.

---

## 14. Điểm mở ảnh hưởng tới kiểm thử

Giữ nguyên trạng thái mở.

| Điểm mở | Ảnh hưởng |
| :--- | :--- |
| DL-01: duyệt 43 quy tắc | Toàn bộ nhóm `CL-R` chưa có giới hạn; khoảng 140 ca kiểm (35 đề mục × 4 ca) chưa viết được |
| [O-04]: đội phát triển, QA, công cụ | Chưa biết ai chạy và tự động hoá đến đâu; mục 11, 12 là đề xuất |
| [O-06]: ai duyệt | `CL-S-06` → `11`, `CL-D-03` cần tài khoản thật; quy tắc 2 người duyệt có thể bị bỏ |
| [E2-Q1]: cách kiểm ngưỡng giá | `CL-R-30`, `CL-B-18` có thể đổi hẳn |
| [E2-Q2], [H-2]: tuần trước, ngày liên tiếp | `CL-R-08`, `09`, `11`, `12` |
| [E2-Q11]: thực đơn chờ duyệt có kiểm lại | `CL-D-11` |
| [O-02], [E2-Q5]: cỡ định lượng, bảng chuẩn | `CL-R-31`, `32`; mẫu tệp công thức ở `CL-X` |

## 15. Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo |
