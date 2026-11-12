---
id: DOC-E9-EPIC-SPEC-MD
title: E9 — Agent Dinh dưỡng viên
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# E9 — Agent Dinh dưỡng viên

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

## Mục tiêu và phạm vi

Khách PER-01 (khách tiềm năng) và PER-02 (người đặt tổng) yêu cầu thực đơn tập thể, xem giải thích, đề nghị chỉnh và gửi nháp cho Gia Phát. [PRD](../gia-phat/01-prd.md) là nguồn 6 feature dưới; không thêm feature thứ bảy. Phạm vi ai được truy cập/khách vãng lai chưa quyết định E9-Q02.

| Feature | Mã cũ | Tên | Ưu tiên | Persona | Capability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-060 | AIN-01 | Agent tạo thực đơn tập thể | P0 | PER-01, PER-02 | Nhận yêu cầu; dựng nháp theo danh mục đã duyệt; kiểm bằng E2 |
| FEAT-061 | AIN-02, AIN-03 | Giải thích và chỉnh thực đơn | P0 | PER-01, PER-02 | Giải thích có nguồn; mỗi lần chỉnh kiểm lại toàn phương án |
| FEAT-062 | AIN-04 | Gửi nháp về Gia Phát / tạo lead | P0 | PER-01, PER-02 | Tiếp nhận đề xuất có nguồn; người thật duyệt trước áp dụng |
| FEAT-063 | AIN-05 | Gợi ý cá nhân qua agent | P1 | PER-03, PER-04 | GATE-ONLY: dùng FEAT-047; không có thiết kế gợi ý |
| FEAT-064 | — | Giới hạn lượt và ngân sách | P0 | PER-08 | Theo nhóm người dùng; trần chi phí AI theo ngày; tham số chưa chọn |
| FEAT-065 | — | Chặn truy cập cost | P0 | Hệ thống | BN-16: không công cụ/quyền đọc dữ liệu kinh tế nội bộ |

**5 feature có thiết kế nháp có điều kiện; FEAT-063 chỉ gate, không tính vào số có thiết kế.** Toàn dự án 56/78 ≈ 71,8% độ phủ tài liệu nháp (51 + 5); 3 gate-only ghi riêng: FEAT-046/047/063. Không là BA được duyệt hoặc tiến độ phần mềm.

Ngoài phạm vi: backend/migration, gọi AI thật, system prompt sản phẩm, chọn model/provider/hạ tầng, thuật toán gợi ý cá nhân, thu/suy luận sức khỏe, tư vấn y khoa/điều trị, tạo thực đơn chính thức/order/báo giá cam kết, CRM E10 và E10–E13. Không sửa schema 65 bảng.

## R9 và G-Next — nguyên văn roadmap

| Release | Tên đợt phát hành | Mục tiêu chính | Danh sách Feature ID | Cỡ | Điều kiện bắt đầu | Ngày dự kiến | Tiêu chí nghiệm thu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `R9` · v1.4.0 | Agent Dinh dưỡng viên (E9) | Khách tự yêu cầu thực đơn; người ăn được gợi ý | `FEAT-060` → `FEAT-065` | L | R5, R6, R8 xong | Chờ O-04 | Trên 30 yêu cầu thử, 100% thực đơn đạt quy tắc cứng; bộ thử 20 câu dò hỏi cost, giá nhập: 0 lần lộ; bộ thử 20 câu về bệnh lý: 100% có lời nhắc và không chẩn đoán; chi phí AI một ngày không vượt trần đã đặt |

**Cổng G-Next** (điều kiện để mở đợt Later): ≥ 90% order của các công ty đã chuyển lên hệ thống ghi nhận qua cổng (BO-06); ≥ 70% suất có lựa chọn của người ăn trước hạn chốt (BO-05); số phiên truy cập tự nhiên sau 60 ngày ≥ 90% mức trước chuyển đổi (BO-09).

R5, R6, R8 xong là điều kiện bắt đầu release; hiện chưa có bằng chứng đạt. Việc mở tài liệu E9 theo người dùng 12/11/2026 không miễn cổng G-Now/Next, không xác nhận nghiệm thu release. Không đặt lịch hoặc story point. Thứ tự chuẩn bị: review nguồn/quyền → review hợp đồng và gate → duyệt dữ liệu/bộ thử → mới xét điều kiện triển khai.

## Phân biệt với tiền thân E5

| Chiều | Agent Dinh dưỡng viên E9 / AIN | Agent Nội bộ E5 / AIO |
| :--- | :--- | :--- |
| Người dùng | PER-01/02; nhóm được dùng và xác minh chờ E9-Q02; PER-03/04 chỉ gate063 | Nội bộ PER-05; PER-08 tra log theo quyền |
| Công cụ | Chỉ projection công khai, kiểm nháp E2, dinh dưỡng an toàn; allowlist hẹp, không SQL/HTTP tùy ý | catalog.read, menu.validate, cost.validate; menu.applyDraft do orchestrator sau lệnh người dùng |
| Dữ liệu đọc | Món/công thức đã duyệt và được phép đưa ra khách; nguồn dinh dưỡng đã lọc; không cost/giá nhập/CK/khoản khoán | Theo giao quyền người dùng–dịch vụ; cost theo quyền, log có usage theo quyền |
| Cổng duyệt | SEND chỉ là đề xuất; người thật Gia Phát duyệt trước áp dụng; điểm nhận chưa chọn | Apply chỉ tạo MENU DRAFT; vẫn phải qua FEAT-013 để duyệt/công bố |
| Cách ly | Tài khoản dịch vụ, quyền DB, queue, hạn mức và cấu hình lời nhắc riêng; phiên này không viết prompt | Không tái dùng credential, queue hoặc quota AIO cho khách |

Nguồn [AIO SRS](../agent-noi-bo/srs/spec.md), [API](../agent-noi-bo/api/api-spec.md), AIO-Q01–06 còn mở. [Câu hỏi](review/questions.md) · [Phụ thuộc](review/dependencies.md) · [RTM](test/traceability.md). E6/E7/E8 dừng chờ trả lời; không hỏi lại hoặc đặc tả tiếp producer.
