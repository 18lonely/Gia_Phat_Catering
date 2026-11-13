---
id: DOC-DECISION-PACK-REPORT
title: Báo cáo gói quyết định và kiểm bảo toàn
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [decision-pack, draft, review]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Báo cáo gói quyết định và kiểm bảo toàn

Nháp · 13/11/2026 · Chuẩn bị quyết định, chưa phê duyệt.

| Phiên bản | Ngày | Vai trò | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 13/11/2026 | BA | Hợp nhất nguồn để review; giữ câu mở |

## Kết quả bàn giao

219 mã nguồn, 197 nhóm DEC, 9 buổi họp. Mỗi mã một dòng; mọi nhóm có buổi họp. 0 câu được trả lời hoặc đóng. Độ phủ giữ 75/78; 0 feature được duyệt, 0 ca sản phẩm đã chạy. FEAT-046/047/063 chỉ gate O-03; FR-MENU-RCP-007 chờ O-02. Không mở epic hoặc viết thêm đặc tả.

Baseline chụp 1175 file hiện có trong docs trước khi viết gói; không chụp lại. Hai file tổng quan chỉ append. [Danh sách file tạo](files-created.json).

## Sổ đã đọc và số đếm

Đếm mã tại bảng câu nguồn; không đếm tham chiếu lặp, heading lặp hoặc mã evidence thành câu mới. Với sổ Cost, O-01/O-06/DL-01/E2-Q1/E2-Q5 đã có ở nguồn gốc nên không lặp dòng. Các mã RV E6 là phát hiện được CG dẫn chiếu, không là câu hỏi nghiệp vụ mới.

| Sổ / bảng nguồn | Phạm vi đếm | Số mã duy nhất đưa vào sổ |
| :--- | :--- | ---: |
| [docs/gia-phat/01-prd.md](../../../01-prd.md) | PRD | 6 |
| [docs/nen-tang/review/questions.md](../../../../nen-tang/review/questions.md) | E1 | 5 |
| [docs/nen-tang/srs/spec.md](../../../../nen-tang/srs/spec.md) | E1 | 6 |
| [docs/thuc-don-dinh-luong/srs/spec.md](../../../../thuc-don-dinh-luong/srs/spec.md) | E2 | 12 |
| [docs/gia-phat/brainstorms/quy-tac-thuc-don.md](../../../brainstorms/quy-tac-thuc-don.md) | E2 | 9 |
| [docs/cost/review/decision-register.md](../../../../cost/review/decision-register.md) | E3 | 27 |
| [docs/cost/accounting/business-rules.md](../../../../cost/accounting/business-rules.md) | E3 | 10 |
| [docs/cost/review/accountant-input.md](../../../../cost/review/accountant-input.md) | E3 | 6 |
| [docs/dinh-duong/review/questions.md](../../../../dinh-duong/review/questions.md) | E4 | 5 |
| [docs/agent-noi-bo/review/questions.md](../../../../agent-noi-bo/review/questions.md) | E5 | 6 |
| [docs/chon-mon-order/review/questions.md](../../../../chon-mon-order/review/questions.md) | E6 | 15 |
| [docs/chon-mon-order/review/contract-gap-register.md](../../../../chon-mon-order/review/contract-gap-register.md) | E6 | 14 |
| [docs/gia-phat/00-ke-hoach-tong-the.md](../../../00-ke-hoach-tong-the.md) | E6 | 1 |
| [docs/giao-nhan-doanh-thu/review/questions.md](../../../../giao-nhan-doanh-thu/review/questions.md) | E7 | 9 |
| [docs/website-cong-khai/review/questions.md](../../../../website-cong-khai/review/questions.md) | E8 | 12 |
| [docs/agent-dinh-duong-vien/review/questions.md](../../../../agent-dinh-duong-vien/review/questions.md) | E9 | 14 |
| [docs/crm-ban-hang/review/questions.md](../../../../crm-ban-hang/review/questions.md) | E10 | 15 |
| [docs/mua-hang-san-xuat/review/questions.md](../../../../mua-hang-san-xuat/review/questions.md) | E11 | 15 |
| [docs/phan-hoi-bao-cao/review/questions.md](../../../../phan-hoi-bao-cao/review/questions.md) | E12 | 18 |
| [docs/chi-phi-loi-nhuan/review/questions.md](../../../../chi-phi-loi-nhuan/review/questions.md) | E13 | 14 |
| Tổng | Khử trùng theo mã nguồn | 219 |

| Nhóm ước tính | Ước tính | Thực đếm | Chênh | Nguyên nhân |
| :--- | ---: | ---: | ---: | :--- |
| O | 6 | 6 | 0 | O-01–06 |
| E1 | 5 | 11 | +6 | Bổ sung N-01–04, Q-14 và Q-18 còn mở tại SRS |
| E2 / DL | 1 | 21 | +20 | DL-01; thêm E2-Q1–11 và H-1–9. H là câu con có mã riêng, không xóa khi gom DL |
| E3 | 19 | 43 | +24 | CK 10 + DATA-COST 6 + E3 16 + FLOW-COST 10 + QA-COST 1; ước tính chỉ lấy E3-Q14–16 |
| E4/E5 | 10 | 11 | +1 | NUTR 4 + DATA-NUTR 1 + AIO 6 |
| E6 | 31 | 30 | −1 | ORD 15 + CG 14 + Q-16; EVID-001/002 là hai bằng chứng, không phải câu mới |
| E7 | 9 | 9 | 0 | Gồm Q-13 |
| E8 | 12 | 12 | 0 | E8-Q01–12 |
| E9 | 14 | 14 | 0 | E9-Q01–14 |
| E10 | 15 | 15 | 0 | E10-Q01–15 |
| E11 | 15 | 15 | 0 | E11-Q01–15 |
| E12 | 18 | 18 | 0 | E12-Q01–18 |
| E13 | 14 | 14 | 0 | E13-Q01–14 |
| Tổng | 169 | 219 | +50 | Không sửa progress-status lịch sử |

Sổ Cost review có 32 dòng chỉ mục, trong đó 27 mã mới tính tại E3 và 5 mã nguồn lặp đã giữ ở PRD/E2. SRS E1 có 9 dòng điểm mở, 6 mã mới tính ở E1 và 3 mã O đã giữ tại PRD. SRS E2 có các tham chiếu O và H đã khử trùng về PRD/bảng quy tắc. [Danh mục máy](source-inventory.json) lưu phạm vi regex và mã đã đếm để kiểm lại độc lập.

## Nguồn nền và quy tắc đã đọc

- [Progress 12/11/2026](../../progress-status-2026-11-12.md): baseline lịch sử 60/78 và danh mục ước tính; không sửa.
- [OVERVIEW](../../../../OVERVIEW.md): ba mốc E11/E12/E13; [dashboard](../../../../project-dashboard.md) để giữ văn phong append.
- [PRD](../../../01-prd.md): O-01–06, BO-01/BO-02 và persona; [roadmap](../../../02-roadmap.md): R1–R13, G-Now/G-Next.
- [Dependencies E11](../../../../mua-hang-san-xuat/review/dependencies.md), [E12](../../../../phan-hoi-bao-cao/review/dependencies.md), [E13](../../../../chi-phi-loi-nhuan/review/dependencies.md).
- [E6 questions và EVID](../../../../chon-mon-order/review/questions.md), [CG và phương án nguồn](../../../../chon-mon-order/review/contract-gap-register.md), [RV](../../../../chon-mon-order/review/decision-findings.md). EVID-001 xác nhận danh sách; EVID-002 giữ ba nội dung mở.
- Bảy data dictionary E7–E13 và mapping E9; [danh mục delta](delta-inventory.json) dẫn từng dòng. [Schema](../../../../nen-tang/srs/schema.dbml) vẫn 65 bảng. ERD, Cost accounting/SRS và E7 SRS dùng để kiểm định nghĩa gốc.
- Tất cả 19 file quy tắc trong .claude/ba-kit/rules đã đọc; mẫu 48-meeting-minutes và 45-gap-analysis. Skill meet/gap/dashboard đã đọc. Mẫu dashboard được skill nhắc không có trong danh mục template; dùng cấu trúc tổng quan hiện hữu, không tạo template mới.

## Phân bố ưu tiên

| Mức | Số câu nguồn |
| :--- | ---: |
| P-MVP | 85 |
| P-NEXT | 68 |
| P-NOW | 4 |
| P-LATER | 62 |

P-NOW dùng cho nhánh Now chưa có căn cứ chặn R1–R5: E1-Q03/N-04 (MFA P1), FLOW-COST-Q10 (mô phỏng P2), E3-Q15 (nhiều MAIN không ảnh hưởng MVP K=1). Release của bốn mã để “chưa rõ”. Những release khác là phạm vi trực tiếp của epic được nối với roadmap, không khẳng định chặn toàn release nếu nguồn chỉ chặn một nhánh. Vai trò “chưa rõ” không được suy từ persona.

## Phân bố theo người quyết định

Đếm theo tổ hợp vai trò nguyên văn ở nguồn; mỗi câu một tổ hợp, không cộng lặp đồng chủ trì. “Người soạn docx” là vai trò nguồn, chưa gán tên.

| Vai trò / tổ hợp vai trò trong nguồn | Số câu |
| :--- | ---: |
| chưa rõ | 89 |
| Giám đốc | 16 |
| Dinh dưỡng viên | 14 |
| Kế toán | 11 |
| Người soạn docx | 8 |
| Giám đốc, kế toán | 6 |
| Giám đốc, Tech lead | 3 |
| Người đặt tổng, BA | 3 |
| Tech lead, BA | 2 |
| BA, Tech lead | 2 |
| Dinh dưỡng viên, Giám đốc | 2 |
| Kế toán, người phụ trách thỏa thuận khách | 2 |
| Dinh dưỡng viên, QA | 2 |
| Chăm sóc khách và vận hành | 2 |
| Tech lead | 1 |
| Dinh dưỡng viên, người duyệt | 1 |
| Người duyệt | 1 |
| Người soạn docx, bếp trưởng | 1 |
| Tech lead và BA | 1 |
| BA, kế toán, Tech lead | 1 |
| Kế toán, UX/BA | 1 |
| Giám đốc, BA | 1 |
| Kế toán, dinh dưỡng viên | 1 |
| Giám đốc, dinh dưỡng viên | 1 |
| BA, chủ sản phẩm/AI lead | 1 |
| Kế toán, vận hành, người phụ trách khách | 1 |
| Kế toán, vận hành, người duyệt | 1 |
| Kế toán, người duyệt | 1 |
| Kế toán, Giám đốc | 1 |
| Người phụ trách thỏa thuận khách, kế toán, Giám đốc | 1 |
| Dinh dưỡng viên, bếp trưởng | 1 |
| Chủ sản phẩm, dinh dưỡng viên | 1 |
| Gia Phát, BA | 1 |
| Vận hành | 1 |
| Người phụ trách khách, DDV | 1 |
| Người đặt tổng, DDV | 1 |
| Vận hành, Giám đốc | 1 |
| Giám đốc, bếp trưởng | 1 |
| Người đặt tổng | 1 |
| DDV, bếp trưởng | 1 |
| Gia Phát, Tech lead | 1 |
| DDV, vận hành | 1 |
| Bếp trưởng, vận hành | 1 |
| Chủ sản phẩm, phụ trách dữ liệu | 1 |
| BA, phụ trách khách, Tech lead/Auth | 1 |
| Chủ sản phẩm, BA, Tech lead | 1 |
| Chủ sản phẩm, vận hành, BA | 1 |
| Tech lead, BA, QA | 1 |
| Vận hành, người duyệt được chỉ định, BA | 1 |
| Bếp, vận hành, BA, Tech lead | 1 |
| BA, dinh dưỡng viên, Tech lead | 1 |
| Nền tảng/Auth, BA, phụ trách khách | 1 |
| Tech lead/API owner, BA | 1 |
| Owner MENU/NUTR, BA, Tech lead | 1 |
| API owner, BA, QA | 1 |
| Chủ sản phẩm/vận hành, BA, Tech lead | 1 |
| BA/UI, QA | 1 |
| Chủ sản phẩm, phụ trách dữ liệu, QA | 1 |
| Chủ nghiệp vụ chăm sóc khách và người phụ trách dữ liệu | 1 |
| Chủ dữ liệu khách và Giám đốc | 1 |
| Giám đốc và chủ dữ liệu khách | 1 |
| Chủ dữ liệu khách, kế toán và trưởng kỹ thuật | 1 |
| Chủ nghiệp vụ bán hàng và Giám đốc | 1 |
| Giám đốc và chủ nghiệp vụ bán hàng | 1 |
| Dinh dưỡng viên và người duyệt báo giá | 1 |
| Giám đốc và kế toán phụ trách hợp đồng | 1 |
| Kế toán và chủ nghiệp vụ bán hàng | 1 |
| Kế toán, người duyệt hợp đồng và vận hành | 1 |
| Trưởng kỹ thuật, chủ các nguồn và QA | 1 |
| Giám đốc, chăm sóc khách, kế toán và QA | 1 |
| Kế toán và Giám đốc | 1 |

## Nhất quán liên epic

0 ứng viên máy và 12 phát hiện thủ công. Phân bố: Cao: 4; Trung bình: 7; Thấp: 1. [Báo cáo XC](../cross-epic-consistency.md) có từng vị trí, mức, đề xuất và người xác nhận. Không có phát hiện máy bị bỏ khỏi báo cáo. Delta gồm 59 dòng thực thể/nhóm logic, không phải 59 bảng mới; danh mục giữ toàn bộ trường riêng nguồn và dẫn trường chung.

## Kiểm tự động

| Script | Kết quả | Bằng chứng |
| :--- | :--- | :--- |
| scan-cross-epic.cjs | PASS; 0 lỗi đọc/quét | [Kết quả](cross-epic-result.json) |
| check-decision-pack.cjs | PASS; 0 lỗi | [Kết quả](structure-result.json) |
| hash-check-decision-pack.cjs | PASS; 0 lỗi | [Kết quả](hash-result.json) |

Checker cấu trúc kiểm front-matter theo rule 18/19, tồn tại mã tại dòng nguồn, số đếm độc lập từ bảng, MD/JSON tương ứng, mọi nhóm có buổi họp, P-MVP ở buổi 1–3, ô trả lời/quyết định trống, link/file/anchor và số dính chữ trong văn xuôi mới. Trích nguyên văn nguồn được miễn sửa lỗi số dính chữ lịch sử để không đổi khuyến nghị; checker vẫn kiểm văn xuôi biên soạn mới.

Checker hash so SHA256/kích thước toàn bộ file cũ; hai file tổng quan so hash prefix theo kích thước cũ để chứng minh chỉ append. Phạm vi kiểm là docs theo yêu cầu baseline; thao tác ghi của các script đều nằm trong gói, ngoại trừ hai append được phép. Không chạy generator/checker cũ.

## Giải thích bốn sai lệch hash lịch sử E12

Đã xem git show 71e2a4c --stat: commit 71e2a4c ngày 12/11/2026 lúc 15:14 gỡ các liên kết đến phiên uc-refresh-2026-11-12 đã xóa. Bốn file: docs/OVERVIEW.md, docs/project-dashboard.md, docs/gia-phat/review/progress-assessment.md, docs/gia-phat/review/next-session-prompt.md; mỗi file giảm 2 dòng. Đây là thay đổi do người dùng đã giải thích, không phải sửa trong phiên này. Không khôi phục link, không ghi lại baseline E12. Baseline gói này chụp trạng thái hiện tại sau commit đó.

## Cần BA làm rõ

Người quyết định chưa được chỉ định đủ tại các dòng sau; vai trò tham dự họp chỉ để chuẩn bị, không thay người ký:

- DATA-COST-Q01 / DEC-80: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L90).
- DATA-COST-Q02 / DEC-81: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L91).
- DATA-COST-Q03 / DEC-82: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L92).
- DATA-COST-Q04 / DEC-83: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L93).
- DATA-COST-Q05 / DEC-84: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L94).
- DATA-COST-Q06 / DEC-85: chưa rõ người quyết định; [nguồn](../../../../cost/review/accountant-input.md#L95).
- Q-16 / DEC-10: chưa rõ người quyết định; [nguồn](../../../00-ke-hoach-tong-the.md#L423).
- Q-13 / DEC-114: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L18).
- E7-Q01 / DEC-115: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L19).
- E7-Q02 / DEC-116: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L20).
- E7-Q03 / DEC-117: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L21).
- E7-Q04 / DEC-118: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L22).
- E7-Q05 / DEC-119: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L23).
- E7-Q06 / DEC-120: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L24).
- E7-Q07 / DEC-121: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L25).
- E7-Q08 / DEC-122: chưa rõ người quyết định; [nguồn](../../../../giao-nhan-doanh-thu/review/questions.md#L26).
- E8-Q01 / DEC-123: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L18).
- E8-Q02 / DEC-124: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L19).
- E8-Q03 / DEC-12: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L20).
- E8-Q04 / DEC-15: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L21).
- E8-Q05 / DEC-13: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L22).
- E8-Q06 / DEC-125: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L23).
- E8-Q07 / DEC-126: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L24).
- E8-Q08 / DEC-127: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L25).
- E8-Q09 / DEC-128: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L26).
- E8-Q10 / DEC-129: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L27).
- E8-Q11 / DEC-130: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L28).
- E8-Q12 / DEC-131: chưa rõ người quyết định; [nguồn](../../../../website-cong-khai/review/questions.md#L29).
- E9-Q01 / DEC-02: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L18).
- E9-Q02 / DEC-132: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L19).
- E9-Q03 / DEC-133: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L20).
- E9-Q04 / DEC-12: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L21).
- E9-Q05 / DEC-134: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L22).
- E9-Q06 / DEC-135: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L23).
- E9-Q07 / DEC-136: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L24).
- E9-Q08 / DEC-137: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L25).
- E9-Q09 / DEC-138: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L26).
- E9-Q10 / DEC-139: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L27).
- E9-Q11 / DEC-13: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L28).
- E9-Q12 / DEC-15: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L29).
- E9-Q13 / DEC-140: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L30).
- E9-Q14 / DEC-01: chưa rõ người quyết định; [nguồn](../../../../agent-dinh-duong-vien/review/questions.md#L31).
- E11-Q01 / DEC-154: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L25).
- E11-Q02 / DEC-03: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L26).
- E11-Q03 / DEC-155: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L27).
- E11-Q04 / DEC-156: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L28).
- E11-Q05 / DEC-157: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L29).
- E11-Q06 / DEC-158: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L30).
- E11-Q07 / DEC-159: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L31).
- E11-Q08 / DEC-160: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L32).
- E11-Q09 / DEC-161: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L33).
- E11-Q10 / DEC-162: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L34).
- E11-Q11 / DEC-163: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L35).
- E11-Q12 / DEC-164: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L36).
- E11-Q13 / DEC-165: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L37).
- E11-Q14 / DEC-166: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L38).
- E11-Q15 / DEC-167: chưa rõ người quyết định; [nguồn](../../../../mua-hang-san-xuat/review/questions.md#L39).
- E12-Q01 / DEC-168: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L25).
- E12-Q02 / DEC-169: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L26).
- E12-Q03 / DEC-170: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L27).
- E12-Q04 / DEC-171: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L28).
- E12-Q05 / DEC-172: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L29).
- E12-Q06 / DEC-173: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L30).
- E12-Q07 / DEC-174: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L31).
- E12-Q08 / DEC-175: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L32).
- E12-Q09 / DEC-176: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L33).
- E12-Q10 / DEC-177: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L34).
- E12-Q11 / DEC-178: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L35).
- E12-Q12 / DEC-179: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L36).
- E12-Q13 / DEC-180: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L37).
- E12-Q14 / DEC-181: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L38).
- E12-Q15 / DEC-182: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L39).
- E12-Q16 / DEC-183: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L40).
- E12-Q17 / DEC-184: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L41).
- E12-Q18 / DEC-185: chưa rõ người quyết định; [nguồn](../../../../phan-hoi-bao-cao/review/questions.md#L42).
- E13-Q01 / DEC-186: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L25).
- E13-Q02 / DEC-187: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L26).
- E13-Q03 / DEC-188: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L27).
- E13-Q04 / DEC-189: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L28).
- E13-Q05 / DEC-190: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L29).
- E13-Q06 / DEC-191: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L30).
- E13-Q07 / DEC-192: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L31).
- E13-Q08 / DEC-14: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L32).
- E13-Q09 / DEC-193: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L33).
- E13-Q10 / DEC-03: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L34).
- E13-Q11 / DEC-194: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L35).
- E13-Q12 / DEC-195: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L36).
- E13-Q13 / DEC-196: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L37).
- E13-Q14 / DEC-197: chưa rõ người quyết định; [nguồn](../../../../chi-phi-loi-nhuan/review/questions.md#L38).

Release chặn chưa rõ: E1-Q03 / DEC-18; N-04 / DEC-24; E3-Q15 / DEC-58; FLOW-COST-Q10 / DEC-69. Giữ P-NOW theo phạm vi roadmap, không tự nâng thành gate MVP.

Các nguồn chỉ ghi tác động chung, không phân tích từng lựa chọn: cần người quyết định xác nhận trước khi dùng làm căn cứ chọn phương án. Các dòng CK/DATA-COST không có khuyến nghị riêng được để trống; không sáng tác phương án. Giữ nguyên bộ câu gốc nhiều nhánh tại link nguồn.

## Giới hạn

- Danh mục là mã câu/gap đang mở ở các sổ được yêu cầu và bảng SRS kế thừa phát hiện khi đọc; đề xuất chưa có mã và câu văn không thuộc sổ không tự được cấp mã nguồn mới. Các câu chưa mã tại accounting mục 6.2 cần BA xác nhận cách truy vết về O-01/E10-Q15/CR hiện có, không tự đóng.
- Chỉ gộp khi có quyết định chung rõ; 197 nhóm giữ nhiều câu độc lập để tránh gộp nhầm. Nhóm có câu nhiều nhánh cần ký từng nhánh; nhánh chưa ký vẫn mở.
- Số ca chỉ là đếm gate trực tiếp có mã; có overlap và có tài liệu dùng viết tắt/range. Ô trống nghĩa là chưa có số đếm trực tiếp đáng tin, không có nghĩa 0 ca bị chặn. Không dùng tổng này để đo test sản phẩm.
- Quét mã dựa cấu trúc bảng/heading; không coi tham chiếu là định nghĩa mới. So chức năng tự động dựa FR; rà ngữ nghĩa bổ sung FEAT-057/060, lead/proposal, cost/doanh thu. Không thay review hợp đồng kỹ thuật.
- Không có dữ liệu thật, người ký hoặc evidence triển khai mới; mọi kết quả kiểm chỉ áp dụng tài liệu. Không gọi mô hình AI, không backend, migration, commit hoặc xóa file.
