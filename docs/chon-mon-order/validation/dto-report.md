# Báo cáo E6: hợp nhất gap và DTO

11/11/2026 · BA/tài liệu; baseline dto-baseline-sha256.json, không Git. Không chạy generator, không sửa wireframe hoặc snapshot bàn giao cũ.

## Kết quả

Sổ14gap có căn cứ/vai trò/artifact/điều kiện đóng;34DTO có ma trận presence/nullability. Sửa quy ước hiện diện API theo điều kiện đã có và qrId nullable tường minh. Không chọn omit/null ở nhánh chưa chốt; không thêm defaults/limits/route/ca test.

## Kiểm tra

- `python docs/chon-mon-order/validation/check-e6.py`: exit0,0lỗi;57AC,26route,65bảng và local links đạt. [Kết quả](check-result.json).
- `node docs/chon-mon-order/validation/render-e6.cjs`: exit0;59tài liệu preview,8/8sơđồ,0lỗi. [Kết quả](diagram-render-result.json).
- `python docs/chon-mon-order/validation/check-dto-review.py`: exit0,0lỗi;34type khớp thứ tự API;14gap đủ cột/mã;13file bảo toàn hash không đổi;3section mới có trong preview. [Kết quả](dto-check-result.json). Chỉ kiểm coverage tài liệu, không validator request/response runtime. Không test backend/UAT/tải/pilot hoặc chạy lại UI vì wireframe không đổi.

## Tiến độ và giới hạn

34/34DTO rà,14/14gap có owner vai trò/điều kiện đóng,0/14gap đóng;40/78feature thiết kế nháp,17/19E6 có điều kiện,0/8RV đóng.99mô tả ca overlap không đổi,0backend. E6-EVID-001/002 bảo toàn; [handoff](../review/dto-handoff.md) ghi việc tiếp theo.

## File thay đổi

[Manifest đầy đủ](dto-change-manifest.md): 8file mới, 8file thay đổi. Không đổi catalog, wireframe, DBML, evidence xác nhận hoặc handoff cũ.
