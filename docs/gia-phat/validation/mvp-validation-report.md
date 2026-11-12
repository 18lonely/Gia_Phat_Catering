# Báo cáo tự kiểm thiết kế E4/E5

Phiên bản 0.1.0 · 2026-11-11 · Draft. Đây là tự kiểm tài liệu, chưa phê duyệt nghiệp vụ hoặc nghiệm thu phần mềm.

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Ghi kết quả kiểm cấu trúc/truy vết và giới hạn bằng chứng |

## Kết quả đã chạy

| Kiểm tra | Kết quả | Giới hạn |
| :--- | :--- | :--- |
| check-mvp-review.py | Đạt: 11 FR/story, 33 AC, 60 TC, 13 method/path duy nhất; FR có UC/story/AC/test, BR/ERR/NFR có ca; liên kết nội bộ của gói không gãy | Kiểm cấu trúc; không chứng minh mọi tổ hợp nghiệp vụ đã được bao phủ |
| DBML → MySQL bằng @dbml/core hiện có trong thư mục kiểm Cost | Đạt: 65 bảng, tên không trùng, refs xuất được; [DDL để review](schema-review.sql) | Không chạy DDL/migration; CHECK trong note/ERD vẫn phải triển khai sau |
| Decimal giả định | Đạt: món 40 kcal/4g/0,8g/6g, tổ hợp50 kcal/5g/1g/7,5g; mốc HALF_UP1,005→1,01 | Không xác minh nguồn thực phẩm; rounding là đề xuất NUTR-Q04 |
| check-backlog.py của Cost | Đạt: 28 story,108 scenario;43 FR có luồng,2 hoãn;24 BR,14 lỗi SRS,6 lỗi API,8 NFR | Baseline vẫn62 NOT RUN/46 BLOCKED |
| check-usecases.py của Cost | Đạt:16 UC,45 dòng ma trận, liên kết và mã tham chiếu | Không chạy luồng phần mềm |
| check-reconciliation.py của Cost | Đạt:10 món/10 ngày giả định và3 mốc làm tròn;32 điểm review giữ trạng thái chưa chốt chi tiết | Không có đối soát kế toán thực tế |
| node --check check-accounting-design.cjs | Đạt cú pháp sau cập nhật số bảng61→65 | Không chạy lại bộ tương tác trình duyệt kế toán vì không sửa UI kế toán; không ghi nhận kết quả UI mới |

Nguồn máy đọc: [mvp-check-result.json](mvp-check-result.json). Gói: [bàn giao](../review/mvp-e4-e5-handoff.md). Lần chạy đầu báo liên kết tới chính file kết quả chưa tồn tại; file được sinh và lần kiểm lại đạt. Không còn lỗi cấu trúc trong lần chạy cuối.

## Trạng thái test phần mềm

| Phân hệ | Tổng ca đã viết | NOT RUN | BLOCKED | Đã chạy backend |
| :--- | ---: | ---: | ---: | ---: |
| Dinh dưỡng | 28 | 23 | 5 | 0 |
| Agent Nội bộ | 32 | 28 | 4 | 0 |
| Tổng gói mới | 60 | 51 | 9 | 0 |

NOT RUN vẫn cần backend/môi trường. BLOCKED còn cần quyết định, dữ liệu hoặc baseline được chỉ ra ở từng ca. Không cộng60 ca này vào108 ca Cost thành tỷ lệ nghiệm thu. Kết quả tự rà đạt không phải chữ ký BA/QA/stakeholder. Mermaid và wireframe ASCII chưa render/kiểm trực quan; chưa có test hiệu năng, bảo mật thực thi, UI hoặc model.

## Tái chạy

```powershell
python docs/gia-phat/validation/check-mvp-review.py
python docs/cost/validation/check-backlog.py
python docs/cost/validation/check-usecases.py
python docs/cost/validation/check-reconciliation.py
node --check docs/cost/validation/check-accounting-design.cjs
```

DBML được export bằng thư viện `@dbml/core` đã có tại `$env:TEMP/gia-phat-cost-validation/node_modules`, không cài thêm dependency và không kết nối DB. DDL là ảnh chụp phục vụ review tại thời điểm này, DBML mới là nguồn thiết kế hiện hành.
