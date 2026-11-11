# Test Cases — Epic E2 · Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `43-test-cases.md` · BA-Kit v1.0 |
| Phiên bản | 0.1.2 |
| Trạng thái | Draft — chưa có QA rà; chưa chạy lần nào (phần mềm chưa được xây) |
| Ngày | 2026-11-11 |
| Căn cứ | [Test checklist v0.1.0](checklist.md) · [Tiêu chí nghiệm thu v0.1.0](../userstories/acceptance-criteria.md) · [SRS epic v0.3.0](../srs/spec.md) · [SRS nền tảng](../../nen-tang/srs/spec.md) |

## 1. Thông tin tổng quan

Tài liệu gồm hai phần:

- **Phần A — Test case chức năng**: mỗi kịch bản nghiệm thu thành một test case. Phần này được **sinh tự động** từ file tiêu chí nghiệm thu (Given → tiền điều kiện, When → bước, Then → kết quả mong đợi), nên nội dung khớp từng chữ với kịch bản gốc. Khi tiêu chí nghiệm thu đổi, sinh lại phần này.
- **Phần B — Test case bổ sung**: viết tay từ các nhóm của checklist mà tiêu chí nghiệm thu không phủ: phân quyền và bảo mật, dữ liệu biên, toàn vẹn dữ liệu, hiệu năng, tích hợp, nhập bảng tính.

**Chưa có trong tài liệu này**

| Phần | Lý do |
| :--- | :--- |
| Test case cho từng quy tắc thực đơn (nhóm `CL-R`, khoảng 140 ca) | Chờ DL-01 duyệt con số |
| Test case giao diện (nhóm `CL-U`, 24 đề mục) | Chạy trực tiếp theo checklist và bảng trạng thái màn hình của user-flow; viết thành test case khi có giao diện thật, vì bước thao tác phụ thuộc bố cục cuối cùng |
| Script tự động | Chờ [O-04]: chưa có đội và công cụ |

### Quy ước

| Mục | Quy ước |
| :--- | :--- |
| Mã test case chức năng | `TC-MENU-{story}{số kịch bản}` — ví dụ `TC-MENU-0103` là kịch bản 3 của `US-MENU-01` |
| Mã test case bổ sung | `TC-MENU-{nhóm}-{số}` với nhóm `S` bảo mật · `B` biên · `D` dữ liệu · `P` hiệu năng · `I` tích hợp · `X` nhập bảng tính |
| Loại | Thuận lợi · Lỗi · Biên (theo thẻ của kịch bản gốc) |
| Trạng thái | **Sẵn sàng** = chạy được khi có phần mềm · **Chờ {mã}** = kịch bản viết theo cách xử lý tạm, phải rà lại khi điểm mở có câu trả lời |
| Tài khoản | **DDV** dinh dưỡng viên · **ND1**, **ND2** người duyệt · **BT** bếp trưởng (chỉ xem) · **QLCS** quản lý cơ sở · **KT** kế toán |
| Ngày | "Hôm nay" = ngày chạy; "D+n" = n ngày sau |
| Kết quả ngầm định | Mọi thao tác ghi đều có bản ghi nhật ký; kiểm một lần ở `TC-MENU-S-12`, không lặp lại ở từng test case |
| Dữ liệu | Tên món, định lượng, giá là dữ liệu kiểm thử minh họa |

### Bộ dữ liệu nền

Dùng cho mọi test case trừ khi tiền điều kiện ghi khác. Chi tiết ở mục 11 của checklist.

- 13 nhóm nguyên liệu, 11 phương pháp chế biến ("Luộc", "Hấp" có cờ ít dầu mỡ; "Chiên" có cờ chiên).
- 60 nguyên liệu; 40 món `ACTIVE` có công thức và giá hiệu lực (16 món chính trong đó 4 Healthy, 11 món phụ, 6 rau, 7 canh).
- Loại suất "Suất 40.000đ" `ACTIVE`: ngưỡng 40.000 đồng, 3 món chính đưa ra, chọn 1, 2 món phụ, có rau, có canh.
- Cặp kỵ "Nem rán" – "Nộm".
- Thực đơn `PUBLISHED` của 4 tuần trước cho "Suất 40.000đ".

---

# Phần A — Test case chức năng

## US-MENU-01 — Tạo và sửa nguyên liệu

Yêu cầu: `FR-MENU-ING-001`, `002` · Use case: `UC-MENU-001` · Ưu tiên: P0 · Checklist: `CL-F-01`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0101` | `AC-MENU-01-1` | Thuận lợi | Tạo nguyên liệu tính theo gram | • DDV đang ở màn hình danh sách nguyên liệu<br>• đã có nhóm nguyên liệu "Lợn" | 1. DDV tạo nguyên liệu "Thịt lợn nạc vai", nhóm "Lợn", đơn vị mua "kg", đơn vị dùng "g", hệ số quy đổi 1000, loại bảo quản "Tươi" | • nguyên liệu được lưu ở trạng thái "ACTIVE" và có mã do hệ thống cấp<br>• nguyên liệu xuất hiện trong danh sách chọn khi lập công thức | Sẵn sàng |
| `TC-MENU-0102` | `AC-MENU-01-2` | Thuận lợi | Tạo nguyên liệu không tính theo gram | Bộ dữ liệu nền | 1. DDV tạo nguyên liệu "Đậu phụ", đơn vị mua "bìa", đơn vị dùng "bìa", hệ số quy đổi 1 | • nguyên liệu được lưu với đơn vị dùng "bìa" | Sẵn sàng |
| `TC-MENU-0103` | `AC-MENU-01-3` | Lỗi | Tên trùng nguyên liệu đã có | • đã có nguyên liệu "Thịt lợn nạc vai" | 1. DDV tạo nguyên liệu tên "thịt lợn nạc vai " (khác hoa thường, thừa dấu cách) | • hệ thống không tạo nguyên liệu<br>• trả lỗi "ERR-MENU-409-01" | Sẵn sàng |
| `TC-MENU-0104` | `AC-MENU-01-4` | Lỗi | Hệ số quy đổi sai với cặp kg – g | Bộ dữ liệu nền | 1. DDV tạo nguyên liệu với đơn vị mua "kg", đơn vị dùng "g", hệ số quy đổi 100 | • hệ thống không tạo nguyên liệu<br>• trả lỗi "ERR-MENU-422-01" tại ô hệ số quy đổi | Sẵn sàng |
| `TC-MENU-0105` | `AC-MENU-01-5` | Lỗi | Nguyên liệu có xương nhưng thiếu tỷ lệ hao hụt | Bộ dữ liệu nền | 1. DDV tạo nguyên liệu "Sườn lợn", tích "có xương hoặc vỏ" và để trống tỷ lệ hao hụt | • hệ thống không tạo nguyên liệu<br>• trả lỗi "ERR-MENU-422-02" | Sẵn sàng |
| `TC-MENU-0106` | `AC-MENU-01-6` | Biên | Không sửa được đơn vị của nguyên liệu đang nằm trong công thức hiệu lực | • nguyên liệu "Cá trắm" nằm trong 2 công thức ở trạng thái "ACTIVE" | 1. DDV sửa đơn vị dùng của "Cá trắm" từ "g" sang "kg" | • hệ thống không lưu thay đổi<br>• trả lỗi "ERR-MENU-409-02" nêu số công thức là 2 | Sẵn sàng |
| `TC-MENU-0107` | `AC-MENU-01-7` | Biên | Hai người sửa cùng một nguyên liệu | • DDV và một tài khoản khác cùng mở nguyên liệu "Cà chua" ở phiên bản 3<br>• tài khoản kia đã lưu thay đổi trước | 1. DDV lưu thay đổi của mình | • hệ thống không ghi đè và trả lỗi "ERR-SYS-409-02" | Sẵn sàng |

## US-MENU-02 — Ngừng dùng nguyên liệu

Yêu cầu: `FR-MENU-ING-003` · Use case: `UC-MENU-001` · Ưu tiên: P0 · Checklist: `CL-F-02`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0201` | `AC-MENU-02-1` | Thuận lợi | Ngừng dùng nguyên liệu không còn công thức nào dùng | • nguyên liệu "Bột nêm cũ" không nằm trong công thức "ACTIVE" nào | 1. DDV chọn "Ngừng dùng" và nhập lý do "Đã đổi sang loại khác" | • nguyên liệu chuyển trạng thái "INACTIVE"<br>• không còn xuất hiện trong danh sách chọn khi lập công thức mới | Sẵn sàng |
| `TC-MENU-0202` | `AC-MENU-02-2` | Lỗi | Ngừng dùng nguyên liệu đang nằm trong công thức hiệu lực | • nguyên liệu "Cá trắm" nằm trong công thức "ACTIVE" của món "Cá kho" và "Cá rán" | 1. DDV chọn "Ngừng dùng" cho "Cá trắm" | • nguyên liệu giữ trạng thái "ACTIVE"<br>• hệ thống trả lỗi "ERR-SYS-409-01" kèm danh sách 2 công thức | Sẵn sàng |
| `TC-MENU-0203` | `AC-MENU-02-3` | Biên | Nguyên liệu chỉ còn trong công thức đã thay thế | • nguyên liệu "Đường thắng" chỉ nằm trong công thức ở trạng thái "SUPERSEDED" | 1. DDV chọn "Ngừng dùng" và nhập lý do hợp lệ | • nguyên liệu chuyển trạng thái "INACTIVE"<br>• công thức "SUPERSEDED" vẫn hiển thị được tên nguyên liệu này | Sẵn sàng |

## US-MENU-03 — Tìm và lọc nguyên liệu

Yêu cầu: `FR-MENU-ING-004` · Use case: `UC-MENU-001` · Ưu tiên: P0 · Checklist: `CL-F-03`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0301` | `AC-MENU-03-1` | Thuận lợi | Lọc theo nhóm và trạng thái | • có 45 nguyên liệu, trong đó 6 nguyên liệu nhóm "Cá" ở trạng thái "ACTIVE" | 1. BT lọc nhóm "Cá" và trạng thái "ACTIVE" | • danh sách hiện đúng 6 nguyên liệu | Sẵn sàng |
| `TC-MENU-0302` | `AC-MENU-03-2` | Biên | Phân trang | • có 45 nguyên liệu | 1. BT mở danh sách không lọc | • trang đầu hiện 20 nguyên liệu và tổng số ghi 45 | Sẵn sàng |
| `TC-MENU-0303` | `AC-MENU-03-3` | Biên | Bộ lọc không ra kết quả | Bộ dữ liệu nền | 1. BT tìm theo tên "xyz không tồn tại" | • danh sách hiện thông báo "Không có nguyên liệu khớp bộ lọc" và nút "Xoá lọc" | Sẵn sàng |
| `TC-MENU-0304` | `AC-MENU-03-4` | Lỗi | Vai trò chỉ xem không có nút sửa | Bộ dữ liệu nền | 1. BT mở danh sách nguyên liệu | • không có nút "Thêm nguyên liệu"<br>• gọi trực tiếp lệnh tạo nguyên liệu trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-04 — Quản lý nhóm nguyên liệu

Yêu cầu: `FR-MENU-ING-005` · Use case: `UC-MENU-001` · Ưu tiên: P0 · Checklist: `CL-F-04`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0401` | `AC-MENU-04-1` | Thuận lợi | Tạo nhóm kèm nguồn đạm | Bộ dữ liệu nền | 1. DDV tạo nhóm "Ếch" với nguồn đạm "Thịt" | • nhóm xuất hiện trong danh sách chọn của nguyên liệu và của món | Chờ H-3 |
| `TC-MENU-0402` | `AC-MENU-04-2` | Lỗi | Tên nhóm trùng | • đã có nhóm "Cá" | 1. DDV tạo nhóm "cá" | • hệ thống trả lỗi "ERR-MENU-409-01" | Sẵn sàng |
| `TC-MENU-0403` | `AC-MENU-04-3` | Biên | Không huỷ được nhóm đang được dùng | • nhóm "Cá" có 6 nguyên liệu và 5 món | 1. DDV huỷ nhóm "Cá" | • nhóm không bị huỷ và hệ thống trả lỗi "ERR-SYS-409-01" | Sẵn sàng |

## US-MENU-05 — Khai mùa vụ

Yêu cầu: `FR-MENU-ING-006` · Use case: `UC-MENU-001` · Ưu tiên: P1 · Checklist: `CL-F-05`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0501` | `AC-MENU-05-1` | Thuận lợi | Khai một khoảng mùa | Bộ dữ liệu nền | 1. DDV khai mùa vụ của "Rau muống" từ tháng 4 đến tháng 9 | • nguyên liệu "Rau muống" có 1 khoảng mùa "4–9" | Sẵn sàng |
| `TC-MENU-0502` | `AC-MENU-05-2` | Lỗi | Tháng ngoài khoảng 1–12 | Bộ dữ liệu nền | 1. DDV khai mùa vụ từ tháng 0 đến tháng 13 | • hệ thống trả lỗi "ERR-MENU-422-03" | Sẵn sàng |
| `TC-MENU-0503` | `AC-MENU-05-3` | Biên | Mùa vụ vắt qua cuối năm | Bộ dữ liệu nền | 1. DDV khai mùa vụ của "Cải thảo" từ tháng 10 đến tháng 2 | • khoảng mùa được lưu<br>• tháng 12 và tháng 1 được coi là trong mùa, tháng 6 là ngoài mùa | Sẵn sàng |

## US-MENU-06 — Quản lý phương pháp chế biến

Yêu cầu: `FR-MENU-DISH-007` · Use case: `UC-MENU-002` · Ưu tiên: P0 · Checklist: `CL-F-06`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0601` | `AC-MENU-06-1` | Thuận lợi | Tạo phương pháp có cờ ít dầu mỡ | Bộ dữ liệu nền | 1. DDV tạo phương pháp "Hấp", không tích "là chiên/rán", tích "ít dầu mỡ" | • phương pháp "Hấp" chọn được cho món<br>• món dùng phương pháp "Hấp" gắn được cờ Healthy | Chờ H-1, H-8 |
| `TC-MENU-0602` | `AC-MENU-06-2` | Lỗi | Tên phương pháp trùng | • đã có phương pháp "Kho" | 1. DDV tạo phương pháp "kho" | • hệ thống trả lỗi "ERR-MENU-409-01" | Sẵn sàng |
| `TC-MENU-0603` | `AC-MENU-06-3` | Biên | Bỏ cờ ít dầu mỡ khi đang có món Healthy dùng phương pháp đó | • món "Cá hấp" ở trạng thái "ACTIVE", có cờ Healthy, dùng phương pháp "Hấp" | 1. DDV bỏ cờ "ít dầu mỡ" của phương pháp "Hấp" | • hệ thống không lưu và trả lỗi "ERR-SYS-409-01" kèm danh sách món Healthy đang dùng | Sẵn sàng |

## US-MENU-07 — Tạo món nháp

Yêu cầu: `FR-MENU-DISH-001` · Use case: `UC-MENU-002` · Ưu tiên: P0 · Checklist: `CL-F-07`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0701` | `AC-MENU-07-1` | Thuận lợi | Tạo món chính đủ thuộc tính | Bộ dữ liệu nền | 1. DDV tạo món "Cá sốt cà chua": vai trò "Món chính", nhóm "Cá", phương pháp "Sốt", kết cấu "Có nước sốt", vị chua "Có", nhóm cost "Cao", chất gây dị ứng "Cá" | • món được lưu ở trạng thái "DRAFT" và có mã do hệ thống cấp<br>• món chưa chọn được khi xếp thực đơn | Sẵn sàng |
| `TC-MENU-0702` | `AC-MENU-07-2` | Lỗi | Tên món trùng | • đã có món "Cá kho" | 1. DDV tạo món tên "Cá kho" | • hệ thống trả lỗi "ERR-MENU-409-01" kèm liên kết tới món đã có | Sẵn sàng |
| `TC-MENU-0703` | `AC-MENU-07-3` | Lỗi | Gắn Healthy với phương pháp không ít dầu mỡ | • phương pháp "Chiên" không có cờ ít dầu mỡ | 1. DDV tạo món phương pháp "Chiên" và tích Healthy | • hệ thống trả lỗi "ERR-MENU-422-04" nêu phương pháp hiện tại là "Chiên" | Sẵn sàng |
| `TC-MENU-0704` | `AC-MENU-07-4` | Lỗi | Món gốc khác vai trò | • món "Canh chua" có vai trò "Canh" | 1. DDV tạo món vai trò "Món chính" và chọn món gốc là "Canh chua" | • hệ thống trả lỗi "ERR-MENU-422-05" | Sẵn sàng |
| `TC-MENU-0705` | `AC-MENU-07-5` | Biên | Món gốc chỉ một cấp | • món "Thịt kho tàu" có món gốc là "Thịt kho trứng cút" | 1. DDV tạo món mới và chọn món gốc là "Thịt kho tàu" | • hệ thống trả lỗi "ERR-MENU-422-05" | Sẵn sàng |
| `TC-MENU-0706` | `AC-MENU-07-6` | Biên | Mỗi thuộc tính có chú giải | Bộ dữ liệu nền | 1. DDV mở form tạo món | • mỗi trong 12 thuộc tính ảnh hưởng quy tắc hiển thị một dòng định nghĩa và ít nhất 1 ví dụ | Sẵn sàng |

## US-MENU-08 — Khai cặp món kỵ nhau

Yêu cầu: `FR-MENU-DISH-008` · Use case: `UC-MENU-002` · Ưu tiên: P0 · Checklist: `CL-F-08`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0801` | `AC-MENU-08-1` | Thuận lợi | Khai một cặp kỵ | Bộ dữ liệu nền | 1. DDV khai cặp "Nem rán" – "Nộm" với ghi chú "cùng kiểu chế biến" | • cặp được lưu<br>• bộ kiểm quy tắc báo vi phạm "BR-MENU-034" khi hai món cùng một ngày | Chờ H-4 |
| `TC-MENU-0802` | `AC-MENU-08-2` | Lỗi | Hai món của cặp giống nhau | Bộ dữ liệu nền | 1. DDV khai cặp "Nem rán" – "Nem rán" | • hệ thống trả lỗi "ERR-MENU-422-07" | Sẵn sàng |
| `TC-MENU-0803` | `AC-MENU-08-3` | Biên | Cặp đã có theo thứ tự ngược | • đã có cặp "Nem rán" – "Nộm" | 1. DDV khai cặp "Nộm" – "Nem rán" | • hệ thống trả lỗi "ERR-MENU-409-01" | Sẵn sàng |

## US-MENU-09 — Tìm và lọc món

Yêu cầu: `FR-MENU-DISH-006` · Use case: — · Ưu tiên: P0 · Checklist: `CL-F-09`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-0901` | `AC-MENU-09-1` | Thuận lợi | Lọc theo vai trò và Healthy | • có 16 món chính "ACTIVE", trong đó 4 món có cờ Healthy | 1. DDV lọc vai trò "Món chính", Healthy "Có", trạng thái "ACTIVE" | • danh sách hiện đúng 4 món | Sẵn sàng |
| `TC-MENU-0902` | `AC-MENU-09-2` | Biên | Món có đề nghị thay đổi đang chờ duyệt | • món "Sườn sốt chua ngọt" có 1 đề nghị thay đổi ở trạng thái "PENDING" | 1. DDV mở danh sách món | • dòng "Sườn sốt chua ngọt" hiện nhãn "chờ duyệt thay đổi" và trạng thái vẫn là "ACTIVE" | Sẵn sàng |
| `TC-MENU-0903` | `AC-MENU-09-3` | Lỗi | Vai trò chỉ xem không thấy giá bán | Bộ dữ liệu nền | 1. BT mở chi tiết một món | • không có nút sửa và không có thẻ "Giá bán" | Sẵn sàng |

## US-MENU-10 — Gửi duyệt món

Yêu cầu: `FR-MENU-DISH-003` · Use case: `UC-MENU-002` · Ưu tiên: P0 · Checklist: `CL-F-10`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1001` | `AC-MENU-10-1` | Thuận lợi | Gửi duyệt món đã có công thức chờ duyệt | • món "Cá hấp" ở trạng thái "DRAFT" và có 1 công thức ở trạng thái "PENDING" | 1. DDV gửi duyệt món "Cá hấp" | • món chuyển trạng thái "PENDING"<br>• mỗi tài khoản có quyền "menu.catalog.approve" nhận 1 thông báo dẫn tới món | Sẵn sàng |
| `TC-MENU-1002` | `AC-MENU-10-2` | Lỗi | Gửi duyệt món chưa có công thức | • món "Gà rán" ở trạng thái "DRAFT" và chưa có công thức nào | 1. DDV gửi duyệt món "Gà rán" | • món giữ trạng thái "DRAFT"<br>• hệ thống trả lỗi "ERR-MENU-422-06" | Sẵn sàng |
| `TC-MENU-1003` | `AC-MENU-10-3` | Biên | Gửi duyệt nhiều món, một món không đạt | • DDV chọn 3 món nháp, trong đó "Gà rán" chưa có công thức | 1. DDV gửi duyệt cả 3 món | • 2 món chuyển "PENDING", "Gà rán" giữ "DRAFT"<br>• kết quả báo "2 thành công, 1 lỗi" kèm lý do của "Gà rán" | Sẵn sàng |
| `TC-MENU-1004` | `AC-MENU-10-4` | Biên | Món có công thức chỉ ở trạng thái nháp | • món "Bò xào" có 1 công thức ở trạng thái "DRAFT" | 1. DDV gửi duyệt món "Bò xào" | • hệ thống trả lỗi "ERR-MENU-422-06" | Sẵn sàng |

## US-MENU-11 — Duyệt hoặc trả lại món

Yêu cầu: `FR-MENU-DISH-004` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-11`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1101` | `AC-MENU-11-1` | Thuận lợi | Duyệt món có công thức đang hiệu lực | • món "Cá hấp" ở trạng thái "PENDING", do DDV tạo, có công thức "ACTIVE" | 1. ND1 duyệt món "Cá hấp" | • món chuyển trạng thái "ACTIVE" và chọn được khi xếp thực đơn<br>• DDV nhận thông báo kết quả | Chờ O-06 |
| `TC-MENU-1102` | `AC-MENU-11-2` | Thuận lợi | Duyệt món và công thức đầu tiên trong cùng một lần | • món "Gà rán" và công thức v1 của nó cùng ở trạng thái "PENDING" | 1. ND1 chọn cả món và công thức rồi duyệt một lần | • công thức chuyển "ACTIVE" trước, sau đó món chuyển "ACTIVE" | Sẵn sàng |
| `TC-MENU-1103` | `AC-MENU-11-3` | Lỗi | Người sửa cuối tự duyệt | • món "Tôm luộc" ở trạng thái "PENDING" và ND1 là người sửa cuối | 1. ND1 duyệt món "Tôm luộc" | • món giữ trạng thái "PENDING"<br>• hệ thống trả lỗi "ERR-SYS-403-01" | Sẵn sàng |
| `TC-MENU-1104` | `AC-MENU-11-4` | Lỗi | Duyệt món khi công thức chưa được duyệt | • món "Gà rán" ở trạng thái "PENDING" và chỉ có công thức ở trạng thái "PENDING" | 1. ND1 duyệt riêng món "Gà rán" | • hệ thống trả lỗi "ERR-MENU-422-06" | Sẵn sàng |
| `TC-MENU-1105` | `AC-MENU-11-5` | Lỗi | Trả lại không có lý do | Bộ dữ liệu nền | 1. ND1 chọn "Trả lại" món "Cá hấp" và để trống lý do | • món giữ trạng thái "PENDING" và hệ thống trả lỗi "ERR-SYS-422-01" | Sẵn sàng |
| `TC-MENU-1106` | `AC-MENU-11-6` | Biên | Trả lại có lý do | Bộ dữ liệu nền | 1. ND1 trả lại món "Cá hấp" với lý do "Thuộc tính kết cấu chưa đúng" | • món về trạng thái "DRAFT"<br>• DDV nhận thông báo kèm nguyên văn lý do | Sẵn sàng |

## US-MENU-12 — Tải mẫu và kiểm tệp nhập

Yêu cầu: `FR-MENU-IMP-001`, `002` · Use case: `UC-MENU-012` · Ưu tiên: P0 · Checklist: `CL-F-12`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1201` | `AC-MENU-12-1` | Thuận lợi | Tệp nguyên liệu không có lỗi | • DDV đã tải mẫu "nguyên liệu" và điền 120 dòng hợp lệ | 1. DDV tải tệp lên và chọn "Kiểm tra" | • hệ thống báo "120 dòng hợp lệ, 0 lỗi" và bật nút "Nhập"<br>• chưa có nguyên liệu nào được tạo | Sẵn sàng |
| `TC-MENU-1202` | `AC-MENU-12-2` | Lỗi | Tệp có dòng lỗi | • tệp món có dòng 14 gắn Healthy với phương pháp "Chiên" và dòng 27 trùng tên món đã có | 1. DDV chọn "Kiểm tra" | • hệ thống trả lỗi "ERR-MENU-422-20" kèm danh sách: dòng 14 – cột Healthy – "ERR-MENU-422-04"; dòng 27 – cột Tên – "ERR-MENU-409-01"<br>• nút "Nhập" bị khoá | Sẵn sàng |
| `TC-MENU-1203` | `AC-MENU-12-3` | Lỗi | Tệp sai mẫu | Bộ dữ liệu nền | 1. DDV tải lên tệp thiếu cột "Đơn vị dùng" | • hệ thống trả lỗi "ERR-MENU-422-20" nêu cột bị thiếu | Sẵn sàng |
| `TC-MENU-1204` | `AC-MENU-12-4` | Biên | Tệp đúng 2.000 dòng và 2.001 dòng | Bộ dữ liệu nền | 1. DDV kiểm tệp 2.000 dòng dữ liệu<br>2. DDV kiểm tệp 2.001 dòng dữ liệu | (sau bước 1) tệp được kiểm<br>(sau bước 2) hệ thống trả lỗi "ERR-MENU-422-20" nêu giới hạn 2.000 dòng | Sẵn sàng |
| `TC-MENU-1205` | `AC-MENU-12-5` | Biên | Hai dòng trong tệp trùng tên nhau | • tệp món có dòng 5 và dòng 9 cùng tên "Cá kho riềng" | 1. DDV chọn "Kiểm tra" | • cả dòng 5 và dòng 9 đều bị đánh dấu lỗi | Sẵn sàng |
| `TC-MENU-1206` | `AC-MENU-12-6` | Biên | Việc kiểm kéo dài hơn 5 giây | • tệp 2.000 dòng cần hơn 5 giây để kiểm | 1. DDV chọn "Kiểm tra" rồi rời trang | • việc kiểm tiếp tục chạy nền<br>• DDV nhận thông báo khi kiểm xong, mở lại được kết quả | Sẵn sàng |

## US-MENU-13 — Nhập tệp đã kiểm sạch

Yêu cầu: `FR-MENU-IMP-003` · Use case: `UC-MENU-012` · Ưu tiên: P0 · Checklist: `CL-F-13`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1301` | `AC-MENU-13-1` | Thuận lợi | Nhập 40 món | • tệp món 40 dòng đã qua kiểm tra không lỗi | 1. DDV chọn "Nhập" | • 40 món được tạo ở trạng thái "DRAFT"<br>• hệ thống báo "40 món đã tạo" kèm liên kết tới danh sách món vừa nhập | Chờ E2-Q10 |
| `TC-MENU-1302` | `AC-MENU-13-2` | Thuận lợi | Nhập nguyên liệu | • tệp nguyên liệu 120 dòng đã qua kiểm tra không lỗi | 1. DDV chọn "Nhập" | • 120 nguyên liệu được tạo ở trạng thái "ACTIVE" | Sẵn sàng |
| `TC-MENU-1303` | `AC-MENU-13-3` | Lỗi | Dữ liệu hệ thống thay đổi giữa lúc kiểm và lúc nhập | • tệp món đã qua kiểm tra không lỗi<br>• sau đó một tài khoản khác tạo món trùng tên với dòng 8 của tệp | 1. DDV chọn "Nhập" | • không có món nào được tạo<br>• hệ thống trả lỗi "ERR-MENU-422-20" và yêu cầu kiểm lại | Sẵn sàng |
| `TC-MENU-1304` | `AC-MENU-13-4` | Biên | Món nhập vào không tự hiệu lực | • DDV vừa nhập 40 món | 1. DDV mở hộp chọn món của một thực đơn | • không món nào trong 40 món xuất hiện | Sẵn sàng |

## US-MENU-14 — Lập công thức nháp

Yêu cầu: `FR-MENU-RCP-001`, `002` · Use case: `UC-MENU-004` · Ưu tiên: P0 · Checklist: `CL-F-14`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1401` | `AC-MENU-14-1` | Thuận lợi | Lập công thức có nguyên liệu chính và phụ | • món "Thịt kho trứng cút" có nhóm nguyên liệu chính "Lợn" | 1. DDV lập công thức hiệu lực từ D+7 với: "Thịt lợn nạc vai" (chính) 65 – 70 – 70 g; "Trứng cút" (không chính) 3 – 3 – 3 quả | • công thức được lưu ở trạng thái "DRAFT" với số phiên bản 1<br>• đơn vị của từng dòng tự lấy theo đơn vị dùng của nguyên liệu | Chờ O-02, E2-Q5 |
| `TC-MENU-1402` | `AC-MENU-14-2` | Lỗi | Không có nguyên liệu chính | Bộ dữ liệu nền | 1. DDV lưu công thức mà không dòng nào được đánh dấu nguyên liệu chính | • hệ thống trả lỗi "ERR-MENU-422-08" | Sẵn sàng |
| `TC-MENU-1403` | `AC-MENU-14-3` | Lỗi | Lặp nguyên liệu | Bộ dữ liệu nền | 1. DDV lưu công thức có 2 dòng cùng nguyên liệu "Cà chua" | • hệ thống trả lỗi "ERR-MENU-422-08" | Sẵn sàng |
| `TC-MENU-1404` | `AC-MENU-14-4` | Lỗi | Chuẩn nhỏ hơn tối thiểu | Bộ dữ liệu nền | 1. DDV lưu công thức có dòng "Cá trắm" tối thiểu 130, chuẩn 120, tối đa 140 | • hệ thống trả lỗi "ERR-MENU-422-09" chỉ rõ dòng sai | Sẵn sàng |
| `TC-MENU-1405` | `AC-MENU-14-5` | Lỗi | Nguyên liệu chính không thuộc nhóm của món | • món "Cá sốt cà chua" có nhóm nguyên liệu chính "Cá" | 1. DDV lưu công thức chỉ có "Cà chua" (nhóm "Rau") là nguyên liệu chính | • hệ thống trả lỗi "ERR-MENU-422-10" nêu nhóm cần có là "Cá" | Sẵn sàng |
| `TC-MENU-1406` | `AC-MENU-14-6` | Biên | Ba giá trị định lượng bằng nhau | Bộ dữ liệu nền | 1. DDV lưu dòng "Trứng cút" tối thiểu 3, chuẩn 3, tối đa 3 | • dòng được chấp nhận | Sẵn sàng |
| `TC-MENU-1407` | `AC-MENU-14-7` | Biên | Rau và canh không bắt buộc khớp nhóm | • món "Canh chua" có vai trò "Canh" và nhóm nguyên liệu chính "Rau" | 1. DDV lưu công thức có nguyên liệu chính duy nhất là "Cá trắm" | • công thức được lưu, không báo "ERR-MENU-422-10" | Sẵn sàng |

## US-MENU-15 — Tạo nguyên liệu trong lúc soạn công thức

Yêu cầu: `FR-MENU-ING-001` · Use case: `UC-MENU-004` · Ưu tiên: P0 · Checklist: `CL-F-15`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1501` | `AC-MENU-15-1` | Thuận lợi | Tạo nguyên liệu và giữ các dòng đã nhập | • DDV đang soạn công thức và đã nhập 3 dòng chưa lưu | 1. DDV mở ngăn "Nguyên liệu mới", tạo "Cá rô phi" hợp lệ và lưu | • "Cá rô phi" xuất hiện trong công thức đang soạn<br>• 3 dòng đã nhập giữ nguyên nguyên liệu và định lượng | Sẵn sàng |
| `TC-MENU-1502` | `AC-MENU-15-2` | Lỗi | Nguyên liệu mới trùng tên | • đã có nguyên liệu "Cá trắm" | 1. DDV tạo "Cá trắm" trong ngăn "Nguyên liệu mới" | • ngăn không đóng và hiện lỗi "ERR-MENU-409-01"<br>• các dòng công thức đã nhập giữ nguyên | Sẵn sàng |
| `TC-MENU-1503` | `AC-MENU-15-3` | Biên | Đóng ngăn mà không lưu | • DDV đã nhập 3 dòng công thức chưa lưu và mở ngăn "Nguyên liệu mới" | 1. DDV chọn "Huỷ" | • không có nguyên liệu nào được tạo và 3 dòng giữ nguyên | Sẵn sàng |

## US-MENU-16 — Duyệt hoặc trả lại công thức

Yêu cầu: `FR-MENU-RCP-003` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-16`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1601` | `AC-MENU-16-1` | Thuận lợi | Duyệt công thức đầu tiên có ngày hiệu lực đã đến | • công thức v1 của "Gà rán" ở trạng thái "PENDING", do DDV tạo, hiệu lực từ hôm nay | 1. ND1 duyệt công thức | • công thức chuyển trạng thái "ACTIVE" | Chờ O-06 |
| `TC-MENU-1602` | `AC-MENU-16-2` | Thuận lợi | Duyệt phiên bản mới có ngày hiệu lực trong tương lai | • "Thịt kho trứng cút" có công thức v1 "ACTIVE" và v2 "PENDING" hiệu lực từ D+10 | 1. ND1 duyệt v2 | • v1 và v2 cùng ở trạng thái "ACTIVE"<br>• công thức hiệu lực cho ngày D+9 là v1, cho ngày D+10 là v2<br>• vào ngày D+10 v1 chuyển trạng thái "SUPERSEDED" | Sẵn sàng |
| `TC-MENU-1603` | `AC-MENU-16-3` | Lỗi | Người tạo tự duyệt | • công thức v1 của "Gà rán" do ND1 tạo, ở trạng thái "PENDING" | 1. ND1 duyệt công thức | • hệ thống trả lỗi "ERR-SYS-403-01" và công thức giữ trạng thái "PENDING" | Sẵn sàng |
| `TC-MENU-1604` | `AC-MENU-16-4` | Lỗi | Sửa công thức đã gửi duyệt | • công thức v1 của "Gà rán" ở trạng thái "PENDING" | 1. DDV sửa định lượng của một dòng | • hệ thống trả lỗi "ERR-MENU-409-03" | Sẵn sàng |
| `TC-MENU-1605` | `AC-MENU-16-5` | Biên | Trả lại công thức | Bộ dữ liệu nền | 1. ND1 trả lại công thức v1 của "Gà rán" với lý do "Định lượng gà thấp hơn bảng chuẩn" | • công thức về trạng thái "DRAFT" và DDV sửa được<br>• DDV nhận thông báo kèm lý do | Sẵn sàng |

## US-MENU-17 — Tạo phiên bản công thức mới

Yêu cầu: `FR-MENU-RCP-004` · Use case: `UC-MENU-004` · Ưu tiên: P0 · Checklist: `CL-F-17`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1701` | `AC-MENU-17-1` | Thuận lợi | Tạo v3 từ v2 | • "Cá sốt cà chua" có công thức v2 ở trạng thái "ACTIVE" với 4 dòng | 1. DDV chọn "Tạo phiên bản mới", nhập lý do "Giá cá tăng" và ngày hiệu lực D+14 | • công thức v3 được tạo ở trạng thái "DRAFT" với 4 dòng giống v2<br>• v2 vẫn ở trạng thái "ACTIVE" | Sẵn sàng |
| `TC-MENU-1702` | `AC-MENU-17-2` | Lỗi | Thiếu lý do | Bộ dữ liệu nền | 1. DDV chọn "Tạo phiên bản mới" và nhập lý do "ngắn" | • hệ thống trả lỗi "ERR-SYS-422-01" và không tạo phiên bản | Sẵn sàng |
| `TC-MENU-1703` | `AC-MENU-17-3` | Biên | Thực đơn đã gắn phiên bản cũ không đổi | • thực đơn tuần sau ở trạng thái "PUBLISHED" đã gắn công thức v2 của "Cá sốt cà chua" | 1. v3 được duyệt với ngày hiệu lực nằm trong tuần sau | • thực đơn đó vẫn gắn v2 | Sẵn sàng |
| `TC-MENU-1704` | `AC-MENU-17-4` | Biên | Đang có một bản nháp | • "Cá sốt cà chua" đã có công thức v3 ở trạng thái "DRAFT" | 1. DDV mở công thức v2 | • không có nút "Tạo phiên bản mới" | Sẵn sàng |

## US-MENU-18 — Lấy đúng công thức hiệu lực theo ngày

Yêu cầu: `FR-MENU-RCP-005` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-18`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1801` | `AC-MENU-18-1` | Thuận lợi | Có một công thức hiệu lực | • "Cá kho" có công thức v1 "ACTIVE" hiệu lực từ 01/10 | 1. hệ thống lấy công thức của "Cá kho" cho ngày 20/11 | • kết quả là v1 | Sẵn sàng |
| `TC-MENU-1802` | `AC-MENU-18-2` | Biên | Hai phiên bản, ngày phục vụ đúng ngày chuyển tiếp | • "Thịt kho trứng cút" có v1 hiệu lực từ 01/08 và v2 hiệu lực từ 23/11, cùng "ACTIVE" | 1. hệ thống lấy công thức cho ngày 22/11 và ngày 23/11 | • kết quả lần lượt là v1 và v2 | Sẵn sàng |
| `TC-MENU-1803` | `AC-MENU-18-3` | Lỗi | Chưa có công thức hiệu lực cho ngày đó | • "Gà rán" chỉ có công thức v1 "ACTIVE" hiệu lực từ 16/11 | 1. hệ thống lấy công thức của "Gà rán" cho ngày 15/11 | • hệ thống trả lỗi "ERR-MENU-404-01" nêu tên món "Gà rán" và ngày 15/11 | Sẵn sàng |

## US-MENU-19 — So sánh hai phiên bản công thức

Yêu cầu: `FR-MENU-RCP-006` · Use case: `UC-MENU-004`, `010` · Ưu tiên: P1 · Checklist: `CL-F-19`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-1901` | `AC-MENU-19-1` | Thuận lợi | Hiện dòng đổi, thêm, bỏ | • v1 có "Thịt lợn" chuẩn 70 g, "Trứng cút" 3 quả, "Đường thắng" 5 g<br>• v2 có "Thịt lợn" chuẩn 65 g, "Trứng cút" 3 quả, "Hành khô" 3 g | 1. ND1 mở so sánh v1 với v2 | • "Thịt lợn" được đánh dấu "đổi định lượng", "Hành khô" là "thêm", "Đường thắng" là "bỏ", "Trứng cút" là "không đổi" | Sẵn sàng |
| `TC-MENU-1902` | `AC-MENU-19-2` | Biên | Hai phiên bản giống hệt nhau | Bộ dữ liệu nền | 1. ND1 so sánh hai phiên bản có cùng các dòng và định lượng | • màn hình ghi "Không có khác biệt" | Sẵn sàng |
| `TC-MENU-1903` | `AC-MENU-19-3` | Lỗi | Công thức đầu tiên không có gì để so sánh | • "Gà rán" chỉ có công thức v1 | 1. ND1 mở chi tiết duyệt công thức v1 | • màn hình hiện bảng định lượng, không hiện phần so sánh | Sẵn sàng |

## US-MENU-20 — Đặt giá bán

Yêu cầu: `FR-MENU-PRC-001` · Use case: `UC-MENU-005` · Ưu tiên: P0 · Checklist: `CL-F-20`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2001` | `AC-MENU-20-1` | Thuận lợi | Đặt giá đầu tiên | • món "Cá hấp" chưa có giá bán | 1. DDV đặt giá 22000 đồng, hiệu lực từ D+1 | • giá được lưu ở trạng thái "PENDING"<br>• tài khoản có quyền "menu.price.approve" nhận thông báo | Chờ E2-Q1 |
| `TC-MENU-2002` | `AC-MENU-20-2` | Lỗi | Giá không phải bội số của 100 đồng | Bộ dữ liệu nền | 1. DDV đặt giá 22050 đồng | • hệ thống trả lỗi "ERR-MENU-422-11" | Sẵn sàng |
| `TC-MENU-2003` | `AC-MENU-20-3` | Lỗi | Ngày hiệu lực là hôm nay | Bộ dữ liệu nền | 1. DDV đặt giá 22000 đồng, hiệu lực từ hôm nay | • hệ thống trả lỗi "ERR-MENU-422-11" | Sẵn sàng |
| `TC-MENU-2004` | `AC-MENU-20-4` | Lỗi | Trùng ngày hiệu lực | • món "Bò xào" đã có giá hiệu lực từ 01/12 | 1. DDV đặt giá khác cũng hiệu lực từ 01/12 | • hệ thống trả lỗi "ERR-MENU-409-04" | Sẵn sàng |
| `TC-MENU-2005` | `AC-MENU-20-5` | Biên | Giá bằng 0 | Bộ dữ liệu nền | 1. DDV đặt giá 0 đồng, hiệu lực từ D+1 | • giá được lưu ở trạng thái "PENDING" | Sẵn sàng |

## US-MENU-21 — Duyệt giá bán và lấy giá hiệu lực

Yêu cầu: `FR-MENU-PRC-002`, `003` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-21`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2101` | `AC-MENU-21-1` | Thuận lợi | Duyệt giá | • giá 26000 đồng của "Bò xào" hiệu lực từ 01/12, do DDV tạo, ở trạng thái "PENDING" | 1. ND1 duyệt giá | • giá chuyển trạng thái "APPROVED"<br>• giá hiệu lực của "Bò xào" cho ngày 30/11 là giá cũ, cho ngày 01/12 là 26000 đồng | Chờ O-06, E2-Q7 |
| `TC-MENU-2102` | `AC-MENU-21-2` | Lỗi | Món chưa có giá hiệu lực | • "Cá hấp" chỉ có giá "APPROVED" hiệu lực từ 01/12 | 1. hệ thống lấy giá của "Cá hấp" cho ngày 25/11 | • hệ thống trả lỗi "ERR-MENU-404-02" | Sẵn sàng |
| `TC-MENU-2103` | `AC-MENU-21-3` | Lỗi | Giá chờ duyệt không được dùng | • "Cá hấp" có giá 22000 đồng hiệu lực từ D+1 ở trạng thái "PENDING" | 1. hệ thống lấy giá của "Cá hấp" cho ngày D+2 | • hệ thống trả lỗi "ERR-MENU-404-02" | Sẵn sàng |
| `TC-MENU-2104` | `AC-MENU-21-4` | Biên | Giá đã hiệu lực không sửa, không huỷ được | • giá 24000 đồng của "Bò xào" ở trạng thái "APPROVED", hiệu lực từ ngày đã qua | 1. DDV sửa hoặc huỷ giá này | • giá không đổi và hệ thống trả lỗi "ERR-MENU-409-10" | Sẵn sàng |
| `TC-MENU-2105` | `AC-MENU-21-5` | Biên | Trả lại giá | Bộ dữ liệu nền | 1. ND1 trả lại giá 26000 đồng với lý do "Tăng quá nhanh so với tháng trước" | • giá chuyển trạng thái "REJECTED" và không bao giờ được dùng | Sẵn sàng |

## US-MENU-22 — Lịch sử giá bán

Yêu cầu: `FR-MENU-PRC-004` · Use case: `UC-MENU-005` · Ưu tiên: P1 · Checklist: `CL-F-22`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2201` | `AC-MENU-22-1` | Thuận lợi | Xem lịch sử | • "Cá sốt cà chua" có giá 21000 đồng từ 01/08 và 22000 đồng từ 01/10, cùng "APPROVED" | 1. DDV mở thẻ "Giá bán" | • danh sách hiện 2 dòng, mới nhất ở trên, dòng 22000 đồng ghi "đang áp dụng" | Sẵn sàng |
| `TC-MENU-2202` | `AC-MENU-22-2` | Biên | Món chưa có giá | Bộ dữ liệu nền | 1. DDV mở thẻ "Giá bán" của món chưa có giá | • màn hình ghi "Món chưa có giá bán" | Sẵn sàng |
| `TC-MENU-2203` | `AC-MENU-22-3` | Lỗi | Vai trò không có quyền xem giá | Bộ dữ liệu nền | 1. BT gọi trực tiếp lệnh xem lịch sử giá | • hệ thống trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-23 — Tạo loại suất

Yêu cầu: `FR-MENU-MTY-001`, `002` · Use case: `UC-MENU-006` · Ưu tiên: P0 · Checklist: `CL-F-23`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2301` | `AC-MENU-23-1` | Thuận lợi | Tạo loại suất 40.000 đồng | Bộ dữ liệu nền | 1. DDV tạo loại suất "Suất 40.000đ": ngưỡng giá 40000, 3 món chính đưa ra, chọn 1, 2 món phụ, có rau, có canh<br>2. DDV kích hoạt loại suất | (sau bước 1) loại suất được lưu ở trạng thái "DRAFT"<br>(sau bước 2) loại suất chuyển "ACTIVE" và chọn được khi tạo thực đơn | Sẵn sàng |
| `TC-MENU-2302` | `AC-MENU-23-2` | Lỗi | Số món chính được chọn lớn hơn số đưa ra | Bộ dữ liệu nền | 1. DDV tạo loại suất với 2 món chính đưa ra và chọn 3 | • hệ thống trả lỗi "ERR-MENU-422-12" | Sẵn sàng |
| `TC-MENU-2303` | `AC-MENU-23-3` | Biên | Số món phụ ở biên | Bộ dữ liệu nền | 1. DDV tạo loại suất với 0 món phụ<br>2. DDV tạo loại suất với 6 món phụ | (sau bước 1) loại suất được lưu<br>(sau bước 2) hệ thống trả lỗi "ERR-MENU-422-12" | Sẵn sàng |
| `TC-MENU-2304` | `AC-MENU-23-4` | Biên | Loại suất nháp chưa dùng được | • loại suất "Suất 35.000đ" ở trạng thái "DRAFT" | 1. DDV tạo thực đơn mới | • "Suất 35.000đ" không có trong danh sách chọn loại suất | Sẵn sàng |

## US-MENU-24 — Khoá cơ cấu loại suất

Yêu cầu: `FR-MENU-MTY-003` · Use case: `UC-MENU-006` · Ưu tiên: P0 · Checklist: `CL-F-24`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2401` | `AC-MENU-24-1` | Thuận lợi | Sửa cơ cấu khi chưa có thực đơn gửi duyệt | • "Suất 40.000đ" chỉ có thực đơn ở trạng thái "DRAFT" | 1. DDV sửa số món phụ từ 2 thành 3 | • thay đổi được lưu | Sẵn sàng |
| `TC-MENU-2402` | `AC-MENU-24-2` | Lỗi | Sửa cơ cấu khi đã có thực đơn chờ duyệt | • "Suất 40.000đ" có 1 thực đơn ở trạng thái "PENDING" | 1. DDV sửa ngưỡng giá từ 40000 thành 42000 | • hệ thống trả lỗi "ERR-MENU-409-05" | Sẵn sàng |
| `TC-MENU-2403` | `AC-MENU-24-3` | Biên | Tên vẫn sửa được | • "Suất 40.000đ" có thực đơn ở trạng thái "PUBLISHED" | 1. DDV đổi tên thành "Suất tiêu chuẩn 40.000đ" | • tên mới được lưu | Sẵn sàng |
| `TC-MENU-2404` | `AC-MENU-24-4` | Biên | Ngừng loại suất không ảnh hưởng thực đơn đã công bố | • "Suất 40.000đ" có thực đơn tuần sau ở trạng thái "PUBLISHED" | 1. DDV ngừng loại suất | • thực đơn tuần sau vẫn ở trạng thái "PUBLISHED"<br>• không tạo được thực đơn mới cho loại suất này | Sẵn sàng |

## US-MENU-25 — Đánh dấu loại suất công khai

Yêu cầu: `FR-MENU-MTY-004` · Use case: `UC-MENU-006` · Ưu tiên: P1 · Checklist: `CL-F-25`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2501` | `AC-MENU-25-1` | Thuận lợi | Bật cờ công khai | Bộ dữ liệu nền | 1. DDV bật cờ "công khai" cho "Suất 40.000đ" | • cờ được lưu và hiện trong danh sách loại suất | Sẵn sàng |
| `TC-MENU-2502` | `AC-MENU-25-2` | Biên | Bật cờ khi loại suất đã có thực đơn công bố | • "Suất 40.000đ" có thực đơn "PUBLISHED" | 1. DDV bật cờ "công khai" | • cờ được lưu (cờ này không thuộc cơ cấu bị khoá) | Sẵn sàng |
| `TC-MENU-2503` | `AC-MENU-25-3` | Lỗi | Vai trò chỉ xem không bật được | Bộ dữ liệu nền | 1. BT gọi trực tiếp lệnh bật cờ "công khai" | • hệ thống trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-26 — Đề nghị sửa thuộc tính món đang dùng

Yêu cầu: `FR-MENU-DISH-002` · Use case: `UC-MENU-003` · Ưu tiên: P0 · Checklist: `CL-F-26`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2601` | `AC-MENU-26-1` | Thuận lợi | Đề nghị đổi một thuộc tính ảnh hưởng quy tắc | • món "Sườn sốt chua ngọt" ở trạng thái "ACTIVE" với vị chua "Không" | 1. DDV đổi vị chua thành "Có", nhập lý do "Gắn thiếu khi tạo món" và gửi đề nghị | • một đề nghị thay đổi được tạo ở trạng thái "PENDING" ghi "Vị chua: Không → Có"<br>• món vẫn "ACTIVE" với vị chua "Không" và hiện nhãn "chờ duyệt thay đổi" | Sẵn sàng |
| `TC-MENU-2602` | `AC-MENU-26-2` | Thuận lợi | Sửa trường không ảnh hưởng quy tắc | Bộ dữ liệu nền | 1. DDV sửa mô tả của món "Sườn sốt chua ngọt" | • mô tả mới được lưu ngay, không tạo đề nghị | Sẵn sàng |
| `TC-MENU-2603` | `AC-MENU-26-3` | Lỗi | Thiếu lý do | Bộ dữ liệu nền | 1. DDV đổi phương pháp chế biến của món "ACTIVE" và gửi đề nghị với lý do 5 ký tự | • hệ thống trả lỗi "ERR-SYS-422-01" và không tạo đề nghị | Sẵn sàng |
| `TC-MENU-2604` | `AC-MENU-26-4` | Lỗi | Giá trị đề nghị vi phạm ràng buộc | • món "Cá rán" ở trạng thái "ACTIVE" dùng phương pháp "Chiên" | 1. DDV đề nghị bật cờ Healthy | • hệ thống trả lỗi "ERR-MENU-422-04" và không tạo đề nghị | Sẵn sàng |
| `TC-MENU-2605` | `AC-MENU-26-5` | Biên | Món đã có đề nghị đang chờ | • món "Sườn sốt chua ngọt" có 1 đề nghị ở trạng thái "PENDING" | 1. DDV mở món | • các ô thuộc tính bị khoá và có nút "Rút đề nghị" | Sẵn sàng |
| `TC-MENU-2606` | `AC-MENU-26-6` | Biên | Rút đề nghị | Bộ dữ liệu nền | 1. DDV chọn "Rút đề nghị" | • đề nghị chuyển trạng thái "WITHDRAWN", món không đổi và sửa lại được | Sẵn sàng |

## US-MENU-27 — Duyệt đề nghị thay đổi

Yêu cầu: `FR-MENU-DISH-002`, `FR-MENU-RUL-006` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-27`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2701` | `AC-MENU-27-1` | Thuận lợi | Duyệt đề nghị sửa món | • đề nghị "Vị chua: Không → Có" của món "Sườn sốt chua ngọt" ở trạng thái "PENDING", do DDV gửi | 1. ND1 duyệt đề nghị | • món có vị chua "Có", đề nghị chuyển "APPROVED", nhãn "chờ duyệt thay đổi" biến mất<br>• thực đơn "DRAFT" có món này được kiểm lại bằng giá trị mới ở lần kiểm kế tiếp | Chờ O-06 |
| `TC-MENU-2702` | `AC-MENU-27-2` | Lỗi | Người đề nghị tự duyệt | • đề nghị do ND1 gửi | 1. ND1 duyệt đề nghị đó | • hệ thống trả lỗi "ERR-SYS-403-01" | Sẵn sàng |
| `TC-MENU-2703` | `AC-MENU-27-3` | Biên | Đề nghị đã lỗi thời | • đề nghị ghi "Phương pháp: Rán → Chiên" cho món "Đậu rán"<br>• sau khi đề nghị được gửi, phương pháp của "Đậu rán" đã bị đổi bằng đường khác | 1. ND1 mở đề nghị | • đề nghị ở trạng thái "STALE", nút "Duyệt" và "Trả lại" bị tắt<br>• người đề nghị nhận thông báo cần gửi lại | Sẵn sàng |
| `TC-MENU-2704` | `AC-MENU-27-4` | Biên | Thực đơn đã gửi duyệt giữ kết quả cũ | • một thực đơn "PENDING" có món "Sườn sốt chua ngọt" | 1. đề nghị đổi vị chua của món được duyệt | • kết quả kiểm quy tắc của thực đơn đó không đổi | Sẵn sàng |
| `TC-MENU-2705` | `AC-MENU-27-5` | Biên | Trả lại đề nghị | Bộ dữ liệu nền | 1. ND1 trả lại đề nghị với lý do hợp lệ | • đề nghị chuyển "REJECTED" và món không đổi | Sẵn sàng |

## US-MENU-28 — Ngừng dùng món

Yêu cầu: `FR-MENU-DISH-005` · Use case: `UC-MENU-003` · Ưu tiên: P0 · Checklist: `CL-F-28`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2801` | `AC-MENU-28-1` | Thuận lợi | Ngừng dùng món không nằm trong thực đơn sắp phục vụ | • món "Mực xào" ở trạng thái "ACTIVE" và không nằm trong thực đơn "PUBLISHED" nào có ngày phục vụ từ hôm nay | 1. DDV chọn "Ngừng dùng" với lý do hợp lệ | • món chuyển trạng thái "INACTIVE" và không còn trong hộp chọn món | Sẵn sàng |
| `TC-MENU-2802` | `AC-MENU-28-2` | Lỗi | Món nằm trong thực đơn đã công bố sắp phục vụ | • món "Cá sốt cà chua" nằm trong thực đơn "PUBLISHED" có ngày phục vụ D+3 | 1. DDV chọn "Ngừng dùng" | • món giữ trạng thái "ACTIVE"<br>• hệ thống trả lỗi "ERR-SYS-409-01" kèm tên thực đơn | Sẵn sàng |
| `TC-MENU-2803` | `AC-MENU-28-3` | Biên | Món chỉ nằm trong thực đơn đã phục vụ xong | • món "Mực xào" chỉ nằm trong thực đơn "PUBLISHED" có ngày phục vụ cuối là hôm qua | 1. DDV chọn "Ngừng dùng" với lý do hợp lệ | • món chuyển trạng thái "INACTIVE" | Sẵn sàng |
| `TC-MENU-2804` | `AC-MENU-28-4` | Biên | Món nằm trong thực đơn nháp | • món "Mực xào" nằm trong một thực đơn "DRAFT" | 1. DDV ngừng dùng món | • món chuyển "INACTIVE"<br>• lần gửi duyệt kế tiếp của thực đơn đó bị chặn bởi "ERR-MENU-422-17" | Sẵn sàng |

## US-MENU-29 — Ảnh món

Yêu cầu: `FR-MENU-DISH-009` · Use case: `UC-MENU-002` · Ưu tiên: P1 · Checklist: `CL-F-29`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-2901` | `AC-MENU-29-1` | Thuận lợi | Tải ảnh hợp lệ | Bộ dữ liệu nền | 1. DDV tải ảnh JPG 2 MB cho món "Cá hấp" | • ảnh được lưu và hiển thị ở chi tiết món | Sẵn sàng |
| `TC-MENU-2902` | `AC-MENU-29-2` | Lỗi | Sai định dạng | Bộ dữ liệu nền | 1. DDV tải tệp GIF cho món | • hệ thống trả lỗi "ERR-SYS-415-01" | Sẵn sàng |
| `TC-MENU-2903` | `AC-MENU-29-3` | Biên | Kích thước ở biên | Bộ dữ liệu nền | 1. DDV tải ảnh PNG đúng 10 MB<br>2. DDV tải ảnh PNG lớn hơn 10 MB | (sau bước 1) ảnh được lưu<br>(sau bước 2) hệ thống trả lỗi "ERR-SYS-413-01" | Sẵn sàng |
| `TC-MENU-2904` | `AC-MENU-29-4` | Biên | Tệp đổi đuôi | Bộ dữ liệu nền | 1. DDV tải tệp PDF đã đổi tên thành ".jpg" | • hệ thống trả lỗi "ERR-SYS-415-01" (kiểm theo nội dung tệp) | Sẵn sàng |

## US-MENU-30 — Nhập công thức và giá bán từ bảng tính

Yêu cầu: `FR-MENU-IMP-001` → `003` · Use case: `UC-MENU-012` · Ưu tiên: P0 · Checklist: `CL-F-30`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3001` | `AC-MENU-30-1` | Thuận lợi | Nhập công thức cho 30 món | • 30 món và các nguyên liệu liên quan đã có trong hệ thống<br>• tệp công thức 95 dòng đã qua kiểm tra không lỗi | 1. DDV chọn "Nhập" | • 30 công thức v1 được tạo ở trạng thái "DRAFT" với tổng 95 dòng nguyên liệu | Chờ O-02 |
| `TC-MENU-3002` | `AC-MENU-30-2` | Thuận lợi | Nhập giá bán | • tệp giá bán 30 dòng đã qua kiểm tra không lỗi | 1. DDV chọn "Nhập" | • 30 giá được tạo ở trạng thái "PENDING" | Sẵn sàng |
| `TC-MENU-3003` | `AC-MENU-30-3` | Lỗi | Công thức tham chiếu món chưa có | • tệp công thức có dòng 12 ghi món "Vịt quay" chưa có trong hệ thống | 1. DDV chọn "Kiểm tra" | • dòng 12 bị báo lỗi "không tìm thấy món" và nút "Nhập" bị khoá | Sẵn sàng |
| `TC-MENU-3004` | `AC-MENU-30-4` | Lỗi | Công thức trong tệp vi phạm khoảng định lượng | • tệp công thức có dòng 20 với tối thiểu 70, chuẩn 65 | 1. DDV chọn "Kiểm tra" | • dòng 20 bị báo lỗi "ERR-MENU-422-09" | Sẵn sàng |
| `TC-MENU-3005` | `AC-MENU-30-5` | Biên | Món trong tệp thiếu nguyên liệu chính | • các dòng của món "Cá kho" trong tệp không có dòng nào đánh dấu nguyên liệu chính | 1. DDV chọn "Kiểm tra" | • mọi dòng của "Cá kho" bị báo lỗi "ERR-MENU-422-08" | Sẵn sàng |

## US-MENU-31 — Tạo thực đơn tuần

Yêu cầu: `FR-MENU-MNU-001` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-31`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3101` | `AC-MENU-31-1` | Thuận lợi | Tạo thực đơn 6 ngày | Bộ dữ liệu nền | 1. DDV tạo thực đơn cho "Suất 40.000đ", tuần bắt đầu thứ Hai 16/11/2026, các ngày phục vụ T2 đến T7 | • thực đơn được tạo ở trạng thái "DRAFT" với 6 ngày<br>• mỗi ngày có 3 ô món chính, 2 ô món phụ, 1 ô rau, 1 ô canh, tất cả trống | Chờ E2-Q3, E2-Q4 |
| `TC-MENU-3102` | `AC-MENU-31-2` | Lỗi | Ngày bắt đầu không phải thứ Hai | Bộ dữ liệu nền | 1. DDV tạo thực đơn với tuần bắt đầu thứ Ba 17/11/2026 | • hệ thống trả lỗi "ERR-MENU-422-13" | Sẵn sàng |
| `TC-MENU-3103` | `AC-MENU-31-3` | Lỗi | Đã có thực đơn cho loại suất và tuần đó | • đã có thực đơn "DRAFT" của "Suất 40.000đ" cho tuần 16/11/2026 | 1. DDV tạo thực đơn thứ hai cho cùng loại suất và tuần | • hệ thống trả lỗi "ERR-MENU-409-06" và mở thực đơn đã có | Sẵn sàng |
| `TC-MENU-3104` | `AC-MENU-31-4` | Biên | Tuần có ngày nghỉ | Bộ dữ liệu nền | 1. DDV tạo thực đơn chỉ chọn T2, T3, T5, T6 | • thực đơn có đúng 4 ngày | Sẵn sàng |
| `TC-MENU-3105` | `AC-MENU-31-5` | Biên | Tạo lại sau khi thực đơn cũ đã huỷ | • thực đơn của "Suất 40.000đ" tuần 16/11/2026 đã bị huỷ | 1. DDV tạo thực đơn mới cho cùng loại suất và tuần | • thực đơn mới được tạo | Sẵn sàng |

## US-MENU-32 — Xếp món vào ô

Yêu cầu: `FR-MENU-MNU-002` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-32`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3201` | `AC-MENU-32-1` | Thuận lợi | Xếp một món chính | • thực đơn "DRAFT" có ô "Món chính 1" của T2 đang trống | 1. DDV chọn món "Thịt kho trứng cút" cho ô đó | • ô hiện "Thịt kho trứng cút"<br>• ô được gắn phiên bản công thức hiệu lực tại ngày T2<br>• bộ kiểm quy tắc chạy lại | Sẵn sàng |
| `TC-MENU-3202` | `AC-MENU-32-2` | Lỗi | Hộp chọn chỉ có món đúng vai trò | Bộ dữ liệu nền | 1. DDV mở hộp chọn món cho ô "Rau" | • danh sách chỉ gồm món có vai trò "Rau" ở trạng thái "ACTIVE"<br>• gọi trực tiếp lệnh xếp món chính vào ô "Rau" trả lỗi "ERR-MENU-422-14" | Sẵn sàng |
| `TC-MENU-3203` | `AC-MENU-32-3` | Lỗi | Món không có công thức hiệu lực ngày phục vụ | • "Gà rán" có công thức hiệu lực từ 18/11 | 1. DDV xếp "Gà rán" vào ngày 16/11 | • món không được xếp và hệ thống trả lỗi "ERR-MENU-404-01" kèm liên kết tới thẻ Công thức của món | Sẵn sàng |
| `TC-MENU-3204` | `AC-MENU-32-4` | Lỗi | Món không có giá bán hiệu lực ngày phục vụ | • "Cá hấp" có giá hiệu lực từ 01/12 | 1. DDV xếp "Cá hấp" vào ngày 16/11 | • món không được xếp và hệ thống trả lỗi "ERR-MENU-404-02" | Sẵn sàng |
| `TC-MENU-3205` | `AC-MENU-32-5` | Biên | Một món một lần mỗi ngày | • "Đậu rán" đã ở ô "Món phụ 1" của T2 | 1. DDV mở hộp chọn món cho ô "Món phụ 2" của T2 | • "Đậu rán" hiện mờ với nhãn "đã có trong ngày" và không chọn được | Sẵn sàng |
| `TC-MENU-3206` | `AC-MENU-32-6` | Biên | Món bị ngừng dùng trong lúc hộp chọn đang mở | • DDV đang mở hộp chọn món và "Mực xào" còn trong danh sách<br>• một tài khoản khác ngừng dùng "Mực xào" | 1. DDV chọn "Mực xào" | • hệ thống trả lỗi "ERR-MENU-422-14" và làm mới danh sách | Sẵn sàng |
| `TC-MENU-3207` | `AC-MENU-32-7` | Biên | Sửa thực đơn không còn ở trạng thái soạn | • thực đơn ở trạng thái "PENDING" | 1. DDV gọi lệnh đổi món ở một ô | • hệ thống trả lỗi "ERR-MENU-409-07" | Sẵn sàng |

## US-MENU-33 — Chọn món mặc định

Yêu cầu: `FR-MENU-MNU-003` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-33`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3301` | `AC-MENU-33-1` | Thuận lợi | Chọn món mặc định | • T2 có 3 món chính "Thịt kho trứng cút", "Cá kho", "Gà luộc" | 1. DDV chọn "Thịt kho trứng cút" làm món mặc định của T2 | • ô đó hiện nhãn "MẶC ĐỊNH" | Sẵn sàng |
| `TC-MENU-3302` | `AC-MENU-33-2` | Lỗi | Chọn món phụ làm mặc định | Bộ dữ liệu nền | 1. DDV gọi lệnh đặt "Đậu rán" (món phụ của T2) làm món mặc định | • hệ thống trả lỗi "ERR-MENU-422-15" | Sẵn sàng |
| `TC-MENU-3303` | `AC-MENU-33-3` | Biên | Bỏ món đang là mặc định | • "Thịt kho trứng cút" là món mặc định của T2 và thực đơn ở trạng thái "CHECKED" | 1. DDV bỏ "Thịt kho trứng cút" khỏi T2 | • T2 không còn món mặc định<br>• thực đơn về trạng thái "DRAFT" | Sẵn sàng |
| `TC-MENU-3304` | `AC-MENU-33-4` | Biên | Đổi món mặc định | • "Thịt kho trứng cút" là món mặc định của T2 | 1. DDV chọn "Cá kho" làm món mặc định của T2 | • chỉ "Cá kho" có nhãn "MẶC ĐỊNH" | Sẵn sàng |

## US-MENU-34 — Xem danh sách và chi tiết thực đơn

Yêu cầu: `FR-MENU-MNU-007` · Use case: `UC-MENU-011` · Ưu tiên: P0 · Checklist: `CL-F-34`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3401` | `AC-MENU-34-1` | Thuận lợi | Dinh dưỡng viên thấy mọi trạng thái | • có 2 thực đơn "PUBLISHED", 1 "PENDING", 1 "DRAFT" | 1. DDV mở danh sách thực đơn | • danh sách hiện 4 thực đơn kèm trạng thái và điểm quy tắc | Sẵn sàng |
| `TC-MENU-3402` | `AC-MENU-34-2` | Thuận lợi | Vai trò chỉ xem chỉ thấy thực đơn đã công bố | Bộ dữ liệu nền | 1. BT mở danh sách thực đơn | • danh sách hiện 2 thực đơn "PUBLISHED" | Sẵn sàng |
| `TC-MENU-3403` | `AC-MENU-34-3` | Lỗi | Mở thực đơn chưa công bố bằng đường dẫn trực tiếp | Bộ dữ liệu nền | 1. BT mở đường dẫn của thực đơn "DRAFT" | • hệ thống trả lỗi "ERR-SYS-404-01" | Sẵn sàng |
| `TC-MENU-3404` | `AC-MENU-34-4` | Biên | Chưa có thực đơn nào | • chưa có thực đơn nào | 1. DDV mở danh sách thực đơn | • màn hình ghi "Chưa có thực đơn" và có nút "Tạo thực đơn" | Sẵn sàng |

## US-MENU-35 — Huỷ thực đơn nháp

Yêu cầu: `FR-MENU-MNU-009` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-35`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3501` | `AC-MENU-35-1` | Thuận lợi | Huỷ thực đơn nháp | • thực đơn ở trạng thái "DRAFT" | 1. DDV chọn "Huỷ thực đơn" và nhập lý do "Dựng thử, không dùng" | • thực đơn bị huỷ và không còn trong danh sách mặc định | Sẵn sàng |
| `TC-MENU-3502` | `AC-MENU-35-2` | Lỗi | Huỷ thực đơn đã gửi duyệt | • thực đơn ở trạng thái "PENDING" | 1. DDV gọi lệnh huỷ thực đơn | • hệ thống trả lỗi "ERR-MENU-409-08" | Sẵn sàng |
| `TC-MENU-3503` | `AC-MENU-35-3` | Biên | Huỷ thực đơn đã kiểm | • thực đơn ở trạng thái "CHECKED" | 1. DDV huỷ với lý do hợp lệ | • thực đơn bị huỷ | Sẵn sàng |
| `TC-MENU-3504` | `AC-MENU-35-4` | Lỗi | Thiếu lý do | Bộ dữ liệu nền | 1. DDV chọn "Huỷ thực đơn" và để trống lý do | • hệ thống trả lỗi "ERR-SYS-422-01" | Sẵn sàng |

## US-MENU-36 — Kiểm quy tắc cấp ngày

Yêu cầu: `FR-MENU-RUL-001`, `003` · Use case: `UC-MENU-008` · Ưu tiên: P0 · Checklist: `CL-F-36`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3601` | `AC-MENU-36-1` | Thuận lợi | Ngày không vi phạm | • T2 có đủ 3 món chính khác nhóm nguyên liệu trong đó đúng 1 món Healthy, 2 món phụ, rau, canh | 1. bộ kiểm chạy | • không có kết quả "không đạt" nào của quy tắc cấp ngày cho T2 | Sẵn sàng |
| `TC-MENU-3602` | `AC-MENU-36-2` | Lỗi | Vi phạm quy tắc cứng về cặp kỵ | • cặp "Nem rán" – "Nộm" đã được khai là kỵ nhau | 1. DDV xếp "Nem rán" và "Nộm" vào hai ô món phụ của T4 | • bảng kiểm có 1 kết quả không đạt mã "BR-MENU-034", loại bắt buộc<br>• kết quả ghi ngày "T4" và hai món "Nem rán", "Nộm" | Sẵn sàng |
| `TC-MENU-3603` | `AC-MENU-36-3` | Biên | Chi tiết vi phạm nêu giá trị đo và giới hạn | • T7 mới có 1 món chính | 1. bộ kiểm chạy | • kết quả "BR-MENU-001" của T7 ghi "có 1/3 món chính" | Sẵn sàng |
| `TC-MENU-3604` | `AC-MENU-36-4` | Biên | Ngày hoàn toàn trống không sinh vi phạm | • T7 chưa có món nào | 1. bộ kiểm chạy | • không có kết quả nào cho T7 | Sẵn sàng |
| `TC-MENU-3605` | `AC-MENU-36-5` | Biên | Kết quả xác định | • một thực đơn cố định và danh mục quy tắc không đổi | 1. bộ kiểm chạy 100 lần | • 100 lần cho cùng danh sách kết quả và cùng điểm | Sẵn sàng |
| `TC-MENU-3606` | `AC-MENU-36-6` | Biên | Thời gian phản hồi | • thực đơn 6 ngày, mỗi ngày 7 món | 1. bộ kiểm chạy 50 lần | • p95 thời gian phản hồi không vượt 2 giây | Sẵn sàng |
| `TC-MENU-3607` | `AC-MENU-36-7` | Biên | Quy tắc bị tắt không chạy | • quy tắc "BR-MENU-034" đã được tắt trong danh mục | 1. DDV xếp "Nem rán" và "Nộm" cùng ngày | • bảng kiểm không có kết quả nào của "BR-MENU-034" | Sẵn sàng |

## US-MENU-37 — Kiểm quy tắc cấp tuần

Yêu cầu: `FR-MENU-RUL-001` · Use case: `UC-MENU-008` · Ưu tiên: P0 · Checklist: `CL-F-37`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3701` | `AC-MENU-37-1` | Thuận lợi | Tuần không vi phạm | • không nhóm nguyên liệu nào có mặt ở món chính quá 2 ngày phục vụ liên tiếp<br>• không món chính nào xuất hiện quá 1 lần trong tuần | 1. bộ kiểm chạy | • không có kết quả không đạt của "BR-MENU-012" và "BR-MENU-013" | Chờ DL-01 |
| `TC-MENU-3702` | `AC-MENU-37-2` | Lỗi | Một nhóm nguyên liệu 3 ngày liền | • T2, T3, T4 đều có một món chính thuộc nhóm "Lợn" | 1. bộ kiểm chạy | • có 1 kết quả không đạt "BR-MENU-012" ghi "Lợn" và các ngày "T2, T3, T4" | Chờ DL-01, H-2 |
| `TC-MENU-3703` | `AC-MENU-37-3` | Biên | Ngày nghỉ làm ngắt chuỗi liên tiếp | • thực đơn chỉ phục vụ T2, T3, T5, T6 và nhóm "Lợn" có ở T2, T3, T5 | 1. bộ kiểm chạy | • chuỗi liên tiếp được tính theo ngày phục vụ: T2, T3, T5 là 3 ngày phục vụ liền nhau<br>• có 1 kết quả không đạt "BR-MENU-012" | Sẵn sàng |
| `TC-MENU-3704` | `AC-MENU-37-4` | Biên | Biến thể đổi tên được đếm theo món gốc | • "Thịt kho tàu" có món gốc là "Thịt kho trứng cút"<br>• T2 có "Thịt kho trứng cút", T5 có "Thịt kho tàu" | 1. bộ kiểm chạy | • có 1 kết quả không đạt "BR-MENU-013" ghi 2 lần xuất hiện ở T2 và T5 | Sẵn sàng |
| `TC-MENU-3705` | `AC-MENU-37-5` | Biên | Không có thực đơn tuần trước | • loại suất chưa có thực đơn cho tuần liền trước | 1. bộ kiểm chạy | • quy tắc tuần chỉ xét các ngày của tuần hiện tại<br>• bảng kiểm ghi chú "không có dữ liệu tuần trước" | Chờ E2-Q2 |

## US-MENU-38 — Điểm quy tắc và trạng thái "đã kiểm"

Yêu cầu: `FR-MENU-RUL-001` · Use case: `UC-MENU-008` · Ưu tiên: P0 · Checklist: `CL-F-38`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3801` | `AC-MENU-38-1` | Thuận lợi | Thực đơn đủ điều kiện chuyển "đã kiểm" | • mọi ô của mọi ngày đã có món và mọi ngày có món mặc định<br>• không có kết quả không đạt nào của quy tắc bắt buộc | 1. bộ kiểm chạy | • thực đơn chuyển trạng thái "CHECKED" và nút "Gửi duyệt" bật | Sẵn sàng |
| `TC-MENU-3802` | `AC-MENU-38-2` | Thuận lợi | Tính điểm | • thực đơn có 2 cảnh báo điểm phạt 3 và 1 cảnh báo điểm phạt 2 | 1. bộ kiểm chạy | • điểm quy tắc là 92 | Chờ DL-01 |
| `TC-MENU-3803` | `AC-MENU-38-3` | Biên | Quy tắc cấp ngày vi phạm ở nhiều ngày | • một quy tắc cấp ngày điểm phạt 3 không đạt ở T2, T4 và T6 | 1. bộ kiểm chạy | • điểm bị trừ 9 | Sẵn sàng |
| `TC-MENU-3804` | `AC-MENU-38-4` | Biên | Điểm không âm | • tổng điểm phạt của các cảnh báo là 120 | 1. bộ kiểm chạy | • điểm quy tắc là 0 | Sẵn sàng |
| `TC-MENU-3805` | `AC-MENU-38-5` | Lỗi | Vi phạm bắt buộc không trừ điểm nhưng chặn trạng thái | • thực đơn đủ món, đủ món mặc định, có 1 vi phạm bắt buộc và không có cảnh báo | 1. bộ kiểm chạy | • điểm quy tắc là 100<br>• thực đơn giữ trạng thái "DRAFT" và nút "Gửi duyệt" tắt | Sẵn sàng |
| `TC-MENU-3806` | `AC-MENU-38-6` | Biên | Thực đơn đã kiểm rơi về nháp | • thực đơn ở trạng thái "CHECKED" | 1. DDV đổi một món làm phát sinh vi phạm bắt buộc | • thực đơn về trạng thái "DRAFT" | Sẵn sàng |

## US-MENU-39 — Kiểm ngưỡng giá suất

Yêu cầu: `FR-MENU-MNU-004` · Use case: `UC-MENU-007` · Ưu tiên: P0 · Checklist: `CL-F-39`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-3901` | `AC-MENU-39-1` | Thuận lợi | Mọi tổ hợp trong ngưỡng | • T2 có món phụ 5000 và 4000, rau 3000, canh 2500 (tổng 14500)<br>• 3 món chính giá 22000, 22000, 23000 | 1. bộ kiểm chạy | • không có kết quả không đạt "BR-COST-012" cho T2 | Chờ E2-Q1 |
| `TC-MENU-3902` | `AC-MENU-39-2` | Lỗi | Một món chính làm suất vượt ngưỡng | • T4 có món phụ, rau, canh tổng 17000 và món chính "Bò xào" giá 24000 | 1. bộ kiểm chạy | • có 1 kết quả không đạt "BR-COST-012" cho T4<br>• kết quả ghi "Bò xào", tổng 41000 và phần vượt 1000 | Chờ E2-Q1 |
| `TC-MENU-3903` | `AC-MENU-39-3` | Biên | Tổng đúng bằng ngưỡng | • T3 có món phụ, rau, canh tổng 16000 và một món chính giá 24000 | 1. bộ kiểm chạy | • không có kết quả không đạt "BR-COST-012" cho món chính đó | Chờ E2-Q1 |
| `TC-MENU-3904` | `AC-MENU-39-4` | Biên | Dùng giá hiệu lực tại ngày phục vụ | • "Bò xào" có giá 24000 đến hết 30/11 và 26000 từ 01/12 | 1. bộ kiểm chạy cho ngày 30/11 và ngày 01/12 | • tổng giá được tính bằng 24000 cho ngày 30/11 và 26000 cho ngày 01/12 | Sẵn sàng |

## US-MENU-40 — Lý do chấp nhận cho cảnh báo mức nặng

Yêu cầu: `FR-MENU-RUL-004` · Use case: `UC-MENU-007`, `008` · Ưu tiên: P0 · Checklist: `CL-F-40`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4001` | `AC-MENU-40-1` | Thuận lợi | Ghi lý do | • thực đơn có 1 cảnh báo điểm phạt 3 | 1. DDV ghi lý do "Khách yêu cầu có thịt lợn mỗi ngày đầu tuần" | • lý do được lưu kèm cảnh báo đó và hiển thị cho người duyệt | Sẵn sàng |
| `TC-MENU-4002` | `AC-MENU-40-2` | Lỗi | Lý do quá ngắn | Bộ dữ liệu nền | 1. DDV ghi lý do "ok" cho cảnh báo điểm phạt 3 rồi gửi duyệt | • hệ thống trả lỗi "ERR-MENU-422-19" | Sẵn sàng |
| `TC-MENU-4003` | `AC-MENU-40-3` | Biên | Lý do tự xoá khi cảnh báo hết | • DDV đã ghi lý do cho cảnh báo "BR-MENU-030" của T4 | 1. DDV đổi món làm T4 chỉ còn 1 món vị chua | • cảnh báo biến mất và lý do đã ghi bị xoá<br>• nếu cảnh báo đó xuất hiện lại sau này, ô lý do trống | Sẵn sàng |
| `TC-MENU-4004` | `AC-MENU-40-4` | Biên | Cảnh báo mức vừa và nhẹ không cần lý do | • thực đơn chỉ có cảnh báo điểm phạt 2 và 1 | 1. DDV gửi duyệt | • việc gửi duyệt không bị chặn vì thiếu lý do | Sẵn sàng |

## US-MENU-41 — Kiểm thực đơn chưa lưu

Yêu cầu: `FR-MENU-RUL-002` · Use case: `UC-MENU-008` · Ưu tiên: P0 · Checklist: `CL-F-41`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4101` | `AC-MENU-41-1` | Thuận lợi | Kết quả giống thực đơn đã lưu | • một thực đơn đã lưu có kết quả kiểm K | 1. tài khoản dịch vụ của agent gửi đúng nội dung thực đơn đó tới lệnh kiểm thực đơn chưa lưu | • kết quả trả về giống hệt K<br>• không có bản ghi nào được tạo hoặc thay đổi | Sẵn sàng |
| `TC-MENU-4102` | `AC-MENU-41-2` | Lỗi | Nội dung chứa món không hợp lệ | Bộ dữ liệu nền | 1. agent gửi thực đơn có một món ở trạng thái "DRAFT" | • hệ thống trả lỗi "ERR-MENU-422-14" nêu món không hợp lệ | Sẵn sàng |
| `TC-MENU-4103` | `AC-MENU-41-3` | Biên | Tải đồng thời | Bộ dữ liệu nền | 1. 20 lời gọi kiểm thực đơn chưa lưu được gửi đồng thời | • p95 thời gian phản hồi không vượt 2 giây và không lời gọi nào lỗi | Sẵn sàng |
| `TC-MENU-4104` | `AC-MENU-41-4` | Lỗi | Tài khoản không có quyền | Bộ dữ liệu nền | 1. BT gọi lệnh kiểm thực đơn chưa lưu | • hệ thống trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-42 — Xem danh mục quy tắc

Yêu cầu: `FR-MENU-RUL-005` · Use case: `UC-MENU-013` · Ưu tiên: P0 · Checklist: `CL-F-42`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4201` | `AC-MENU-42-1` | Thuận lợi | Xem danh mục | Bộ dữ liệu nền | 1. DDV mở danh mục quy tắc | • mỗi quy tắc hiện mã, tên, câu gốc trong file quy chuẩn, loại, điểm phạt, phạm vi ngày hoặc tuần, tham số, trạng thái bật/tắt | Chờ DL-01 |
| `TC-MENU-4202` | `AC-MENU-42-2` | Biên | Quy tắc có đề nghị đang chờ duyệt | • quy tắc "BR-MENU-012" có 1 đề nghị thay đổi "PENDING" | 1. DDV mở danh mục quy tắc | • dòng "BR-MENU-012" hiện nhãn "chờ duyệt thay đổi", giá trị hiển thị là giá trị đang áp dụng | Sẵn sàng |
| `TC-MENU-4203` | `AC-MENU-42-3` | Lỗi | Vai trò chỉ xem không sửa được | Bộ dữ liệu nền | 1. BT mở danh mục quy tắc | • không có nút "Sửa"<br>• gọi trực tiếp lệnh đề nghị sửa quy tắc trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-43 — Đề nghị sửa quy tắc

Yêu cầu: `FR-MENU-RUL-006` · Use case: `UC-MENU-013` · Ưu tiên: P0 · Checklist: `CL-F-43`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4301` | `AC-MENU-43-1` | Thuận lợi | Đề nghị đổi tham số | • "BR-MENU-012" đang có tham số số ngày liên tiếp tối đa là 2 | 1. DDV đề nghị đổi thành 3 với lý do "Thịt lợn dùng nhiều nhất, giới hạn 2 gây cảnh báo ở mọi thực đơn" | • một đề nghị "PENDING" được tạo ghi "2 → 3"<br>• bộ kiểm vẫn dùng giá trị 2 | Chờ E2-Q11 |
| `TC-MENU-4302` | `AC-MENU-43-2` | Thuận lợi | Đề nghị được duyệt | • đề nghị "2 → 3" của "BR-MENU-012" ở trạng thái "PENDING", do DDV gửi | 1. ND1 duyệt đề nghị | • tham số của "BR-MENU-012" là 3<br>• thực đơn "DRAFT" được kiểm bằng giá trị 3 ở lần kiểm kế tiếp | Sẵn sàng |
| `TC-MENU-4303` | `AC-MENU-43-3` | Lỗi | Điểm phạt ngoài khoảng | Bộ dữ liệu nền | 1. DDV đề nghị đặt điểm phạt 5 cho một quy tắc mềm | • hệ thống trả lỗi "ERR-MENU-422-16" | Sẵn sàng |
| `TC-MENU-4304` | `AC-MENU-43-4` | Lỗi | Thiếu lý do | Bộ dữ liệu nền | 1. DDV đề nghị tắt một quy tắc mà không nhập lý do | • hệ thống trả lỗi "ERR-SYS-422-01" | Sẵn sàng |
| `TC-MENU-4305` | `AC-MENU-43-5` | Biên | Quy tắc mới chặt hơn làm thực đơn đã kiểm rơi về nháp | • một thực đơn "CHECKED" đạt khi quy tắc "BR-MENU-010" đang tắt | 1. đề nghị bật "BR-MENU-010" được duyệt và thực đơn được kiểm lại<br>2. thực đơn có 2 món chính cùng nhóm nguyên liệu trong một ngày | • thực đơn về trạng thái "DRAFT" và hiện nhãn "cần kiểm lại" trong danh sách | Sẵn sàng |
| `TC-MENU-4306` | `AC-MENU-43-6` | Biên | Thực đơn đã gửi duyệt giữ kết quả cũ | • một thực đơn "PENDING" có kết quả kiểm K | 1. một đề nghị sửa quy tắc được duyệt | • kết quả kiểm của thực đơn đó vẫn là K | Chờ E2-Q11 |

## US-MENU-44 — Gửi duyệt thực đơn

Yêu cầu: `FR-MENU-APV-001`, `006` · Use case: `UC-MENU-009` · Ưu tiên: P0 · Checklist: `CL-F-44`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4401` | `AC-MENU-44-1` | Thuận lợi | Gửi duyệt thực đơn đã kiểm | • thực đơn ở trạng thái "CHECKED" với điểm 91 | 1. DDV chọn "Gửi duyệt" | • bộ kiểm chạy lại ngay trước khi chuyển trạng thái<br>• thực đơn chuyển "PENDING", hiện "chờ duyệt 0/1" và ở chế độ chỉ đọc<br>• mỗi tài khoản có quyền "menu.menu.approve" nhận 1 thông báo | Chờ E2-Q6 |
| `TC-MENU-4402` | `AC-MENU-44-2` | Lỗi | Còn ô trống và thiếu món mặc định | • T7 còn 6 ô trống và T6, T7 chưa có món mặc định | 1. DDV chọn "Gửi duyệt" | • hệ thống trả lỗi "ERR-MENU-422-17" liệt kê các ô trống và các ngày thiếu món mặc định<br>• thực đơn giữ trạng thái "DRAFT" | Sẵn sàng |
| `TC-MENU-4403` | `AC-MENU-44-3` | Lỗi | Còn vi phạm bắt buộc | • thực đơn đủ món nhưng có 1 vi phạm "BR-MENU-034" | 1. DDV chọn "Gửi duyệt" | • hệ thống trả lỗi "ERR-MENU-422-18" nêu số vi phạm là 1 | Sẵn sàng |
| `TC-MENU-4404` | `AC-MENU-44-4` | Lỗi | Cảnh báo mức nặng chưa có lý do | • thực đơn có 2 cảnh báo điểm phạt 3, mới ghi lý do cho 1 | 1. DDV chọn "Gửi duyệt" | • hệ thống trả lỗi "ERR-MENU-422-19" nêu còn 1 cảnh báo thiếu lý do | Sẵn sàng |
| `TC-MENU-4405` | `AC-MENU-44-5` | Biên | Món bị ngừng dùng sau khi thực đơn đã kiểm | • thực đơn "CHECKED" có món "Mực xào"<br>• "Mực xào" vừa bị ngừng dùng | 1. DDV chọn "Gửi duyệt" | • hệ thống trả lỗi "ERR-MENU-422-17" nêu món "Mực xào" không còn dùng được | Sẵn sàng |
| `TC-MENU-4406` | `AC-MENU-44-6` | Biên | Điểm dưới ngưỡng cần hai người duyệt | • tham số "QUY_TAC_DIEM_TOI_THIEU" là 80 và thực đơn có điểm 74 | 1. DDV gửi duyệt thành công | • thực đơn hiện "chờ duyệt 0/2" | Sẵn sàng |
| `TC-MENU-4407` | `AC-MENU-44-7` | Biên | Bộ kiểm đăng ký thêm báo không đạt | • một bộ kiểm khác đã đăng ký vào bước gửi duyệt và trả kết quả không đạt | 1. DDV chọn "Gửi duyệt" | • thực đơn giữ trạng thái cũ và hiện thông báo của bộ kiểm đó | Sẵn sàng |

## US-MENU-45 — Duyệt hoặc trả lại thực đơn

Yêu cầu: `FR-MENU-APV-002` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-45`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4501` | `AC-MENU-45-1` | Thuận lợi | Duyệt thực đơn cần một người duyệt | • thực đơn "PENDING" do DDV tạo, cần 1 người duyệt | 1. ND1 duyệt | • thực đơn chuyển "APPROVED"<br>• kết quả kiểm quy tắc và phiên bản công thức đã gắn bị đóng băng<br>• DDV nhận thông báo | Chờ O-06 |
| `TC-MENU-4502` | `AC-MENU-45-2` | Thuận lợi | Màn hình duyệt hiện đủ thông tin | Bộ dữ liệu nền | 1. ND1 mở thực đơn chờ duyệt | • màn hình hiện lưới món theo ngày, món mặc định, điểm quy tắc<br>• mỗi cảnh báo điểm phạt 3 hiện kèm lý do chấp nhận của người dựng | Sẵn sàng |
| `TC-MENU-4503` | `AC-MENU-45-3` | Lỗi | Người tạo tự duyệt | • thực đơn "PENDING" do ND1 tạo | 1. ND1 duyệt | • hệ thống trả lỗi "ERR-SYS-403-01" | Sẵn sàng |
| `TC-MENU-4504` | `AC-MENU-45-4` | Lỗi | Trả lại thiếu lý do | Bộ dữ liệu nền | 1. ND1 chọn "Trả lại" và để trống lý do | • hệ thống trả lỗi "ERR-SYS-422-01" và thực đơn giữ "PENDING" | Sẵn sàng |
| `TC-MENU-4505` | `AC-MENU-45-5` | Biên | Trả lại có lý do | Bộ dữ liệu nền | 1. ND1 trả lại với lý do "Thứ Tư có 3 món chiên, đề nghị đổi" | • thực đơn về "DRAFT", DDV sửa được và nhận thông báo kèm lý do<br>• lần gửi duyệt sau bắt đầu vòng duyệt mới từ 0 | Sẵn sàng |
| `TC-MENU-4506` | `AC-MENU-45-6` | Biên | Công thức đổi sau khi thực đơn đã duyệt | • thực đơn "APPROVED" gắn công thức v1 của "Thịt kho trứng cút" | 1. công thức v2 của món đó được duyệt và có hiệu lực trong tuần của thực đơn | • thực đơn vẫn gắn v1 | Sẵn sàng |

## US-MENU-46 — Trang chờ duyệt

Yêu cầu: `FR-MENU-DISH-004`, `RCP-003`, `PRC-002`, `APV-002` · Use case: `UC-MENU-010` · Ưu tiên: P0 · Checklist: `CL-F-46`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4601` | `AC-MENU-46-1` | Thuận lợi | Xem theo loại | • có 3 món, 2 công thức, 2 giá bán, 3 đề nghị thay đổi, 2 thực đơn đang chờ duyệt | 1. ND1 mở trang "Chờ duyệt" | • trang hiện 12 mục nhóm theo 5 loại, mỗi bộ lọc loại kèm số đếm đúng | Chờ O-06, E2-Q7 |
| `TC-MENU-4602` | `AC-MENU-46-2` | Thuận lợi | Duyệt hàng loạt | • ND1 tích chọn 3 món, trong đó 1 món ND1 là người sửa cuối | 1. ND1 chọn "Duyệt mục đã chọn" | • 2 món chuyển "ACTIVE", 1 món giữ "PENDING"<br>• kết quả báo "2 thành công, 1 lỗi" kèm "ERR-SYS-403-01" cho món bị lỗi | Sẵn sàng |
| `TC-MENU-4603` | `AC-MENU-46-3` | Biên | Không có gì chờ duyệt | • không có mục nào chờ ND1 duyệt | 1. ND1 mở trang "Chờ duyệt" | • trang ghi "Không có nội dung chờ duyệt" | Sẵn sàng |
| `TC-MENU-4604` | `AC-MENU-46-4` | Biên | Mục đã được người khác xử lý | • ND1 và ND2 cùng mở một giá bán chờ duyệt<br>• ND2 đã duyệt trước | 1. ND1 chọn "Duyệt" | • hệ thống trả lỗi "ERR-SYS-409-02" và tải lại trạng thái hiện tại | Sẵn sàng |
| `TC-MENU-4605` | `AC-MENU-46-5` | Lỗi | Tài khoản không có quyền duyệt | Bộ dữ liệu nền | 1. DDV mở đường dẫn trang "Chờ duyệt" | • hệ thống trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |
| `TC-MENU-4606` | `AC-MENU-46-6` | Biên | Duyệt bằng quyền được uỷ đã hết hạn | • ND2 được ND1 uỷ quyền duyệt thực đơn đến hết hôm qua | 1. ND2 duyệt một thực đơn | • hệ thống trả lỗi "ERR-AUTH-403-02" | Sẵn sàng |

## US-MENU-47 — Thông báo duyệt

Yêu cầu: `FR-SYS-NTF-001` · Use case: `UC-MENU-009`, `010` · Ưu tiên: P0 · Checklist: `CL-F-47`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4701` | `AC-MENU-47-1` | Thuận lợi | Người duyệt nhận thông báo | Bộ dữ liệu nền | 1. DDV gửi duyệt một thực đơn | • mỗi tài khoản có quyền duyệt thực đơn có 1 thông báo trạng thái "mới"<br>• bấm thông báo mở thẳng màn hình chi tiết duyệt của thực đơn đó | Sẵn sàng |
| `TC-MENU-4702` | `AC-MENU-47-2` | Thuận lợi | Người tạo nhận kết quả trả lại | Bộ dữ liệu nền | 1. ND1 trả lại thực đơn với lý do "Thứ Tư có 3 món chiên" | • DDV có 1 thông báo chứa nguyên văn lý do, bấm vào mở thực đơn ở chế độ sửa | Sẵn sàng |
| `TC-MENU-4703` | `AC-MENU-47-3` | Biên | Gửi duyệt nhiều món một lần | Bộ dữ liệu nền | 1. DDV gửi duyệt 10 món trong một lần | • mỗi người duyệt nhận 1 thông báo gộp ghi "10 món chờ duyệt", không phải 10 thông báo | Sẵn sàng |
| `TC-MENU-4704` | `AC-MENU-47-4` | Lỗi | Người gửi không tự nhận thông báo chờ duyệt | • ND1 vừa có quyền tạo vừa có quyền duyệt | 1. ND1 gửi duyệt một món do mình tạo | • ND1 không nhận thông báo chờ duyệt cho món đó | Sẵn sàng |

## US-MENU-48 — Công bố thực đơn

Yêu cầu: `FR-MENU-APV-003` · Use case: `UC-MENU-011` · Ưu tiên: P0 · Checklist: `CL-F-48`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4801` | `AC-MENU-48-1` | Thuận lợi | Công bố | • thực đơn "APPROVED" có ngày phục vụ đầu tiên là D+5 | 1. DDV chọn "Công bố" | • thực đơn chuyển "PUBLISHED"<br>• BT thấy thực đơn trong danh sách<br>• tài khoản vai trò quản lý cơ sở và bếp trưởng nhận thông báo | Chờ E2-Q9 |
| `TC-MENU-4802` | `AC-MENU-48-2` | Lỗi | Ngày phục vụ đầu tiên là hôm nay | • thực đơn "APPROVED" có ngày phục vụ đầu tiên là hôm nay | 1. DDV chọn "Công bố" | • hệ thống trả lỗi "ERR-MENU-409-09" và thực đơn giữ "APPROVED" | Sẵn sàng |
| `TC-MENU-4803` | `AC-MENU-48-3` | Biên | Ngày phục vụ đầu tiên là ngày mai | • thực đơn "APPROVED" có ngày phục vụ đầu tiên là D+1 | 1. DDV chọn "Công bố" | • thực đơn chuyển "PUBLISHED" | Sẵn sàng |
| `TC-MENU-4804` | `AC-MENU-48-4` | Biên | Thực đơn chưa duyệt không có nút công bố | • thực đơn ở trạng thái "PENDING" | 1. DDV mở thực đơn | • không có nút "Công bố" | Sẵn sàng |

## US-MENU-49 — Thu hồi và sửa lại

Yêu cầu: `FR-MENU-APV-004`, `005` · Use case: `UC-MENU-011` · Ưu tiên: P0 · Checklist: `CL-F-49`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-4901` | `AC-MENU-49-1` | Thuận lợi | Thu hồi rồi sửa | • thực đơn ở trạng thái "PUBLISHED" | 1. DDV chọn "Thu hồi" với lý do "Nhà cung cấp báo hết cá trắm cả tuần"<br>2. DDV chọn "Sửa" | (sau bước 1) thực đơn chuyển "WITHDRAWN" và BT không còn thấy trong danh sách<br>(sau bước 2) thực đơn về "DRAFT" và sửa được | Chờ E2-Q8 |
| `TC-MENU-4902` | `AC-MENU-49-2` | Lỗi | Thu hồi thiếu lý do | Bộ dữ liệu nền | 1. DDV chọn "Thu hồi" với lý do 4 ký tự | • hệ thống trả lỗi "ERR-SYS-422-01" và thực đơn giữ "PUBLISHED" | Sẵn sàng |
| `TC-MENU-4903` | `AC-MENU-49-3` | Biên | Sửa lại phải qua đủ chu trình | • thực đơn vừa về "DRAFT" sau thu hồi | 1. DDV đổi 1 món | • thực đơn phải được kiểm, gửi duyệt, duyệt rồi mới công bố lại được | Sẵn sàng |
| `TC-MENU-4904` | `AC-MENU-49-4` | Biên | Kết quả kiểm tính lại theo giá trị hiện hành | • sau khi thực đơn được công bố, thuộc tính vị chua của một món trong thực đơn đã đổi thành "Có" | 1. DDV thu hồi, chọn "Sửa" và bộ kiểm chạy | • kết quả kiểm dùng thuộc tính mới của món đó | Sẵn sàng |
| `TC-MENU-4905` | `AC-MENU-49-5` | Biên | Thu hồi phát sự kiện cho phân hệ khác | Bộ dữ liệu nền | 1. DDV thu hồi thực đơn | • hệ thống phát sự kiện "thực đơn bị thu hồi" mang mã thực đơn và lý do | Sẵn sàng |

## US-MENU-50 — Hai người duyệt khi điểm thấp

Yêu cầu: `FR-MENU-RUL-007` · Use case: `UC-MENU-010` · Ưu tiên: P1 · Checklist: `CL-F-50`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-5001` | `AC-MENU-50-1` | Thuận lợi | Hai người duyệt lần lượt | • thực đơn "PENDING" có điểm 74, cần 2 người duyệt | 1. ND1 duyệt<br>2. ND2 duyệt | (sau bước 1) thực đơn vẫn "PENDING" và hiện "đã duyệt 1/2"<br>(sau bước 2) thực đơn chuyển "APPROVED" | Chờ O-06 |
| `TC-MENU-5002` | `AC-MENU-50-2` | Lỗi | Một người duyệt hai lần | • ND1 đã duyệt thực đơn cần 2 người duyệt | 1. ND1 duyệt lần nữa | • hệ thống trả lỗi "ERR-SYS-403-01" và thực đơn vẫn "đã duyệt 1/2" | Chờ O-06 |
| `TC-MENU-5003` | `AC-MENU-50-3` | Biên | Điểm đúng bằng ngưỡng | • tham số "QUY_TAC_DIEM_TOI_THIEU" là 80 và thực đơn có điểm 80 | 1. DDV gửi duyệt | • thực đơn cần 1 người duyệt | Sẵn sàng |
| `TC-MENU-5004` | `AC-MENU-50-4` | Biên | Người thứ hai trả lại | • ND1 đã duyệt thực đơn cần 2 người duyệt | 1. ND2 trả lại với lý do hợp lệ | • thực đơn về "DRAFT" và quyết định duyệt của ND1 không còn hiệu lực cho vòng sau | Chờ O-06 |

## US-MENU-51 — Sao chép thực đơn

Yêu cầu: `FR-MENU-MNU-005` · Use case: `UC-MENU-007` · Ưu tiên: P1 · Checklist: `CL-F-51`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-5101` | `AC-MENU-51-1` | Thuận lợi | Sao chép sang tuần mới | • thực đơn tuần 09/11 của "Suất 40.000đ" có đủ 42 ô | 1. DDV sao chép sang tuần 23/11 | • thực đơn mới ở trạng thái "DRAFT" với 42 ô giống nguồn<br>• mỗi ô gắn công thức hiệu lực tại ngày phục vụ mới<br>• món mặc định của từng ngày được sao chép | Sẵn sàng |
| `TC-MENU-5102` | `AC-MENU-51-2` | Lỗi | Tuần đích đã có thực đơn | • tuần 23/11 đã có thực đơn của "Suất 40.000đ" | 1. DDV sao chép sang tuần 23/11 | • hệ thống trả lỗi "ERR-MENU-409-06" | Sẵn sàng |
| `TC-MENU-5103` | `AC-MENU-51-3` | Biên | Thực đơn nguồn có món đã ngừng dùng | • thực đơn nguồn có "Mực xào" ở T3 và "Mực xào" đã "INACTIVE" | 1. DDV sao chép | • ô tương ứng của T3 để trống<br>• màn hình liệt kê "Mực xào" trong danh sách món bị bỏ | Sẵn sàng |
| `TC-MENU-5104` | `AC-MENU-51-4` | Biên | Thực đơn sao chép được kiểm ngay | Bộ dữ liệu nền | 1. DDV sao chép một thực đơn | • bộ kiểm chạy trên bản sao và bảng kiểm hiện kết quả theo quy tắc hiện hành | Sẵn sàng |

## US-MENU-52 — Lịch sử món đã dùng

Yêu cầu: `FR-MENU-MNU-006` · Use case: `UC-MENU-007` · Ưu tiên: P1 · Checklist: `CL-F-52`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-5201` | `AC-MENU-52-1` | Thuận lợi | Hiện ngày đã dùng | • "Cá kho" đã xuất hiện ở T4 11/11 trong thực đơn "PUBLISHED" của "Suất 40.000đ" | 1. DDV mở hộp chọn món chính cho tuần 16/11 của "Suất 40.000đ" | • dòng "Cá kho" ghi "đã dùng: T4 11/11" | Sẵn sàng |
| `TC-MENU-5202` | `AC-MENU-52-2` | Biên | Món chưa dùng trong 4 tuần | Bộ dữ liệu nền | 1. DDV mở hộp chọn món | • món không xuất hiện trong 4 tuần trước ghi "chưa dùng 4 tuần gần nhất" | Sẵn sàng |
| `TC-MENU-5203` | `AC-MENU-52-3` | Biên | Không tính loại suất khác | • "Cá kho" chỉ xuất hiện trong thực đơn của "Suất 35.000đ" | 1. DDV mở hộp chọn món cho "Suất 40.000đ" | • dòng "Cá kho" ghi "chưa dùng 4 tuần gần nhất" | Sẵn sàng |
| `TC-MENU-5204` | `AC-MENU-52-4` | Lỗi | Không tính thực đơn nháp và đã huỷ | • "Cá kho" chỉ xuất hiện trong một thực đơn "DRAFT" của tuần trước | 1. DDV mở hộp chọn món | • dòng "Cá kho" ghi "chưa dùng 4 tuần gần nhất" | Sẵn sàng |

## US-MENU-53 — Xuất PDF

Yêu cầu: `FR-MENU-MNU-008` · Use case: `UC-MENU-011` · Ưu tiên: P1 · Checklist: `CL-F-53`

| TC ID | AC | Loại | Tên | Tiền điều kiện | Bước thực hiện | Kết quả mong đợi | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-5301` | `AC-MENU-53-1` | Thuận lợi | Xuất thực đơn đã công bố | • thực đơn "PUBLISHED" 6 ngày | 1. DDV chọn "Xuất PDF" | • tệp PDF có lưới 6 cột ngày × 7 dòng vị trí với tên món, đánh dấu món mặc định<br>• tiêu đề ghi tên loại suất và khoảng ngày của tuần | Sẵn sàng |
| `TC-MENU-5302` | `AC-MENU-53-2` | Biên | Xuất thực đơn chưa công bố | • thực đơn ở trạng thái "DRAFT" | 1. DDV chọn "Xuất PDF" | • mỗi trang của tệp có dòng "BẢN NHÁP — CHƯA CÔNG BỐ" | Sẵn sàng |
| `TC-MENU-5303` | `AC-MENU-53-3` | Lỗi | Vai trò chỉ xem xuất thực đơn chưa công bố | Bộ dữ liệu nền | 1. BT gọi lệnh xuất PDF của thực đơn "DRAFT" | • hệ thống trả lỗi "ERR-SYS-404-01" | Sẵn sàng |
| `TC-MENU-5304` | `AC-MENU-53-4` | Biên | Tệp không chứa giá và cost | Bộ dữ liệu nền | 1. DDV xuất PDF một thực đơn | • tệp không có giá bán, giá nhập hay cost | Sẵn sàng |


---

# Phần B — Test case bổ sung

## B.1 Phân quyền và bảo mật

| TC ID | Checklist | Tiền điều kiện / dữ liệu | Bước | Kết quả mong đợi | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-S-01` | `CL-S-01` | 6 tài khoản, mỗi tài khoản một vai trò nội bộ: `GIAM_DOC`, `DINH_DUONG_VIEN`, `QL_CO_SO`, `BEP_TRUONG`, `KT_MUA_HANG`, `KT_DOANH_THU` | Với từng tài khoản, gọi 1 API đại diện cho từng quyền trong 12 quyền `menu.*` (72 lời gọi) | Kết quả cho phép / từ chối khớp 100% bảng mục 2.2 của SRS; lời gọi bị từ chối trả `ERR-AUTH-403-02` | SRS 2.2; `FR-AUTH-RBAC-001` |
| `TC-MENU-S-02` | `CL-S-02` | Đăng nhập BT | Mở lần lượt 16 màn hình của epic | Không màn hình nào có nút tạo, sửa, huỷ, gửi duyệt, duyệt, công bố, thu hồi, nhập | User-flow mục 2 |
| `TC-MENU-S-03` | `CL-S-03` | Đăng nhập BT; có mã của 1 nguyên liệu, 1 món, 1 công thức nháp, 1 thực đơn nháp | Gọi trực tiếp từng API ghi của epic (tạo, sửa, huỷ, gửi duyệt, duyệt, công bố, thu hồi, nhập) | Mọi lời gọi trả `ERR-AUTH-403-02`; không bản ghi nào thay đổi | `ERR-AUTH-403-02` |
| `TC-MENU-S-04` | `CL-S-04` | Có 1 thực đơn `DRAFT`, 1 `PENDING`, 1 `APPROVED`, 1 `WITHDRAWN`, 1 `PUBLISHED`; đăng nhập BT | (1) Mở danh sách thực đơn. (2) Mở đường dẫn chi tiết của từng thực đơn. (3) Gọi xuất PDF từng thực đơn | (1) Chỉ thấy thực đơn `PUBLISHED`. (2), (3) Bốn thực đơn còn lại trả `ERR-SYS-404-01` | `FR-MENU-MNU-007` |
| `TC-MENU-S-05` | `CL-S-05` | Đăng nhập BT, rồi QLCS | (1) Mở chi tiết món. (2) Gọi API giá hiệu lực và lịch sử giá. (3) Xuất PDF thực đơn đã công bố. (4) Xem bảng kiểm của thực đơn đã công bố | (1) Không có thẻ Giá bán. (2) `ERR-AUTH-403-02`. (3) Tệp không có giá. (4) Kết quả `BR-COST-012` không hiện số tiền | SRS 2.2; `FR-MENU-MNU-008` |
| `TC-MENU-S-06` | `CL-S-06` | ND1 có thêm quyền tạo; ND1 tạo và gửi duyệt 1 món, 1 công thức, 1 giá, 1 đề nghị thay đổi, 1 thực đơn | ND1 duyệt lần lượt 5 mục | Cả 5 lần trả `ERR-SYS-403-01`; 5 mục giữ trạng thái chờ duyệt | `BR-SEC-008` |
| `TC-MENU-S-07` | `CL-S-07` | DDV tạo 1 món nháp; ND1 (có quyền ghi) sửa mô tả món; DDV gửi duyệt | ND1 duyệt món | `ERR-SYS-403-01` | `BR-SEC-008` |
| `TC-MENU-S-08` | `CL-S-08` | Như `S-06`, thêm 2 món do DDV tạo đang chờ duyệt | ND1 tích chọn cả 3 món và duyệt hàng loạt | 2 món của DDV chuyển `ACTIVE`; món của ND1 giữ `PENDING` kèm `ERR-SYS-403-01` | `BR-SEC-008` |
| `TC-MENU-S-09` | `CL-S-09` | Thực đơn `PENDING` cần 2 người duyệt; ND1 đã duyệt | ND1 gọi lệnh duyệt lần nữa qua giao diện và qua API | Cả hai trả `ERR-SYS-403-01`; số quyết định duyệt vẫn là 1 | `BR-MNU-008` |
| `TC-MENU-S-10` | `CL-S-10` | ND1 uỷ quyền `menu.menu.approve` cho QLCS từ hôm nay đến D+2; có 1 thực đơn và 1 giá bán chờ duyệt | (1) QLCS duyệt thực đơn. (2) QLCS duyệt giá bán. (3) Chỉnh ngày hệ thống sang D+3, QLCS duyệt 1 thực đơn khác | (1) Thành công; quyết định ghi kèm mã uỷ quyền. (2) `ERR-AUTH-403-02` (uỷ quyền không gồm quyền duyệt giá). (3) `ERR-AUTH-403-02` | `FR-AUTH-RBAC-003` |
| `TC-MENU-S-11` | `CL-S-11` | QLCS được uỷ quyền duyệt món và có quyền ghi; QLCS sửa 1 món đang chờ duyệt | QLCS duyệt món đó | `ERR-SYS-403-01` | `BR-SEC-008` |
| `TC-MENU-S-12` | `CL-S-12` | Nhật ký trống cho các bản ghi dùng trong test | Thực hiện mỗi hành động 1 lần: tạo, sửa, ngừng dùng nguyên liệu; tạo, gửi duyệt, duyệt, trả lại món; tạo phiên bản công thức; đặt và duyệt giá; tạo, xếp món, gửi duyệt, duyệt, công bố, thu hồi, huỷ thực đơn; đề nghị và duyệt sửa quy tắc | Mỗi hành động có đúng 1 bản ghi nhật ký với: người thực hiện, thời điểm, thực thể, mã bản ghi, hành động, giá trị cũ → mới của từng trường đổi, lý do (khi bắt buộc), mã yêu cầu | `FR-SYS-AUD-001` |
| `TC-MENU-S-13` | `CL-S-13` | Tài khoản dịch vụ `svc-agent-noi-bo` thay mặt DDV | Gọi kiểm thực đơn chưa lưu; rồi (khi có ở R5) lưu một thực đơn nháp | Lượt chạy ghi cả tài khoản dịch vụ và DDV; lệnh kiểm chưa lưu không sinh bản ghi nhật ký thay đổi | `FR-SYS-AUD-001`; `BR-SEC-009` |
| `TC-MENU-S-14` | `CL-S-14` | Các bản ghi ở trạng thái phù hợp | Thực hiện không có lý do, rồi với lý do 9 ký tự: trả lại, thu hồi, huỷ thực đơn, tạo phiên bản công thức, đề nghị sửa món, đề nghị sửa quy tắc, ngừng dùng nguyên liệu, ngừng dùng món | Mọi lần trả `ERR-SYS-422-01`; không bản ghi nào đổi | `BR-AUD-001` |
| `TC-MENU-S-15` | `CL-S-15` | Danh sách API của epic; tài khoản `QUAN_TRI` | Rà danh sách API và giao diện tìm lệnh xoá hẳn; gọi phương thức `DELETE` lên từng tài nguyên | Không có lệnh xoá cứng; bản ghi huỷ còn trong cơ sở dữ liệu với `cancelled_at` | `FR-SYS-AUD-004` |
| `TC-MENU-S-16` | `CL-S-16` | Đăng nhập DDV | Nhập `<script>alert(1)</script>` và `"><img src=x onerror=alert(1)>` vào: tên và mô tả món, tên nguyên liệu, lý do, ghi chú cặp kỵ, lý do chấp nhận cảnh báo. Mở lại ở danh sách, chi tiết, màn duyệt, thông báo, PDF | Chuỗi hiển thị nguyên văn dạng văn bản ở mọi nơi; không có mã nào chạy | `NFR-SEC-004` |
| `TC-MENU-S-17` | `CL-S-17` | Đăng nhập DDV | Gửi `' OR '1'='1`, `; DROP TABLE dishes--`, ký tự `%` và `_` vào tham số tìm tên, lọc, sắp xếp, `page`, `pageSize` của danh sách nguyên liệu, món, thực đơn | Không lỗi 500; kết quả là danh sách rỗng hoặc lỗi 422; dữ liệu nguyên vẹn | `NFR-SEC-004` |
| `TC-MENU-S-18` | `CL-S-18` | Đăng nhập DDV | Tải lên làm ảnh món: tệp PDF đổi đuôi `.jpg`; tệp `.exe` đổi đuôi `.png`; tệp tên `../../x.jpg`; tệp 10 MB + 1 byte | Ba tệp đầu: `ERR-SYS-415-01` hoặc tên được làm sạch và lưu ngoài thư mục gốc; tệp cuối: `ERR-SYS-413-01` | `FR-SYS-FILE-001` |
| `TC-MENU-S-19` | `CL-S-19` | Đăng nhập DDV | Nhập tệp `.xlsx`: có ô bắt đầu bằng `=HYPERLINK(...)` ở cột tên; tệp nén lồng nhiều lớp; tệp hỏng cấu trúc | Ô công thức được đọc như văn bản, không được tính; hai tệp sau trả `ERR-MENU-422-20`; máy chủ không treo quá 30 giây | `FR-MENU-IMP-002` |
| `TC-MENU-S-20` | `CL-S-20` | BT có mã của 1 thực đơn nháp và 1 đề nghị thay đổi lấy từ tài khoản khác | Thay mã đó vào đường dẫn và vào thân yêu cầu của các API đọc | `ERR-SYS-404-01` hoặc `ERR-AUTH-403-02`; không lộ nội dung | `FR-AUTH-RBAC-001` |
| `TC-MENU-S-21` | `CL-S-21` | DDV đang soạn thực đơn, đã xếp 10 ô | Làm phiên hết hạn (thu hồi phiên), rồi xếp ô thứ 11 | Chuyển về đăng nhập với `ERR-AUTH-401-02`; sau đăng nhập quay lại đúng thực đơn; 10 ô đã lưu còn nguyên | `ERR-AUTH-401-02` |
| `TC-MENU-S-22` | `CL-S-22` | Tài khoản dịch vụ `svc-agent-dinh-duong-vien` | Gọi: tra cứu món đã duyệt; kiểm thực đơn chưa lưu; xem giá bán; mọi API ghi của epic | Hai lệnh đầu thành công; các lệnh còn lại `ERR-AUTH-403-02` | `BR-SEC-010` |

## B.2 Dữ liệu biên

Mỗi test case chạy lần lượt các giá trị trong cột "Giá trị → kết quả". "Nhận" = lưu được; "Từ chối" kèm mã lỗi.

| TC ID | Checklist | Trường | Giá trị → kết quả mong đợi | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-B-01` | `CL-B-01` | Tên nguyên liệu | Rỗng → từ chối · 1 ký tự → nhận · 120 ký tự → nhận · 121 ký tự → từ chối · toàn dấu cách → từ chối · "Thịt lợn (nạc vai) – loại 1" → nhận, hiển thị đúng | ERD 4.1 |
| `TC-MENU-B-02` | `CL-B-02` | Tên món | Rỗng → từ chối · 160 ký tự → nhận · 161 ký tự → từ chối | ERD 4.2 |
| `TC-MENU-B-03` | `CL-B-03` | So trùng tên (đã có "Cá kho") | "cá kho" → `ERR-MENU-409-01` · " Cá kho " → `ERR-MENU-409-01` · "Cá  kho" (2 dấu cách) → `ERR-MENU-409-01` · "Ca kho" → nhận · "Cá kho riềng" → nhận | `BR-CAT-001` |
| `TC-MENU-B-04` | `CL-B-04` | Hệ số quy đổi | 0 → `ERR-MENU-422-01` · −1 → `ERR-MENU-422-01` · 0,0001 → nhận · 99999999,9999 → nhận · "abc" → `ERR-MENU-422-01` · kg/g với 1000 → nhận, với 999 → `ERR-MENU-422-01` | `BR-CAT-002` |
| `TC-MENU-B-05` | `CL-B-05` | Tỷ lệ hao hụt (có xương/vỏ) | Trống → `ERR-MENU-422-02` · 0 → `ERR-MENU-422-02` · 0,01 → nhận · 99,99 → nhận · 100 → `ERR-MENU-422-02` · −5 → `ERR-MENU-422-02` · 12,345 → `ERR-MENU-422-02` (tối đa 2 chữ số thập phân, `BR-CAT-021`) | `BR-CAT-003` |
| `TC-MENU-B-06` | `CL-B-06` | Tháng mùa vụ | 0–5 → `ERR-MENU-422-03` · 1–12 → nhận · 4–13 → `ERR-MENU-422-03` · 10–2 → nhận (vắt qua cuối năm) · 6–6 → nhận | `FR-MENU-ING-006` |
| `TC-MENU-B-07` | `CL-B-07` | Định lượng (tối thiểu / chuẩn / tối đa) | 0/0/0 → `ERR-MENU-422-09` · 0,001/0,001/0,001 → nhận · 3/3/3 → nhận · 65/70/70 → nhận · 70/65/70 → `ERR-MENU-422-09` · 65/75/70 → `ERR-MENU-422-09` · 1,2345 → `ERR-MENU-422-09` (tối đa 3 chữ số thập phân, `BR-CAT-021`) · 9999999,999 → nhận | `BR-CAT-011` |
| `TC-MENU-B-08` | `CL-B-08` | Số dòng công thức | 0 dòng → `ERR-MENU-422-08` · 1 dòng là nguyên liệu chính → nhận · 30 dòng → nhận | `BR-CAT-010` |
| `TC-MENU-B-09` | `CL-B-09` | Ngày hiệu lực công thức | Hôm qua → `ERR-MENU-422-21` · hôm nay → nhận · D+1 → nhận · D+365 → nhận · trùng hoặc trước ngày hiệu lực của phiên bản `ACTIVE` khác cùng món → `ERR-MENU-422-21` | `BR-CAT-014`, `BR-CAT-022` |
| `TC-MENU-B-10` | `CL-B-10` | Giá bán | −100 → `ERR-MENU-422-11` · 0 → nhận · 50 → `ERR-MENU-422-11` · 100 → nhận · 22050 → `ERR-MENU-422-11` · 22000,5 → `ERR-MENU-422-11` · 999.999.900 → nhận | `BR-CAT-015` |
| `TC-MENU-B-11` | `CL-B-11` | Ngày hiệu lực giá | Hôm qua → `ERR-MENU-422-11` · hôm nay → `ERR-MENU-422-11` · D+1 → nhận · trùng ngày đã có → `ERR-MENU-409-04` | `BR-CAT-016` |
| `TC-MENU-B-12` | `CL-B-12` | Ngưỡng giá loại suất | 0 → `ERR-MENU-422-12` · 1 → nhận · 100.000.000 → nhận · 40050 → `ERR-MENU-422-12` (phải là bội số của 100 đồng) | `BR-CAT-017` |
| `TC-MENU-B-13` | `CL-B-13` | Món chính đưa ra / được chọn | 0/0 → `ERR-MENU-422-12` · 1/1 → nhận · 3/1 → nhận · 3/3 → nhận · 2/3 → `ERR-MENU-422-12` · 3/0 → `ERR-MENU-422-12` | `BR-CAT-017` |
| `TC-MENU-B-14` | `CL-B-14` | Số món phụ | 0 → nhận · 5 → nhận · 6 → `ERR-MENU-422-12` · −1 → `ERR-MENU-422-12` | `BR-CAT-017` |
| `TC-MENU-B-15` | `CL-B-15` | Loại suất không rau, không canh | Tạo thực đơn → lưới không có dòng rau, canh; xếp đủ món → không có kết quả `BR-MENU-004`; gửi duyệt được | `BR-MNU-002` |
| `TC-MENU-B-16` | `CL-B-16` | Ngày bắt đầu tuần | Chủ nhật → `ERR-MENU-422-13` · thứ Hai → nhận · thứ Ba → `ERR-MENU-422-13` · thứ Hai 30/11 (tuần vắt sang tháng 12) → nhận · thứ Hai 28/12 (vắt sang năm sau) → nhận, ngày hiển thị đúng | `FR-MENU-MNU-001` |
| `TC-MENU-B-17` | `CL-B-17` | Số ngày phục vụ | 0 ngày → `ERR-MENU-422-13` · 1 ngày → nhận · 6 ngày → nhận · 7 ngày (có Chủ nhật) → chờ [E2-Q3] | `FR-MENU-MNU-001` |
| `TC-MENU-B-18` | `CL-B-18` | Tổng giá suất (ngưỡng 40.000) | 39.900 → đạt · 40.000 → đạt · 40.100 → không đạt `BR-COST-012`, ghi vượt 100 | `FR-MENU-MNU-004`; chờ [E2-Q1] |
| `TC-MENU-B-19` | `CL-B-19` | Điểm quy tắc (ngưỡng 80) | Tổng phạt 0 → 100, 1 người duyệt · phạt 20 → 80, 1 người duyệt · phạt 21 → 79, 2 người duyệt · phạt 100 → 0 · phạt 130 → 0 | `BR-MNU-008` |
| `TC-MENU-B-20` | `CL-B-20` | Lý do | 9 ký tự → `ERR-SYS-422-01` · 10 ký tự → nhận · 500 ký tự → nhận · 501 ký tự → từ chối · 12 dấu cách → `ERR-SYS-422-01` | `BR-AUD-001` |
| `TC-MENU-B-21` | `CL-B-21` | Điểm phạt quy tắc | Quy tắc mềm: 0 → `ERR-MENU-422-16` · 1 → nhận · 3 → nhận · 4 → `ERR-MENU-422-16`. Quy tắc cứng: 0 → nhận · 1 → `ERR-MENU-422-16` | `BR-MNU-007` |
| `TC-MENU-B-22` | `CL-B-22` | Tham số quy tắc (kiểu đếm) | 0 → nhận · −1 → `ERR-MENU-422-16` · 2,5 → `ERR-MENU-422-16` (tham số đếm phải là số nguyên) · "abc" → `ERR-MENU-422-16` | `BR-MNU-007` |
| `TC-MENU-B-23` | `CL-B-23` | Ngày phục vụ đầu tiên khi công bố | Hôm qua → `ERR-MENU-409-09` · hôm nay → `ERR-MENU-409-09` · D+1 → công bố được | `BR-MNU-009` |
| `TC-MENU-B-24` | `CL-B-24` | Kích thước ảnh món | 0 byte → từ chối · 10 MB → nhận · 10 MB + 1 byte → `ERR-SYS-413-01` | `FR-SYS-FILE-001` |
| `TC-MENU-B-25` | `CL-B-25` | Số dòng tệp nhập | Chỉ có dòng tiêu đề → `ERR-MENU-422-20` · 1 dòng → nhận · 2.000 dòng → nhận · 2.001 dòng → `ERR-MENU-422-20` | `FR-MENU-IMP-002` |
| `TC-MENU-B-26` | `CL-B-26` | Phân trang danh sách món (45 món) | `page=0` → `ERR-SYS-422-03` · `page=3` → 5 món · `page=4` → danh sách rỗng, `total=45` · `pageSize=100` → nhận · `pageSize=101` → `ERR-SYS-422-03` | SRS nền tảng 3.3 |

## B.3 Toàn vẹn dữ liệu và đồng thời

| TC ID | Checklist | Tiền điều kiện / dữ liệu | Bước | Kết quả mong đợi | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-D-01` | `CL-D-01` | Hai phiên DDV và một tài khoản ghi khác, cùng mở một bản ghi | Lần lượt với món nháp, công thức nháp, loại suất nháp, thực đơn nháp: cả hai sửa, người thứ nhất lưu, người thứ hai lưu | Người thứ hai nhận `ERR-SYS-409-02`; dữ liệu là của người thứ nhất | Khoá phiên bản |
| `TC-MENU-D-02` | `CL-D-02` | 1 giá bán chờ duyệt; ND1 và ND2 cùng mở | Gửi hai lệnh duyệt cách nhau dưới 100 ms | Đúng 1 dòng quyết định; lệnh kia trả `ERR-SYS-409-02`; giá `APPROVED` | `FR-MENU-PRC-002` |
| `TC-MENU-D-03` | `CL-D-03` | Thực đơn cần 2 người duyệt, chưa ai duyệt | ND1 và ND2 gửi lệnh duyệt đồng thời | Đúng 2 dòng quyết định; thực đơn chuyển `APPROVED` đúng 1 lần; có đúng 1 thông báo kết quả cho DDV | `BR-MNU-008` |
| `TC-MENU-D-04` | `CL-D-04` | Đăng nhập DDV | Gửi lệnh tạo nguyên liệu 2 lần với cùng `Idempotency-Key`; rồi lần thứ ba với khoá khác và cùng nội dung | Hai lần đầu trả cùng 1 bản ghi; lần thứ ba trả `ERR-MENU-409-01` | SRS nền tảng 3.3 |
| `TC-MENU-D-05` | `CL-D-05` | Chưa có thực đơn tuần sau của "Suất 40.000đ" | Hai phiên gửi lệnh tạo thực đơn cho cùng loại suất và tuần, đồng thời | Đúng 1 thực đơn được tạo; lệnh kia trả `ERR-MENU-409-06` | `BR-MNU-001` |
| `TC-MENU-D-06` | `CL-D-06` | Món `ACTIVE` chưa có đề nghị | Hai phiên gửi đề nghị thay đổi cho cùng món, đồng thời | Đúng 1 đề nghị `PENDING`; lệnh kia bị từ chối | `FR-MENU-DISH-002` |
| `TC-MENU-D-07` | `CL-D-07` | Tệp món 100 dòng sạch | Bắt đầu nhập; làm lỗi ghi ở dòng 100 (tạo món trùng tên ngay trước khi nhập) | 0 món được tạo; `ERR-MENU-422-20` | `FR-MENU-IMP-003` |
| `TC-MENU-D-08` | `CL-D-08` | Bộ dữ liệu nền; thêm 5 món có 2 phiên bản công thức với ngày hiệu lực trong 60 ngày tới | Với mỗi món `ACTIVE` và mỗi ngày từ hôm nay đến D+60, gọi lấy công thức hiệu lực | Mỗi cặp (món, ngày) trả đúng 1 công thức hoặc `ERR-MENU-404-01`; không cặp nào trả 2 | `BR-CAT-014` |
| `TC-MENU-D-09` | `CL-D-09` | Món có v1 `ACTIVE` và v2 `ACTIVE` hiệu lực từ D+1 | (1) Chỉnh ngày sang D+1, chạy tác vụ chuyển phiên bản. (2) Chạy lại lần hai. (3) Lặp lại kịch bản nhưng bỏ chạy ở D+1, chạy ở D+2 | (1) v1 → `SUPERSEDED`. (2) Không đổi gì thêm. (3) v1 → `SUPERSEDED`; công thức hiệu lực của D+1 và D+2 đều là v2 | `FR-MENU-RCP-003` |
| `TC-MENU-D-10` | `CL-D-10` | Thực đơn `PENDING` gắn v1 của một món | Duyệt v2 của món đó với ngày hiệu lực trong tuần của thực đơn; duyệt thực đơn; công bố | Ở cả 3 thời điểm thực đơn vẫn gắn v1 | `FR-MENU-APV-002` |
| `TC-MENU-D-11` | `CL-D-11` | Thực đơn `PENDING` có kết quả kiểm K | Lần lượt: duyệt đề nghị đổi thuộc tính một món trong thực đơn; duyệt đề nghị sửa một quy tắc; duyệt giá mới cho một món | Sau cả 3 thay đổi, kết quả kiểm của thực đơn vẫn là K | `FR-MENU-RUL-006`; chờ [E2-Q11] |
| `TC-MENU-D-12` | `CL-D-12` | Đề nghị A đổi vị chua của món X đang `PENDING` | Bằng tài khoản `QUAN_TRI` hoặc đường nhập khác, đổi vị chua của món X; rồi ND1 mở đề nghị A | Đề nghị A ở trạng thái `STALE`; không duyệt được; DDV nhận thông báo | ERD 3.5 |
| `TC-MENU-D-13` | `CL-D-13` | Một thực đơn cố định có ít nhất 5 vi phạm | Chạy bộ kiểm 100 lần | 100 kết quả giống nhau về danh sách, thứ tự, chi tiết và điểm | `NFR-MENU-005` |
| `TC-MENU-D-14` | `CL-D-14` | Chỉnh được giờ hệ thống | (1) Lúc 23:59 giờ Việt Nam ngày N: đặt giá hiệu lực N+1 → nhận. (2) Lúc 00:01 ngày N+1: đặt giá hiệu lực N+1. (3) Lúc 06:59 và 07:01 giờ Việt Nam: lấy công thức hiệu lực "hôm nay" | (2) `ERR-MENU-422-11`. (3) Cả hai thời điểm trả cùng công thức của ngày theo giờ Việt Nam | SRS nền tảng 2.4 |
| `TC-MENU-D-15` | `CL-D-15` | Thực đơn nháp đã huỷ; nguyên liệu "X" đã huỷ | (1) Mở danh sách mặc định. (2) Tra cơ sở dữ liệu và nhật ký. (3) Tạo nguyên liệu mới tên "X" | (1) Không thấy bản ghi huỷ. (2) Bản ghi còn, có `cancelled_at` và lý do. (3) Tạo được | `BR-CAT-001` |
| `TC-MENU-D-16` | `CL-D-16` | Chuỗi tham chiếu: nguyên liệu → công thức `ACTIVE`; món → thực đơn `PUBLISHED` sắp phục vụ; nhóm → món; phương pháp ít dầu mỡ → món Healthy | Thử ngừng dùng hoặc huỷ từng bản ghi gốc; thử bỏ cờ ít dầu mỡ | Cả 4 lần bị chặn bằng `ERR-SYS-409-01` kèm danh sách bản ghi đang dùng | `BR-CAT-005`, `BR-CAT-020` |

## B.4 Hiệu năng

Chạy trên môi trường có cấu hình bằng môi trường vận hành thật (`NFR-PERF-001`). Cấu hình đó chưa xác định — chờ [O-04].

| TC ID | Checklist | Dữ liệu | Bước | Kết quả mong đợi | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-P-01` | `CL-P-01` | Thực đơn đã lưu 6 ngày × 7 món | Gọi kiểm thực đơn 50 lần liên tiếp | p95 ≤ 2 giây | `NFR-MENU-001` |
| `TC-MENU-P-02` | `CL-P-02` | Nội dung thực đơn 6 ngày × 7 món | Gửi 20 lời gọi kiểm thực đơn chưa lưu đồng thời, lặp 10 đợt | p95 ≤ 2 giây; 0 lỗi | `NFR-MENU-002` |
| `TC-MENU-P-03` | `CL-P-03` | Bộ dữ liệu lớn: thực đơn `PUBLISHED` của 52 tuần trước | Như `P-01` | p95 ≤ 2 giây và không cao hơn kết quả `P-01` quá 10% | `NFR-CAP-001` |
| `TC-MENU-P-04` | `CL-P-04` | Tệp món 2.000 dòng sạch | Kiểm tệp | Hoàn tất ≤ 30 giây; giao diện chuyển chạy nền sau 5 giây và báo tiến độ | `NFR-MENU-003` |
| `TC-MENU-P-05` | `CL-P-05` | 2.000 món, 1.000 nguyên liệu | Gọi danh sách món và nguyên liệu, có và không có bộ lọc, 100 lần mỗi loại | p95 ≤ 300 ms | `NFR-MENU-004` |
| `TC-MENU-P-06` | `CL-P-06` | 500 món chính `ACTIVE`; thực đơn 4 tuần trước | Mở hộp chọn món chính 100 lần | p95 ≤ 300 ms, có đủ thông tin lịch sử 4 tuần | `FR-MENU-MNU-006` |
| `TC-MENU-P-07` | `CL-P-07` | 200 mục chờ duyệt thuộc 5 loại | Mở trang chờ duyệt 100 lần | p95 ≤ 300 ms | `NFR-PERF-001` |
| `TC-MENU-P-08` | `CL-P-08` | 100 món chờ duyệt có công thức `ACTIVE` | Duyệt hàng loạt 100 món | Hoàn tất ≤ 5 giây; 100 món `ACTIVE`; 100 dòng quyết định | Chỉ tiêu là đề xuất |
| `TC-MENU-P-09` | `CL-P-09` | Thực đơn 6 ngày đã công bố | Xuất PDF 20 lần | Mỗi lần ≤ 5 giây | Chỉ tiêu là đề xuất |

## B.5 Tích hợp với phân hệ khác

| TC ID | Checklist | Tiền điều kiện / dữ liệu | Bước | Kết quả mong đợi | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-I-01` | `CL-I-01` | 2 tài khoản có quyền duyệt món; ND1 có thêm quyền tạo | (1) DDV gửi duyệt 10 món một lần. (2) ND1 gửi duyệt 1 món do mình tạo. (3) ND2 trả lại 1 món của DDV | (1) ND1 và ND2 mỗi người 1 thông báo ghi "10 món". (2) Chỉ ND2 nhận thông báo. (3) DDV nhận 1 thông báo có lý do, liên kết mở đúng món | `BR-MNU-010` |
| `TC-MENU-I-02` | `CL-I-02` | Tham số `QUY_TAC_DIEM_TOI_THIEU` = 80; thực đơn A điểm 85 đang `PENDING` (cần 1 người); thực đơn B điểm 85 đang `CHECKED` | Đổi tham số thành 90 (có duyệt); gửi duyệt B | A vẫn cần 1 người duyệt; B cần 2 người duyệt | `FR-SYS-PRM-001` |
| `TC-MENU-I-03` | `CL-I-03` | — | Chạy `TC-MENU-S-10` | Như `TC-MENU-S-10` | `FR-AUTH-RBAC-003` |
| `TC-MENU-I-04` | `CL-I-04` | Có món ở cả 4 trạng thái; món `ACTIVE` có công thức ở cả 4 trạng thái | Gọi dịch vụ tra cứu món và công thức đã duyệt | Chỉ trả món `ACTIVE` và công thức `ACTIVE` hiệu lực theo ngày yêu cầu | SRS 2.1 |
| `TC-MENU-I-05` | `CL-I-05` | Có thực đơn ở cả 6 trạng thái | (1) Gọi dịch vụ tra cứu thực đơn đã công bố. (2) Thu hồi thực đơn `PUBLISHED`, gọi lại ngay | (1) Chỉ trả thực đơn `PUBLISHED`. (2) Thực đơn vừa thu hồi không còn trong kết quả | SRS 2.1 |
| `TC-MENU-I-06` | `CL-I-06` | 5 thực đơn đã lưu có vi phạm khác nhau | Với mỗi thực đơn: lấy kết quả kiểm đã lưu; gửi cùng nội dung qua lệnh kiểm chưa lưu bằng tài khoản dịch vụ | 5 cặp kết quả giống hệt nhau | `FR-MENU-RUL-002` |
| `TC-MENU-I-07` | `CL-I-07` | Một bộ nghe sự kiện kiểm thử đã đăng ký | Thu hồi 1 thực đơn với lý do hợp lệ | Bộ nghe nhận đúng 1 sự kiện "thực đơn bị thu hồi" mang mã thực đơn và lý do | `FR-MENU-APV-004` |
| `TC-MENU-I-08` | `CL-I-08` | Thực đơn `CHECKED`; một bộ kiểm giả luôn trả "không đạt" | (1) Đăng ký bộ kiểm giả, gửi duyệt. (2) Gỡ bộ kiểm giả, gửi duyệt | (1) Thực đơn giữ `CHECKED`, hiện thông báo của bộ kiểm giả. (2) Thực đơn chuyển `PENDING`. Mã của phân hệ MENU không đổi giữa hai lần | `FR-MENU-APV-006` |
| `TC-MENU-I-09` | `CL-I-09` | Món có ảnh | Lấy liên kết ảnh; mở ngay; mở lại sau 16 phút; mở bằng tài khoản không đăng nhập | Lần đầu mở được; sau 16 phút liên kết hết hạn; ảnh không truy cập được nếu không có chữ ký hợp lệ | `FR-SYS-FILE-001` |

## B.6 Nhập bảng tính — theo cột

Mỗi test case dùng một tệp chứa đúng các lỗi nêu ở cột "Dữ liệu", mỗi lỗi một dòng, cùng ít nhất 3 dòng hợp lệ. Kết quả chung: `ERR-MENU-422-20`, nút Nhập bị khoá, 0 bản ghi được tạo, trừ khi ghi khác.

| TC ID | Checklist | Loại tệp | Dữ liệu | Kết quả mong đợi riêng | Tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TC-MENU-X-01` | `CL-X-01` | Món | 4 tệp: thiếu cột "Vai trò"; thừa cột lạ; đổi thứ tự 2 cột; đổi tên cột "Tên món" thành "Tên" | Thiếu cột, đổi tên cột: báo sai mẫu, nêu cột. Thừa cột: tệp được nhận, cột lạ bị bỏ qua kèm cảnh báo nêu tên cột. Đổi thứ tự: tệp được nhận (`BR-CAT-023` a, b) | `FR-MENU-IMP-002` |
| `TC-MENU-X-02` | `CL-X-02` | Nguyên liệu | Dòng trống giữa tệp; tên có dấu cách đầu cuối; hệ số "1000" ở dạng văn bản; hao hụt "12,5" và "12.5" | Tệp không có lỗi, nút Nhập bật: dòng trống bị bỏ qua; dấu cách thừa được cắt; "1000" dạng văn bản đọc thành 1000; "12,5" và "12.5" đều đọc thành 12,5 (`BR-CAT-023` c–f) | `FR-MENU-IMP-002` |
| `TC-MENU-X-03` | `CL-X-03` | Món | Vai trò "Món mặn"; kết cấu "Giòn"; nhóm cost "Trung bình" | Mỗi dòng báo lỗi tại đúng cột, kèm danh sách giá trị hợp lệ | `FR-MENU-IMP-002` |
| `TC-MENU-X-04` | `CL-X-04` | Nguyên liệu | 2 dòng cùng tên; 1 dòng trùng nguyên liệu đã có; 1 dòng nhóm "Hải sản" không tồn tại | Cả 2 dòng trùng nhau bị báo; dòng trùng hệ thống báo `ERR-MENU-409-01`; dòng nhóm lạ báo "không tìm thấy nhóm" | `BR-CAT-001` |
| `TC-MENU-X-05` | `CL-X-05` | Nguyên liệu | kg/g với hệ số 100; có xương/vỏ không có hao hụt | Báo `ERR-MENU-422-01`, `ERR-MENU-422-02` tại đúng dòng | `BR-CAT-002`, `003` |
| `TC-MENU-X-06` | `CL-X-06` | Món | Tên trùng; nhóm không tồn tại; phương pháp không tồn tại; Healthy với "Chiên"; món gốc không tồn tại; món gốc khác vai trò | Báo lần lượt `ERR-MENU-409-01`, "không tìm thấy nhóm", "không tìm thấy phương pháp", `ERR-MENU-422-04`, "không tìm thấy món gốc", `ERR-MENU-422-05` | `BR-CAT-006`, `007` |
| `TC-MENU-X-07` | `CL-X-07` | Món | Dòng 3 có món gốc là món ở dòng 8 của cùng tệp | Tệp được nhận: món ở dòng 3 được gắn đúng món gốc ở dòng 8 (`BR-CAT-023` g) | `BR-CAT-007` |
| `TC-MENU-X-08` | `CL-X-08` | Công thức | Món không tồn tại; nguyên liệu không tồn tại; nguyên liệu `INACTIVE` | Báo "không tìm thấy món", "không tìm thấy nguyên liệu", `ERR-MENU-422-08` | `BR-CAT-010` |
| `TC-MENU-X-09` | `CL-X-09` | Công thức | Món A không có dòng nguyên liệu chính; món B lặp "Cà chua"; món C có tối thiểu 70, chuẩn 65; món D (nhóm Cá) có nguyên liệu chính nhóm Rau | Mọi dòng của A và B báo `ERR-MENU-422-08`; dòng sai của C báo `ERR-MENU-422-09`; mọi dòng của D báo `ERR-MENU-422-10` | `BR-CAT-010` → `012` |
| `TC-MENU-X-10` | `CL-X-10` | Công thức | Các dòng của món A nằm ở dòng 2, 3 và 15 | Tệp được nhận: 3 dòng được gộp thành một công thức của món A (`BR-CAT-023` g) | `FR-MENU-IMP-002` |
| `TC-MENU-X-11` | `CL-X-11` | Giá bán | Món không tồn tại; giá 22050; ngày hiệu lực hôm nay; trùng ngày hiệu lực đã có | Báo "không tìm thấy món", `ERR-MENU-422-11`, `ERR-MENU-422-11`, `ERR-MENU-409-04` | `BR-CAT-015`, `016` |
| `TC-MENU-X-12` | `CL-X-12` | Cả 4 loại | 4 tệp sạch, nhập theo thứ tự nguyên liệu → món → công thức → giá | Nguyên liệu `ACTIVE`; món `DRAFT`; công thức `DRAFT`; giá `PENDING`. Không bản ghi nào xuất hiện trong hộp chọn món của thực đơn | `BR-CAT-019` |
| `TC-MENU-X-13` | `CL-X-13` | Món | Nhập một tệp sạch; kiểm lại chính tệp đó | Lần hai: mọi dòng báo `ERR-MENU-409-01` | `BR-CAT-001` |
| `TC-MENU-X-14` | `CL-X-14` | Món | Tệp `.xls`; `.csv`; `.xlsx` có 2 trang tính; `.xlsx` có mật khẩu | `.xls`, `.csv`: `ERR-SYS-415-01`. Hai trang tính: đọc trang có tên đúng mẫu, bỏ qua trang còn lại kèm cảnh báo (`BR-CAT-023` h). Có mật khẩu: `ERR-MENU-422-20` | `FR-MENU-IMP-002` |

---

## Tổng hợp

| Phần | Nhóm | Số test case | Ghi chú |
| :--- | :--- | :---: | :--- |
| A | Chức năng (từ tiêu chí nghiệm thu) | 239 | 65 thuận lợi · 78 lỗi · 96 biên; 209 sẵn sàng, 30 chờ điểm mở |
| B | Phân quyền và bảo mật | 22 | |
| B | Dữ liệu biên | 26 | |
| B | Toàn vẹn dữ liệu và đồng thời | 16 | |
| B | Hiệu năng | 9 | |
| B | Tích hợp | 9 | |
| B | Nhập bảng tính | 14 | |
| | **Cộng** | **335** | 11 chỗ SRS chưa quy định ở phần B đã được đưa vào SRS v0.3.0 |

## Độ phủ quy tắc và mã lỗi

Theo yêu cầu của skill: mọi mã `ERR` và `BR` phải có test case.

- **Mã lỗi**: cả 33 mã `ERR-MENU` của SRS v0.3.0 xuất hiện trong ít nhất một test case (đã soát bằng script).
- **Quy tắc dữ liệu và vòng đời** (`BR-CAT`, `BR-MNU`): bảng dưới, 33 trên 33 quy tắc.
- **Quy tắc xây thực đơn** (`BR-MENU`, `BR-COST`): mới có test case cho `BR-MENU-001`, `012`, `013`, `034` và `BR-COST-012` ở mức khung; phần còn lại chờ DL-01.

| Quy tắc | Tên | Test case |
| :--- | :--- | :--- |
| `BR-CAT-001` | Tên không trùng | `TC-MENU-0103`, `TC-MENU-0702`, `TC-MENU-B-03` |
| `BR-CAT-002` | Hệ số quy đổi | `TC-MENU-0104`, `TC-MENU-B-04` |
| `BR-CAT-003` | Hao hụt bắt buộc | `TC-MENU-0105`, `TC-MENU-B-05` |
| `BR-CAT-004` | Khoá đơn vị khi đang dùng | `TC-MENU-0106` |
| `BR-CAT-005` | Không huỷ khi đang dùng | `TC-MENU-0202`, `TC-MENU-0403`, `TC-MENU-2802`, `TC-MENU-D-16` |
| `BR-CAT-006` | Healthy cần phương pháp ít dầu mỡ | `TC-MENU-0703` |
| `BR-CAT-007` | Món gốc một cấp | `TC-MENU-0704`, `TC-MENU-0705` |
| `BR-CAT-008` | Thuộc tính ảnh hưởng quy tắc | `TC-MENU-2601`, `TC-MENU-2602` |
| `BR-CAT-009` | Món hoạt động cần công thức | `TC-MENU-1002`, `TC-MENU-1102`, `TC-MENU-1104` |
| `BR-CAT-010` | Cấu trúc công thức | `TC-MENU-1402`, `TC-MENU-1403`, `TC-MENU-B-08` |
| `BR-CAT-011` | Khoảng định lượng | `TC-MENU-1404`, `TC-MENU-1406`, `TC-MENU-B-07` |
| `BR-CAT-012` | Nhóm nguyên liệu chính khớp món | `TC-MENU-1405`, `TC-MENU-1407` |
| `BR-CAT-013` | Công thức đã duyệt là bất biến | `TC-MENU-1604`, `TC-MENU-1701` |
| `BR-CAT-014` | Một công thức hiệu lực mỗi ngày | `TC-MENU-1602`, `TC-MENU-1801`, `TC-MENU-1802`, `TC-MENU-D-08` |
| `BR-CAT-015` | Giá bán hợp lệ | `TC-MENU-2002`, `TC-MENU-2005`, `TC-MENU-B-10` |
| `BR-CAT-016` | Giá đã hiệu lực là bất biến | `TC-MENU-2003`, `TC-MENU-2104`, `TC-MENU-B-11` |
| `BR-CAT-017` | Cấu hình loại suất | `TC-MENU-2302`, `TC-MENU-2303`, `TC-MENU-B-13`, `TC-MENU-B-14` |
| `BR-CAT-018` | Khoá cơ cấu loại suất | `TC-MENU-2402`, `TC-MENU-2403` |
| `BR-CAT-019` | Nhập không bỏ qua duyệt | `TC-MENU-1304`, `TC-MENU-X-12` |
| `BR-CAT-020` | Giữ cờ ít dầu mỡ khi còn món Healthy dùng | `TC-MENU-0603`, `TC-MENU-D-16` |
| `BR-CAT-021` | Độ chính xác của số | `TC-MENU-B-04`, `TC-MENU-B-05`, `TC-MENU-B-07` |
| `BR-CAT-022` | Ngày hiệu lực của công thức | `TC-MENU-B-09` |
| `BR-CAT-023` | Quy ước đọc tệp nhập | `TC-MENU-X-01`, `TC-MENU-X-02`, `TC-MENU-X-07`, `TC-MENU-X-10`, `TC-MENU-X-14` |
| `BR-MNU-001` | Một thực đơn mỗi loại suất mỗi tuần | `TC-MENU-3103`, `TC-MENU-3105`, `TC-MENU-D-05` |
| `BR-MNU-002` | Số ô theo loại suất | `TC-MENU-3101`, `TC-MENU-3202` |
| `BR-MNU-003` | Một món một lần mỗi ngày | `TC-MENU-3205` |
| `BR-MNU-004` | Món mặc định | `TC-MENU-3302` |
| `BR-MNU-005` | Điều kiện gửi duyệt | `TC-MENU-4402`, `TC-MENU-4403`, `TC-MENU-4405` |
| `BR-MNU-006` | Lý do cho vi phạm mềm–nặng | `TC-MENU-4002`, `TC-MENU-4404` |
| `BR-MNU-007` | Giới hạn sửa quy tắc | `TC-MENU-4303`, `TC-MENU-B-21` |
| `BR-MNU-008` | Hai người duyệt khi điểm thấp | `TC-MENU-4406`, `TC-MENU-5001`, `TC-MENU-5002`, `TC-MENU-5003`, `TC-MENU-5004`, `TC-MENU-S-09`, `TC-MENU-D-03` |
| `BR-MNU-009` | Công bố không quá muộn | `TC-MENU-4802`, `TC-MENU-4803`, `TC-MENU-B-23` |
| `BR-MNU-010` | Thông báo duyệt | `TC-MENU-4703`, `TC-MENU-4704`, `TC-MENU-I-01` |

## Chỗ SRS chưa nêu, phát hiện khi viết test case

Khi viết phần B có 11 chỗ SRS v0.2.0 chưa quy định. **Cả 11 chỗ đã được đưa vào SRS epic v0.3.0 (mục 4.4) và SRS nền tảng v0.1.1 ngày 11/11/2026**; kết quả mong đợi của các test case liên quan đã được điền theo đó. Cách xử lý là đề xuất của BA, chưa có người nghiệp vụ duyệt. Bảng dưới giữ lại để đối chiếu.

| # | Câu hỏi | Test case |
| :--- | :--- | :--- |
| 1 | Số có nhiều chữ số thập phân hơn cột lưu được (hao hụt 12,345; định lượng 1,2345): làm tròn hay từ chối? | `TC-MENU-B-05`, `B-07` |
| 2 | Ngày hiệu lực của công thức có được ở quá khứ không? | `TC-MENU-B-09` |
| 3 | Hai phiên bản công thức của một món có cùng ngày hiệu lực thì sao? | `TC-MENU-B-09` |
| 4 | Ngưỡng giá loại suất có buộc là bội số của 100 đồng như giá món không? | `TC-MENU-B-12` |
| 5 | Tham số đếm của quy tắc có nhận số thập phân không? | `TC-MENU-B-22` |
| 6 | Tham số phân trang ngoài khoảng (`page=0`, `pageSize=101`): từ chối hay tự chỉnh? | `TC-MENU-B-26` |
| 7 | Tệp nhập thừa cột hoặc đổi thứ tự cột: bỏ qua hay từ chối? | `TC-MENU-X-01` |
| 8 | Dòng trống giữa tệp; số ở dạng văn bản; dấu thập phân phẩy và chấm | `TC-MENU-X-02` |
| 9 | Món gốc nằm ở dòng sau trong cùng tệp | `TC-MENU-X-07` |
| 10 | Các dòng công thức của một món không liền nhau | `TC-MENU-X-10` |
| 11 | Tệp `.xlsx` có nhiều trang tính | `TC-MENU-X-14` |

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo: phần A sinh từ tiêu chí nghiệm thu v0.1.0; phần B viết từ checklist v0.1.0 |
| 0.1.1 | 2026-11-11 | BA | Điền kết quả mong đợi cho 13 ô "SRS chưa nêu" theo SRS epic v0.3.0; thêm `BR-CAT-021` → `023` vào bảng độ phủ |

## Bổ sung thiết kế ca quy tắc — 11/11/2026

[86ca đạt/vi phạm](rule-test-cases.md) đã viết theo đề xuất hiện hành cho43quy tắc. Tất cả vẫn BLOCKED DL-01/điểm mở nguồn; chưa phải khoảng140ca rule được QA chốt và chưa chạy engine. [RTM chuẩn hóa](traceability.md) giữ bộ story/AC/test baseline hiện có.

### Lịch sử bổ sung

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.2 | 2026-11-11 | Liên kết86ca rule nháp vàRTM; không đổi ca baseline hoặc trạng thái đã chạy |
