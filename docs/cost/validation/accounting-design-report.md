# Báo cáo đồng bộ thiết kế và rà bàn giao kế toán

Phiên bản0.1.0 ·11/11/2026 · BA tự rà thiết kế; **chưa có phê duyệt nghiệp vụ/UAT**.

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | Đồng bộ hợp đồng/dữ liệu/UI/backlog, kiểm nguyên tắc giá và khoản riêng, ghi điều kiện còn thiếu |

## 1. Kết quả theo yêu cầu

| Nhóm việc | Đã thực hiện | Phần chưa thể coi là hoàn tất |
| :--- | :--- | :--- |
| Thiết kế kế toán | PriceInput v0.2,8 giao tiếp API extension,4 bảng dữ liệu mới,4 màn tương tác,6 story/18 AC-test thiết kế | Chi tiết CK còn mở; backend/migration/settlement chưa thực hiện |
| Nhánh Cost | Có phương án cụ thể kiểm lại khi duyệt, tuần nguyên tử, hiệu lực bảng đặc thù và quyền xem | Chủ sở hữu chưa xác nhận; không tự đóng Q05/Q06/Q07/E3-Q16 |
| Dữ liệu thật | Người dùng xác nhận chưa có; thêm DATA-COST-Q01–06 ngay trong phiếu dữ liệu | Chưa có10 món/10 ngày thật, không chạy đối soát kế toán thật |
| Nhất quán/bàn giao | Epic/roadmap dùng tiêu chí cụ thể NFR-COST-002; điều kiện CHAN/CANH_BAO nhất quán; liên kết tài liệu đã rà | Chưa có người duyệt/ký baseline, chưa nghiệm thu phần mềm |

## 2. Bằng chứng kiểm tra kỹ thuật thiết kế

- DBML v0.4.0 compile/xuất MySQL được:61 bảng, không trùng tên; Cost gốc15 bảng giữ nguyên,4 bảng mở rộng ở nhóm riêng. Xuất DDL không phải chạy migration.
- Catalog Cost37 endpoint đã thay PriceInput; catalog extension8 method/path không trùng. 6 story gắn API/bảng/màn và18 scenario có Given/When/Then; không cộng6 FR-ACC vào45 FR Cost gốc.
- Playwright trên Chrome:4/4 màn chạy desktop1440px và mobile390px, không lỗi JS hoặc tràn ngang toàn trang.
- Kiểm giá100000 chưaVAT8% →108000,108000 đãVAT giữ nguyên, VAT theo amount8000, thiếuVAT bị chặn, gross phần lẻ chưa cho lưu.
- Cờ hóa đơnfalse giữ VATnull khi chưa biết, không tự gán0; lưu thỏa thuận draft không đổi snapshot đơn.
- Khoản riêng fixed2000×100 và preview5% của gross4000000 →200000; phải trả4000000 không đổi. Basis chưa rõ → calculatedAmount chưa xác định.
- Đơn đổi80 suất: tiền đơn3200000 do đổi số suất, khoản riêng cũ200000 giữ lại NEEDS_REVIEW; event replay không lặp, preview version cũ không lưu. Mất mạng không ghi draft; ghi chú HTML được escape khi hiển thị.
- Xem ảnh desktop/mobile: form, trạng thái và số tiền đọc được. Ẩn UI theo quyền chỉ là mô phỏng; không chứng minh bảo mật backend.

Script: [check-accounting-design.cjs](check-accounting-design.cjs). Ảnh: [desktop](accounting-desktop.png), [mobile](accounting-mobile.png).

```powershell
node docs/cost/validation/check-accounting-design.cjs "$env:TEMP/gia-phat-cost-validation"
python docs/cost/validation/check-backlog.py
python docs/cost/validation/check-usecases.py
```

108 ca baseline vẫn62 NOT RUN/46 BLOCKED,12 ca nghiệp vụ kế toán và18 ca thiết kế bổ sung chưa chạy backend. Các ca baseline dùng giá cost cuối; HTTP fixture nhập giá phải chuyển sang PriceInput v0.2, đặc biệt mã lỗi phần lẻ/basis theo hợp đồng mới. Số ca tài liệu không phải số test production đã PASS.

## 3. Quyết định và tiêu chí đã thống nhất ở mức tài liệu

Giữ xác nhận người dùng: cost gồm VAT phải trả, nhu cầu hóa đơn riêng, chiết khấu khoản riêng theo đơn không giảm phải trả. **Không tự chọn** cơ sở%/quyền/chi trả/thay đổi khoản sau hủy;10 câu CK vẫn CHỜ XÁC NHẬN.

SRS NFR-COST-002 là nguồn đối soát cụ thể: mỗi món sai lệch<=1đ, cost% mỗi ngày<=0,01 điểm phần trăm. Đã bỏ tiêu chí1% mơ hồ khỏi dòng nghiệm thu hiện hành của epic/roadmap. Dung sai không cho phép đảo nhãn đạt/vượt; vẫn so ngưỡng sau làm tròn theo BR-CALC-006. CHAN chặn gửi duyệt khi vượt, CANH_BAO cảnh báo; thiếu giá/VAT/bảng đặc thù vẫn chặn. Công bố theo cổng MENU, không thêm điều kiện cấm tuyệt đối trái chế độ.

## 4. Danh mục bàn giao hiện hành

- [Hợp đồng API](../api/accounting-contract.md), [catalog extension](../api/accounting-endpoints.json), [catalog Cost](../api/endpoint-catalog.json).
- [ERD/từ điển dữ liệu](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml).
- [Wireframe kế toán](../html-wireframe/accounting-workbench.html), liên kết từ18 màn Cost.
- [Backlog mở rộng](../userstories/accounting-backlog.md), [AC/test thiết kế](../accounting/design-tests.md).
- [Phương án nhánh Cost](../review/cost-branch-decisions.md), [câu hỏi CK](../accounting/business-rules.md), [câu hỏi dữ liệu](../review/accountant-input.md).

Trước khi triển khai: review quyền mới, phương án nhánh, rounding/migration legacy, activation hợp đồng giá và lifecycle khoản riêng. Trước nghiệm thu: có nguồn dữ liệu thật, môi trường/backend, actual/evidence và người có thẩm quyền duyệt. Gói này không ghi tên/ngày ký thay họ.
