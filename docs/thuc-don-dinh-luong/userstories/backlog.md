# Danh mục User Story & Backlog: Epic E2 · Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `27-userstory.md` · BA-Kit v1.0 |
| Phiên bản | 0.1.0 |
| Trạng thái | Draft |
| Ngày | 2026-11-10 |
| Tài liệu liên quan | [SRS epic](../srs/spec.md) · [Sơ đồ use case](../srs/usecase-diagram.md) · [User-flow](../ui/user-flow.md) · [Epic-spec](../epic-spec.md) |

### Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-10 | BA | Khởi tạo từ SRS v0.1.0 và 13 use case |

## Cách đọc

- **Điểm (SP)** là **ước lượng sơ bộ của BA** theo thang 1 – 2 – 3 – 5 – 8, chỉ để so sánh độ lớn giữa các story. Đội phát triển chưa được xác định ([O-04]) nên chưa có ước lượng thật; đội sẽ ước lượng lại khi nhận backlog.
- **Chặn bởi**: điểm mở phải có câu trả lời trước khi story vào sprint. Ô trống = không bị chặn.
- **Nghiệm thu chính** là tóm tắt để story kiểm thử được. Tiêu chí đầy đủ dạng Given / When / Then viết ở bước `/ac`, với mã `AC-MENU-{số story}-{số thứ tự}`.
- Vai trò trong câu story: **Dinh dưỡng viên** (A-06) · **Người duyệt** (vai trò `GIAM_DOC` hoặc người được uỷ quyền, [O-06]) · **Nhân viên nội bộ** (mọi vai trò có quyền xem) · **Agent** (A-11, A-12, dùng từ R5).
- Mọi story đều kế thừa từ nền tảng (E1): phân quyền, nhật ký thay đổi, khuôn lỗi, khoá phiên bản. Các story không lặp lại những điều đó.

---

## Lát R2.1: Danh mục

| Story ID | User Story | FR | UC | SP | Ưu tiên | Chặn bởi | Nghiệm thu chính |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `US-MENU-01` | Là một **Dinh dưỡng viên**, tôi muốn **tạo và sửa nguyên liệu với đơn vị mua, đơn vị dùng, hệ số quy đổi và tỷ lệ hao hụt** để **lập công thức bằng đúng đơn vị bếp đang dùng (gram, bìa, quả)**. | `FR-MENU-ING-001`, `002` | `UC-MENU-001` | 3 | P0 | | Tên trùng bị từ chối; hao hụt bắt buộc khi có xương/vỏ; không sửa được đơn vị của nguyên liệu đang nằm trong công thức hiệu lực |
| `US-MENU-02` | Là một **Dinh dưỡng viên**, tôi muốn **ngừng dùng một nguyên liệu** để **nó không còn xuất hiện khi lập công thức mới**. | `FR-MENU-ING-003` | `UC-MENU-001` | 2 | P0 | | Bị chặn kèm danh sách công thức nếu nguyên liệu đang nằm trong công thức hiệu lực |
| `US-MENU-03` | Là một **Nhân viên nội bộ**, tôi muốn **tìm và lọc nguyên liệu theo tên, nhóm, loại bảo quản, trạng thái** để **tra đúng nguyên liệu trong vài giây**. | `FR-MENU-ING-004` | `UC-MENU-001` | 2 | P0 | | Phân trang 20 dòng; có trạng thái rỗng và "không khớp bộ lọc" |
| `US-MENU-04` | Là một **Dinh dưỡng viên**, tôi muốn **quản lý danh sách nhóm nguyên liệu chính kèm nguồn đạm** để **hệ thống so được hai món có trùng nguyên liệu chính hay không**. | `FR-MENU-ING-005` | `UC-MENU-001` | 2 | P0 | [H-3] | Không huỷ được nhóm đang có nguyên liệu hoặc món dùng |
| `US-MENU-05` | Là một **Dinh dưỡng viên**, tôi muốn **khai các tháng trong mùa của một loại rau** để **được nhắc khi xếp rau trái mùa**. | `FR-MENU-ING-006` | `UC-MENU-001` | 2 | P1 | | Một nguyên liệu có 0 hoặc nhiều khoảng tháng; tháng ngoài 1–12 bị từ chối |
| `US-MENU-06` | Là một **Dinh dưỡng viên**, tôi muốn **quản lý danh sách phương pháp chế biến và đánh dấu phương pháp nào là chiên, phương pháp nào ít dầu mỡ** để **hệ thống kiểm được quy tắc về món chiên và món Healthy**. | `FR-MENU-DISH-007` | `UC-MENU-002` | 2 | P0 | [H-1], [H-8] | Mỗi phương pháp có 2 cờ; tên không trùng |
| `US-MENU-07` | Là một **Dinh dưỡng viên**, tôi muốn **tạo một món ở trạng thái nháp với đủ 12 thuộc tính và chất gây dị ứng** để **món có đủ thông tin cho bộ kiểm quy tắc**. | `FR-MENU-DISH-001` | `UC-MENU-002` | 5 | P0 | | Tên trùng bị từ chối; không gắn được Healthy với phương pháp không ít dầu mỡ; món gốc phải cùng vai trò; mỗi thuộc tính có chú giải và ví dụ trên màn hình |
| `US-MENU-08` | Là một **Dinh dưỡng viên**, tôi muốn **khai các cặp món không được xếp cùng ngày** để **hệ thống chặn những tổ hợp như nem và nộm**. | `FR-MENU-DISH-008` | `UC-MENU-002` | 2 | P0 | [H-4] | Hai món của cặp phải khác nhau; cặp không trùng |
| `US-MENU-09` | Là một **Nhân viên nội bộ**, tôi muốn **tìm và lọc món theo tên, vai trò, nhóm nguyên liệu, phương pháp, Healthy, trạng thái** để **xem nhanh danh mục món hiện có**. | `FR-MENU-DISH-006` | Chưa có | 2 | P0 | | Vai trò chỉ xem không thấy nút sửa; món có đề nghị chờ duyệt hiện nhãn |
| `US-MENU-10` | Là một **Dinh dưỡng viên**, tôi muốn **gửi duyệt một hoặc nhiều món nháp** để **món được đưa vào sử dụng sau khi có người thứ hai kiểm tra**. | `FR-MENU-DISH-003` | `UC-MENU-002` | 2 | P0 | | Bị chặn nếu món chưa có công thức chờ duyệt hoặc đang hiệu lực; người duyệt nhận thông báo |
| `US-MENU-11` | Là một **Người duyệt**, tôi muốn **duyệt hoặc trả lại món, từng món hoặc nhiều món một lần** để **chỉ những món gắn thuộc tính đúng mới vào được thực đơn**. | `FR-MENU-DISH-004` | `UC-MENU-010` | 3 | P0 | [O-06] | Không tự duyệt món mình tạo hoặc sửa; trả lại bắt buộc lý do; không duyệt được món chưa có công thức đã duyệt, trừ khi duyệt cùng lúc |
| `US-MENU-12` | Là một **Dinh dưỡng viên**, tôi muốn **tải mẫu bảng tính và kiểm tra tệp đã điền trước khi nhập** để **biết chính xác dòng nào sai mà chưa ghi gì vào hệ thống**. | `FR-MENU-IMP-001`, `002` | `UC-MENU-012` | 5 | P0 | | Lỗi báo theo số dòng và cột; tệp sai mẫu hoặc quá 2.000 dòng bị từ chối; kiểm quá 5 giây thì chạy nền. Phạm vi lát này: nguyên liệu và món |
| `US-MENU-13` | Là một **Dinh dưỡng viên**, tôi muốn **nhập toàn bộ tệp đã kiểm sạch trong một lần** để **đưa dữ liệu gốc vào hệ thống mà không gõ tay từng dòng**. | `FR-MENU-IMP-003` | `UC-MENU-012` | 3 | P0 | [E2-Q10] | Tất cả hoặc không gì cả; món vào trạng thái nháp, không tự hiệu lực |

## Lát R2.2: Công thức, giá bán, loại suất

| Story ID | User Story | FR | UC | SP | Ưu tiên | Chặn bởi | Nghiệm thu chính |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `US-MENU-14` | Là một **Dinh dưỡng viên**, tôi muốn **lập công thức nháp cho một món với định lượng sống tối thiểu – chuẩn – tối đa của từng nguyên liệu** để **ghi lại định mức theo bảng chuẩn của Gia Phát**. | `FR-MENU-RCP-001`, `002` | `UC-MENU-004` | 5 | P0 | [O-02], [E2-Q5] | Phải có ≥ 1 nguyên liệu chính, không lặp nguyên liệu; tối thiểu ≤ chuẩn ≤ tối đa; món chính và món phụ phải có nguyên liệu chính thuộc nhóm của món; đơn vị tự lấy theo nguyên liệu |
| `US-MENU-15` | Là một **Dinh dưỡng viên**, tôi muốn **tạo nguyên liệu còn thiếu ngay trong lúc soạn công thức** để **không mất các dòng đã nhập**. | `FR-MENU-ING-001` | `UC-MENU-004` | 2 | P0 | | Nguyên liệu mới xuất hiện ngay trong công thức đang soạn; các dòng khác giữ nguyên |
| `US-MENU-16` | Là một **Người duyệt**, tôi muốn **duyệt hoặc trả lại công thức** để **không ai tự quyết định lượng (thứ quyết định cost) của chính mình**. | `FR-MENU-RCP-003` | `UC-MENU-010` | 5 | P0 | [O-06] | Người tạo không tự duyệt; công thức đã gửi duyệt không sửa được; khi duyệt, phiên bản cũ chuyển "đã thay thế" đúng vào ngày hiệu lực của phiên bản mới |
| `US-MENU-17` | Là một **Dinh dưỡng viên**, tôi muốn **tạo phiên bản mới từ công thức đang hiệu lực, có lý do và ngày hiệu lực** để **điều chỉnh định lượng mà không làm thay đổi các thực đơn đã dùng phiên bản cũ**. | `FR-MENU-RCP-004` | `UC-MENU-004` | 3 | P0 | | Phiên bản mới là bản nháp sao chép các dòng; phiên bản cũ vẫn hiệu lực đến khi bản mới được duyệt và đến ngày hiệu lực |
| `US-MENU-18` | Là một **Dinh dưỡng viên**, tôi muốn **hệ thống luôn dùng đúng công thức có hiệu lực vào ngày phục vụ** để **cost và dinh dưỡng của một ngày không bị tính bằng định lượng của ngày khác**. | `FR-MENU-RCP-005` | `UC-MENU-007` | 2 | P0 | | Với mỗi món và ngày có đúng 1 công thức hiệu lực; không có thì báo lỗi rõ tên món và ngày |
| `US-MENU-19` | Là một **Người duyệt**, tôi muốn **xem bảng so sánh giữa phiên bản công thức đề nghị và phiên bản đang hiệu lực** để **thấy ngay định lượng nào đổi**. | `FR-MENU-RCP-006` | `UC-MENU-004`, `010` | 3 | P1 | | Hiện dòng thêm, bớt, đổi định lượng |
| `US-MENU-20` | Là một **Dinh dưỡng viên**, tôi muốn **đặt giá bán (đã gồm VAT) cho một món với ngày hiệu lực** để **hệ thống kiểm được tổng giá suất so với ngưỡng của loại suất**. | `FR-MENU-PRC-001` | `UC-MENU-005` | 3 | P0 | [E2-Q1] | Giá là bội số của 100 đồng; ngày hiệu lực từ ngày mai trở đi; không trùng ngày hiệu lực |
| `US-MENU-21` | Là một **Người duyệt**, tôi muốn **duyệt hoặc trả lại giá bán** để **giá hiển thị cho khách luôn được kiểm soát**. | `FR-MENU-PRC-002`, `003` | `UC-MENU-010` | 3 | P0 | [O-06], [E2-Q7] | Giá đã hiệu lực không sửa, không huỷ; với mỗi món và ngày lấy đúng giá đã duyệt có hiệu lực gần nhất |
| `US-MENU-22` | Là một **Dinh dưỡng viên**, tôi muốn **xem lịch sử giá bán của một món** để **biết giá đã thay đổi thế nào theo thời gian**. | `FR-MENU-PRC-004` | `UC-MENU-005` | 1 | P1 | | Danh sách theo ngày hiệu lực, đánh dấu giá đang áp dụng |
| `US-MENU-23` | Là một **Dinh dưỡng viên**, tôi muốn **tự tạo loại suất với ngưỡng giá, số món chính đưa ra, số món phụ, có rau, có canh** để **định nghĩa được suất cho từng mức giá mà không cần lập trình**. | `FR-MENU-MTY-001`, `002` | `UC-MENU-006` | 3 | P0 | | Số món chính được chọn ≥ 1 và ≤ số đưa ra; số món phụ 0–5; kích hoạt rồi mới tạo được thực đơn |
| `US-MENU-24` | Là một **Dinh dưỡng viên**, tôi muốn **hệ thống khoá cơ cấu của loại suất đã có thực đơn gửi duyệt** để **thực đơn đã duyệt không bị sai lệch vì ai đó đổi số món**. | `FR-MENU-MTY-003` | `UC-MENU-006` | 2 | P0 | | Tên và cờ công khai vẫn sửa được; sửa cơ cấu bị từ chối kèm gợi ý tạo loại suất mới |
| `US-MENU-25` | Là một **Dinh dưỡng viên**, tôi muốn **đánh dấu một loại suất là công khai** để **nó xuất hiện trên website khi phần website hoàn thành**. | `FR-MENU-MTY-004` | `UC-MENU-006` | 1 | P1 | | Cờ lưu được; chưa có hiệu ứng hiển thị trong R2 |
| `US-MENU-26` | Là một **Dinh dưỡng viên**, tôi muốn **đề nghị sửa thuộc tính của một món đang dùng, kèm lý do** để **sửa được chỗ gắn sai mà món vẫn dùng được trong lúc chờ duyệt**. | `FR-MENU-DISH-002` | `UC-MENU-003` | 5 | P0 | | Sửa tên, mô tả, dị ứng lưu ngay; sửa thuộc tính ảnh hưởng quy tắc tạo đề nghị chờ duyệt; món giữ giá trị cũ; mỗi món tối đa 1 đề nghị đang chờ; rút được đề nghị |
| `US-MENU-27` | Là một **Người duyệt**, tôi muốn **duyệt hoặc trả lại một đề nghị thay đổi, với bảng giá trị cũ – mới và lý do** để **mọi thay đổi ảnh hưởng tới bộ kiểm quy tắc đều có người thứ hai xem**. | `FR-MENU-DISH-002`, `FR-MENU-RUL-006` | `UC-MENU-010` | 3 | P0 | [O-06] | Duyệt thì giá trị mới ghi vào bản ghi gốc; đề nghị lỗi thời không duyệt được; dùng chung cho đề nghị sửa món và sửa quy tắc |
| `US-MENU-28` | Là một **Dinh dưỡng viên**, tôi muốn **ngừng dùng một món** để **nó không còn được chọn cho thực đơn mới**. | `FR-MENU-DISH-005` | `UC-MENU-003` | 2 | P0 | | Bị chặn kèm danh sách nếu món nằm trong thực đơn đã công bố có ngày phục vụ từ hôm nay trở đi |
| `US-MENU-29` | Là một **Dinh dưỡng viên**, tôi muốn **gắn ảnh cho món** để **khách thấy hình món khi chọn**. | `FR-MENU-DISH-009` | `UC-MENU-002` | 2 | P1 | | JPG, PNG, WEBP; tối đa 10 MB |
| `US-MENU-30` | Là một **Dinh dưỡng viên**, tôi muốn **nhập công thức và giá bán từ bảng tính** để **đưa định lượng và giá của các món ban đầu vào một lần**. | `FR-MENU-IMP-001` → `003` | `UC-MENU-012` | 5 | P0 | [O-02] | Dòng tham chiếu món hoặc nguyên liệu chưa có bị báo lỗi; công thức vào trạng thái nháp, giá vào trạng thái chờ duyệt |

## Lát R2.3: Thực đơn và bộ kiểm quy tắc

| Story ID | User Story | FR | UC | SP | Ưu tiên | Chặn bởi | Nghiệm thu chính |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `US-MENU-31` | Là một **Dinh dưỡng viên**, tôi muốn **tạo thực đơn nháp cho một loại suất và một tuần, chọn các ngày phục vụ** để **có khung trống đúng số ô của loại suất**. | `FR-MENU-MNU-001` | `UC-MENU-007` | 3 | P0 | [E2-Q3], [E2-Q4] | Tuần bắt đầu thứ Hai; mỗi loại suất một thực đơn mỗi tuần; mỗi ngày có đúng số ô theo cấu hình loại suất |
| `US-MENU-32` | Là một **Dinh dưỡng viên**, tôi muốn **xếp, đổi, bỏ món ở từng ô của từng ngày** để **dựng thực đơn tuần**. | `FR-MENU-MNU-002` | `UC-MENU-007` | 5 | P0 | | Chỉ chọn được món đang dùng đúng vai trò của ô; một món một lần mỗi ngày; món thiếu công thức hoặc giá hiệu lực không xếp được; hệ thống gắn công thức hiệu lực tại ngày phục vụ |
| `US-MENU-33` | Là một **Dinh dưỡng viên**, tôi muốn **chọn món mặc định cho từng ngày trong các món chính của ngày đó** để **người không chọn trước hạn chốt vẫn có suất**. | `FR-MENU-MNU-003` | `UC-MENU-007` | 2 | P0 | | Món mặc định phải là món chính của ngày; bỏ món đó khỏi ngày thì món mặc định bị xoá |
| `US-MENU-34` | Là một **Nhân viên nội bộ**, tôi muốn **xem danh sách và chi tiết thực đơn theo loại suất, tuần, trạng thái** để **biết tuần nào ăn gì**. | `FR-MENU-MNU-007` | `UC-MENU-011` | 3 | P0 | | Vai trò không có quyền ghi chỉ thấy thực đơn đã công bố; mở thực đơn chưa công bố bằng đường dẫn trực tiếp trả "không tìm thấy" |
| `US-MENU-35` | Là một **Dinh dưỡng viên**, tôi muốn **huỷ một thực đơn nháp, kèm lý do** để **dọn những bản dựng thử**. | `FR-MENU-MNU-009` | `UC-MENU-007` | 1 | P0 | | Chỉ huỷ được thực đơn chưa gửi duyệt |
| `US-MENU-36` | Là một **Dinh dưỡng viên**, tôi muốn **mỗi lần đổi món thì thấy ngay thực đơn vi phạm quy tắc nào của từng ngày, ở món nào** để **sửa ngay trong lúc dựng thay vì tự rà**. | `FR-MENU-RUL-001`, `003` | `UC-MENU-008` | 8 | P0 | DL-01 | Chạy mọi quy tắc cấp ngày đang bật; mỗi vi phạm nêu mã, ngày, món, giá trị đo, giới hạn; kết quả trong ≤ 2 giây; cùng đầu vào luôn cho cùng kết quả; mỗi quy tắc có 1 ca đạt và 1 ca vi phạm |
| `US-MENU-37` | Là một **Dinh dưỡng viên**, tôi muốn **thấy các vi phạm xét trên cả tuần (lặp món, nguyên liệu nhiều ngày liền, lặp rau và canh, độ đa dạng)** để **thực đơn tuần không nhàm chán**. | `FR-MENU-RUL-001` | `UC-MENU-008` | 5 | P0 | DL-01, [E2-Q2], [H-2] | Chạy mọi quy tắc cấp tuần đang bật; món có món gốc được đếm theo món gốc; không có dữ liệu tuần trước thì chỉ tính trong tuần |
| `US-MENU-38` | Là một **Dinh dưỡng viên**, tôi muốn **thấy điểm quy tắc trên thang 100 và phân biệt vi phạm bắt buộc với cảnh báo** để **biết thực đơn đã gửi duyệt được chưa**. | `FR-MENU-RUL-001` | `UC-MENU-008` | 3 | P0 | DL-01 | Điểm = 100 trừ tổng điểm phạt của cảnh báo, sàn 0; quy tắc cấp ngày vi phạm ở nhiều ngày bị trừ mỗi ngày một lần; thực đơn chuyển "đã kiểm" khi đủ món, đủ món mặc định, không còn vi phạm bắt buộc |
| `US-MENU-39` | Là một **Dinh dưỡng viên**, tôi muốn **hệ thống kiểm tổng giá bán của mỗi tổ hợp suất so với ngưỡng giá của loại suất** để **không công bố thực đơn mà người ăn chọn xong lại vượt định mức**. | `FR-MENU-MNU-004` | `UC-MENU-007` | 3 | P0 | **[E2-Q1]** | Theo phương án đang đề xuất: mỗi món chính + mọi món phụ + rau + canh của ngày ≤ ngưỡng; vi phạm nêu món chính nào vượt và vượt bao nhiêu |
| `US-MENU-40` | Là một **Dinh dưỡng viên**, tôi muốn **ghi lý do chấp nhận cho từng cảnh báo mức nặng** để **người duyệt hiểu vì sao tôi giữ món đó**. | `FR-MENU-RUL-004` | `UC-MENU-007`, `008` | 2 | P0 | | Lý do từ 10 ký tự; lý do tự xoá khi cảnh báo đó hết |
| `US-MENU-41` | Là một **Agent**, tôi muốn **gửi một thực đơn chưa lưu để nhận kết quả kiểm quy tắc** để **thử nhiều phương án bằng đúng bộ kiểm mà người dùng thấy**. | `FR-MENU-RUL-002` | `UC-MENU-008` | 3 | P0 | | Không ghi dữ liệu; kết quả giống hệt khi kiểm thực đơn đã lưu có cùng nội dung; 20 lời gọi đồng thời với p95 ≤ 2 giây |
| `US-MENU-42` | Là một **Nhân viên nội bộ**, tôi muốn **xem danh mục quy tắc với loại, điểm phạt, phạm vi và con số hiện hành** để **biết thực đơn đang được kiểm theo tiêu chuẩn nào**. | `FR-MENU-RUL-005` | `UC-MENU-013` | 2 | P0 | DL-01 | Danh mục nạp từ bảng quy tắc đã duyệt; hiện câu gốc trong file quy chuẩn |
| `US-MENU-43` | Là một **Dinh dưỡng viên**, tôi muốn **đề nghị bật/tắt, đổi loại, đổi điểm phạt hoặc con số của một quy tắc, kèm lý do** để **điều chỉnh tiêu chuẩn khi thực tế thay đổi mà không cần sửa phần mềm**. | `FR-MENU-RUL-006` | `UC-MENU-013` | 5 | P0 | [E2-Q11] | Có hiệu lực sau khi duyệt; thực đơn nháp dùng quy tắc mới từ lần kiểm kế tiếp; thực đơn từ chờ duyệt trở đi giữ kết quả cũ; không thêm được quy tắc mới qua giao diện |

## Lát R2.4: Duyệt, công bố và phần P1

| Story ID | User Story | FR | UC | SP | Ưu tiên | Chặn bởi | Nghiệm thu chính |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| `US-MENU-44` | Là một **Dinh dưỡng viên**, tôi muốn **gửi duyệt thực đơn** để **người duyệt nhận được một thực đơn đã qua kiểm tự động**. | `FR-MENU-APV-001`, `006` | `UC-MENU-009` | 5 | P0 | [E2-Q6] | Hệ thống kiểm lại ngay trước khi chuyển; bị chặn khi còn ô trống, thiếu món mặc định, còn vi phạm bắt buộc, hoặc cảnh báo mức nặng chưa có lý do; có chỗ móc để đợt cost thêm bước kiểm mà không sửa phân hệ này |
| `US-MENU-45` | Là một **Người duyệt**, tôi muốn **xem thực đơn cùng điểm quy tắc, các cảnh báo và lý do của người dựng, rồi duyệt hoặc trả lại** để **quyết định dựa trên đủ thông tin**. | `FR-MENU-APV-002` | `UC-MENU-010` | 3 | P0 | [O-06] | Không tự duyệt; trả lại bắt buộc lý do và đưa thực đơn về nháp; duyệt thì đóng băng kết quả kiểm và công thức đã gắn |
| `US-MENU-46` | Là một **Người duyệt**, tôi muốn **thấy mọi nội dung đang chờ mình duyệt ở một trang, nhóm theo loại** để **không bỏ sót và duyệt được nhiều mục một lần**. | `FR-MENU-DISH-004`, `RCP-003`, `PRC-002`, `APV-002` | `UC-MENU-010` | 3 | P0 | [O-06], [E2-Q7] | Lọc theo loại kèm số đếm; duyệt hàng loạt báo số thành công và lý do từng mục lỗi; mục đã được người khác xử lý thì báo và tải lại |
| `US-MENU-47` | Là một **Dinh dưỡng viên hoặc Người duyệt**, tôi muốn **nhận thông báo khi có nội dung chờ duyệt hoặc có kết quả duyệt** để **không phải tự vào kiểm tra**. | `FR-SYS-NTF-001` | `UC-MENU-009`, `010` | 2 | P0 | | Thông báo dẫn thẳng tới nội dung; kết quả trả lại kèm lý do |
| `US-MENU-48` | Là một **Dinh dưỡng viên**, tôi muốn **công bố thực đơn đã duyệt** để **bếp, quản lý cơ sở và các phân hệ sau thấy thực đơn chính thức**. | `FR-MENU-APV-003` | `UC-MENU-011` | 2 | P0 | [E2-Q9] | Chỉ công bố được khi ngày phục vụ đầu tiên sau hôm nay; bếp và quản lý cơ sở nhận thông báo |
| `US-MENU-49` | Là một **Dinh dưỡng viên**, tôi muốn **thu hồi thực đơn đã công bố kèm lý do, rồi sửa và gửi duyệt lại** để **sửa được sai sót mà không sửa lén thực đơn đang chạy**. | `FR-MENU-APV-004`, `005` | `UC-MENU-011` | 3 | P0 | [E2-Q8] | Lý do từ 10 ký tự; sau thu hồi thực đơn về nháp và đi lại toàn bộ chu trình; kết quả kiểm tính lại theo giá trị hiện hành |
| `US-MENU-50` | Là một **Người duyệt**, tôi muốn **thực đơn có điểm quy tắc dưới ngưỡng phải có hai người duyệt** để **thực đơn nhiều cảnh báo được xem kỹ hơn**. | `FR-MENU-RUL-007` | `UC-MENU-010` | 3 | P1 | **[O-06]** | Ngưỡng là tham số (đề xuất 80); một người không duyệt hai lần; hiện tiến độ "đã duyệt 1/2". Không làm được nếu Gia Phát chỉ có một người duyệt |
| `US-MENU-51` | Là một **Dinh dưỡng viên**, tôi muốn **sao chép thực đơn của một tuần trước làm bản nháp** để **không dựng lại từ đầu**. | `FR-MENU-MNU-005` | `UC-MENU-007` | 3 | P1 | | Món không còn dùng bị bỏ trống và được liệt kê |
| `US-MENU-52` | Là một **Dinh dưỡng viên**, tôi muốn **khi chọn món thấy món đó đã xuất hiện ngày nào trong 4 tuần gần nhất** để **tránh lặp món mà khách vừa ăn**. | `FR-MENU-MNU-006` | `UC-MENU-007` | 3 | P1 | | Tính trong cùng loại suất |
| `US-MENU-53` | Là một **Dinh dưỡng viên**, tôi muốn **xuất thực đơn tuần ra PDF** để **gửi cho bếp hoặc dán tại điểm phục vụ**. | `FR-MENU-MNU-008` | `UC-MENU-011` | 3 | P1 | | Lưới ngày × vị trí × tên món; thực đơn chưa công bố có dòng "bản nháp" trên mỗi trang |

---

## Tổng hợp

| Lát | Số story | P0 | P1 | Tổng SP (sơ bộ) |
| :--- | :---: | :---: | :---: | :---: |
| R2.1 Danh mục | 13 | 12 | 1 | 35 |
| R2.2 Công thức, giá bán, loại suất | 17 | 13 | 4 | 50 |
| R2.3 Thực đơn và bộ kiểm | 13 | 13 | 0 | 45 |
| R2.4 Duyệt, công bố, P1 | 10 | 6 | 4 | 30 |
| **Cộng** | **53** | **44** | **9** | **160** |

Yêu cầu chức năng chưa thành story: `FR-MENU-RCP-007` (nhiều cỡ định lượng): chờ [O-02] quyết có làm hay không.

## Kiểm INVEST

| Tiêu chí | Tình trạng |
| :--- | :--- |
| Độc lập | Các story trong cùng lát triển khai được theo thứ tự bất kỳ, trừ các chuỗi bắt buộc: `07` → `10` → `11` · `14` → `16` → `17` · `31` → `32` → `33` · `36`, `37`, `38` cùng dùng một khung bộ kiểm (làm `36` trước) · `44` → `45` → `48` → `49` · `26`, `43` → `27` |
| Thương lượng được | Các con số (2.000 dòng, 10 MB, ngưỡng 80 điểm, 4 tuần lịch sử, bội số 100 đồng) là đề xuất, đổi được mà không đổi bản chất story |
| Có giá trị | Mỗi story nêu lợi ích cho một vai trò cụ thể. `US-MENU-18` và `US-MENU-41` phục vụ gián tiếp (đúng số liệu; agent ở R5) nhưng là điều kiện để các đợt sau chạy được |
| Ước lượng được | 24 trong 53 story có điểm mở ở cột "Chặn bởi": 5 story chỉ chờ biết ai là người duyệt ([O-06]); 19 story chờ câu trả lời nghiệp vụ, trong đó 5 story (`13`, `43`, `44`, `48`, `49`) làm được ngay theo cách đang xử lý tạm. Đội chưa ước lượng chắc được 14 story còn lại |
| Vừa vặn | Lớn nhất là `US-MENU-36` (8 điểm): khung bộ kiểm cộng khoảng 20 quy tắc cấp ngày. Nếu quá một sprint, tách theo nhóm quy tắc của bảng quy tắc (A cơ cấu · B nguyên liệu · C phương pháp · D khẩu vị · E khả thi) |
| Kiểm thử được | Mỗi story có nghiệm thu chính; tiêu chí Given / When / Then viết ở bước `/ac` |

## Story bị chặn bởi điểm mở

Giữ nguyên trạng thái mở. Xếp theo mức độ ảnh hưởng.

| Điểm mở | Story bị chặn | Hệ quả nếu chưa có câu trả lời |
| :--- | :--- | :--- |
| DL-01: duyệt 43 quy tắc | `36`, `37`, `38`, `42` | Không có con số để viết ca kiểm thử; lát R2.3 không nghiệm thu được |
| [O-06]: ai duyệt | `11`, `16`, `21`, `27`, `45`, `46`, `50` | Dựng được chức năng nhưng không cấu hình được người dùng thật; `50` có thể phải bỏ |
| [E2-Q1]: cách kiểm ngưỡng giá | `20`, `39` | Chưa rõ giá từng món dùng để làm gì; `39` có thể đổi hẳn |
| [O-02]: một hay nhiều cỡ định lượng | `14`, `30` | Mẫu bảng tính và màn hình soạn công thức có thêm cột hay không |
| [E2-Q5]: bảng định lượng chuẩn | `14` | Có thêm một bảng chuẩn và một bước kiểm khi lưu công thức hay không |
| [H-1], [H-3], [H-4], [H-8] | `04`, `06`, `08` | Chức năng làm được; chỉ thiếu dữ liệu khởi tạo |
| [E2-Q2], [H-2] | `37` | Quy tắc tuần có đọc dữ liệu tuần trước hay không |
| [E2-Q3], [E2-Q4] | `31` | Số cột của lưới; một hay nhiều thực đơn mỗi loại suất |
| [E2-Q6], [E2-Q8], [E2-Q9], [E2-Q10], [E2-Q11] | `44`, `49`, `48`, `13`, `43` | Story làm được theo cách đang xử lý tạm; câu trả lời khác đi sẽ thêm việc |
