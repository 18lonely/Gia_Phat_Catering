---
id: DOC-E7-TEST-EVIDENCE-PROTOCOL-MD
title: Protocol bằng chứng E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Protocol bằng chứng E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

Test case giữ Actual/Evidence trống đến khi chạy sản phẩm. Với POST ghi actor/scope, nguồn/version trước, request (ẩn token), response/requestId, resource/audit sau và chứng từ; mất response phải phân biệt trước/sau commit. GET chụp nguồn trước/sau để chứng minh không tạo dữ liệu. Không dùng mock làm persistence evidence.

Ca thành công có gate: ghi quyết định/policy version đã được duyệt trước khi chạy; không giả policy bằng fixture. Link cần proof hợp lệ theo policy được duyệt, không in token. Kỳ LOCKED thử cả delivery/discrepancy/revenue/receipt và quyết định stale/tự duyệt; snapshot cũ phải còn nguyên.

Q-13 cần ví dụ được xác nhận trước oracle timeout/fallback. MISA cần sản phẩm/version/template, file hash/revision nguồn, biên nhận nhập hoặc lỗi thực tế. R7 cần tháng dữ liệu thật 2 khách và biên bản; không dùng synthetic. Không gửi yêu cầu ra ngoài trong phiên BA.

Giữ E6 CG/EVID, CK/DATA-COST và các snapshot lịch sử. Mỗi lần kiểm tài liệu ghi scope và công cụ riêng trong validation E7.
