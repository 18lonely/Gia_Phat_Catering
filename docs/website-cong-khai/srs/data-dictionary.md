---
id: DOC-E8-SRS-DATA-DICTIONARY-MD
title: Delta dữ liệu đề xuất E8
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# Delta dữ liệu đề xuất E8

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E8-Q12; XC-05; E8-Q13 |


Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

**Chỉ đề xuất, chưa merge vào65 bảng.** Logical entities dưới không phải DDL, không chọn CMS hoặc persistence. Mọi kiểu/length/index/retention cần review E8-Q06/08/12.

| Entity delta | Trường logic | Liên kết / invariant | Gate |
| :--- | :--- | :--- | :--- |
| pub_content_revisions | contentRef, revision, type, title, slug, sanitizedBody, mediaRefs, status, publicRevisionRef | Public pointer chỉ revision được phép; revision cũ giữ nguồn, version chống ghi đè | E8-Q08 |
| pub_url_mappings | inventoryRef, sourceURL, action, targetPath, revision, verification, activationEvidence | Một URL nguồn một quyết định trong revision, không vòng lặp; không coi bài xóa là miễn R8 | E8-Q01/02 |
| pub_sample_projections | publicSampleRef, menuRef/version, recipeRefs, nutrientCalculationRef, publicPriceRef, eligibilityEvidence | Chỉ trường allowlist; pointer vào nguồn không công khai ID nội bộ | E8-Q03/04 |
| pub_price_permissions | publicPriceRef, amount, displayBasis, approverEvidence, effectiveRange | Có thể thay bằng nguồn được xác nhận; không tự lấy ngưỡng giá | E8-Q03 |
| pub_trial_contexts | trialRef, allowedInputs, publicResult, provenance | Không hồ sơ người ăn/health; có cần lưu và expiry chưa quyết | E8-Q05/12 |
| pub_lead_intake | leadRef, minimalContact, source, consentVersion/evidence, trialRef?, receivedAt | Chỉ lưu khi policy đồng ý; nguồn đi cùng record, không dùng bảng khách thật | E8-Q06 |
| pub_lead_handoffs | leadRef, handoffIdentity, state, receiptRef?, lastErrorCode | Chưa receipt không ACK; không enum/phễu CRM | E8-Q06/07 |
| pub_media_metadata | fileRef, altText, rightsEvidenceRef, placements, revision | Chỉ file cho phép; ảnh/banner dùng revision nội dung | E8-Q09 |

> Chờ E8-Q13 — XC-05. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-05](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Không tăng số bảng hiện hành. Không thêm schema sức khỏe. Chưa chốt normalization, constraints DB, index hoặc transaction boundaries; các invariant cần backend evidence sau này.

## Quy ước tài liệu liên epic — XC-04

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E8-Q12 — XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
