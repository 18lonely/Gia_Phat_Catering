---
id: DOC-E8-USER-GUIDE
title: Hướng dẫn vận hành E8
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e8]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E8: Website công khai

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Người quản trị nội dung, người xử lý lead. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-PUB-001: Xem trang giới thiệu

[Use case gốc](usecases/UC-PUB-001.md)

1. Khách truy cập slug trang thuộc UI-PUB-01.
2. Hệ thống tra trang tương ứng và xác định revision được phép xuất bản.
3. Hệ thống lấy nội dung, media và metadata thuộc tập trường công khai, loại dữ liệu quản trị/nội bộ khỏi phản hồi.
4. Hệ thống trả nội dung đúng revision cùng liên kết tới dịch vụ, dự án và đối tác được công khai.
5. Khách đọc trang và chọn liên kết liên quan; hệ thống tiếp tục phục vụ theo quyền công khai của trang đích.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Slug không có nội dung công khai, thuộc bản nháp hoặc đã thu hồi: hệ thống trả ERR-PUB-404-01 và hướng về danh sách; không lộ sự tồn tại bản nháp, dữ liệu giữ nguyên.
- 2b. Chưa có policy cho nhánh xuất bản: hệ thống báo chưa đủ điều kiện ERR-PUB-422-02, giữ BLOCKED E8-Q08; không tự công bố.
- 3a. Nguồn không khả dụng: hệ thống trả ERR-PUB-503-01 với thông báo an toàn; không giả trang đã tải và không thay dữ liệu.
- 4a. Revision nguồn thay đổi trước lúc trả trang: hệ thống kiểm lại bản được phép công khai; không phát tán revision cũ đã bị thu hồi.

### UC-PUB-002: Xem tin và bài viết

[Use case gốc](usecases/UC-PUB-002.md)

1. Khách chọn bộ lọc và trang danh sách tại UI-PUB-02.
2. Hệ thống tìm các bài được phép công khai theo bộ lọc và quy ước phân trang được duyệt.
3. Hệ thống trả danh sách với tiêu đề và metadata công khai; bài chưa duyệt không có trong danh sách, sitemap hay kết quả tìm kiếm.
4. Khách chọn một bài; hệ thống tra slug và kiểm lại revision còn được phép đọc công khai.
5. Hệ thống trả tiêu đề, nội dung và media đúng revision của bài để khách đọc; không ghi trạng thái bài.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Không có bài phù hợp: hệ thống trả danh sách rỗng; không tạo bài giả, dữ liệu giữ nguyên.
- 4a. Bài chưa duyệt, thu hồi hoặc không tồn tại: hệ thống trả ERR-PUB-404-01, không lộ bản nháp; khách có thể về danh sách.
- 2b. Nguồn/quyền công khai chưa đủ: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q01/08; không dùng policy mặc định.
- 4b. Revision thay đổi trong lúc đọc: hệ thống kiểm lại bản được phép; không dùng bản đã thu hồi để trả chi tiết.
- 5a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01 và thông báo an toàn; dữ liệu bài không đổi.

### UC-PUB-003: Chuẩn bị mapping WordPress

[Use case gốc](usecases/UC-PUB-003.md)

1. Người quản trị nạp thông tin inventory tại UI-PUB-07 và đối chiếu từng sourceId, URL nguồn, title/body/media/ngày công bố gốc trong DL-08.
2. Người quản trị chuẩn bị nội dung nháp theo quyền soạn; hệ thống làm sạch HTML, giữ provenance và ngày gốc riêng ngày chuyển.
3. Hệ thống kiểm sourceId đã có để không nhân đôi bài khi chuẩn bị lại; người quản trị đối chiếu nội dung, ảnh và liên kết với bản nguồn.
4. Người quản trị khai báo URL nguồn, target, KEEP/REDIRECT và revision; giữ ánh xạ sourceId tới contentRef/revision và targetPath.
5. Hệ thống kiểm quyền, revision, URL trùng, đích công khai và vòng lặp; liệt kê ngoại lệ theo từng URL, không bỏ khỏi mẫu số.
6. Hệ thống lưu bảng mapping nháp, kết quả đối chiếu và dấu vết; trả danh sách chặn để người quản trị rà.
7. Người quản trị kiểm lại nháp; nội dung chỉ công bố qua UC-PUB-011 khi đủ điều kiện, mapping chưa tự kích hoạt.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Thiếu DL-08: hệ thống báo ERR-PUB-422-02 và BLOCKED E8-Q01/02; chưa có căn cứ tính độ phủ URL.
- 3a. Media thiếu, bài trùng hoặc đã xóa chưa có quyết định: hệ thống ghi ngoại lệ BLOCKED; giữ dòng trong inventory, không nhân đôi hoặc tự chọn đích.
- 5a. Mapping vòng lặp, trùng nguồn hoặc đích không công khai: hệ thống trả ERR-PUB-422-03; không kích hoạt mapping sai.
- 5b. Revision đã đổi: hệ thống trả ERR-PUB-409-01, yêu cầu tải lại đối chiếu; không ghi đè bản mới.
- 5c. Hết phiên/thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01; chưa lưu thay đổi mapping.
- 6a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01, giữ requestId để đối soát; chưa xác định đã ghi hay chưa, không báo hoàn tất.

### UC-PUB-004: Phục vụ URL cũ

[Use case gốc](usecases/UC-PUB-004.md)

1. Trình duyệt khách gửi yêu cầu đọc URL cũ tới website.
2. Hệ thống đối chiếu nguyên URL với inventory và mapping đã được duyệt, không kích hoạt mapping từ yêu cầu GET.
3. Hệ thống kiểm đích còn công khai và mapping không tạo vòng lặp hay chuyển hướng tới URL tùy ý.
4. Với KEEP, handler website trả HTTP 200 cùng nội dung đúng; với REDIRECT, handler trả HTTP 301 và Location đã được duyệt tại URL khách truy cập.
5. Trình duyệt hiển thị nội dung hoặc theo Location tới trang đích; hệ thống chỉ phục vụ dữ liệu công khai.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. URL ngoài inventory hoặc bài xóa chưa có quyết định: hệ thống không giả thành bài cũ đã map; nhánh chưa đủ căn cứ giữ BLOCKED E8-Q01/02, mapping không đổi.
- 3a. Vòng lặp hoặc đích nháp: hệ thống chặn mapping với ERR-PUB-422-03; không phát Location sai và không công khai đích nháp.
- 2b. Policy/nguồn chưa đủ: hệ thống trả ERR-PUB-422-02; không tự chọn KEEP hay REDIRECT.
- 3b. Đích thay revision/thu hồi: hệ thống kiểm lại quyền công khai, không dùng đích cũ đã mất hiệu lực; mapping không được tự sửa qua GET.
- 4a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01 với thông báo an toàn; không giả chuyển hướng thành công, dữ liệu giữ nguyên.

### UC-PUB-005: Xem thực đơn mẫu có giá

[Use case gốc](usecases/UC-PUB-005.md)

1. Khách chọn mẫu tại UI-PUB-03; hệ thống nhận publicSampleId và ngày hiển thị.
2. Hệ thống tra projection công khai và kiểm quyền hiển thị giá suất theo nguồn được cho phép.
3. Hệ thống đối chiếu menu, recipe và nutrition revision cùng ngày nguồn, kiểm phần thiếu hoặc hết hiệu lực.
4. Hệ thống lấy định lượng theo suất, năng lượng kcal, đạm/béo/bột đường theo g và dị ứng; không lấy price_cap hoặc giá hợp đồng làm giá public.
5. Hệ thống trả tuần mẫu, giá và dữ liệu đủ căn cứ với nhãn “ước tính từ định lượng sống”, kèm nguồn để khách đọc.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Mẫu không tồn tại hoặc không công khai: hệ thống trả ERR-PUB-404-01; không lộ bản nháp, dữ liệu không đổi.
- 3a. Giá chưa được phép, nguồn stale/missing hoặc thiếu policy: hệ thống trả ERR-PUB-422-02 và giữ BLOCKED E8-Q03/04 cho phần phụ thuộc; không báo trang mẫu đã đầy đủ.
- 3b. Revision đổi trong lúc đọc: hệ thống kiểm lại nguồn; không ghép các revision lệch nhau để giả kết quả đủ.
- 5a. Nguồn không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có kết quả mẫu hợp lệ, không ghi dữ liệu nghiệp vụ.

### UC-PUB-006: Dựng thử thực đơn tuần

[Use case gốc](usecases/UC-PUB-006.md)

1. Khách chọn loại suất công khai, nhập số suất và lựa chọn kiêng nguyên liệu tại UI-PUB-04.
2. Hệ thống kiểm số suất nguyên dương và đầu vào thuộc tập được phép; không nhận trường bệnh lý/người ăn.
3. Hệ thống kiểm policy dựng thử và nguồn được duyệt trước khi yêu cầu bộ dựng xử lý nhu cầu.
4. Khi đủ điều kiện, bộ dựng trả phương án tuần mẫu theo đầu vào; hệ thống kiểm kết quả theo policy đã có căn cứ, không nới quy tắc cứng.
5. Hệ thống lọc kết quả thành nội dung công khai và trả mẫu có nhãn chưa áp dụng để khách xem.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Số suất âm, bằng 0 hoặc không nguyên: hệ thống trả ERR-PUB-422-01, yêu cầu sửa; chưa yêu cầu dựng mẫu.
- 3a. Chưa chốt engine/policy hoặc nguồn: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q05/04; không dựng kết quả giả.
- 4a. Không tìm được phương án: hệ thống trả trạng thái không có phương án; quy tắc cứng giữ nguyên, không tạo order.
- 4b. Dịch vụ dựng không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có mẫu hợp lệ, không báo hoàn tất.
- 5a. Nguồn đổi trước khi trả mẫu: hệ thống kiểm lại revision/nguồn; không trả mẫu phụ thuộc nguồn chưa được phép.

### UC-PUB-007: Gửi form tư vấn

[Use case gốc](usecases/UC-PUB-007.md)

1. Khách nhập thông tin liên hệ tối thiểu tại UI-PUB-05, đọc nội dung consent và thể hiện đồng ý theo bản được duyệt.
2. Hệ thống nhận thông tin, consent/version, nguồn và trialRef nếu có; kiểm trường bắt buộc và dữ liệu được phép.
3. Hệ thống đối chiếu provenance nguồn, tính hợp lệ của trialRef và điều kiện lưu/chống spam đã được phê duyệt.
4. Hệ thống lưu bền vững yêu cầu tư vấn kèm nguồn, consent và tham chiếu mẫu hợp lệ; không dùng customers/eaters làm nơi lưu mặc định.
5. Chỉ sau khi xác định bản ghi đã lưu, hệ thống trả mã tiếp nhận an toàn cho khách; không báo CRM đã nhận thay cho receipt bàn giao.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu consent hoặc trường bắt buộc: hệ thống trả ERR-PUB-422-01 và chỉ rõ trường cần sửa; chưa tạo lead.
- 3a. Chưa chọn nơi lưu/policy: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q06/07; không giả đã tiếp nhận.
- 3b. Vượt giới hạn chống spam đã duyệt: hệ thống trả ERR-PUB-429-01; không tự retry tạo yêu cầu mới.
- 4a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống trả thông báo chưa xác nhận hoàn tất theo ERR-PUB-500-01 và giữ mã yêu cầu để đối soát; trạng thái lưu chưa rõ, không gửi lại bằng định danh mới.
- 5a. Thông báo hoặc bên nhận CRM lỗi sau khi lưu: hệ thống giữ bản ghi/nguồn đã có; không dùng lỗi thông báo để phủ nhận việc lưu hoặc báo đã bàn giao.

### UC-PUB-008: Theo dõi điểm nối lead

[Use case gốc](usecases/UC-PUB-008.md)

1. CSKH chọn leadRef tại UI-PUB-08 để tra tình trạng bàn giao.
2. Hệ thống kiểm phiên, quyền đọc lead và phạm vi bản ghi.
3. Hệ thống đọc trạng thái bàn giao đã có cùng source/trialRef và receiptRef nếu bên nhận đã phản hồi.
4. Hệ thống phân biệt bản ghi đã lưu nhưng chưa receipt với trạng thái có receipt; lỗi bên nhận được hiển thị riêng.
5. Hệ thống trả tình trạng chờ bàn giao, lỗi hoặc đã có receipt để CSKH theo dõi; GET không gửi thông báo hay thực hiện bàn giao.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Phiên hết hạn hoặc thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; không trả thông tin lead, dữ liệu không đổi.
- 2b. Lead không tồn tại hoặc ngoài scope: hệ thống trả ERR-PUB-404-01; không lộ thông tin liên hệ.
- 3a. Chưa có receipt hoặc CRM không khả dụng: hệ thống hiển thị chờ E10/lỗi theo trạng thái đã lưu; lead và source/trialRef còn nguyên, không báo đã đồng bộ.
- 3b. Policy phụ thuộc chưa đủ: hệ thống hiển thị BLOCKED E8-Q06/07/11 với ERR-PUB-422-02 cho nhánh chưa thể xử lý; không tự bàn giao.
- 5a. Không đọc được dịch vụ: hệ thống trả ERR-PUB-503-01 và requestId an toàn; dữ liệu lead không bị sửa.

### UC-PUB-009: Soạn và sửa nội dung

[Use case gốc](usecases/UC-PUB-009.md)

1. Người soạn chọn nội dung tại UI-PUB-06, xem revision/version đang sửa hoặc bắt đầu nháp mới.
2. Người soạn nhập loại trang/bài/banner, title, body, slug và mediaRefs; gửi version khi cập nhật bản đã có.
3. Hệ thống kiểm phiên/quyền thao tác, slug, trường được phép và version; không nhận cờ công khai qua lệnh sửa.
4. Hệ thống kiểm nội dung HTML và media theo chính sách an toàn, không để script được thực thi/phát tán.
5. Hệ thống ghi revision nháp và audit, trả bản nháp/version mới; revision đang công khai giữ nguyên.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Version cũ: hệ thống trả ERR-PUB-409-01, yêu cầu tải lại để đối chiếu; không ghi đè bản mới.
- 3b. Hết phiên/thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01; nháp chưa được ghi.
- 4a. HTML có script hoặc media chưa an toàn: hệ thống ngăn thực thi/phát tán và yêu cầu rà nội dung; bản công khai giữ nguyên, chưa báo nháp hợp lệ.
- 3c. Policy quyền/media chưa đủ: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q08/09; không tự chọn CMS hay quyền.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01 và requestId để đối soát; kết quả lưu chưa rõ, không gửi lệnh mới để ghi đè.

### UC-PUB-010: Xem trước nội dung

[Use case gốc](usecases/UC-PUB-010.md)

1. Người soạn chọn contentId và revision cần xem trước tại UI-PUB-06.
2. Hệ thống xác thực phiên, quyền xem trước và phạm vi nội dung của người yêu cầu.
3. Hệ thống đọc đúng revision được yêu cầu và đối chiếu trạng thái nguồn để nhận diện bản đã thay đổi.
4. Hệ thống render nội dung/media an toàn và gắn nhãn nháp/xem trước.
5. Hệ thống trả bản xem trước chỉ trong phạm vi được phép; không đưa preview vào public cache hoặc index.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Phiên thiếu/hết hạn hoặc thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; không render bản nháp cho người yêu cầu.
- 3a. Nội dung không có hoặc ngoài scope: hệ thống trả ERR-PUB-404-01; không tiết lộ nội dung nháp, dữ liệu giữ nguyên.
- 3b. Revision đã cũ: hệ thống cảnh báo bản thay đổi để người soạn kiểm lại; không tự ghi hay công bố bản mới.
- 2b. Policy chưa được chọn: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q08; không mở preview công khai để vượt gate.
- 4a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có preview hợp lệ, revision không đổi.

### UC-PUB-011: Yêu cầu công bố hoặc thu hồi

[Use case gốc](usecases/UC-PUB-011.md)

1. Người có quyền chọn nội dung/revision tại UI-PUB-06 và rà bản muốn công bố hoặc thu hồi.
2. Người đó gửi contentId, revision, action và lý do thao tác.
3. Hệ thống kiểm phiên/quyền, policy duyệt và điều kiện độc lập người duyệt nếu workflow có duyệt.
4. Hệ thống kiểm revision, media và URL của nội dung đúng điều kiện công khai/thu hồi.
5. Khi đủ điều kiện, hệ thống ghi quyết định công bố hoặc thu hồi cùng audit, bảo đảm cache phản ánh quyết định.
6. Hệ thống trả revision công khai hoặc trạng thái thu hồi; bản đã thu hồi không tiếp tục được phục vụ công khai.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Thiếu phiên/quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; trạng thái công bố giữ nguyên.
- 3b. Chưa có policy hoặc thiếu điều kiện duyệt: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q08/09/02; chưa công bố/thu hồi.
- 4a. Revision đã thay đổi: hệ thống trả ERR-PUB-409-01, yêu cầu rà lại; không áp quyết định cũ cho bản mới.
- 4b. Media/URL chưa đủ điều kiện: hệ thống trả ERR-PUB-422-02; không công bố nội dung không an toàn.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01, giữ requestId để đối soát; chưa xác định hoàn tất, không báo public đã đổi thành công.

### UC-PUB-012: Quản lý ảnh và banner

[Use case gốc](usecases/UC-PUB-012.md)

1. Người quản trị chọn ảnh/banner tại UI-PUB-09 và cung cấp fileRef.
2. Người quản trị nhập altText, vị trí banner, quyền sử dụng và version khi cập nhật.
3. Hệ thống kiểm quyền thao tác, version, loại file an toàn và quyền đưa ảnh ra công khai.
4. Hệ thống đọc các vị trí/revision đang sử dụng ảnh để người quản trị rà tác động trước thay/gỡ.
5. Khi đủ điều kiện, hệ thống lưu media metadata nháp gắn với nội dung và audit, trả danh sách vị trí sử dụng; không tự công khai ảnh.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. File không thuộc loại ảnh an toàn được phép: hệ thống trả ERR-PUB-415-01; chưa ghi media hợp lệ hoặc đưa ảnh lên public.
- 3b. File private/thiếu quyền công khai hoặc policy: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q09/08; file không trở thành public.
- 4a. Ảnh đang được sử dụng: hệ thống hiển thị các vị trí để rà; khi chưa đủ quyết định gỡ/thay, liên kết đang dùng giữ nguyên.
- 3c. Phiên hết hạn/thiếu quyền hoặc version đã đổi: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01/ERR-PUB-409-01 tương ứng; không ghi đè metadata.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01 và mã yêu cầu để đối soát; trạng thái lưu chưa rõ, không báo hoàn tất.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-PUB-400-01 | Yêu cầu chưa đúng định dạng. | Sửa trường được chỉ ra |
| ERR-PUB-401-01 | Vui lòng đăng nhập. | Đăng nhập rồi mở lại |
| ERR-PUB-403-01 | Bạn không có quyền thực hiện. | Liên hệ quản trị quyền |
| ERR-PUB-404-01 | Không tìm thấy nội dung. | Quay lại danh sách |
| ERR-PUB-409-01 | Nội dung đã thay đổi hoặc yêu cầu trùng. | Tải lại/đối soát trước gửi tiếp |
| ERR-PUB-422-01 | Vui lòng kiểm tra thông tin nhập. | Sửa trường có lỗi |
| ERR-PUB-422-02 | Chưa đủ điều kiện cung cấp nội dung này. | Giữ chờ, quản trị rà gate |
| ERR-PUB-422-03 | Mapping URL chưa hợp lệ. | Sửa mapping, rà DL-08 |
| ERR-PUB-415-01 | Định dạng ảnh chưa được hỗ trợ. | Chọn ảnh phù hợp chính sách |
| ERR-PUB-429-01 | Bạn thao tác quá nhanh. | Chờ theo phản hồi; không tự retry tạo mới |
| ERR-PUB-500-01 | Chưa thể xác nhận đã hoàn tất. | Giữ mã yêu cầu, đối soát trước gửi lại |
| ERR-PUB-503-01 | Dịch vụ tạm chưa sẵn sàng. | Thử lại sau; không giả kết quả |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
