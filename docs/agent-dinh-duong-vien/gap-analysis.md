---
id: DOC-E9-GAP-ANALYSIS
title: Rà khoảng trống E9
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, ai-agent, ain]
depends_on: [DOC-E9-SRS-SPEC-MD, DOC-E9-REVIEW-QUESTIONS-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E9: Agent Dinh dưỡng viên

Draft · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 13 FR, 13 UC, 11 API, 4 port, 3 state, delta mapping, 7 màn hình; đối chiếu kiến trúc AI agent 14/11/2026 |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [từ điển](srs/data-dictionary.md), [mapping](api/data-mapping.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API và allowlist](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [kiến trúc AI agent](../nen-tang/srs/agent-architecture.md).
- **Cách rà:** tìm trạng thái không có thao tác chuyển, yêu cầu riêng tư chưa có FR, và chỗ lệch giữa gói E9 (12/11) với kiến trúc agent viết sau (14/11).
- **Không làm:** không trả lời E9-Q01 đến E9-Q15, không thêm công cụ, không viết system prompt, không chọn nhà cung cấp.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E9-01` | Lệch tài liệu | API allowlist; kiến trúc AI agent mục 4.1, 6 | Kiến trúc 14/11 cho AIN công cụ "Tra cứu tài liệu" qua RAG chỉ mục công khai; allowlist E9 chỉ có 3 công cụ, không có RAG, không có quy tắc nguồn nào được vào chỉ mục công khai | High | Phân tích tác động bằng skill `cr` trước khi sửa E9; câu "ai duyệt tài liệu trước khi vào kho RAG" (đã ghi ở OVERVIEW 14/11) cần mã trong gói quyết định |
| `GAP-E9-10` | Lệch tài liệu | Kiến trúc AI agent mục 4.1; BR-AIN-006, BR-AIN-013 | Kiến trúc 14/11 cho AIN công cụ "Kiểm ngân sách" trả đạt hoặc không đạt; gói E9 cấm AIN nhận mọi nhãn có thể dùng dò ngưỡng cost, và cách trả kết quả khi vượt ngưỡng còn chờ E9-Q05 | High | Không sửa nguồn nào trong phiên này; đưa vào cùng phân tích `cr` với GAP-E9-01 để chọn một phía làm căn cứ |
| `GAP-E9-02` | Lệch tài liệu | NFR-AIN-007; API-AIN-003 | NFR yêu cầu tín hiệu đầu tiên trong 5 giây và kiến trúc dùng SSE, nhưng API chỉ có GET đọc trạng thái; chưa có kênh đẩy tiến trình | Medium | Gom vào E9-Q13; xác nhận có dùng SSE cho AIN không rồi bổ sung API |
| `GAP-E9-03` | Pháp lý / riêng tư | BR-AIN-011; NFR-AIN-006 | Không có FR, UC hay API cho khách xem lại hoặc yêu cầu xóa hội thoại và đề xuất của mình, dù NFR đặt hạn xóa 72 giờ | High | Gom vào E9-Q10; cần người phụ trách pháp lý xác nhận phạm vi xóa (chat, log, nhà cung cấp, bản sao lưu) |
| `GAP-E9-04` | Thiếu chức năng | State bản nháp gửi về | State có HUMAN_REVIEW, NEEDS_CLARIFICATION, DECLINED, REVIEWED_PROPOSAL nhưng không có FR cho người Gia Phát xử lý đề xuất, hay cho khách trả lời yêu cầu làm rõ | Medium | Gom vào E9-Q06; khi chọn đầu nhận thì quyết định phần xử lý thuộc E9 hay E10 |
| `GAP-E9-05` | Thiếu API | FR-AIN-CONF-001; API-AIN-010 | FR nói "nếu policy cần duyệt thì tạo đề nghị, tách người tạo khỏi người duyệt", nhưng chỉ có PUT; không có endpoint duyệt hoặc từ chối đề nghị đổi hạn mức | Medium | Gom vào E9-Q08; có thể dùng chung `change_requests` và `approvals` nền |
| `GAP-E9-06` | Thiếu chức năng | State lượt và ngân sách | UNKNOWN_HELD chuyển sang SETTLED "khi đối soát có bằng chứng", nhưng FR-AIN-LOG chỉ đọc; không có thao tác cho quản trị xác nhận đối soát hoặc nhập bằng chứng từ hóa đơn nhà cung cấp | Medium | Gom vào E9-Q07/13; chờ chọn nhà cung cấp để biết nguồn usage |
| `GAP-E9-07` | Cảnh báo | FEAT-064 | Không có FR cảnh báo quản trị khi sắp chạm trần ngày, khi có nhiều UNKNOWN_HELD, hoặc khi nhóm bị chặn | Medium | Đề xuất câu hỏi mới: ngưỡng và kênh cảnh báo; không tự đặt ngưỡng |
| `GAP-E9-08` | Dữ liệu thật | NFR-AIN-002, 003; R9 | Bộ 30 yêu cầu thực đơn, 20 câu dò cost, 20 câu bệnh lý và oracle chưa được soạn hay duyệt | High | Giữ BLOCKED E9-Q09; không dùng synthetic làm nghiệm thu R9 |
| `GAP-E9-09` | Lạm dụng | FR-AIN-SESS-001; FR-AIN-LIMT-001 | Hạn mức tính theo người và nhóm; nếu cho khách vãng lai (E9-Q02) thì chưa có biện pháp chống tạo nhiều phiên để vượt hạn mức | Medium | Gom vào E9-Q02; quyết định cùng cơ chế xác minh khách |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại delta trong mapping |

## 4. Giữ nguyên

E9-Q01 đến E9-Q15 giữ CHỜ TRẢ LỜI. FEAT-063 vẫn chỉ gate O-03; không thu, suy luận hay lưu dữ liệu sức khỏe. Câu đề xuất mới ở GAP-E9-01 và GAP-E9-07 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không backend, không gọi mô hình AI.
