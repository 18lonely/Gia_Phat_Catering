# Báo cáo rà UC E6 — 12/11/2026

Chỉ BA/tài liệu. Workspace D:\BA không có Git; không tìm thấy AGENTS.md trong workspace hoặc D:\. Baseline hash trước sửa: [uc-baseline-sha256.json](uc-baseline-sha256.json). Đã đọc các mốc tiếp nối/DTO và dùng catalog, SRS, lifecycle, AC/test hiện có; không chạy generator hoặc sửa snapshot handoff/report cũ.

## Kết quả

[19/19 UC](../review/uc-operation-review.md) được rà và sửa: 12 có ghi HTTP, 3 worker, 2 đọc, 2 gate-only. Tách GET khỏi commit/receipt/retry key; worker khỏi actor mở UI; tách tạo plan và bếp đọc, reminder và theo dõi. Bỏ input profile/consent ở gate trong UC/SRS. Grant A chỉ mô tả request scope, không chốt một/nhiều công ty. Hướng dẫn kiểm thử dùng principal/evidence theo loại thao tác; giữ nguyên 57 dòng ca và trạng thái.

## Kiểm tra

- `check-e6.py`: exit0,0lỗi;19UC/57AC/26route/65bảng;29NOT RUN/28BLOCKED. Lượt đầu báo link manifest chưa tạo; đã bổ sung manifest và chạy lại đạt.
- `render-e6.cjs`: exit0;60tài liệu preview,8/8sơ đồ,0lỗi. [Preview](../preview.html).
- `check-dto-review.py`: exit0,34DTO/14gap;13file bảo toàn hash,0lỗi.
- `check-contract-review.py`: exit0,12INV và11file bảo toàn,0lỗi.
- `check-adapter-review.py`: exit0,26route/6oracle synthetic và12file bảo toàn,0lỗi;0route thực thi.
- Kiểm bổ sung bằng Python đối chiếu baseline:19UC đủ mã AC/TC và nhãn synthetic; bỏ mẫu ghi chung khỏi UC, kiểm nhánh GET/service/gate;24file bảo vệ giữ hash. Khôi phục riêng intro/frontmatter của bộ57ca để so hash với baseline xác nhận mọi dòng ca/status nguyên trạng. [Kết quả](uc-check-result.json).

Đây chỉ là kiểm cấu trúc tài liệu, oracle synthetic và bảo toàn nguồn, không backend/UAT/tải/pilot. Không sửa wireframe nên không chạy check-ui hoặc chụp lại desktop/mobile.

## Tiến độ, chặn và tiếp nối

40/78 feature thiết kế nháp (51,3%); E6 17/19 có điều kiện (89,5%), RTM19/19. 19UC/57AC/26HTTP/2port/13màn/8sơ đồ/65bảng. 34/34DTO đã rà;14gap OPEN,0/14đóng;0/8RVđóng. 99mô tả ca overlap:57ca29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED;0test backend.

Identity/scope, C→S/vượtT, nguồn/định lượng plan, hạn/quyền, persistence/event/receipt, envelope/presence và các policy còn chặn theo [sổ chung](../review/contract-gap-register.md). Không có evidence mới để đóng. Giữ E6-EVID-001/002 và Cost/O-02/O-03. Bước tiếp theo rà story/checklist/luồng còn dùng sai ranh giới, không lặp review UC hoặc tự mở policy; xem [prompt tiếp nối](../../gia-phat/review/next-session-prompt.md).

## File thay đổi

[Manifest đầy đủ so baseline](uc-change-manifest.md). Các nguồn sửa gồm19UC, SRS, hướng dẫn57ca, sổ gap, gap-analysis, dashboard, tiến độ và prompt; thêm ma trận UC/báo cáo/baseline/manifest/kết quả kiểm. Preview và sơ đồ được renderer cập nhật; không đổi wireframe/API/catalog/AC/schema hay handoff/report lịch sử.
