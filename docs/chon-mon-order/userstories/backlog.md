---
id: DOC-CHON-MON-ORDER-USERSTORIES-BACKLOG
title: Backlog capability E6
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Backlog capability E6

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Story point chưa ước lượng; mỗi dòng dưới là capability story chưa phân rã đủ sprint. Đã có57AC cho19story; không tuyên bố19story ready khi các gate còn mở.

| Story | Feature / FR | Nội dung | Gate |
| :--- | :--- | :--- | :--- |
| US-E6-001 | FEAT-030; FR-AUTH-EXT-001 | Là một Gia Phát, tôi muốn cấp tài khoản người đặt tổng để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q01 |
| US-E6-002 | FEAT-031; FR-AUTH-QREG-001 | Là một Người ăn, tôi muốn đăng ký người ăn qua qr công ty để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q01 |
| US-E6-003 | FEAT-032; FR-AUTH-QSES-001 | Là một Người ăn qua QR, tôi muốn mở phiên qr không tài khoản để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q01 |
| US-E6-004 | FEAT-033; FR-AUTH-QRM-001 | Là một Người đặt tổng, tôi muốn quản lý qr và người ăn để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q02 |
| US-E6-005 | FEAT-034; FR-CUS-SVC-001 | Là một Dinh dưỡng viên, tôi muốn quản lý dữ liệu phục vụ tối thiểu để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q03 |
| US-E6-006 | FEAT-035; FR-ORD-QTA-001 | Là một Người đặt tổng, tôi muốn đặt định mức công ty để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q04 |
| US-E6-007 | FEAT-036; FR-ORD-SEL-001 | Là một Người ăn, tôi muốn chọn hoặc đổi món trong ngày để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q01, ORD-Q04 |
| US-E6-008 | FEAT-037; FR-ORD-WEEK-001 | Là một Người ăn có tài khoản, tôi muốn chọn trước cả tuần để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q05 |
| US-E6-009 | FEAT-038; FR-ORD-SUB-001 | Là một Người đặt tổng, tôi muốn tổng hợp và chốt số suất để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q06 |
| US-E6-010 | FEAT-039; FR-ORD-DEF-001 | Là scheduler có service principal, tôi muốn gán phần chưa chọn về mặc định trong cùng PORT-LOCK của US-E6-011; không job hoặc commit riêng. | ORD-Q06, ORD-Q07 |
| US-E6-011 | FEAT-040; FR-ORD-LOCK-001 | Là scheduler có service principal, tôi muốn khóa số tại hạn qua PORT-LOCK, commit revision/outbox; worker tạo plan sau. Vận hành GET kết quả không kích hoạt job. | Q-16, ORD-Q07 |
| US-E6-012 | FEAT-041; FR-ORD-CHG-001 | Là một Người đặt tổng/nội bộ, tôi muốn đề nghị đổi sau chốt để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | Q-16, O-06, ORD-Q08 |
| US-E6-013 | FEAT-042; FR-ORD-PXY-001 | Là một Dinh dưỡng viên, tôi muốn nhập hộ order để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q06 |
| US-E6-014 | FEAT-043; FR-ORD-REM-001 | Là scheduler có service principal, tôi muốn gửi nhắc qua PORT-REM; vận hành GET reminder-runs chỉ theo dõi, không gửi lại. | Q-14 |
| US-E6-015 | FEAT-044; FR-ORD-MODE-001 | Là một Người đặt tổng, tôi muốn tắt chọn món theo khách để số chọn/đặt/sản xuất được xử lý đúng phạm vi và truy vết. | ORD-Q09 |
| US-E6-016 | FEAT-045; FR-NUTR-DSP-001 | Là người ăn, tôi muốn đọc thông tin món công bố qua GET; không tạo Calculation, receipt hoặc commit nghiệp vụ. | NUTR-Q03 |
| US-E6-017 | FEAT-046; FR-NUTR-PROF-001 | Là người ăn có tài khoản, tôi muốn thấy cổng GATE-046 chưa mở; không nhập profile/consent hoặc thu dữ liệu sức khỏe. | O-03 |
| US-E6-018 | FEAT-047; FR-NUTR-REC-001 | Là người ăn có tài khoản, tôi muốn thấy cổng GATE-047 chưa mở; không thu hồ sơ hoặc chạy thuật toán gợi ý. | O-03 |
| US-E6-019 | FEAT-048; FR-PLAN-MEAL-001 | Là bếp trưởng/quản lý cơ sở, tôi muốn GET kế hoạch/revision do worker chuẩn bị; đọc không build/publish/ack/start-production. | ORD-Q10 |

## Bổ sung 0.2.0 — điều kiện review

19 mã story trên được giữ để không phá truy vết. [57 AC](acceptance-criteria.md), [19 UC](../srs/usecase-diagram.md), [RTM đầy đủ liên kết](../test/traceability.md) và [57 ca bổ sung](../test/review-test-cases.md) thay nhận định “chỉ có AC chọn/chốt”. Nội dung chi tiết mỗi story nằm ở UC/AC tương ứng số thứ tự; chưa story point hay nhãn sprint-ready. Story 017/018 chỉ đặc tả gate, chưa có happy path sức khỏe được duyệt.

Definition of Ready đề xuất: có người duyệt và nguồn quyết định cho các gate tác động; chốt API/data delta; fixture/expected được QA review; policy deadline/identity/version rõ. Definition of Done phần mềm phải gồm build, security/load test, evidence và pilot theo roadmap; tài liệu này không đạt thay phần mềm.

Làm rõ 12/11/2026 — DOCUMENT_CLARIFIED: grant phạm vi A trong ví dụ synthetic chỉ là scope yêu cầu, không chốt một/nhiều công ty. GET không retry bằng Idempotency-Key. Căn cứ [ma trận UC](../review/uc-operation-review.md), [catalog](../api/endpoint-catalog.json), SRS và AC/TC cùng số; không đổi mã story/gate hoặc tạo capability mới.
