# Wireframe ASCII — Agent Nội bộ

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Phác thảo luồng review; không gọi mô hình và không ghi MENU. Nút Áp dụng nháp là điểm xác nhận của người vận hành trong sản phẩm, không phải xác nhận cho việc soạn tài liệu này.

## UI-AIO-01 — Yêu cầu tuần (API-AIO-001)

```text
┌ AGENT NỘI BỘ / DỰNG THỰC ĐƠN ──────────────────────────┐
│ Loại suất [ ] Tuần bắt đầu [thứ Hai] Cơ sở [chọn nhiều]│
│ Kiêng nguyên liệu [chips]  Loại món [chips]            │
│ Yêu cầu thêm [____________________________________]   │
│ [Tạo phương án]     Đầu ra là nháp, cần người duyệt    │
│ Đang chờ / Đang kiểm quy tắc và cost — 00:00 / 01:00   │
│ Cần làm rõ: [câu hỏi] [Trả lời và gửi yêu cầu mới]     │
└───────────────────────────────────────────────────────┘
```

Chọn cơ sở trước; không có quyền thì không liệt kê. Kiêng kỵ được xác nhận thành chips nguyên liệu/món, không chỉ ẩn trong chat. Khi đang chạy khóa nút gửi trùng, vẫn có thể rời trang và xem runId; không có nút “hủy” giả khi chưa có hợp đồng hủy.

## UI-AIO-02 — Phương án và chỉnh bằng lời (API-AIO-002/003/004)

```text
┌ BẢN NHÁP ĐỀ XUẤT — RUN ... / REVISION ... ─────────────┐
│ Thứ | Chính | Phụ | Rau | Canh | Mặc định              │
│ ...                                                 │
│ Bảng kiểm: quy tắc cứng / mềm / điểm / lý do           │
│ Cost: Ngày × cơ sở | Đạt/Vượt/Thiếu | % nếu có quyền   │
│ Dinh dưỡng: có dữ liệu ước tính / chưa sẵn sàng        │
│ Đổi bằng lời [____________________________________]   │
│ [Tạo phương án sửa]  Diff: món cũ → mới tại ngày/slot │
│ [Áp dụng nháp] [Quay lại yêu cầu]                      │
├ Xác nhận áp dụng ─────────────────────────────────────┤
│ Ghi toàn tuần thành DRAFT. Chưa gửi duyệt/công bố.     │
│ [Xác nhận áp dụng] [Quay lại xem diff]                 │
└───────────────────────────────────────────────────────┘
```

Chỉ VALID có nút áp dụng. NEEDS_INPUT hiển thị câu hỏi; BLOCKED_DATA hiển thị nguyên liệu/nguồn thiếu; NO_SOLUTION nêu ràng buộc không đạt và cho sửa yêu cầu, không trình bày thực đơn lỗi như kết quả đạt. 409 nguồn cũ hiển thị yêu cầu chạy lại. Áp dụng thành công mở MENU DRAFT và nút “Đi tới quy trình duyệt” của MENU; không tự duyệt. Không có quyền Cost thì chỉ hiện kết luận an toàn, không lộ số trong tooltip, diff hoặc log.

## UI-AIO-03 — Lượt chạy / nhật ký (API-AIO-005/006)

```text
┌ NHẬT KÝ AGENT NỘI BỘ ──────────────────────────────────┐
│ Từ [ ] Đến [ ] Người [ ] Trạng thái [ ] [Lọc]         │
│ Run | Người | Bắt đầu | Outcome | Token | Chi phí     │
│ ... | ...   | ...    | ...     | ...   | Chưa xác định│
├ Chi tiết run ─────────────────────────────────────────┤
│ Model/prompt version | RequestId | Thời gian          │
│ seq | tool | bắt đầu/kết thúc | kết quả đã lọc         │
│ FAILED/TIMEOUT: không có phương án để áp dụng          │
│ [Xem thêm sự kiện] [Tạo yêu cầu mới]                   │
└───────────────────────────────────────────────────────┘
```

Không hiển thị null cost thành 0đ. Người tạo chỉ xem run của mình theo quyền; màn tra cứu nhiều người yêu cầu aio.logs.read. Request/log bị escape khi hiển thị. Không có xuất log hoặc nút nâng quota trong MVP chưa được duyệt.
