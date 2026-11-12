---
id: DOC-E8-TEST-EVIDENCE-PROTOCOL-MD
title: Protocol bằng chứng QA
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Protocol bằng chứng QA

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Mỗi ca runtime cần environment/build, dữ liệu nguồn/revision và quyền/consent/policy đã duyệt, requestId, thời điểm, response đã che PII, read-back và audit nếu ghi. GET kiểm không tạo domain object; URL test cần status/Location/final target và so bản nguồn.

Lead: tách fault trước commit, sau commit trước response, retry và receipt CRM; xác minh record+source cùng tồn tại. Không coi thông báo/email là bằng chứng commit. Public security: kiểm raw HTTP, HTML/SSR/meta/JSON-LD, asset/cache và log nhìn thấy, không chỉ screenshot. Publication: kiểm revision/public pointer/cache cả khi rollback. BO-09 cần export baseline và phép tính cùng window/filter, không screenshot số giả.

Actual/Evidence các ca sản phẩm để trống đến khi chạy được. Result checker/renderer/UI chỉ tài liệu/mock, không điền PASS vào ca runtime. Gate chưa giải đáp phải ghi BLOCKED cùng mã trước chạy. Không dùng fixture synthetic thay DL-08, R4 hoặc giá thật.
