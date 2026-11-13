# Gói review và bàn giao Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft.

## Tài liệu để bắt đầu review

1. [Sổ 32 điểm mở](decision-register.md): nguồn, người cần xác nhận, phương án thảo luận, đánh đổi và tài liệu phải cập nhật.
2. [46 ca đang bị chặn](blocked-tests.md): điều kiện thiếu, nhóm xử lý đề xuất và bằng chứng cần có.
3. [Phiếu dữ liệu kế toán](accountant-input.md): 10 món/10 ngày thực tế, chưa điền số giả vào ô xác nhận.
4. [10 món/10 ngày giả định](../test/fixtures/README.md): ví dụ số và file JSON để đội kỹ thuật đọc; đã kiểm số học bằng Decimal.
5. [Backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [108 test case](../test/test-cases.md), [RTM](../test/traceability.md), [API](../api/api-spec.md), [wireframe](../html-wireframe/cost-workbench.html).

## Kịch bản review đề xuất

| Phiên | Người tham gia theo vai trò | Đầu ra cần ghi |
| :--- | :--- | :--- |
| Công thức và dữ liệu | Kế toán, dinh dưỡng viên, Giám đốc | Quyết định O-01, E3-Q1/Q2/Q4/Q12/Q14/Q15/Q16; nguồn10 món/10 ngày |
| Luồng và quyền | BA, Giám đốc, kế toán | Q01/Q04/Q05/Q06/Q07, quyền bếp, người duyệt/thay thế; ví dụ ngày/cơ sở cho từng quyết định |
| Hợp đồng kỹ thuật | Tech lead, BA, QA | Mã NCC ngừng; version/transaction, idempotency24h, store/outbox, cảnh báo nguyên liệu; kế hoạch migration |
| Bộ kiểm thử | QA, BA, Tech lead | Chốt expected, fixtures, ưu tiên chạy, build/môi trường và người ghi evidence |
| Phần sau R3 | Chủ sản phẩm và người phụ trách | P1/P2, ngân sách agent Q09; hai FR hoãn chỉ mở khi có quyết định phạm vi |

Đây là đề xuất tổ chức, chưa gửi lời mời hay giao việc cho ai. Ngày họp, người phụ trách cụ thể và hạn hoàn thành còn trống.

## Biên bản quyết định: sao chép cho từng mã

| Trường | Nội dung |
| :--- | :--- |
| Mã điểm mở / phiên bản tài liệu | Chưa điền |
| Phương án được chọn và lý do | Chưa quyết định |
| Ví dụ đầu vào → kết quả, trường hợp biên/lỗi | Chưa điền |
| Phạm vi áp dụng / thời điểm hiệu lực | Chưa điền |
| Người quyết định / ngày / liên kết bằng chứng | Chưa có |
| FR/BR/API/schema/UI/AC/test bị ảnh hưởng | Đối chiếu sổ quyết định và RTM trước khi đóng |
| Người cập nhật / người kiểm tra | Chưa phân công |

Một điểm chỉ đóng khi có quyết định có nguồn, các tài liệu bị ảnh hưởng đã đồng bộ và người review kiểm lại ví dụ/ca biên. Chốt nghiệp vụ không đồng nghĩa test đã PASS; sau khi đủ đầu vào, ca chuyển sang NOT RUN rồi mới chạy.

## Điều kiện chuyển sang triển khai và UAT

| Cổng | Bằng chứng cần có | Hiện tại |
| :--- | :--- | :--- |
| Baseline nghiệp vụ | Phạm vi R3, cấu hình, quyền, luồng ngoại lệ được chủ sở hữu review | Chưa ký duyệt |
| Thiết kế kỹ thuật | API/migration/ràng buộc/transaction, ownership MENU–COST và xử lý retry nhất quán | API/ERD nháp; chưa có migration/backend |
| Bộ đối soát | Dữ liệu kế toán có nguồn và expected độc lập | Chỉ có dữ liệu giả định |
| Môi trường test | Build, DB test, role accounts, seed/reset, job clock, đo tải/log | Chưa có bằng chứng môi trường trong gói này |
| Kết quả test | Actual/evidence cho ca thuộc release, defect và retest | 0 ca backend đã chạy |
| UAT | Người nghiệm thu, phạm vi, ca kiểm và tiêu chí xử lý lỗi còn mở được thống nhất | Chưa ký duyệt |

Mẫu evidence mỗi lần chạy: TC ID, build/commit, môi trường, ngày giờ, tài khoản/vai trò/cơ sở, fixture/version, requestId, expected, actual, trạng thái, ảnh/log đã lọc, defect và retest. Không ghi token hoặc dữ liệu nhạy cảm không cần thiết vào báo cáo.

## Kiểm tra gói tài liệu

```powershell
python docs/cost/validation/check-backlog.py
python docs/cost/validation/check-reconciliation.py
```

Hai script kiểm truy vết và số học mẫu; không gọi backend, không thay test chức năng/NFR/UAT. [Báo cáo khoảng trống](../gap-analysis.md) ghi phần còn thiếu.

## Cập nhật từ phiên nghiệp vụ kế toán

Người dùng đã xác nhận một phần O-01 và cách chiết khấu khách ghi riêng: xem [nghiệp vụ](../accounting/business-rules.md), [CR](../cr/CR-COST-2026-001.md), [hướng dẫn kế toán](../user-guide.md), [12 ca mới](../accounting/acceptance.md). Sổ32 mục hiện có O-01 PARTIALLY_CONFIRMED; không thay108 ca cũ bằng trạng thái đã đạt. Hai bộ có phạm vi riêng.

## Bản bàn giao thiết kế kế toán v0.2

[API v0.2](../api/accounting-contract.md) · [DBML/ERD v0.4](../../nen-tang/srs/erd.md) · [4 màn](../html-wireframe/accounting-workbench.html) · [6 story/18 ca](../userstories/accounting-backlog.md) · [báo cáo tự rà](../validation/accounting-design-report.md).

- Tiêu chí thiết kế đã thống nhất NFR-COST-002 ở SRS/epic/roadmap; chưa có chữ ký stakeholder hay dữ liệu test thực tế.
- FLOW-Q05/Q06/Q07/E3-Q16 có phương án chi tiết tại [nhánh mở](cost-branch-decisions.md); không đánh dấu đã chốt.
- Người dùng đã xác nhận chưa có dữ liệu; DATA-COST-Q01–06 được ghi trong phiếu kế toán. Không dựng dữ liệu thật thay người cung cấp.
- DBML compile và wireframe tương tác đạt kiểm kỹ thuật; chưa có migration chạy, API triển khai hoặc UAT.
