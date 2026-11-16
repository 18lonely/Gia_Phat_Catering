---
id: DOC-REVIEW-OPEN-QUESTIONS-KHUON
title: Điểm cần BA quyết sau đợt chuẩn hóa khuôn
version: 0.1.1
phase: Review
domain: Gia Phát
tags: [review, khuon, error-matrix, data-dictionary, user-guide, knowledge-graph]
author: BA
last_updated: 2026-11-16
---
# Điểm cần BA quyết sau đợt chuẩn hóa khuôn

Draft · 16/11/2026 · Ghi lại các chỗ đã tự chọn hướng an toàn trong đợt tách ma trận lỗi, từ điển dữ liệu, viết user guide và sinh knowledge graph. Cột Quyết định để trống.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 2026-11-16 | BA | Sửa KH-01, KH-02, KH-10 (mục 4) |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo |

## 1. Đã làm

| Bước | Kết quả |
| :--- | :--- |
| Ma trận lỗi E1 đến E6 | 6 file `srs/error-matrix.md` mới; 6 `srs/spec.md` sửa. Số dòng ERR trước và sau khớp: 24, 33, 14, 9, 10, 4 |
| Từ điển dữ liệu E1 đến E5 | 5 file `srs/data-dictionary.md` mới; 5 `srs/erd.md` sửa. Tổng dòng bảng trước 658, sau 658 (không tính bảng lịch sử của file mới) |
| User guide | 12 file `user-guide.md` mới cho E1, E2, E4 đến E13; bản Cost giữ nguyên. Nội dung lấy nguyên văn luồng chính, nhánh rẽ của UC và ma trận lỗi |
| Knowledge graph | `docs/knowledge-graph.json` sinh theo Rule 18 |

## 2. Cần BA quyết

| Mã | Vấn đề | Hướng đã chọn tạm | Quyết định |
| :--- | :--- | :--- | :--- |
| KH-01 | Ba script kiểm cũ đọc mã ERR từ `srs/spec.md`: `gia-phat/validation/check-completion.py` (dòng 50), `gia-phat/validation/check-mvp-review.py` (dòng 35), `cost/validation/check-backlog.py` (dòng 16). Sau khi tách, chạy lại sẽ thấy 0 mã ERR và đạt rỗng | Không sửa script lịch sử. Nếu chạy lại cần đọc thêm `srs/error-matrix.md` | |
| KH-02 | Liên kết theo số dòng `spec.md#Lnnn` trong sổ quyết định, nhóm DEC, câu hỏi theo nghiệp vụ, rà liên epic đã lệch **từ trước** đợt này (ví dụ E2-Q1 trỏ `#L444` là dòng H-5, không phải E2-Q1) | Chỉ dịch số dòng theo phần đã tách, giữ nguyên độ lệch cũ. Nên đổi sang liên kết theo mục | |
| KH-03 | Từ điển miền CUS và ORD (mục 6.1, 6.2 ERD tổng) thuộc E6 nhưng việc giao chỉ gồm E1 đến E5 | Giữ nguyên trong `nen-tang/srs/erd.md`; E6 vẫn có từ điển delta riêng | |
| KH-04 | Bốn bảng mở rộng kế toán (`customer_price_terms`, `order_pricing_snapshots`, `order_discount_records`, `order_discount_events`) nối CUS và ORD nhưng do CR Cost tạo | Chuyển vào từ điển E3 theo nguồn CR-COST-2026-001 | |
| KH-05 | Mục 1 quy ước kiểu, mục 2 bản đồ miền, mục 5.3 công thức tính, mục 7 khung các miền sau là nội dung chung, không phải từ điển một epic | Giữ trong ERD tổng | |
| KH-06 | `nutrient_values` (mục 5.2 ERD tổng) nằm chung mục COST và NUTR | Chuyển vào từ điển E4 | |
| KH-07 | Không có template `46-knowledge-graph-index.md` mà skill `/kg` khai báo; số 46 trong kho là doc-drift | Sinh theo Rule 18, không có file bảng tra cứu riêng; tóm tắt nằm trong khóa `summary` của JSON | |
| KH-08 | 138 tài liệu chưa có `id` trong frontmatter (ví dụ OVERVIEW, PRD, SRS E4, E5) | Knowledge graph dùng id tạm `PATH:<đường dẫn>` | |
| KH-09 | 160 file khai báo `depends_on: [DOC-PRD-GIA-PHAT]` nhưng PRD không có frontmatter id | Giữ nguyên; cạnh này treo trong graph | |
| KH-10 | 2 liên kết hỏng có từ trước, trỏ tới `gia-phat/review/next-session-prompt.md` đã bị xóa (trong `project-dashboard.md` và `gia-phat/review/progress-assessment.md`) | Chưa sửa vì không rõ nên trỏ sang đâu | |
| KH-11 | User guide lấy nguyên văn bước của UC nên còn thuật ngữ kỹ thuật (requestId, scope, 409) | Giữ nguyên để không viết đoán; cần biên tập lại trước khi đưa người dùng cuối | |
| KH-12 | Không làm `api/test-checklist.md`, `api/production-readiness.md` | Theo chỉ dẫn, chờ có backend | |

## 3. Không có epic nào bị bỏ ở bước user guide

Mọi epic chưa có user guide đều có use case có luồng chính đánh số và có wireframe. E6 chỉ có 4 mã lỗi riêng nên bảng tra cứu sự cố ngắn.

## 4. Đã sửa ngày 16/11/2026

| Mã | Cách sửa | Kiểm |
| :--- | :--- | :--- |
| KH-01 | Ba script `check-completion.py`, `check-mvp-review.py`, `check-backlog.py` đọc thêm `srs/error-matrix.md` khi đọc `srs/spec.md` | Biểu thức của từng script đọc lại đúng 24 mã E1, 9 mã E4, 10 mã E5, 14 mã E3 |
| KH-02 | Liên kết `#Lnnn` trong sổ quyết định, nhóm DEC, câu hỏi theo nghiệp vụ và sổ câu hỏi E2, E3 được tính lại theo dòng thật của mã câu hỏi ở file đích; chữ "Nguồn, dòng N" cập nhật theo | 0 liên kết không tìm thấy mã; chạy lại không đổi thêm. Còn 169 liên kết theo dòng không gắn với mã câu hỏi nên giữ nguyên |
| KH-10 | Bỏ hai liên kết tới tệp prompt đã xóa trong `project-dashboard.md` và `gia-phat/review/progress-assessment.md` | 0 liên kết hỏng trong `docs/` |

Liên kết theo số dòng vẫn dễ lệch khi file nguồn đổi; KH-02 chỉ sửa trạng thái hiện tại.

