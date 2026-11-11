# Báo cáo E6 — adapter/validation

11/11/2026 · BA/tài liệu; baseline adapter-baseline-sha256.json. Không Git, không chạy generator, không thay handoff/report cũ hoặc wireframe.

## Nội dung

Đối chiếu envelope E1/E6, NUTR/MENU projection/provenance và mapping error an toàn; sửa UC đọc món; matrix26route;6biến thể oracle synthetic (không6test mới). Đồng bộ dependency/RTM/evidence/gap/dashboard/prompt.

## Kiểm tra

- `python docs/chon-mon-order/validation/check-e6.py`: exit0,0lỗi;57AC,26route,65bảng và liên kết giữ hợp lệ. [JSON](check-result.json).
- `node docs/chon-mon-order/validation/render-e6.cjs`: exit0;56tài liệu trong preview,8/8sơ đồ,0lỗi. [JSON](diagram-render-result.json).
- `python docs/chon-mon-order/validation/check-adapter-review.py`: exit0,0lỗi;26/26route matrix khớp method/path catalog;6oracle đúng cấu trúc mong đợi;3section preview;12file bảo toàn hash không đổi. [JSON](adapter-check-result.json). Chỉ kiểm artifact/expected, không thực thi projection, API hoặc chính sách nghiệp vụ. Không chạy UI vì wireframe không đổi; không backend/UAT/tải/pilot. Các mapping adapter mới là đề xuất, E1-Q01/NUTR-Q03 và các ORD-Q giữ mở.

## Tiến độ / tiếp theo

26/26route có review;0/26được thực thi.40/78feature thiết kế nháp,17/19E6 có điều kiện,19/19RTM,0/8RV đóng.99mô tả ca có overlap,0test backend;57AC và trạng thái ca không đổi. [Handoff mới](../review/adapter-handoff.md) nêu gap và việc tiếp theo; E6-EVID-001/002 bảo toàn.

## File thay đổi

[Manifest đầy đủ](adapter-change-manifest.md): 9file mới, 11file thay đổi. Không đổi wireframe, catalog, DBML, evidence xác nhận hoặc các handoff cũ.
