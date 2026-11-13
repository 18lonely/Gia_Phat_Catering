---
id: DOC-FOLLOWUP-REPORT
title: Báo cáo rà tiếp gói quyết định ngày 13/11/2026
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [draft, followup]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Báo cáo rà tiếp gói quyết định ngày 13/11/2026

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 13/11/2026 | BA | XC-01–12; DEC-27 và nhóm tách; BA-Q01–51; giữ câu trả lời trống |

Đã xử lý phần BA tự làm được trên tài liệu. Độ phủ giữ **75/78**; **0 câu được trả lời**, 0 feature được duyệt, 0 ca sản phẩm đã chạy. Đây không phải BA được duyệt. Không backend, migration, gọi mô hình AI, commit hoặc xóa file.

## Vai trò và release

| Phạm vi | Trước | Có căn cứ làm rõ | Chuyển thành câu BA còn mở |
| :--- | ---: | ---: | ---: |
| Vai trò của 219 câu gốc | 89 chưa rõ | 6 | 83 |
| Release của 219 câu gốc | 4 chưa rõ | 0 | 4 |

Căn cứ 5 câu E7-Q03–07: BRD dòng 130 xác định Kế toán là chủ nghiệp vụ giá nhập, doanh thu, đối soát; không cấp quyền duyệt ngoại lệ. E13-Q05: roadmap dòng 103 và epic-spec E13 dòng 29 yêu cầu Giám đốc duyệt nguyên tắc phân bổ. Mỗi dòng đã có file:dòng trong JSON và phần căn cứ của sổ Markdown.

URD dòng 65 và 247 vẫn giữ giả định người duyệt theo O-06; epic E11 dòng 35 và E12 dòng 39 nói persona không tự cấp quyền. PRD chưa chỉ định Product Owner. Không tìm thấy RACI đủ để điền các vai trò còn lại. Không suy release chỉ từ P1/P2 hoặc đợt Now. [51 câu BA](../ba-open-questions.md) gồm 43 câu thẩm quyền cho 83 câu gốc, 3 câu release cho 4 câu gốc và 5 câu thẩm quyền cho 5 câu epic mới. DATA-COST-Q01–06 cùng BA-Q01; chưa chỉ định người cung cấp hoặc người review độc lập.

## Nhóm quyết định

| Chỉ số | Số lượng |
| :--- | ---: |
| Nhóm lịch sử | 197 |
| Nhóm gộp vào DEC-27 | 6 |
| Câu tách khỏi nhóm chủ đề cũ | 18 |
| Nhóm cho 219 câu gốc sau rà | 209 |
| Câu epic mới / nhóm riêng mới | 5 |
| Tổng hiện hành | 214 nhóm / 224 câu nguồn |

Không đạt khoảng tham khảo 60–90 vì nguồn chưa chứng minh cùng người ký và cùng quyết định. Gộp cơ học theo epic, kế toán hoặc hợp đồng kỹ thuật sẽ che các lựa chọn độc lập. Rà lại còn phát hiện 12 nhóm cũ chỉ chung chủ đề: sức khỏe và điều kiện mở, hạ tầng và hạn mức, thẩm quyền nhiều nghiệp vụ, identity/scope, hao hụt, hạn chốt, phát hành, giá public, bộ dựng, lợi nhuận, nguồn public. Đã tách 18 câu để tránh một chữ ký bị hiểu là chốt toàn nhóm.

DEC-27 hợp nhất DEC-29/39/40/41/42/44 vào mã nhỏ nhất. Đầu ra ký một lần là phiên bản đầy đủ của bộ quy tắc DL-01, có biên tuần, Healthy, lặp nhóm nguyên liệu, cặp loại trừ và danh mục chế biến; cùng vai trò Người soạn docx. Không điền các giá trị đang hỏi. [Bảng ánh xạ đủ 197 mã và bảng tách theo mã nguồn](../decision-groups.md); [bản máy ánh xạ](decision-map.json), [bản máy tách](decision-splits.json).

## Xử lý 12 XC

| XC | Loại | Trạng thái | Giới hạn |
| :--- | :--- | :--- | :--- |
| XC-01 | A | ĐÃ SỬA | Chỉ sửa VAT đầu vào theo ACC-CONF-02; giữ O-01 mở. |
| XC-02 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-03 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-04 | B | ĐÃ SỬA | Đã thống nhất cách mô tả; mapping wire vẫn BLOCKED theo câu contract E7–E13. |
| XC-05 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-06 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-07 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-08 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-09 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-10 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-11 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |
| XC-12 | C | CHỜ QUYẾT ĐỊNH | Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. |

[Chi tiết từng file và câu chờ](xc-resolution.md). XC-01 sửa ERD, phiếu kế toán và dependency E13 theo ACC-CONF-02; không đóng O-01. XC-04 chỉ thống nhất cách mô tả, dẫn quy ước trong 7 từ điển và 7 API spec; không tự chọn kiểu wire hoặc sửa endpoint catalog khi chưa có mapping được duyệt. XC-08 và XC-12 không đủ căn cứ xếp B; giữ loại C. Các XC khác tái dùng câu tương đương có sẵn, trừ khoảng trống XC-05/12 đã thêm mã.

## Câu hỏi mới theo epic

| Epic / mã | Nội dung và phần chặn | Sổ nguồn |
| :--- | :--- | :--- |
| E1-Q06 | NFR-PERF-003 đo ký tự nội dung đầu hay phản hồi tiến trình đầu; mốc bắt đầu, kết thúc và cách đo với polling là gì? BLOCKED kết luận đạt phép đo phản hồi đầu E1/E5. XC-12; DEC-198. | [docs/nen-tang/review/questions.md](../../../../nen-tang/review/questions.md) |
| AIO-Q07 | E5 phải cung cấp bằng chứng nào để đối chiếu phép đo phản hồi đầu NFR-PERF-003 với polling và thời gian dựng thực đơn? BLOCKED nghiệm thu phép đo phản hồi đầu; AIO-Q01 và E1-Q06 còn mở. XC-12; DEC-199. | [docs/agent-noi-bo/review/questions.md](../../../../agent-noi-bo/review/questions.md) |
| E8-Q13 | Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại? BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. XC-05; DEC-200. | [docs/website-cong-khai/review/questions.md](../../../../website-cong-khai/review/questions.md) |
| E9-Q15 | Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại? BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. XC-05; DEC-201. | [docs/agent-dinh-duong-vien/review/questions.md](../../../../agent-dinh-duong-vien/review/questions.md) |
| E10-Q16 | Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại? BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. XC-05; DEC-202. | [docs/crm-ban-hang/review/questions.md](../../../../crm-ban-hang/review/questions.md) |

Mỗi câu mới append cuối bảng nguồn; ô Trả lời trống. Câu gốc không bị đóng hoặc chọn phương án. Trạng thái CHỜ trong các sổ cũ vẫn giữ, không chuyển thành câu trả lời. 224 ô answer trong sổ hợp nhất và 51 ô Trả lời BA đều trống.

## Kiểm thử và truy vết

Không có ca nào đổi NOT RUN thành BLOCKED: các nhánh thành công thật liên quan vốn đã BLOCKED. Đã bổ sung gate tại ca và RTM, giữ ca invariant giả định NOT RUN. Không sửa expected nghiệp vụ.

| Gate mới | Ca đang BLOCKED được bổ sung liên kết |
| :--- | :--- |
| E1-Q06 / XC-12 | TC-CORE-NFR-003 |
| AIO-Q07 / XC-12 | TC-AIO-NFR-01; ca này đo hoàn tất, chưa thay thế phép đo phản hồi đầu độc lập |
| E8-Q13 / XC-05 | TC-PUB-007-H, TC-PUB-008-H |
| E9-Q15 / XC-05 | TC-AIN-006-01, TC-AIN-007-01 |
| E10-Q16 / XC-05 | TC-CRM-003-01 |

XC-02/03/06/07/09/10/11 tái dùng câu đang chặn tại E11–E13; không hạ gate, không chuyển PASS. Bằng chứng bữa đã ăn vẫn khác order/giao/nhận. E1-Q06/AIO-Q07 cần chốt phép đo trước khi xác định ca đo riêng.

## Preview

Đã chạy render-e11.cjs, render-e12.cjs, render-e13.cjs bằng thư viện cục bộ; mỗi epic có 7 sơ đồ, 0 lỗi render. Preview E11/E12/E13 phản ánh Markdown mới. HTML/SVG sinh lại có lịch sử phiên bản 13/11/2026.

Preview đã cũ vì E1–E10 không chạy generator/checker cũ:

- [docs/nen-tang/preview.html](../../../../nen-tang/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/cost/preview.html](../../../../cost/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/agent-noi-bo/preview.html](../../../../agent-noi-bo/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/giao-nhan-doanh-thu/preview.html](../../../../giao-nhan-doanh-thu/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/website-cong-khai/preview.html](../../../../website-cong-khai/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/agent-dinh-duong-vien/preview.html](../../../../agent-dinh-duong-vien/preview.html): chưa phản ánh sửa đổi phiên này.
- [docs/crm-ban-hang/preview.html](../../../../crm-ban-hang/preview.html): chưa phản ánh sửa đổi phiên này.

## Kết quả kiểm và bảo toàn

Baseline mới chứa 1.201 file, chụp trước sửa và không ghi lại. Kết quả lịch sử, manifest và baseline các gói được giữ nguyên. Script preserve-results.cjs chặn ghi report/baseline/manifest và chuyển JSON kết quả checker/renderer sang thư mục phiên này trước khi ghi.

| Bộ kiểm | Trạng thái hiện hành | Bằng chứng |
| :--- | :--- | :--- |
| structure-result.json | Chờ chạy | Chưa có |
| diff-result.json | Chờ chạy | Chưa có |
| decision-pack-structure-result.json | FAIL: 3 lỗi | [Kết quả](decision-pack-structure-result.json) |
| decision-pack-cross-epic-result.json | Chờ chạy | Chưa có |
| mua-hang-san-xuat-structure-result.json | Chờ chạy | Chưa có |
| phan-hoi-bao-cao-structure-result.json | Chờ chạy | Chưa có |
| chi-phi-loi-nhuan-structure-result.json | Chờ chạy | Chưa có |

Checker quyết định được sửa vì kiểm cũ khóa số câu, nhóm, manifest và phiên bản lịch sử. Bản mới đọc group-index và câu mới của follow-up; vẫn giữ kiểm mã, nguồn, answer, meeting, link và spacing. Không cập nhật manifest lịch sử. Câu mới được giữ nguyên thay vì cắt mất phạm vi để vừa giới hạn 30 từ.

Checker follow-up kiểm khai báo câu hỏi mới trên toàn repo: một định nghĩa ở sổ nguồn; các tham chiếu trong sổ hợp nhất, báo cáo và preview không tính là định nghĩa trùng. Kiểm mọi nguồn một dòng trong sổ hợp nhất, mapping, XC, lịch sử ngày, link và khoảng trắng số trong văn xuôi mới. Checker diff kiểm hash toàn docs, không xóa, schema 65 bảng, PRD/roadmap/progress và mọi baseline/result/report/manifest lịch sử; hai file tổng quan chỉ append so với baseline.

## File đã sửa hoặc thêm theo phạm vi

Danh sách đầy đủ có SHA256/kích thước tại [diff-result.json](diff-result.json). Các file cùng epic dưới đây gồm tài liệu và artifact sinh lại.

### agent-dinh-duong-vien

- [docs/agent-dinh-duong-vien/api/api-spec.md](../../../../agent-dinh-duong-vien/api/api-spec.md)
- [docs/agent-dinh-duong-vien/api/data-mapping.md](../../../../agent-dinh-duong-vien/api/data-mapping.md)
- [docs/agent-dinh-duong-vien/review/questions.md](../../../../agent-dinh-duong-vien/review/questions.md)
- [docs/agent-dinh-duong-vien/srs/data-dictionary.md](../../../../agent-dinh-duong-vien/srs/data-dictionary.md)
- [docs/agent-dinh-duong-vien/test/test-cases.md](../../../../agent-dinh-duong-vien/test/test-cases.md)
- [docs/agent-dinh-duong-vien/test/traceability.md](../../../../agent-dinh-duong-vien/test/traceability.md)

### agent-noi-bo

- [docs/agent-noi-bo/review/questions.md](../../../../agent-noi-bo/review/questions.md)
- [docs/agent-noi-bo/test/test-cases.md](../../../../agent-noi-bo/test/test-cases.md)
- [docs/agent-noi-bo/test/traceability.md](../../../../agent-noi-bo/test/traceability.md)

### chi-phi-loi-nhuan

- [docs/chi-phi-loi-nhuan/api/api-spec.md](../../../../chi-phi-loi-nhuan/api/api-spec.md)
- [docs/chi-phi-loi-nhuan/preview.html](../../../../chi-phi-loi-nhuan/preview.html)
- [docs/chi-phi-loi-nhuan/review/dependencies.md](../../../../chi-phi-loi-nhuan/review/dependencies.md)
- [docs/chi-phi-loi-nhuan/review/questions.md](../../../../chi-phi-loi-nhuan/review/questions.md)
- [docs/chi-phi-loi-nhuan/srs/data-dictionary.md](../../../../chi-phi-loi-nhuan/srs/data-dictionary.md)
- [docs/chi-phi-loi-nhuan/srs/diagrams/index.html](../../../../chi-phi-loi-nhuan/srs/diagrams/index.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-1.html](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-1.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-1.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-1.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-2.html](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-2.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-2.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-2.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-3.html](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-3.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-3.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-3.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-4.html](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-4.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-4.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-4.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-5.html](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-5.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/srs-states-5.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/srs-states-5.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-1.html](../../../../chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-1.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-1.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-1.svg)
- [docs/chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-2.html](../../../../chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-2.html)
- [docs/chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-2.svg](../../../../chi-phi-loi-nhuan/srs/diagrams/ui-user-flow-2.svg)

### cost

- [docs/cost/review/accountant-input.md](../../../../cost/review/accountant-input.md)

### crm-ban-hang

- [docs/crm-ban-hang/api/api-spec.md](../../../../crm-ban-hang/api/api-spec.md)
- [docs/crm-ban-hang/review/questions.md](../../../../crm-ban-hang/review/questions.md)
- [docs/crm-ban-hang/srs/data-dictionary.md](../../../../crm-ban-hang/srs/data-dictionary.md)
- [docs/crm-ban-hang/test/test-cases.md](../../../../crm-ban-hang/test/test-cases.md)
- [docs/crm-ban-hang/test/traceability.md](../../../../crm-ban-hang/test/traceability.md)

### gia-phat

- [docs/gia-phat/review/decision-pack/ba-open-questions.md](../ba-open-questions.md)
- [docs/gia-phat/review/decision-pack/cross-epic-consistency.md](../cross-epic-consistency.md)
- [docs/gia-phat/review/decision-pack/decision-groups.md](../decision-groups.md)
- [docs/gia-phat/review/decision-pack/decision-register.json](../decision-register.json)
- [docs/gia-phat/review/decision-pack/decision-register.md](../decision-register.md)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/ba-questions.json](ba-questions.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/baseline.json](baseline.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/change-log.json](change-log.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/check-followup.cjs](check-followup.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/chi-phi-loi-nhuan-diagram-render-result.json](chi-phi-loi-nhuan-diagram-render-result.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/conventions.md](conventions.md)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/decision-map.json](decision-map.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/decision-pack-structure-result.json](decision-pack-structure-result.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/decision-splits.json](decision-splits.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/diff-report.cjs](diff-report.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/edit-documents.cjs](edit-documents.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/group-index.json](group-index.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/impact-analysis.md](impact-analysis.md)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/mua-hang-san-xuat-diagram-render-result.json](mua-hang-san-xuat-diagram-render-result.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/new-questions.json](new-questions.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/phan-hoi-bao-cao-diagram-render-result.json](phan-hoi-bao-cao-diagram-render-result.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/preserve-results.cjs](preserve-results.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/refine-document-review.cjs](refine-document-review.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/write-report.cjs](write-report.cjs)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/xc-resolution.json](xc-resolution.json)
- [docs/gia-phat/review/decision-pack/followup-2026-11-13/xc-resolution.md](xc-resolution.md)
- [docs/gia-phat/review/decision-pack/meeting-agenda.md](../meeting-agenda.md)
- [docs/gia-phat/review/decision-pack/README.md](../README.md)
- [docs/gia-phat/review/decision-pack/validation/check-decision-pack.cjs](../validation/check-decision-pack.cjs)

### giao-nhan-doanh-thu

- [docs/giao-nhan-doanh-thu/api/api-spec.md](../../../../giao-nhan-doanh-thu/api/api-spec.md)
- [docs/giao-nhan-doanh-thu/review/questions.md](../../../../giao-nhan-doanh-thu/review/questions.md)
- [docs/giao-nhan-doanh-thu/srs/data-dictionary.md](../../../../giao-nhan-doanh-thu/srs/data-dictionary.md)

### mua-hang-san-xuat

- [docs/mua-hang-san-xuat/api/api-spec.md](../../../../mua-hang-san-xuat/api/api-spec.md)
- [docs/mua-hang-san-xuat/preview.html](../../../../mua-hang-san-xuat/preview.html)
- [docs/mua-hang-san-xuat/review/dependencies.md](../../../../mua-hang-san-xuat/review/dependencies.md)
- [docs/mua-hang-san-xuat/review/questions.md](../../../../mua-hang-san-xuat/review/questions.md)
- [docs/mua-hang-san-xuat/srs/data-dictionary.md](../../../../mua-hang-san-xuat/srs/data-dictionary.md)
- [docs/mua-hang-san-xuat/srs/diagrams/index.html](../../../../mua-hang-san-xuat/srs/diagrams/index.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-1.html](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-1.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-1.svg](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-1.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-2.html](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-2.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-2.svg](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-2.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-3.html](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-3.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-3.svg](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-3.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-4.html](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-4.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-4.svg](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-4.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-5.html](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-5.html)
- [docs/mua-hang-san-xuat/srs/diagrams/srs-states-5.svg](../../../../mua-hang-san-xuat/srs/diagrams/srs-states-5.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/ui-user-flow-1.html](../../../../mua-hang-san-xuat/srs/diagrams/ui-user-flow-1.html)
- [docs/mua-hang-san-xuat/srs/diagrams/ui-user-flow-1.svg](../../../../mua-hang-san-xuat/srs/diagrams/ui-user-flow-1.svg)
- [docs/mua-hang-san-xuat/srs/diagrams/ui-user-flow-2.html](../../../../mua-hang-san-xuat/srs/diagrams/ui-user-flow-2.html)
- [docs/mua-hang-san-xuat/srs/diagrams/ui-user-flow-2.svg](../../../../mua-hang-san-xuat/srs/diagrams/ui-user-flow-2.svg)

### nen-tang

- [docs/nen-tang/review/questions.md](../../../../nen-tang/review/questions.md)
- [docs/nen-tang/srs/erd.md](../../../../nen-tang/srs/erd.md)
- [docs/nen-tang/test/test-cases.md](../../../../nen-tang/test/test-cases.md)
- [docs/nen-tang/test/traceability.md](../../../../nen-tang/test/traceability.md)

### OVERVIEW.md

- [docs/OVERVIEW.md](../../../../OVERVIEW.md)

### phan-hoi-bao-cao

- [docs/phan-hoi-bao-cao/api/api-spec.md](../../../../phan-hoi-bao-cao/api/api-spec.md)
- [docs/phan-hoi-bao-cao/preview.html](../../../../phan-hoi-bao-cao/preview.html)
- [docs/phan-hoi-bao-cao/review/dependencies.md](../../../../phan-hoi-bao-cao/review/dependencies.md)
- [docs/phan-hoi-bao-cao/review/questions.md](../../../../phan-hoi-bao-cao/review/questions.md)
- [docs/phan-hoi-bao-cao/srs/data-dictionary.md](../../../../phan-hoi-bao-cao/srs/data-dictionary.md)
- [docs/phan-hoi-bao-cao/srs/diagrams/index.html](../../../../phan-hoi-bao-cao/srs/diagrams/index.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-1.html](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-1.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-1.svg](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-1.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-2.html](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-2.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-2.svg](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-2.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-3.html](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-3.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-3.svg](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-3.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-4.html](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-4.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-4.svg](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-4.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-5.html](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-5.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/srs-states-5.svg](../../../../phan-hoi-bao-cao/srs/diagrams/srs-states-5.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/ui-user-flow-1.html](../../../../phan-hoi-bao-cao/srs/diagrams/ui-user-flow-1.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/ui-user-flow-1.svg](../../../../phan-hoi-bao-cao/srs/diagrams/ui-user-flow-1.svg)
- [docs/phan-hoi-bao-cao/srs/diagrams/ui-user-flow-2.html](../../../../phan-hoi-bao-cao/srs/diagrams/ui-user-flow-2.html)
- [docs/phan-hoi-bao-cao/srs/diagrams/ui-user-flow-2.svg](../../../../phan-hoi-bao-cao/srs/diagrams/ui-user-flow-2.svg)

### project-dashboard.md

- [docs/project-dashboard.md](../../../../project-dashboard.md)

### website-cong-khai

- [docs/website-cong-khai/api/api-spec.md](../../../../website-cong-khai/api/api-spec.md)
- [docs/website-cong-khai/review/questions.md](../../../../website-cong-khai/review/questions.md)
- [docs/website-cong-khai/srs/data-dictionary.md](../../../../website-cong-khai/srs/data-dictionary.md)
- [docs/website-cong-khai/test/test-cases.md](../../../../website-cong-khai/test/test-cases.md)
- [docs/website-cong-khai/test/traceability.md](../../../../website-cong-khai/test/traceability.md)

## Giới hạn và việc tiếp theo

Thẩm quyền, contract wire, nguồn dữ liệu thực tế và mọi quyết định nghiệp vụ chưa có chữ ký vẫn BLOCKED. BA-Q không là phê duyệt; xác định vai trò không cấp quyền runtime. Không chọn precision, công thức lợi nhuận, mẫu số BO-02, điều kiện consent, lịch lưu/xóa, người ký hoặc nhà cung cấp. Quy ước XC-04 cần xác nhận mapping riêng; chưa chứng minh tương thích tích hợp. Không có kiểm thử sản phẩm hay số liệu thực tế mới.

## Prompt tiếp nối

> Là BA tại D:\BA, chỉ làm tài liệu. Đọc báo cáo followup-2026-11-13, sổ DEC hiện hành, bảng ánh xạ/tách và BA-Q. Chỉ cập nhật theo quyết định đã ký có nguồn, mỗi lần một nhóm DEC. Dùng skill cr để phân tích tác động trước sửa; kiểm người ký, phạm vi, phiên bản và từng câu thành viên. Không lấy trả lời một phần làm đóng nhóm. Nếu thiếu thẩm quyền hoặc nguồn, giữ câu mở tại đúng epic và BLOCKED phần phụ thuộc, tiếp tục phần độc lập. Chụp baseline mới, tăng patch và ghi lịch sử có nguồn. Giữ cost gồm VAT phải trả, cờ hóa đơn riêng, chiết khấu riêng, NFR-COST-002, O-02/O-03 và schema 65 bảng. Không backend, migration, gọi mô hình AI, commit, xóa file hoặc ghi đè kết quả lịch sử. Chạy lại checker phù hợp, lưu kết quả phiên mới; không sửa PRD/roadmap hoặc suy tiến độ được duyệt từ độ phủ 75/78.
