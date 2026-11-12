---
id: DOC-E8-SRS-DATA-DICTIONARY-MD
title: Delta dữ liệu đề xuất E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Delta dữ liệu đề xuất E8

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

Không tăng số bảng hiện hành. Không thêm schema sức khỏe. Chưa chốt normalization, constraints DB, index hoặc transaction boundaries; các invariant cần backend evidence sau này.
