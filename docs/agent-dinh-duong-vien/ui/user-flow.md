# User flow — E9

Draft · 12/11/2026 · Các nhánh thành công chỉ là thiết kế có điều kiện, chưa mở vận hành.

## PER-01 / PER-02

```mermaid
flowchart TD
 A[Khach mo agent] --> B{Identity consent policy du?}
 B -->|Khong| X[Chan an toan UI07]
 B -->|Co| C[Nhap loai suat so suat khau vi]
 C --> D{Input ro va khong suc khoe?}
 D -->|Khong ro| C
 D -->|Benh ly| X
 D -->|Goi y ca nhan| G[Gate 063 dong UI07]
 D -->|Hop le| E{Quota budget reserve du?}
 E -->|Khong| Q[Het luot hoac tam chan UI06]
 E -->|Co| F[Dung candidate tu nguon duyet]
 F --> H{E2 kiem cung dat?}
 H -->|Loi hoac vi pham| X
 H -->|Dat| I[Xem nhap va giai thich UI02]
 I --> J[Chinh UI03]
 J --> E
 I --> K{Gui nhap va consent du?}
 K -->|Chua du hoac source stale| X
 K -->|Du| L{Noi nhan da chot va luu ben vung?}
 L -->|Khong| X
 L -->|Co| M[Receipt UI04 cho nguoi that]
```

Happy: yêu cầu khả thi→kiểm→giải thích→chỉnh→kiểm lại→xác nhận gửi→receipt. Error: mất phiên, sai input, quota, validator/provider lỗi, gate chưa chốt, không có nơi lưu. Edge: hai tab sửa cùng revision; source đổi giữa xem và gửi; retry sau mất ACK; thu hồi quyền giữa tool; kiêng kỵ tự do không rõ không suy thành bệnh. PER-01 không mặc định guest được phép; PER-02 không tự được dùng data công ty ngoài scope. Không thử mở FEAT-063 theo persona.

## PER-08 có quyền hạn mức

```mermaid
flowchart TD
 A[Mo quan tri UI05] --> B{Quyen duoc cap?}
 B -->|Khong| X[403 an toan]
 B -->|Co| C[Xem policy va usage da loc]
 C --> D{Usage da xac nhan?}
 D -->|Khong| U[UNKNOWN giu reservation]
 D -->|Co| E[De nghi doi han muc va ly do]
 U --> E
 E --> F{Policy duyet thay doi da chot?}
 F -->|Chua| G[BLOCKED khong kich hoat]
 F -->|Co| H{Can duyet?}
 H -->|Co| I[Nguoi khac duyet theo E1]
 H -->|Khong| J[Kiem version va hieu luc]
 I --> J
 J -->|Xung dot| C
 J -->|Hop le| K[Audit va policy version moi]
```

Error: không quyền, không có policy/đơn vị, version conflict, lỗi audit không cập nhật thành công. Edge: giảm cap dưới spent+reserved chặn nhận mới, không xóa debt; đổi nhóm không cấp lại lượt lách trần; đổi ngày không xóa lượt đang chờ quyết toán; cần duyệt thì không tự duyệt. Q07/08/13 giữ BLOCKED, không đặt số cấu hình.
