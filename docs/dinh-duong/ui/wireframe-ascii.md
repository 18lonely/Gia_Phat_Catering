# Wireframe ASCII — Dinh dưỡng

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Phác thảo review, không phải UI đã chạy. Không có dữ liệu dinh dưỡng thực tế. Đơn vị luôn nằm cạnh số; thao tác lưu/tính chỉ bật khi đủ đầu vào. Quyền ẩn nút không thay kiểm quyền server.

## UI-NUTR-01 — Thành phần và độ phủ (API-NUTR-001/002/006/007)

```text
┌ DINH DƯỠNG / BẢNG THÀNH PHẦN ──────────────────────────┐
│ Tìm nguyên liệu [________]  Công thức [chọn 30 món...]  │
│ Độ phủ: --/-- [Kiểm độ phủ]   [Chỉ xem còn thiếu]       │
│ Nguyên liệu | Nguồn/ấn bản | Đủ/Thiếu | [Mở]            │
├ Chi tiết nguyên liệu ──────────────────────────────────┤
│ kcal/100g [ ]  Đạm g/100g [ ] Béo [ ] Bột đường [ ]     │
│ Phần ăn được % [ ]  Gram / đơn vị dùng [ ]             │
│ Nguồn [ ] Ấn bản [ ] Trang/mã thực phẩm [ ]             │
│ Lý do sửa [________________] Version [chỉ đọc]         │
│ [Lưu] [Hủy nhập] [Lịch sử phiên bản]                   │
│ Thiếu nguồn/quy đổi: thông báo ngay cạnh trường        │
└───────────────────────────────────────────────────────┘
```

Không tự điền ediblePct=100; nếu DB legacy có default thì vẫn yêu cầu xác nhận mapping. Hủy nhập chỉ bỏ thay đổi chưa lưu. Lịch sử hiển thị người/ngày/lý do/giá trị cũ mới, không có nút xóa lịch sử. 409 giữ form, hiện giá trị mới để người dùng đối chiếu; không tự ghi đè.

## UI-NUTR-02 — Dinh dưỡng món (API-NUTR-003/005)

```text
┌ MÓN / DINH DƯỠNG ──────────────────────────────────────┐
│ Món [ ] Công thức ACTIVE [ ] Ngày phục vụ [ ] [Tính]   │
│ ƯỚC TÍNH TỪ ĐỊNH LƯỢNG SỐNG                           │
│ Năng lượng -- kcal | Đạm -- g | Béo -- g | Bột -- g     │
│ Nguyên liệu | Gram ăn được | Bốn chỉ số | Nguồn/version│
│ [Xem kết quả cũ]  [Tính lại theo nguồn hiện hành]       │
│ Nguồn đã thay đổi / Thiếu nguyên liệu: ...             │
└───────────────────────────────────────────────────────┘
```

Thiếu dữ liệu thì dấu “--” và danh sách thiếu thay cho 0; không vẽ số tổng từng phần. Nguồn đã đổi không làm mất bản cũ; badge “Cũ” đi kèm thời điểm tính.

## UI-NUTR-03 — Dinh dưỡng tổ hợp suất (API-NUTR-004/005)

```text
┌ SUẤT / CHỌN TỔ HỢP ────────────────────────────────────┐
│ Thực đơn [ ] Version [ ] Ngày [ ] Loại suất [chỉ đọc] │
│ Món chính: ( ) A  ( ) B   / số món cần chọn: ...        │
│ Món cố định: [danh sách phụ/rau/canh từ ngày]           │
│ [Tính tổ hợp này]                                     │
│ Ước tính từ định lượng sống | Tổng bốn chỉ số          │
│ Đã gồm: [tên và recipeId] | Chưa gồm: [nếu chưa rõ]     │
│ [Mở phân rã từng món] [Quay về thực đơn]               │
└───────────────────────────────────────────────────────┘
```

Món cố định bắt buộc được đưa vào request, không chọn lặp. Nếu cơm/gia vị chưa được xác định thuộc suất, hiển thị phạm vi đã tính và câu hỏi NUTR-Q03, không gọi đây là số đã nghiệm thu cho suất đầy đủ. Có nhiều món chính thì UI chọn đúng số theo loại suất, không ép luôn một món.
