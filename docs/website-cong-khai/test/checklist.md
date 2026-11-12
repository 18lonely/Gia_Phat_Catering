---
id: DOC-E8-TEST-CHECKLIST-MD
title: Checklist kiểm E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Checklist kiểm E8

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

- [ ] Đúng6 feature,5 P0 và FEAT-057 P1; không PUB-05/CRM E10.
- [ ] R8 nguyên văn; DL-08/R4/domain và G-Now/G-Next chưa tự đạt.
- [ ] FR→UC→story→AC→API→UI→test đầy đủ, gate có mã.
- [ ] Inventory thật khớp100%URL, giữ/301 không loop/open redirect; bài xóa/trùng có quyết định.
- [ ] Nguồn mẫu/giá/version/dị ứng đủ quyền;4 chỉ số có nhãn/đơn vị, missing khác0.
- [ ] Trial không hồ sơ sức khỏe, không order/Agent E9, không nới quy tắc cứng.
- [ ] Lead ghi bền vững+source, consent, không duplicate, receipt E10 và notification tách riêng.
- [ ] Không cost/giá nhập/cost%/khoản khoán/CK/nội bộ trong raw response/SSR/cache/error/media.
- [ ] Admin quyền/version/audit; script/upload/CSRF/IDOR; public không đọc preview.
- [ ] BO-09 baseline và công cụ có bằng chứng, không tính synthetic.
- [ ] UI desktop/mobile không tràn, modal/form/error/focus.
- [ ] Hash E1–E7/PRD/roadmap giữ;4 file tổng quan chỉ append.

[Ca AC](test-cases.md) · [ca hệ thống](system-cases.md) · [protocol](evidence-protocol.md). Checkbox chưa tích không phải kết quả kiểm phiên; xem validation report.
