---
id: DOC-DINH-DUONG-USER-GUIDE
title: Hướng dẫn vận hành E4
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e4]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E4: Dinh dưỡng

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Dinh dưỡng viên. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-NUTR-001: Quản lý bảng thành phần

[Use case gốc](usecases/UC-NUTR-001.md)

1. Người dùng mở UI-NUTR-01 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm kiểu và miền giá trị; bắt buộc nguồn D-17 có ấn bản và trang/mã thực phẩm; ghi giá trị hiện hành, bản lịch sử và audit trong một giao dịch; không ngầm dùng mặc định 100 khi chưa được người nhập xác nhận.
4. Hệ thống trả NutrientValue với version mới; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
- 2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
- 3a. I1 có version=1: 422; ERR-NUTR-422-01; không ghi bất kỳ bảng nào.
- 3b. hai người cùng đọc I1 version=1; người thứ nhất đã ghi version=2: 409 ERR-NUTR-409-01; giá trị version=2 không bị ghi đè.
- 4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

### UC-NUTR-002: Kiểm độ phủ nguyên liệu

[Use case gốc](usecases/UC-NUTR-002.md)

1. Người dùng mở UI-NUTR-01 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Lấy tập nguyên liệu duy nhất từ đúng phiên bản công thức; đếm đủ 4 chỉ số, nguồn, đơn vị và tỷ lệ; chỉ số 0 hợp lệ khác null; trả thiếu theo nguyên liệu và món bị ảnh hưởng, không tự điền số.
4. Hệ thống trả Coverage: complete/total, missing[], recipeVersions; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
- 2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
- 3a. I2 chưa có bảng thành phần: 200; complete=1,total=2; missing ghi I2 và cả hai recipeId; không thay null bằng 0.
- 3b. I1 có cả bốn chỉ số bằng 0 và nguồn đầy đủ: lần đầu complete=1; lần sau 401 ERR-NUTR-401-01; không trả dữ liệu.
- 4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

### UC-NUTR-003: Tính dinh dưỡng món

[Use case gốc](usecases/UC-NUTR-003.md)

1. Người dùng mở UI-NUTR-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Theo từng dòng qty_std × hệ số gram × edible_pct/100 × chỉ số/100; cộng Decimal chưa làm tròn; không áp COST_AP_HAO_HUT, không suy năng lượng bằng 4-4-9; trả phân rã và nguồn. Recipe phải có hiệu lực ngày phục vụ.
4. Hệ thống trả Calculation DISH, 4 totals, breakdown, provenance, label; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
- 2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
- 3a. công thức dùng 1 quả nhưng gramsPerUnit thiếu: 422 ERR-NUTR-422-02; totals=null; chỉ rõ nguyên liệu thiếu quy đổi, không trả tổng một phần.
- 3b. qty=1 quả; gramsPerUnit=50; edible=80%; cùng thành phần I1: hai kết quả bằng nhau:40.00/4.00/0.80/6.00; không nhân hao hụt Cost.
- 4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

### UC-NUTR-004: Tính dinh dưỡng tổ hợp suất

[Use case gốc](usecases/UC-NUTR-004.md)

1. Người dùng mở UI-NUTR-03 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm món thuộc ngày và đủ số món theo meal_type; chỉ cộng món chọn và món cố định đúng một lần; không cộng tất cả lựa chọn chính, không lấy món đắt nhất của COST; gắn recipeId/version và nguồn vào kết quả.
4. Hệ thống trả Calculation MEAL theo tổ hợp tường minh; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
- 2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
- 3a. suất cần 1 chính, người dùng chọn A và B: 422 ERR-NUTR-422-03; không tính tổng.
- 3b. đang xem menuVersion=2, một người sửa thành 3: 409 ERR-NUTR-409-01 hoặc 404 ERR-NUTR-404-01 tương ứng; không lộ dữ liệu ngoài quyền.
- 4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

### UC-NUTR-005: Xem kết quả và nguồn lịch sử

[Use case gốc](usecases/UC-NUTR-005.md)

1. Người dùng mở UI-NUTR-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kết quả tính thành công lưu bất biến inputs_snapshot và totals; GET trả bản cũ cùng isStale nếu nguồn hiện tại khác. Tính lại tạo id mới; không thay lịch sử hay biến bản tính thành bản duyệt thực đơn.
4. Hệ thống trả Calculation, sourceVersions, isStale, label; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
- 2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
- 3a. người dùng không có quyền cơ sở của C1: 404 ERR-NUTR-404-01; không trả totals hoặc nguồn.
- 3b. C1 và C2 là hai lần tính, clientRevision 1 và 2: UI giữ C2; lịch sử vẫn xem C1; cả hai có nhãn ước tính từ định lượng sống.
- 4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-NUTR-400-01 | Yêu cầu chưa đúng định dạng. | Sửa trường được chỉ ra |
| ERR-NUTR-401-01 | Vui lòng đăng nhập lại. | Đăng nhập |
| ERR-NUTR-403-01 | Bạn không có quyền thực hiện. | Liên hệ quản trị |
| ERR-NUTR-404-01 | Không tìm thấy dữ liệu. | Chọn lại dữ liệu thuộc quyền |
| ERR-NUTR-409-01 | Dữ liệu đã thay đổi. | Tải lại và tính lại |
| ERR-NUTR-422-01 | Thành phần dinh dưỡng chưa hợp lệ. | Kiểm trường báo lỗi |
| ERR-NUTR-422-02 | Chưa đủ dữ liệu để tính. | Bổ sung nguyên liệu được liệt kê |
| ERR-NUTR-422-03 | Tổ hợp món chưa hợp lệ. | Chọn đúng số món |
| ERR-NUTR-500-01 | Chưa thể hoàn tất. | Dùng requestId để đối soát; không tự coi đã lưu |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
