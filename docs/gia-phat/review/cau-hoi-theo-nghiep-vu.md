---
id: DOC-QUESTIONS-BY-DOMAIN
title: Câu hỏi mở theo nghiệp vụ và mức độ quan trọng
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [questions, review, draft]
depends_on: [DOC-DECISION-PACK-REGISTER]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Câu hỏi mở theo nghiệp vụ và mức độ quan trọng

Nháp · 13/11/2026 · Danh sách để hỏi, **chưa có câu nào được trả lời**.

Trích từ [Sổ quyết định hợp nhất](decision-pack/decision-register.md) v0.1.1: 224 câu, nhóm theo nghiệp vụ (epic), trong mỗi nghiệp vụ xếp theo mức độ quan trọng. Cột **Câu hỏi** dẫn tới đúng dòng câu gốc; cột **Nhóm** dẫn tới phân tích nhóm quyết định. Khi trả lời, cập nhật ở tài liệu nguồn và sổ quyết định — file này chỉ để điều hướng.

## Quy ước mức độ

| Mức | Mã | Ý nghĩa |
| :--- | :--- | :--- |
| 🔴 Cao | P-MVP | Chặn MVP (R1–R5) |
| 🟠 Khá cao | P-NOW | Việc Now, chưa chứng minh chặn MVP |
| 🟡 Trung bình | P-NEXT | Đợt Next (R6–R9) |
| 🟢 Thấp | P-LATER | Đợt Later (R10–R13) |

Người quyết định “chưa rõ” hoặc release “chưa rõ” cần BA xác minh trước khi hỏi — xem [sổ BA-Q](decision-pack/ba-open-questions.md).

## Tổng hợp

| Nghiệp vụ | 🔴 Cao | 🟠 Khá cao | 🟡 TB | 🟢 Thấp | Tổng |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [PRD · Tổng thể sản phẩm](#prd-tong-the-san-pham) | 4 | – | 2 | – | 6 |
| [E1 · Nền tảng](#e1-nen-tang) | 9 | 2 | 1 | – | 12 |
| [E2 · Thực đơn & định lượng](#e2-thuc-don-dinh-luong) | 21 | – | – | – | 21 |
| [E3 · Cost](#e3-cost) | 41 | 2 | – | – | 43 |
| [E4 · Dinh dưỡng](#e4-dinh-duong) | 5 | – | – | – | 5 |
| [E5 · Agent Nội bộ](#e5-agent-noi-bo) | 7 | – | – | – | 7 |
| [E6 · Chọn món & order](#e6-chon-mon-order) | – | – | 30 | – | 30 |
| [E7 · Giao nhận & doanh thu](#e7-giao-nhan-doanh-thu) | – | – | 9 | – | 9 |
| [E8 · Website công khai](#e8-website-cong-khai) | – | – | 13 | – | 13 |
| [E9 · Agent Dinh dưỡng viên](#e9-agent-dinh-duong-vien) | – | – | 15 | – | 15 |
| [E10 · CRM & bán hàng](#e10-crm-ban-hang) | – | – | – | 16 | 16 |
| [E11 · Mua hàng & sản xuất](#e11-mua-hang-san-xuat) | – | – | – | 15 | 15 |
| [E12 · Phản hồi & báo cáo](#e12-phan-hoi-bao-cao) | – | – | – | 18 | 18 |
| [E13 · Chi phí & lợi nhuận](#e13-chi-phi-loi-nhuan) | – | – | – | 14 | 14 |
| **Tổng** | **87** | **4** | **70** | **63** | **224** |

## Theo người quyết định — chỉ mức 🔴 Cao

Dùng để chuẩn bị buổi hỏi: mỗi người cần trả lời những câu nào trước MVP.

| Người quyết định | Số câu | Mã câu |
| :--- | ---: | :--- |
| Dinh dưỡng viên | 13 | O-02, E2-Q3, E2-Q4, E2-Q8, E2-Q9, E2-Q10, E2-Q5, H-5, H-9, E3-Q8, NUTR-Q03, DATA-NUTR-Q01, AIO-Q05 |
| Giám đốc | 12 | O-04, O-06, E1-Q05, N-01, N-02, Q-18, E2-Q7, E3-Q6, E3-Q9, E3-Q10, E3-Q11, E3-Q12 |
| Kế toán | 11 | O-01, H-6, H-7, E3-Q3, E3-Q4, E3-Q5, E3-Q13, E3-Q14, FLOW-COST-Q01, CK-Q03, CK-Q06 |
| Người soạn docx | 8 | DL-01, E2-Q2, H-1, H-2, H-3, H-4, H-8, E3-Q7 |
| chưa rõ | 8 | DATA-COST-Q01, DATA-COST-Q02, DATA-COST-Q03, DATA-COST-Q04, DATA-COST-Q05, DATA-COST-Q06, E1-Q06, AIO-Q07 |
| Giám đốc, kế toán | 5 | N-03, E3-Q1, E3-Q16, FLOW-COST-Q06, CK-Q04 |
| Tech lead, BA | 2 | E1-Q01, AIO-Q06 |
| BA, Tech lead | 2 | E1-Q04, QA-COST-Q01 |
| Dinh dưỡng viên, Giám đốc | 2 | E2-Q1, NUTR-Q01 |
| Kế toán, người phụ trách thỏa thuận khách | 2 | CK-Q01, CK-Q05 |
| Dinh dưỡng viên, QA | 2 | NUTR-Q04, AIO-Q03 |
| Giám đốc, Tech lead | 2 | AIO-Q01, AIO-Q04 |
| Tech lead | 1 | E1-Q02 |
| Dinh dưỡng viên, người duyệt | 1 | E2-Q6 |
| Người duyệt | 1 | E2-Q11 |
| Người soạn docx, bếp trưởng | 1 | E3-Q2 |
| Tech lead và BA | 1 | FLOW-COST-Q02 |
| BA, kế toán, Tech lead | 1 | FLOW-COST-Q03 |
| Kế toán, UX/BA | 1 | FLOW-COST-Q04 |
| Giám đốc, BA | 1 | FLOW-COST-Q05 |
| Kế toán, dinh dưỡng viên | 1 | FLOW-COST-Q07 |
| Giám đốc, dinh dưỡng viên | 1 | FLOW-COST-Q08 |
| BA, chủ sản phẩm/AI lead | 1 | FLOW-COST-Q09 |
| Kế toán, vận hành, người phụ trách khách | 1 | CK-Q02 |
| Kế toán, vận hành, người duyệt | 1 | CK-Q07 |
| Kế toán, người duyệt | 1 | CK-Q08 |
| Kế toán, Giám đốc | 1 | CK-Q09 |
| Người phụ trách thỏa thuận khách, kế toán, Giám đốc | 1 | CK-Q10 |
| Dinh dưỡng viên, bếp trưởng | 1 | NUTR-Q02 |
| Chủ sản phẩm, dinh dưỡng viên | 1 | AIO-Q02 |

## PRD · Tổng thể sản phẩm

### 🔴 Cao — 4 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| O-01 | [Cost gồm những khoản nào; thuế suất VAT](../01-prd.md#L250) | Kế toán | R3 | [DEC-05](decision-pack/decision-groups.md#dec-05) |  |
| O-02 | [Một món một định lượng hay nhiều cỡ định lượng](../01-prd.md#L251) | Dinh dưỡng viên | R2 | [DEC-04](decision-pack/decision-groups.md#dec-04) | Chặn: 1 FR: FR-MENU-RCP-007 |
| O-04 | [Đội phát triển, hạ tầng, nhà cung cấp AI, ngân sách](../01-prd.md#L253) | Giám đốc | R1, R5 | [DEC-02](decision-pack/decision-groups.md#dec-02) |  |
| O-06 | [Ai duyệt ngoại lệ và ai thay khi vắng](../01-prd.md#L255) | Giám đốc | R1 | [DEC-03](decision-pack/decision-groups.md#dec-03) |  |

### 🟡 Trung bình — 2 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| O-03 | [Gợi ý cá nhân có xét bệnh lý không](../01-prd.md#L252) | Giám đốc | R6, R9 | [DEC-01](decision-pack/decision-groups.md#dec-01) |  |
| O-05 | [Trường học, bệnh viện, tiệc cỗ có trong bản đầu không](../01-prd.md#L254) | Giám đốc | R6 | [DEC-16](decision-pack/decision-groups.md#dec-16) |  |

## E1 · Nền tảng

### 🔴 Cao — 9 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E1-Q01 | [Thống nhất envelope lỗi và page/cursor giữa E1 và E3/E4/E5 thế nào?](../../nen-tang/review/questions.md#L23) | Tech lead, BA | R1 | [DEC-06](decision-pack/decision-groups.md#dec-06) | Đề xuất: E1/E2 giữ chuẩn SRS page; các extension cursor/envelope ghi ngoại lệ đề xuất, chưa coi API toàn hệ thống đã nhất quán |
| E1-Q02 | [Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không?](../../nen-tang/review/questions.md#L24) | Tech lead | R1 | [DEC-17](decision-pack/decision-groups.md#dec-17) | Đề xuất: Không replay mật khẩu tạm; backend store/transaction chưa có |
| E1-Q04 | [Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu?](../../nen-tang/review/questions.md#L26) | BA, Tech lead | R1 | [DEC-19](decision-pack/decision-groups.md#dec-19) | Đề xuất: Đề xuất NEW→SEEN→RESOLVED; bảng notifications hiện chưa có version/event key; cần delta trước backend |
| E1-Q05 | [Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào?](../../nen-tang/review/questions.md#L27) | Giám đốc | R1 | [DEC-20](decision-pack/decision-groups.md#dec-20) | Đề xuất: Chưa thêm quyền nghiệp vụ cho QUAN_TRI; cần quyết định trước vận hành |
| N-01 | [Nhân viên đăng nhập bằng số điện thoại, email, hay tên do quản trị đặt? (Bếp trưởng có thể không có email công việc.)](../../nen-tang/srs/spec.md#L403) | Giám đốc | R1 | [DEC-21](decision-pack/decision-groups.md#dec-21) |  |
| N-02 | [Ai giữ vai trò quản trị hệ thống: người của Gia Phát hay đội phát triển?](../../nen-tang/srs/spec.md#L404) | Giám đốc | R1 | [DEC-22](decision-pack/decision-groups.md#dec-22) |  |
| N-03 | [Thời gian lưu nhật ký thay đổi (đề xuất 5 năm) và nhật ký đăng nhập (đề xuất 1 năm)](../../nen-tang/srs/spec.md#L405) | Giám đốc, kế toán | R1 | [DEC-23](decision-pack/decision-groups.md#dec-23) | Chặn: 1 ca (gate trực tiếp) |
| Q-18 | [Số người ăn, số công ty, số điểm giao mỗi ngày](../../nen-tang/srs/spec.md#L408) | Giám đốc | R1 | [DEC-26](decision-pack/decision-groups.md#dec-26) | Chặn: 1 ca (gate trực tiếp) |
| E1-Q06 | [NFR-PERF-003 đo ký tự nội dung đầu hay phản hồi tiến trình đầu; mốc bắt đầu, kết thúc và cách đo với polling là gì?](../../nen-tang/review/questions.md#L28) | chưa rõ | R5 | [DEC-198](decision-pack/decision-groups.md#dec-198) | Đề xuất: Nguồn đề xuất phản hồi tiến trình đầu; chưa chọn thay NFR gốc. |

### 🟠 Khá cao — 2 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E1-Q03 | [MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể?](../../nen-tang/review/questions.md#L25) | Giám đốc, Tech lead | chưa rõ | [DEC-18](decision-pack/decision-groups.md#dec-18) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: P1 gated; không tự triển khai chỉ dựa ô nhập6 số |
| N-04 | [Có bắt buộc xác thực 2 bước cho Giám đốc, kế toán doanh thu, quản trị không?](../../nen-tang/srs/spec.md#L406) | Giám đốc | chưa rõ | [DEC-24](decision-pack/decision-groups.md#dec-24) | Chặn: 5 ca (gate trực tiếp) |

### 🟡 Trung bình — 1 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-14 | [Kênh thông báo ngoài (Zalo OA, SMS, email)](../../nen-tang/srs/spec.md#L407) | Giám đốc | R6 | [DEC-25](decision-pack/decision-groups.md#dec-25) | Chặn: 5 ca (gate trực tiếp) |

## E2 · Thực đơn & định lượng

### 🔴 Cao — 21 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DL-01 | [Duyệt 43 quy tắc](../../thuc-don-dinh-luong/srs/spec.md#L440) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) | Chặn: 86 ca rule; 2 ca Cost (khác bộ) |
| E2-Q1 | [Cách kiểm ngưỡng giá suất](../../thuc-don-dinh-luong/srs/spec.md#L444) | Dinh dưỡng viên, Giám đốc | R2 | [DEC-28](decision-pack/decision-groups.md#dec-28) |  |
| E2-Q2 | [Quy tắc tuần có xét tuần trước không](../../thuc-don-dinh-luong/srs/spec.md#L445) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| E2-Q3 | [Tuần phục vụ gồm những ngày nào](../../thuc-don-dinh-luong/srs/spec.md#L446) | Dinh dưỡng viên | R2 | [DEC-30](decision-pack/decision-groups.md#dec-30) |  |
| E2-Q4 | [Thực đơn chung hay riêng theo khách](../../thuc-don-dinh-luong/srs/spec.md#L447) | Dinh dưỡng viên | R2 | [DEC-31](decision-pack/decision-groups.md#dec-31) |  |
| E2-Q6 | [Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)](../../thuc-don-dinh-luong/srs/spec.md#L448) | Dinh dưỡng viên, người duyệt | R2 | [DEC-32](decision-pack/decision-groups.md#dec-32) |  |
| E2-Q7 | [Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?](../../thuc-don-dinh-luong/srs/spec.md#L449) | Giám đốc | R2 | [DEC-33](decision-pack/decision-groups.md#dec-33) |  |
| E2-Q8 | [Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?](../../thuc-don-dinh-luong/srs/spec.md#L450) | Dinh dưỡng viên | R2 | [DEC-34](decision-pack/decision-groups.md#dec-34) |  |
| E2-Q9 | [Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)](../../thuc-don-dinh-luong/srs/spec.md#L451) | Dinh dưỡng viên | R2 | [DEC-35](decision-pack/decision-groups.md#dec-35) |  |
| E2-Q10 | [Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)](../../thuc-don-dinh-luong/srs/spec.md#L452) | Dinh dưỡng viên | R2 | [DEC-36](decision-pack/decision-groups.md#dec-36) |  |
| E2-Q11 | [Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)](../../thuc-don-dinh-luong/srs/spec.md#L453) | Người duyệt | R2 | [DEC-37](decision-pack/decision-groups.md#dec-37) |  |
| E2-Q5 | [Khoảng định lượng và chất độn dùng chuẩn từng món hay bảng theo nguyên liệu/kiểu món; lưu ở đâu?](../../thuc-don-dinh-luong/srs/spec.md#L454) | Dinh dưỡng viên | R2 | [DEC-38](decision-pack/decision-groups.md#dec-38) |  |
| H-1 | [Món Healthy chỉ được luộc, hay hấp / áp chảo ít dầu / nướng cũng được tính?](../brainstorms/quy-tac-thuc-don.md#L120) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| H-2 | ["Nhiều ngày liên tiếp" là mấy ngày? Thịt lợn có được nới hơn các nhóm khác không (vì dùng nhiều nhất)?](../brainstorms/quy-tac-thuc-don.md#L121) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| H-3 | [Duyệt danh sách nhóm nguyên liệu chính nào để so trùng; sườn tách riêng hay gộp vào lợn?](../brainstorms/quy-tac-thuc-don.md#L122) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| H-4 | [Ngoài "nem – nộm" còn những cặp món nào không được xếp cùng ngày?](../brainstorms/quy-tac-thuc-don.md#L123) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| H-5 | [Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào?](../brainstorms/quy-tac-thuc-don.md#L124) | Dinh dưỡng viên | R2 | [DEC-43](decision-pack/decision-groups.md#dec-43) |  |
| H-6 | [Suất ăn đang xuất hoá đơn với thuế suất VAT bao nhiêu? (Cần kế toán trả lời.)](../brainstorms/quy-tac-thuc-don.md#L125) | Kế toán | R2 | [DEC-05](decision-pack/decision-groups.md#dec-05) |  |
| H-7 | [Hiện tại khi tính 52%, kế toán/bếp đang cộng những khoản nào? Gạo, gia vị, dầu ăn, tráng miệng có tính không?](../brainstorms/quy-tac-thuc-don.md#L126) | Kế toán | R2 | [DEC-05](decision-pack/decision-groups.md#dec-05) |  |
| H-8 | [Danh sách phương pháp chế biến — đề xuất: luộc, hấp, kho, rang, xào, sốt, chiên/rán, áp chảo, nướng, nộm/trộn, cuốn. Thiếu hoặc thừa gì?](../brainstorms/quy-tac-thuc-don.md#L127) | Người soạn docx | R2 | [DEC-27](decision-pack/decision-groups.md#dec-27) |  |
| H-9 | [Loại suất giá khác giữ định lượng từng món hay dùng nhiều cỡ định lượng với giá khác nhau?](../brainstorms/quy-tac-thuc-don.md#L128) | Dinh dưỡng viên | R2 | [DEC-04](decision-pack/decision-groups.md#dec-04) |  |

## E3 · Cost

### 🔴 Cao — 41 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E3-Q1 | [Cost phần món chính](../../cost/review/decision-register.md#L12) | Giám đốc, kế toán | R3 | [DEC-45](decision-pack/decision-groups.md#dec-45) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc DAT_NHAT giai đoạn đầu; so với BINH_QUAN/MAC_DINH trên10 ngày thực tế trước khi chọn. |
| E3-Q2 | [Định lượng sống đã gồm xương, vỏ chưa](../../cost/review/decision-register.md#L13) | Người soạn docx, bếp trưởng | R3 | [DEC-09](decision-pack/decision-groups.md#dec-09) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Xác nhận định lượng sống là trước hay sau loại xương/vỏ; chỉ áp hao hụt một lần. |
| E3-Q3 | [Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào](../../cost/review/decision-register.md#L14) | Kế toán | R3 | [DEC-46](decision-pack/decision-groups.md#dec-46) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q4 | [Giá nào là giá tham chiếu](../../cost/review/decision-register.md#L15) | Kế toán | R3 | [DEC-47](decision-pack/decision-groups.md#dec-47) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q5 | [Tần suất cập nhật giá thực tế](../../cost/review/decision-register.md#L16) | Kế toán | R3 | [DEC-48](decision-pack/decision-groups.md#dec-48) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q6 | [Giá nhập có cần duyệt](../../cost/review/decision-register.md#L17) | Giám đốc | R3 | [DEC-49](decision-pack/decision-groups.md#dec-49) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q7 | [Định nghĩa cost cao / thấp](../../cost/review/decision-register.md#L18) | Người soạn docx | R3 | [DEC-50](decision-pack/decision-groups.md#dec-50) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q8 | [Nguồn số suất trước khi có order](../../cost/review/decision-register.md#L19) | Dinh dưỡng viên | R3 | [DEC-51](decision-pack/decision-groups.md#dec-51) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q9 | [Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ](../../cost/review/decision-register.md#L20) | Giám đốc | R3 | [DEC-52](decision-pack/decision-groups.md#dec-52) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q10 | [Chặn chuyển bếp](../../cost/review/decision-register.md#L21) | Giám đốc | R3 | [DEC-53](decision-pack/decision-groups.md#dec-53) | Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q11 | [Bếp trưởng có xem giá và cost](../../cost/review/decision-register.md#L22) | Giám đốc | R3 | [DEC-54](decision-pack/decision-groups.md#dec-54) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q12 | [Khi tính BINH_QUAN hoặc DAT_NHAT, món chính Healthy (thường rẻ hơn) có được tính vào không](../../cost/review/decision-register.md#L25) | Giám đốc | R3 | [DEC-55](decision-pack/decision-groups.md#dec-55) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q13 | [Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không](../../cost/review/decision-register.md#L26) | Kế toán | R3 | [DEC-56](decision-pack/decision-groups.md#dec-56) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác. |
| E3-Q14 | [FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không?](../../cost/review/decision-register.md#L27) | Kế toán | R3 | [DEC-57](decision-pack/decision-groups.md#dec-57) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ giá đã hiệu lực bất biến, chỉ đổi tham chiếu tương lai; nếu cần hồi tố phải thiết kế nghiệp vụ riêng. |
| E3-Q16 | [Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá?](../../cost/review/decision-register.md#L29) | Giám đốc, kế toán | R3 | [DEC-59](decision-pack/decision-groups.md#dec-59) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc cùng món/cỡ/cơ sở, ngày lập đến ngày phục vụ <=N ngày; chốt riêng công thức đổi có làm hết hiệu lực không. |
| FLOW-COST-Q01 | [Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào?](../../cost/review/decision-register.md#L30) | Kế toán | R3 | [DEC-60](decision-pack/decision-groups.md#dec-60) | Đề xuất: Yêu cầu chọn giá thay thế trong cùng giao dịch hủy, nếu còn báo giá khác cùng nhóm. |
| FLOW-COST-Q02 | [Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào?](../../cost/review/decision-register.md#L31) | Tech lead và BA | R3 | [DEC-61](decision-pack/decision-groups.md#dec-61) | Chặn: 6 ca (gate trực tiếp)<br>Đề xuất: Review phương án API hiện có: key/hash theo actor/method/path, TTL24h, đối soát, commit nguyên tử. |
| FLOW-COST-Q03 | [Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào?](../../cost/review/decision-register.md#L32) | BA, kế toán, Tech lead | R3 | [DEC-62](decision-pack/decision-groups.md#dec-62) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Tạo thiết kế cảnh báo nguyên liệu riêng, không dùng cost_alerts bắt buộc menu_day_id. |
| FLOW-COST-Q04 | [Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào?](../../cost/review/decision-register.md#L33) | Kế toán, UX/BA | R3 | [DEC-63](decision-pack/decision-groups.md#dec-63) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Hiện dấu — và ghi Không áp dụng khi mẫu số0; giữ delta tiền nếu tính được. |
| FLOW-COST-Q05 | [Ai được đọc danh sách/chi tiết khoản khoán?](../../cost/review/decision-register.md#L34) | Giám đốc, BA | R3 | [DEC-64](decision-pack/decision-groups.md#dec-64) | Đề xuất: Xác nhận ma trận đọc danh mục quản trị riêng với quyền xem khoản trong phân rã cost. |
| FLOW-COST-Q06 | [Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào?](../../cost/review/decision-register.md#L35) | Giám đốc, kế toán | R3 | [DEC-65](decision-pack/decision-groups.md#dec-65) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc kiểm lại tại duyệt cuối; nếu đủ điều kiện thì chụp bộ vừa kiểm cùng transaction. |
| FLOW-COST-Q07 | [Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ?](../../cost/review/decision-register.md#L36) | Kế toán, dinh dưỡng viên | R3 | [DEC-66](decision-pack/decision-groups.md#dec-66) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc all-or-nothing cho cả batch tuần; trả lỗi theo ngày, không ghi ngày hợp lệ khi có lỗi. |
| FLOW-COST-Q08 | [Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao?](../../cost/review/decision-register.md#L37) | Giám đốc, dinh dưỡng viên | R3 | [DEC-67](decision-pack/decision-groups.md#dec-67) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Tách hai tình huống: vốn vượt khi duyệt và phục hồi rồi vượt lại; xác định có mở cảnh báo mới hay cập nhật lịch sử. |
| FLOW-COST-Q09 | [Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không?](../../cost/review/decision-register.md#L38) | BA, chủ sản phẩm/AI lead | R3 | [DEC-68](decision-pack/decision-groups.md#dec-68) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc KHONG_XAC_DINH ưu tiên khi bất kỳ ngày/cơ sở không tính được, kể cả thiếu VAT. |
| QA-COST-Q01 | [NCC tồn tại INACTIVE trả 404-01 hay 422-02?](../../cost/review/decision-register.md#L42) | BA, Tech lead | R3 | [DEC-70](decision-pack/decision-groups.md#dec-70) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc422-02 khi NCC tồn tại nhưng INACTIVE;404-01 chỉ tham chiếu không tồn tại hoặc nguyên liệu không dùng. |
| CK-Q01 | [Chiết khấu % tính trên tiền suất đã gồm VAT hay chưa VAT? Cơ sở tính có bao gồm khoản phụ thu nào không?](../../cost/accounting/business-rules.md#L91) | Kế toán, người phụ trách thỏa thuận khách | R3 | [DEC-71](decision-pack/decision-groups.md#dec-71) |  |
| CK-Q02 | [Chiết khấu áp dụng mọi suất hay từng loại/dòng; số lượng căn cứ đặt, giao hay khách xác nhận?](../../cost/accounting/business-rules.md#L92) | Kế toán, vận hành, người phụ trách khách | R3 | [DEC-72](decision-pack/decision-groups.md#dec-72) |  |
| CK-Q03 | [Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào?](../../cost/accounting/business-rules.md#L93) | Kế toán | R3 | [DEC-73](decision-pack/decision-groups.md#dec-73) |  |
| CK-Q04 | [Ai lập/sửa, ai duyệt chiết khấu; phân cấp tiền/tỷ lệ, tự duyệt và người thay khi vắng thế nào?](../../cost/accounting/business-rules.md#L94) | Giám đốc, kế toán | R3 | [DEC-207](decision-pack/decision-groups.md#dec-207) |  |
| CK-Q05 | [Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai?](../../cost/accounting/business-rules.md#L95) | Kế toán, người phụ trách thỏa thuận khách | R3 | [DEC-74](decision-pack/decision-groups.md#dec-74) |  |
| CK-Q06 | [Xác nhận/xử lý chiết khấu lúc chốt, giao, thanh toán hay cuối kỳ; xử lý một phần và chứng từ thế nào?](../../cost/accounting/business-rules.md#L96) | Kế toán | R3 | [DEC-75](decision-pack/decision-groups.md#dec-75) |  |
| CK-Q07 | [Đơn đổi suất/giá/loại khi chiết khấu chưa xử lý: tự tính lại, duyệt lại và giữ phiên bản cũ thế nào?](../../cost/accounting/business-rules.md#L97) | Kế toán, vận hành, người duyệt | R3 | [DEC-76](decision-pack/decision-groups.md#dec-76) |  |
| CK-Q08 | [Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không?](../../cost/accounting/business-rules.md#L98) | Kế toán, người duyệt | R3 | [DEC-77](decision-pack/decision-groups.md#dec-77) |  |
| CK-Q09 | [Đơn đổi/hủy sau chi trả/bù trừ: thu hồi, bù kỳ sau hay điều chỉnh riêng; ai duyệt, chứng từ nào?](../../cost/accounting/business-rules.md#L99) | Kế toán, Giám đốc | R3 | [DEC-78](decision-pack/decision-groups.md#dec-78) |  |
| CK-Q10 | [Một đơn hưởng đồng thời chiết khấu %/tiền mỗi suất hoặc nhiều chương trình được không; cộng dồn, ưu tiên, trần thế nào?](../../cost/accounting/business-rules.md#L100) | Người phụ trách thỏa thuận khách, kế toán, Giám đốc | R3 | [DEC-79](decision-pack/decision-groups.md#dec-79) |  |
| DATA-COST-Q01 | [Ai phụ trách cung cấp và xác nhận 10 món/10 ngày thực tế? Khi nào có dữ liệu?](../../cost/review/accountant-input.md#L95) | chưa rõ | R3 | [DEC-80](decision-pack/decision-groups.md#dec-80) |  |
| DATA-COST-Q02 | [File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào?](../../cost/review/accountant-input.md#L96) | chưa rõ | R3 | [DEC-81](decision-pack/decision-groups.md#dec-81) |  |
| DATA-COST-Q03 | [Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào?](../../cost/review/accountant-input.md#L97) | chưa rõ | R3 | [DEC-82](decision-pack/decision-groups.md#dec-82) |  |
| DATA-COST-Q04 | [Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào?](../../cost/review/accountant-input.md#L98) | chưa rõ | R3 | [DEC-83](decision-pack/decision-groups.md#dec-83) |  |
| DATA-COST-Q05 | [Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập?](../../cost/review/accountant-input.md#L99) | chưa rõ | R3 | [DEC-84](decision-pack/decision-groups.md#dec-84) |  |
| DATA-COST-Q06 | [Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào?](../../cost/review/accountant-input.md#L100) | chưa rõ | R3 | [DEC-85](decision-pack/decision-groups.md#dec-85) |  |

### 🟠 Khá cao — 2 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E3-Q15 | [Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick](../../cost/review/decision-register.md#L28) | Dinh dưỡng viên | chưa rõ | [DEC-58](decision-pack/decision-groups.md#dec-58) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: R3 giới hạn K=1; chỉ mở K>1 khi xác nhận tổng lượt chọn chia hết K và cách xử lý phần dư. |
| FLOW-COST-Q10 | [Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào?](../../cost/review/decision-register.md#L39) | Giám đốc, kế toán | chưa rõ | [DEC-69](decision-pack/decision-groups.md#dec-69) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Giữ P2; chốt vai trò, phạm vi cơ sở, trạng thái thực đơn và cửa sổ ngày trước khi mở. |

## E4 · Dinh dưỡng

### 🔴 Cao — 5 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| NUTR-Q01 | [Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu?](../../dinh-duong/review/questions.md#L13) | Dinh dưỡng viên, Giám đốc | R4 | [DEC-86](decision-pack/decision-groups.md#dec-86) | Đề xuất: đề xuất, chưa có workflow duyệt riêng |
| NUTR-Q02 | [qty_std là gram sống còn xương/vỏ hay gram phần ăn được? Xác nhận edible_pct và quy đổi theo từng nguyên liệu để không trừ hai lần.](../../dinh-duong/review/questions.md#L14) | Dinh dưỡng viên, bếp trưởng | R4 | [DEC-213](decision-pack/decision-groups.md#dec-213) | Chặn: 2 ca (gate trực tiếp) |
| NUTR-Q03 | [Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi?](../../dinh-duong/review/questions.md#L15) | Dinh dưỡng viên | R4 | [DEC-87](decision-pack/decision-groups.md#dec-87) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: đề xuất tổ hợp tường minh, không sao chép cách chọn món đắt nhất Cost |
| NUTR-Q04 | [Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.](../../dinh-duong/review/questions.md#L16) | Dinh dưỡng viên, QA | R4 | [DEC-88](decision-pack/decision-groups.md#dec-88) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost. |
| DATA-NUTR-Q01 | [Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp.](../../dinh-duong/review/questions.md#L17) | Dinh dưỡng viên | R4 | [DEC-89](decision-pack/decision-groups.md#dec-89) | Chặn: 1 ca (gate trực tiếp) |

## E5 · Agent Nội bộ

### 🔴 Cao — 7 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AIO-Q01 | [Nhà cung cấp/model, ngân sách, concurrency, số lần thử, token tối đa và cách ghi chi phí/tỷ giá nào?](../../agent-noi-bo/review/questions.md#L14) | Giám đốc, Tech lead | R5 | [DEC-205](decision-pack/decision-groups.md#dec-205) | Chặn: 1 ca (gate trực tiếp) |
| AIO-Q02 | [Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không?](../../agent-noi-bo/review/questions.md#L15) | Chủ sản phẩm, dinh dưỡng viên | R5 | [DEC-90](decision-pack/decision-groups.md#dec-90) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: đề xuất NO_SOLUTION không cho áp dụng |
| AIO-Q03 | [20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao?](../../agent-noi-bo/review/questions.md#L16) | Dinh dưỡng viên, QA | R5 | [DEC-91](decision-pack/decision-groups.md#dec-91) | Chặn: 2 ca (gate trực tiếp) |
| AIO-Q04 | [Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào?](../../agent-noi-bo/review/questions.md#L17) | Giám đốc, Tech lead | R5 | [DEC-92](decision-pack/decision-groups.md#dec-92) |  |
| AIO-Q05 | [Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào?](../../agent-noi-bo/review/questions.md#L18) | Dinh dưỡng viên | R5 | [DEC-93](decision-pack/decision-groups.md#dec-93) |  |
| AIO-Q06 | [Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout?](../../agent-noi-bo/review/questions.md#L19) | Tech lead, BA | R5 | [DEC-94](decision-pack/decision-groups.md#dec-94) | Đề xuất: đề xuất, chưa có endpoint MENU được triển khai |
| AIO-Q07 | [E5 phải cung cấp bằng chứng nào để đối chiếu phép đo phản hồi đầu NFR-PERF-003 với polling và thời gian dựng thực đơn?](../../agent-noi-bo/review/questions.md#L20) | chưa rõ | R5 | [DEC-199](decision-pack/decision-groups.md#dec-199) | Đề xuất: Đối chiếu đề xuất E1-Q06; giữ hai chỉ số riêng, chưa chọn cách đo. |

## E6 · Chọn món & order

### 🟡 Trung bình — 30 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ORD-Q01 | [Định danh duy nhất người ăn có tài khoản/QR bằng gì; xử lý nhiều thiết bị/QR chia sẻ và account trùng ra sao?](../../chon-mon-order/review/questions.md#L20) | Gia Phát, BA | R6 | [DEC-07](decision-pack/decision-groups.md#dec-07) | Chặn: 9 ca (gate trực tiếp) |
| ORD-Q02 | [Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa?](../../chon-mon-order/review/questions.md#L21) | Người đặt tổng, BA | R6 | [DEC-95](decision-pack/decision-groups.md#dec-95) | Chặn: 2 ca (gate trực tiếp) |
| ORD-Q03 | [Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order?](../../chon-mon-order/review/questions.md#L22) | Vận hành | R6 | [DEC-96](decision-pack/decision-groups.md#dec-96) | Chặn: 2 ca (gate trực tiếp) |
| ORD-Q04 | [Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào?](../../chon-mon-order/review/questions.md#L23) | Người phụ trách khách, DDV | R6 | [DEC-97](decision-pack/decision-groups.md#dec-97) | Chặn: 4 ca (gate trực tiếp) |
| ORD-Q05 | [Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào?](../../chon-mon-order/review/questions.md#L24) | Người đặt tổng, BA | R6 | [DEC-98](decision-pack/decision-groups.md#dec-98) | Chặn: 2 ca (gate trực tiếp) |
| ORD-Q06 | [T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món?](../../chon-mon-order/review/questions.md#L25) | Người đặt tổng, DDV | R6 | [DEC-99](decision-pack/decision-groups.md#dec-99) | Chặn: 9 ca (gate trực tiếp) |
| ORD-Q07 | [Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao?](../../chon-mon-order/review/questions.md#L26) | Vận hành, Giám đốc | R6 | [DEC-100](decision-pack/decision-groups.md#dec-100) | Chặn: 9 ca (gate trực tiếp) |
| ORD-Q08 | [Ngưỡng đổi sau chốt, vai trò duyệt, delta âm và khi bếp đã sản xuất xử lý thế nào?](../../chon-mon-order/review/questions.md#L27) | Giám đốc, bếp trưởng | R6 | [DEC-10](decision-pack/decision-groups.md#dec-10) | Chặn: 2 ca (gate trực tiếp) |
| ORD-Q09 | [Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi?](../../chon-mon-order/review/questions.md#L28) | Người đặt tổng | R6 | [DEC-101](decision-pack/decision-groups.md#dec-101) | Chặn: 2 ca (gate trực tiếp) |
| ORD-Q10 | [R6 luôn 1 MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao?](../../chon-mon-order/review/questions.md#L29) | DDV, bếp trưởng | R6 | [DEC-102](decision-pack/decision-groups.md#dec-102) | Chặn: 3 ca (gate trực tiếp) |
| ORD-Q11 | [Người đặt tổng có thể quản lý nhiều khách/điểm không; role customer scope và audit QR guest/service lưu thế nào khi user_roles/sessions/audit_logs hiện yêu cầu user?](../../chon-mon-order/review/questions.md#L37) | Gia Phát, Tech lead | R6 | [DEC-08](decision-pack/decision-groups.md#dec-08) |  |
| ORD-Q12 | [MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn?](../../chon-mon-order/review/questions.md#L38) | DDV, vận hành | R6 | [DEC-103](decision-pack/decision-groups.md#dec-103) | Chặn: 1 ca (gate trực tiếp) |
| ORD-Q13 | [Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày?](../../chon-mon-order/review/questions.md#L39) | Người đặt tổng, BA | R6 | [DEC-104](decision-pack/decision-groups.md#dec-104) |  |
| ORD-Q14 | [Bếp phải xác nhận nhận phiên bản kế hoạch mới không; ai phát hành/cho IN_PRODUCTION và xử lý bản in cũ?](../../chon-mon-order/review/questions.md#L40) | Bếp trưởng, vận hành | R6 | [DEC-11](decision-pack/decision-groups.md#dec-11) | Chặn: 1 ca (gate trực tiếp) |
| ORD-Q15 | [Nếu mở O-03: consent/version, rút đồng ý, thời hạn xóa/lưu log, phạm vi bệnh lý và tiêu chí gợi ý cụ thể?](../../chon-mon-order/review/questions.md#L41) | Chủ sản phẩm, phụ trách dữ liệu | R6 | [DEC-203](decision-pack/decision-groups.md#dec-203) | Chặn: 1 ca (gate trực tiếp) |
| E6-CG-01 | [Identity/binding/credential/guest audit; RV01, ORD-Q01/02/11; EVID001 chỉ xác nhận danh sách](../../chon-mon-order/review/contract-gap-register.md#L7) | BA, phụ trách khách, Tech lead/Auth | R6 | [DEC-211](decision-pack/decision-groups.md#dec-211) | Đề xuất: Dùng một định danh thành viên nội bộ ổn định gắn danh sách đã được quản lý xác nhận; account và guest nếu được hỗ trợ cùng tham chiếu thành viên đó. Quản lý xác nhận đúng người trước khi cấp liên kết/mã kích hoạt dùng một lần; QR tại điểm chỉ dẫn vào luồng, không tự chứng minh danh tính. Khôi phục/thu hồi phải kiểm lại người nhận và lưu audit. Không dùng mã nhân viên công khai làm mật khẩu. |
| E6-CG-02 | [Scope người đặt tổng một/nhiều công ty; ORD-Q11, EVID002](../../chon-mon-order/review/contract-gap-register.md#L8) | Chủ sản phẩm, BA, Tech lead | R6 | [DEC-212](decision-pack/decision-groups.md#dec-212) |  |
| E6-CG-03 | [C có danh tính/gộp, C→S, vượtT, hủy/zero; RV02/03, ORD-Q06/13, EVID002](../../chon-mon-order/review/contract-gap-register.md#L9) | Chủ sản phẩm, vận hành, BA | R6 | [DEC-105](decision-pack/decision-groups.md#dec-105) |  |
| E6-CG-04 | [Summary token, receipt, outbox transaction/retention; RV04, E1-Q02](../../chon-mon-order/review/contract-gap-register.md#L10) | Tech lead, BA, QA | R6 | [DEC-106](decision-pack/decision-groups.md#dec-106) | Đề xuất: Giữ summary token theo scope; dữ liệu nghiệp vụ, revision, audit thành công, receipt và outbox cùng một transaction. UC010/011 dùng một PORT-LOCK và một lần khóa; eventKey khác HTTP key. Receipt đã commit được kiểm quyền hiện tại rồi replay, không ghi lại. Worker xử lý event sau commit, retry không tạo revision trùng. |
| E6-CG-05 | [Hạn, thiếu nguồn, remediation, quyền/ngưỡng đổi; RV08, ORD-Q07/08/12, Q-16/O-06](../../chon-mon-order/review/contract-gap-register.md#L11) | Vận hành, người duyệt được chỉ định, BA | R6 | [DEC-214](decision-pack/decision-groups.md#dec-214) | Đề xuất: Đề xuất lệnh chọn/chốt chỉ hợp lệ khi thời điểm kiểm hạn trong transaction theo đồng hồ server nhỏ hơn deadline hiệu lực; đúng deadline thuộc sau hạn. Thiếu nguồn/counter lệch thì giữ trạng thái cũ và NEEDS_ATTENTION. Vận hành lập yêu cầu xử lý nguồn; người duyệt được chỉ định, khác người tạo/sửa cuối, quyết định ngoại lệ. Retry kỹ thuật không gia hạn. |
| E6-CG-06 | [Expected source/completeness, publish/ack/start; RV05/06, ORD-Q03/13/14](../../chon-mon-order/review/contract-gap-register.md#L12) | Bếp, vận hành, BA, Tech lead | R6 | [DEC-216](decision-pack/decision-groups.md#dec-216) | Đề xuất: Worker tạo bản kế hoạch để kiểm tra; chỉ cho phát hành khi tập nguồn kỳ vọng có căn cứ, không còn nguồn thiếu và các revision được kiểm lại. Bản thiếu/UNKNOWN chỉ phục vụ xử lý, không coi đủ để sản xuất. Đề xuất vận hành được cấp quyền phát hành, bếp trưởng theo scope xác nhận đúng revision, rồi ghi bắt đầu sản xuất bằng thao tác riêng. Bản mới cần xác nhận riêng; ack cũ không áp cho bản mới. |
| E6-CG-07 | [Delta line identity, unit/role/portion và món mới; RV07, ORD-Q04/08/10/12, O-02](../../chon-mon-order/review/contract-gap-register.md#L13) | BA, dinh dưỡng viên, Tech lead | R6 | [DEC-107](decision-pack/decision-groups.md#dec-107) | Đề xuất: Ưu tiên tham chiếu lineId bất biến của revision gốc khi sửa dòng đã tồn tại; so sánh snapshot theo dish+recipe+portion+role+unit. Thay recipe A bằng B biểu diễn giảm A và tăng B, dù tổng suất không đổi. Không cộng suất với gram. |
| E6-CG-08 | [Customer master/account/service lifecycle; ORD-Q03/11](../../chon-mon-order/review/contract-gap-register.md#L14) | Nền tảng/Auth, BA, phụ trách khách | R6 | [DEC-108](decision-pack/decision-groups.md#dec-108) | Đề xuất: Nền tảng quản lý mã khách tối thiểu và vòng đời account; E6 tham chiếu khách đã tồn tại, tạo/cập nhật điểm phục vụ và grant tách biệt. Chỉ cho thao tác chọn/chốt khi có đủ nguồn và quyền theo từng thao tác. Tạo account thành công nhưng grant thất bại: giữ account chưa có quyền E6, xử lý lại bước grant sau khi kiểm quyền. |
| E6-CG-09 | [Envelope/pagination/error mapping; E1-Q01](../../chon-mon-order/review/contract-gap-register.md#L15) | Tech lead/API owner, BA | R6 | [DEC-06](decision-pack/decision-groups.md#dec-06) | Đề xuất: Đề xuất E6 dùng success envelope theo E1: success/data/meta/timestamp; data list chỉ items, page/pageSize/total đặt ở meta, tránh lặp metadata. Error giữ code/message/details/requestId như E1/E6 đang mô tả. Adapter chuyển từ từng nguồn, không trả nguyên upstream body. |
| E6-CG-10 | [NUTR provenance/kind/stale, refresh/cache/fallback; NUTR-Q03/04, ORD-Q04/12](../../chon-mon-order/review/contract-gap-register.md#L16) | Owner MENU/NUTR, BA, Tech lead | R6 | [DEC-109](decision-pack/decision-groups.md#dec-109) | Đề xuất: Calculation được principal service có quyền chuẩn bị trước bằng job/event khi nguồn thay đổi; GET chỉ đọc và đối chiếu provenance. Ưu tiên opaque source reference an toàn cho người ăn, provenance đầy đủ lưu nội bộ. Chưa có kết quả đúng nguồn thì không dùng kết quả cũ như hiện hành; thiếu dữ liệu đã xác định trả null/missing an toàn, lỗi phụ thuộc/thiếu cache cần outcome riêng, không giả bằng 0. |
| E6-CG-11 | [Required/optional/null, limits, enum/query, create-version chưa rõ](../../chon-mon-order/review/contract-gap-register.md#L17) | API owner, BA, QA | R6 | [DEC-110](decision-pack/decision-groups.md#dec-110) | Đề xuất: Đề xuất required thiếu thì báo lỗi; optional cho phép vắng nhưng không tự cho phép null; unknown dùng null chỉ ở field được định nghĩa nullable. Không tự lấy hôm nay cho effectiveDate, không tự chọn scope hoặc chuyển unknown thành 0. Mỗi nhánh response có bảng field hiện diện riêng, ví dụ Registration pending không phát token hoặc bịa userId. |
| E6-CG-12 | [Tuần/mode/reminder policy; ORD-Q05/09, Q-14/E1-Q04](../../chon-mon-order/review/contract-gap-register.md#L18) | Chủ sản phẩm/vận hành, BA, Tech lead | R6 | [DEC-111](decision-pack/decision-groups.md#dec-111) | Đề xuất: Đề xuất chọn tuần nhận kết quả theo từng ngày: ngày hợp lệ được ghi, ngày lỗi trả lỗi riêng; không ghi một phần trong cùng ngày. Đề xuất thay đổi bật/tắt chọn món chỉ có hiệu lực từ ngày phục vụ tương lai được chọn rõ, giữ lịch sử và không tự xóa lựa chọn đã ghi. Nhắc trước mắt chỉ qua thông báo nội bộ cho người đủ điều kiện trong scope. |
| E6-CG-13 | [Wireframe chỉ mô phỏng một nguồn/version đồng bộ](../../chon-mon-order/review/contract-gap-register.md#L19) | BA/UI, QA | R6 | [DEC-112](decision-pack/decision-groups.md#dec-112) |  |
| E6-CG-14 | [Gate sức khỏe và dữ liệu/QA môi trường chưa có](../../chon-mon-order/review/contract-gap-register.md#L20) | Chủ sản phẩm, phụ trách dữ liệu, QA | R6 | [DEC-113](decision-pack/decision-groups.md#dec-113) |  |
| Q-16 | [Hạn 15:00 ngày D-1, ngưỡng 5 %/10 suất/trước 06:00 đúng thực tế không; chọn ngưỡng nhỏ hơn hay lớn hơn?](../00-ke-hoach-tong-the.md#L423) | chưa rõ | R6 | [DEC-215](decision-pack/decision-groups.md#dec-215) | Chặn: 6 ca (gate trực tiếp) |

## E7 · Giao nhận & doanh thu

### 🟡 Trung bình — 9 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-13 | [Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?](../../giao-nhan-doanh-thu/review/questions.md#L23) | chưa rõ | R7 | [DEC-114](decision-pack/decision-groups.md#dec-114) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Giữ chờ và xử lý thủ công có bằng chứng; hoặc suy định theo thỏa thuận khách có thời hạn/thông báo/tranh chấp. Chưa chọn. |
| E7-Q01 | [Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?](../../giao-nhan-doanh-thu/review/questions.md#L24) | chưa rõ | R7 | [DEC-115](decision-pack/decision-groups.md#dec-115) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Phiên có quyền hoặc token giới hạn scope cần review Auth; không lấy QR E6 làm quyền ký nhận. |
| E7-Q02 | [Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?](../../giao-nhan-doanh-thu/review/questions.md#L25) | chưa rõ | R7 | [DEC-116](decision-pack/decision-groups.md#dec-116) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ phiếu gốc + thỏa thuận/phiếu bù; cần chống đếm trùng và quyền. |
| E7-Q03 | [Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?](../../giao-nhan-doanh-thu/review/questions.md#L26) | Kế toán | R7 | [DEC-117](decision-pack/decision-groups.md#dec-117) | Đề xuất: Căn cứ từng đơn có evidence; không mặc định số nhận/số chốt. |
| E7-Q04 | [Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?](../../giao-nhan-doanh-thu/review/questions.md#L27) | Kế toán | R7 | [DEC-118](decision-pack/decision-groups.md#dec-118) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Hiện phải trả, VAT, doanh thu trước VAT riêng; không mượn dung sai Cost. |
| E7-Q05 | [Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?](../../giao-nhan-doanh-thu/review/questions.md#L28) | Kế toán | R7 | [DEC-119](decision-pack/decision-groups.md#dec-119) | Đề xuất: Snapshot từng vòng; chỉ Giám đốc duyệt mới mở. Điều kiện khác chưa chọn. |
| E7-Q06 | [Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?](../../giao-nhan-doanh-thu/review/questions.md#L29) | Kế toán | R7 | [DEC-120](decision-pack/decision-groups.md#dec-120) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Chứng từ/phân bổ riêng; không suy CK đã bù trừ. |
| E7-Q07 | [Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?](../../giao-nhan-doanh-thu/review/questions.md#L30) | Kế toán | R7 | [DEC-121](decision-pack/decision-groups.md#dec-121) | Đề xuất: Nhận mẫu có version và thử nhập môi trường được cấp; chưa giả CSV/XLSX, cột, mã thuế/tài khoản. |
| E7-Q08 | [Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?](../../giao-nhan-doanh-thu/review/questions.md#L31) | chưa rõ | R7 | [DEC-122](decision-pack/decision-groups.md#dec-122) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Kế thừa an toàn nền; review kỹ thuật, không đặt TTL/retry/limits tùy ý. |

## E8 · Website công khai

### 🟡 Trung bình — 13 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E8-Q01 | [DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ?](../../website-cong-khai/review/questions.md#L23) | chưa rõ | R8 | [DEC-123](decision-pack/decision-groups.md#dec-123) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Xuất inventory có mã bài/URL/status/hash; hoặc crawl đối chiếu bản export, không thay export bằng URL đoán |
| E8-Q02 | [Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback?](../../website-cong-khai/review/questions.md#L24) | chưa rõ | R8 | [DEC-124](decision-pack/decision-groups.md#dec-124) | Đề xuất: Giữ đường dẫn có thể bảo toàn; 301 tới nội dung tương đương. Bài xóa cần quyết định riêng; 404/410 không tự tính đạt R8 |
| E8-Q03 | [Giá suất nào được công khai; ai duyệt, thời hạn hiệu lực và cách ghi VAT/giá tham khảo ra sao?](../../website-cong-khai/review/questions.md#L25) | chưa rõ | R8 | [DEC-12](decision-pack/decision-groups.md#dec-12) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Bản giá công khai riêng được duyệt hoặc tham chiếu giá được cho phép; không lấy price_cap hay giá hợp đồng làm mặc định |
| E8-Q04 | [Nguồn E2/E4 ở trạng thái nào đủ điều kiện hiển thị định lượng, 4 chỉ số và dị ứng; làm gì khi stale/thu hồi/thiếu?](../../website-cong-khai/review/questions.md#L26) | chưa rõ | R8 | [DEC-15](decision-pack/decision-groups.md#dec-15) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Tham chiếu menu PUBLISHED, recipe ACTIVE đúng ngày và calculation có provenance; thêm phê duyệt công khai khi cần. NUTR chưa có trạng thái duyệt riêng |
| E8-Q05 | [FEAT-057 sinh mẫu từ thư viện, thuật toán hay cách khác; có phải qua máy kiểm E2; giới hạn loại suất/số suất/kiêng kỵ/ngày/lượt là gì?](../../website-cong-khai/review/questions.md#L27) | chưa rõ | R8 | [DEC-13](decision-pack/decision-groups.md#dec-13) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Lọc mẫu được duyệt hoặc dựng qua bộ kiểm không lưu E2; chưa chọn. Không nới quy tắc cứng hoặc triển khai Agent E9 |
| E8-Q06 | [Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào?](../../website-cong-khai/review/questions.md#L28) | chưa rõ | R8 | [DEC-125](decision-pack/decision-groups.md#dec-125) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Kho lead E8 riêng rồi chuyển khi E10 có contract; hoặc đầu nhận hiện hữu được duyệt. Không tự dùng customers/eaters làm lead |
| E8-Q07 | [Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao?](../../website-cong-khai/review/questions.md#L29) | chưa rõ | R8 | [DEC-126](decision-pack/decision-groups.md#dec-126) | Đề xuất: Rate limit nền + kiểm trường; bổ sung giải pháp sau review. Thông báo riêng trạng thái lưu lead, không coi gửi thông báo là lưu thành công |
| E8-Q08 | [Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào?](../../website-cong-khai/review/questions.md#L30) | chưa rõ | R8 | [DEC-127](decision-pack/decision-groups.md#dec-127) | Chặn: 5 ca (gate trực tiếp)<br>Đề xuất: Tách quyền soạn và công bố, có thể thêm duyệt độc lập; hoặc workflow ít bước được xác nhận. Không tự gán PER-05 toàn quyền |
| E8-Q09 | [Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào?](../../website-cong-khai/review/questions.md#L31) | chưa rõ | R8 | [DEC-128](decision-pack/decision-groups.md#dec-128) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Tái dùng files nền với metadata public riêng; chỉ loại ảnh trong tập nền, không tự mở SVG; lịch/cỡ chờ xác nhận |
| E8-Q10 | [BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo?](../../website-cong-khai/review/questions.md#L32) | chưa rõ | R8 | [DEC-129](decision-pack/decision-groups.md#dec-129) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: So phiên tự nhiên theo cùng công cụ/định nghĩa và kỳ so sánh tương đương; lưu bằng chứng baseline trước cutover |
| E8-Q11 | [Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04?](../../website-cong-khai/review/questions.md#L33) | chưa rõ | R8 | [DEC-130](decision-pack/decision-groups.md#dec-130) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Xác nhận quyền, diễn tập chuyển và rollback rồi mới chọn cửa sổ; không tự chọn nhà cung cấp hoặc ngày |
| E8-Q12 | [Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì?](../../website-cong-khai/review/questions.md#L34) | chưa rõ | R8 | [DEC-131](decision-pack/decision-groups.md#dec-131) | Đề xuất: Kế thừa nền khi tương thích; E4 dùng cursor/envelope khác nên adapter cần review, không tự freeze TTL/retry |
| E8-Q13 | [Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](../../website-cong-khai/review/questions.md#L35) | chưa rõ | R8 | [DEC-200](decision-pack/decision-groups.md#dec-200) | Đề xuất: Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. |

## E9 · Agent Dinh dưỡng viên

### 🟡 Trung bình — 15 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E9-Q01 | [O-04: nhà cung cấp mô hình, hạ tầng, vùng/nơi xử lý dữ liệu và đường chuyển dữ liệu nào được duyệt?](../../agent-dinh-duong-vien/review/questions.md#L23) | chưa rõ | R9 | [DEC-206](decision-pack/decision-groups.md#dec-206) | Đề xuất: So sánh phương án tự quản lý hoặc dịch vụ sau đánh giá dữ liệu; chưa chọn provider/model |
| E9-Q02 | [Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền?](../../agent-dinh-duong-vien/review/questions.md#L24) | chưa rõ | R9 | [DEC-132](decision-pack/decision-groups.md#dec-132) | Đề xuất: Chỉ tài khoản hoặc thêm guest có xác minh; không lấy IP làm danh tính mặc định |
| E9-Q03 | [Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào?](../../agent-dinh-duong-vien/review/questions.md#L25) | chưa rõ | R9 | [DEC-133](decision-pack/decision-groups.md#dec-133) | Đề xuất: Danh mục sở thích/nguyên liệu đã duyệt; nội dung ngoài danh mục dừng làm rõ; không suy luận bệnh |
| E9-Q04 | [Có hiển thị giá suất cho khách không, nguồn/hiệu lực/nhãn giá nào được duyệt?](../../agent-dinh-duong-vien/review/questions.md#L26) | chưa rõ | R9 | [DEC-217](decision-pack/decision-groups.md#dec-217) | Đề xuất: Projection giá public riêng hoặc không hiển thị cho đến khi có nguồn; không dùng price_cap làm giá bán |
| E9-Q05 | [Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không?](../../agent-dinh-duong-vien/review/questions.md#L27) | chưa rõ | R9 | [DEC-134](decision-pack/decision-groups.md#dec-134) | Đề xuất: Thông báo chung không phân biệt nguyên nhân kinh tế hoặc chuyển người thật; chưa chọn; không truyền cost result cho model |
| E9-Q06 | [FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào?](../../agent-dinh-duong-vien/review/questions.md#L28) | chưa rõ | R9 | [DEC-135](decision-pack/decision-groups.md#dec-135) | Đề xuất: Kho tiếp nhận riêng hoặc đầu nhận hiện hữu được duyệt; chỉ ACK khi ghi bền vững; tách receipt và duyệt |
| E9-Q07 | [FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần?](../../agent-dinh-duong-vien/review/questions.md#L29) | chưa rõ | R9 | [DEC-136](decision-pack/decision-groups.md#dec-136) | Đề xuất: Đếm lượt được nhận hoặc lượt hoàn tất theo policy được duyệt; reserve theo upper bound + đối soát; không có số mặc định |
| E9-Q08 | [Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy?](../../agent-dinh-duong-vien/review/questions.md#L30) | chưa rõ | R9 | [DEC-137](decision-pack/decision-groups.md#dec-137) | Đề xuất: PER-08 là persona quản trị nhưng quyền cụ thể phải cấp; nếu cần duyệt áp tách người tạo/sửa cuối |
| E9-Q09 | [Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì?](../../agent-dinh-duong-vien/review/questions.md#L31) | chưa rõ | R9 | [DEC-138](decision-pack/decision-groups.md#dec-138) | Đề xuất: Duyệt manifest, dữ liệu khả thi và rubric độc lập trước chạy; từ chối/timeout không thay thực đơn đạt |
| E9-Q10 | [Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider?](../../agent-dinh-duong-vien/review/questions.md#L32) | chưa rõ | R9 | [DEC-139](decision-pack/decision-groups.md#dec-139) | Đề xuất: Tối thiểu hóa; tách audit metadata khỏi nội dung; chốt quy trình xóa theo NFR-PRIV-001, không dùng retention log thay retention chat |
| E9-Q11 | [FEAT-057 E8 và FEAT-060 E9 dùng chung bộ dựng hay tách; contract kiểm nguồn/quy tắc và quyền public thế nào?](../../agent-dinh-duong-vien/review/questions.md#L33) | chưa rõ | R9 | [DEC-218](decision-pack/decision-groups.md#dec-218) | Đề xuất: Có thể dùng chung port kiểm thuần, hoặc bộ dựng riêng; không dùng lại credential/quota AIO |
| E9-Q12 | [Nguồn nào đủ điều kiện public; stale/thu hồi/thiếu dinh dưỡng/dị ứng xử lý ra sao; tuần/ngày phục vụ và nhiều cỡ?](../../agent-dinh-duong-vien/review/questions.md#L34) | chưa rõ | R9 | [DEC-220](decision-pack/decision-groups.md#dec-220) | Đề xuất: Projection có phiên bản nguồn, không coi thiếu là 0 hoặc không dị ứng; refresh phải kiểm lại |
| E9-Q13 | [Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9?](../../agent-dinh-duong-vien/review/questions.md#L35) | chưa rõ | R9 | [DEC-140](decision-pack/decision-groups.md#dec-140) | Đề xuất: Key bền vững gắn chủ thể/route/body; giữ reservation khi usage chưa rõ; profile theo nền chưa chọn số quota |
| E9-Q14 | [Mở FEAT-063 cần phê duyệt nào sau O-03/FEAT-046/047; PER-04 không tài khoản có được dùng không?](../../agent-dinh-duong-vien/review/questions.md#L36) | chưa rõ | R9 | [DEC-204](decision-pack/decision-groups.md#dec-204) | Đề xuất: Giữ gate đóng; sau quyết định mới review phạm vi persona, consent/quyền và contract FEAT-047; không xây nhánh gợi ý trước |
| E9-Q15 | [Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](../../agent-dinh-duong-vien/review/questions.md#L37) | chưa rõ | R9 | [DEC-201](decision-pack/decision-groups.md#dec-201) | Đề xuất: Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. |

## E10 · CRM & bán hàng

### 🟢 Thấp — 16 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E10-Q01 | [Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?](../../crm-ban-hang/review/questions.md#L26) | Chủ nghiệp vụ chăm sóc khách và người phụ trách dữ liệu | R10 | [DEC-141](decision-pack/decision-groups.md#dec-141) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Chỉ lưu trường phục vụ chăm sóc có nguồn; tách lịch sử nghiệp vụ và thông tin liên hệ. |
| E10-Q02 | [Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?](../../crm-ban-hang/review/questions.md#L27) | Chủ dữ liệu khách và Giám đốc | R10 | [DEC-142](decision-pack/decision-groups.md#dec-142) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Danh sách nghi trùng giải thích được, người thật rà từng cặp; tiêu chí cụ thể cần người quyết định cung cấp. |
| E10-Q03 | [Ai lập, ai duyệt gộp/hoàn tác; có người thay và kiểm tách nhiệm vụ thế nào?](../../crm-ban-hang/review/questions.md#L28) | Giám đốc và chủ dữ liệu khách | R10 | [DEC-208](decision-pack/decision-groups.md#dec-208) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Người duyệt khác người lập/sửa cuối; quyền gộp và hoàn tác riêng. |
| E10-Q04 | [Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?](../../crm-ban-hang/review/questions.md#L29) | Chủ dữ liệu khách, kế toán và trưởng kỹ thuật | R10 | [DEC-143](decision-pack/decision-groups.md#dec-143) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Ghi bù có diff, giữ snapshot tài chính; có xung đột thì chờ phương án được duyệt. |
| E10-Q05 | [Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?](../../crm-ban-hang/review/questions.md#L30) | Chăm sóc khách và vận hành | R10 | [DEC-144](decision-pack/decision-groups.md#dec-144) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Giữ sự kiện có bằng chứng, tín hiệu riêng với trạng thái; người thật xác nhận chuyển quan trọng. |
| E10-Q06 | [Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?](../../crm-ban-hang/review/questions.md#L31) | Chăm sóc khách và vận hành | R10 | [DEC-145](decision-pack/decision-groups.md#dec-145) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Đếm kỳ phục vụ dự kiến đủ nguồn và giải thích từng tín hiệu; thiếu lịch thì chưa đánh giá. |
| E10-Q07 | [Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?](../../crm-ban-hang/review/questions.md#L32) | Chủ nghiệp vụ bán hàng và Giám đốc | R10 | [DEC-146](decision-pack/decision-groups.md#dec-146) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Lịch sử chuyển giai đoạn có bằng chứng; đếm một cơ hội duy nhất trong cùng tập đo. |
| E10-Q08 | [Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?](../../crm-ban-hang/review/questions.md#L33) | Giám đốc và chủ nghiệp vụ bán hàng | R10 | [DEC-147](decision-pack/decision-groups.md#dec-147) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Bản phát hành bất biến có revision/hash, bằng chứng chấp thuận gắn đúng bản. |
| E10-Q09 | [Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?](../../crm-ban-hang/review/questions.md#L34) | Dinh dưỡng viên và người duyệt báo giá | R10 | [DEC-148](decision-pack/decision-groups.md#dec-148) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Bản chụp projection được phép, có revision/hash; nguồn không đủ thì chặn phát hành. |
| E10-Q10 | [Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?](../../crm-ban-hang/review/questions.md#L35) | Giám đốc và kế toán phụ trách hợp đồng | R10 | [DEC-149](decision-pack/decision-groups.md#dec-149) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Lưu nguồn văn bản, người xác nhận và thời điểm; chỉ kích hoạt sau đủ bằng chứng. |
| E10-Q11 | [Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?](../../crm-ban-hang/review/questions.md#L36) | Kế toán và chủ nghiệp vụ bán hàng | R10 | [DEC-150](decision-pack/decision-groups.md#dec-150) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Chốt một quy ước ngày cho hợp đồng và consumer; giữ khóa phạm vi hiện có cho tới khi có quyết định. |
| E10-Q12 | [Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?](../../crm-ban-hang/review/questions.md#L37) | Kế toán, người duyệt hợp đồng và vận hành | R10 | [DEC-151](decision-pack/decision-groups.md#dec-151) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Mặc định thiết kế giữ lịch sử và chờ quyết định riêng cho hồi tố; chỉ dùng giá mới khi đủ hiệu lực. |
| E10-Q13 | [Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?](../../crm-ban-hang/review/questions.md#L38) | Trưởng kỹ thuật, chủ các nguồn và QA | R10 | [DEC-152](decision-pack/decision-groups.md#dec-152) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Adapter từng nguồn; khóa nghiệp vụ bền vững và đối soát sau timeout; profile theo nền. |
| E10-Q14 | [Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?](../../crm-ban-hang/review/questions.md#L39) | Giám đốc, chăm sóc khách, kế toán và QA | R10 | [DEC-153](decision-pack/decision-groups.md#dec-153) | Đề xuất: Manifest nguồn có ngày chốt và chữ ký xác nhận, đối chiếu từng khách/hợp đồng, công khai thiếu. |
| E10-Q15 | [Biên lợi nhuận nội bộ trên báo giá dùng công thức, thành phần và nguồn phiên bản nào; ai được xem?](../../crm-ban-hang/review/questions.md#L40) | Kế toán và Giám đốc | R10 | [DEC-14](decision-pack/decision-groups.md#dec-14) | Đề xuất: Giữ giá trị chưa xác định tới khi công thức/nguồn được duyệt; quyền riêng với báo giá. |
| E10-Q16 | [Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](../../crm-ban-hang/review/questions.md#L41) | chưa rõ | R10 | [DEC-202](decision-pack/decision-groups.md#dec-202) | Đề xuất: Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. |

## E11 · Mua hàng & sản xuất

### 🟢 Thấp — 15 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E11-Q01 | [Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng?](../../mua-hang-san-xuat/review/questions.md#L26) | chưa rõ | R11 | [DEC-154](decision-pack/decision-groups.md#dec-154) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Tách nhu cầu gộp khỏi lượng đề nghị mua; chưa tự trừ tồn hoặc đặt mức tối thiểu. |
| E11-Q02 | [Ai lập, duyệt, phát hành đơn mua; xử lý sửa/hủy và người thay thế thế nào?](../../mua-hang-san-xuat/review/questions.md#L27) | chưa rõ | R11 | [DEC-209](decision-pack/decision-groups.md#dec-209) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Dùng tách tạo/duyệt của E1; chưa gán vai trò duyệt hoặc hạn mức. |
| E11-Q03 | [Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào?](../../mua-hang-san-xuat/review/questions.md#L28) | chưa rõ | R11 | [DEC-155](decision-pack/decision-groups.md#dec-155) | Đề xuất: Chỉ quản lý lô FROZEN/DRY; chưa chọn FIFO/FEFO hay bắt buộc hạn dùng. |
| E11-Q04 | [Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao?](../../mua-hang-san-xuat/review/questions.md#L29) | chưa rõ | R11 | [DEC-156](decision-pack/decision-groups.md#dec-156) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ lượng đặt, lượng thực nhận, lượng chấp nhận riêng; cần quyết định trước ghi nhận chính thức. |
| E11-Q05 | [Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không?](../../mua-hang-san-xuat/review/questions.md#L30) | chưa rõ | R11 | [DEC-157](decision-pack/decision-groups.md#dec-157) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Dùng tệp nội bộ E1 và ảnh gắn đúng phiếu; không OCR, không tự chọn thời hạn lưu. |
| E11-Q06 | [Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào?](../../mua-hang-san-xuat/review/questions.md#L31) | chưa rõ | R11 | [DEC-158](decision-pack/decision-groups.md#dec-158) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Tách phiếu nhận, nghĩa vụ phải trả và chứng từ thanh toán; chưa suy đã trả từ đã nhận. |
| E11-Q07 | [Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung?](../../mua-hang-san-xuat/review/questions.md#L32) | chưa rõ | R11 | [DEC-159](decision-pack/decision-groups.md#dec-159) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Giữ nguồn mua và phân bổ riêng, chưa chọn phương pháp phân bổ. |
| E11-Q08 | [BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào?](../../mua-hang-san-xuat/review/questions.md#L33) | chưa rõ | R11 | [DEC-160](decision-pack/decision-groups.md#dec-160) | Đề xuất: Đề nghị so hai tỷ lệ cùng phạm vi và cùng mẫu số đã duyệt; không thay mục tiêu ≤ 3 điểm phần trăm. |
| E11-Q09 | [Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào?](../../mua-hang-san-xuat/review/questions.md#L34) | chưa rõ | R11 | [DEC-161](decision-pack/decision-groups.md#dec-161) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Lưu phân công nháp theo cơ sở/ca; chưa đặt số người hoặc giờ ca. |
| E11-Q10 | [Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi?](../../mua-hang-san-xuat/review/questions.md#L35) | chưa rõ | R11 | [DEC-162](decision-pack/decision-groups.md#dec-162) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Tách kết quả QC khỏi phiếu giao E7; mục không đạt/thiếu không tự coi đạt. |
| E11-Q11 | [Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì?](../../mua-hang-san-xuat/review/questions.md#L36) | chưa rõ | R11 | [DEC-163](decision-pack/decision-groups.md#dec-163) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Có mã mẫu gắn bữa/cơ sở, người ghi và thời điểm; không tự đặt hạn hoặc định lượng mẫu. |
| E11-Q12 | [Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào?](../../mua-hang-san-xuat/review/questions.md#L37) | chưa rõ | R11 | [DEC-164](decision-pack/decision-groups.md#dec-164) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Chỉ tạo ứng viên nháp; nguồn đổi phải kiểm lại, không sửa trực tiếp order/plan. |
| E11-Q13 | [Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt?](../../mua-hang-san-xuat/review/questions.md#L38) | chưa rõ | R11 | [DEC-165](decision-pack/decision-groups.md#dec-165) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Đề nghị version kiểm khi ghi, audit và chống lặp; không chọn TTL, retry hoặc SLA mới. |
| E11-Q14 | [Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào?](../../mua-hang-san-xuat/review/questions.md#L39) | chưa rõ | R11 | [DEC-166](decision-pack/decision-groups.md#dec-166) | Đề xuất: Đối chiếu PriceInput; không ghi đè giá hiệu lực hoặc tự đặt giá tham chiếu. |
| E11-Q15 | [Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân?](../../mua-hang-san-xuat/review/questions.md#L40) | chưa rõ | R11 | [DEC-167](decision-pack/decision-groups.md#dec-167) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Dùng nhãn chất gây dị ứng của món và ràng buộc thực đơn đã được phép; thiếu căn cứ thì chặn. |

## E12 · Phản hồi & báo cáo

### 🟢 Thấp — 18 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E12-Q01 | [Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì?](../../phan-hoi-bao-cao/review/questions.md#L26) | chưa rõ | R12 | [DEC-168](decision-pack/decision-groups.md#dec-168) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Dùng thang có phiên bản và nguồn quyết định; chưa chọn số mức hoặc trung bình. |
| E12-Q02 | [Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao?](../../phan-hoi-bao-cao/review/questions.md#L27) | chưa rõ | R12 | [DEC-169](decision-pack/decision-groups.md#dec-169) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Kế thừa identity E6 khi được chốt; giữ nguồn và receipt, không chọn quy tắc một người một điểm thay stakeholder. |
| E12-Q03 | [Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào?](../../phan-hoi-bao-cao/review/questions.md#L28) | chưa rõ | R12 | [DEC-170](decision-pack/decision-groups.md#dec-170) | Đề xuất: Tách tiếp nhận khỏi giải quyết; chưa đặt SLA hoặc người xử lý. |
| E12-Q04 | [Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào?](../../phan-hoi-bao-cao/review/questions.md#L29) | chưa rõ | R12 | [DEC-171](decision-pack/decision-groups.md#dec-171) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Giữ provenance lựa chọn thật và định nghĩa có phiên bản; hiển thị chưa xác định trước khi duyệt. Không chọn sẵn một mẫu số. |
| E12-Q05 | [Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao?](../../phan-hoi-bao-cao/review/questions.md#L30) | chưa rõ | R12 | [DEC-172](decision-pack/decision-groups.md#dec-172) | Đề xuất: Người thật review căn cứ; kiểm lại E2/dị ứng/E3, không đổi thực đơn trực tiếp. |
| E12-Q06 | [Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào?](../../phan-hoi-bao-cao/review/questions.md#L31) | chưa rõ | R12 | [DEC-173](decision-pack/decision-groups.md#dec-173) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Review catalog M-FBR-01…09 theo công việc từng vai trò; không coi danh sách đề xuất là mặc định. |
| E12-Q07 | [Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope?](../../phan-hoi-bao-cao/review/questions.md#L32) | chưa rõ | R12 | [DEC-174](decision-pack/decision-groups.md#dec-174) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Quyền trường riêng, deny by default, projection ở server/tool/DB; không tự cấp do tên vai trò. |
| E12-Q08 | [Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào?](../../phan-hoi-bao-cao/review/questions.md#L33) | chưa rõ | R12 | [DEC-175](decision-pack/decision-groups.md#dec-175) | Đề xuất: Giữ riêng cost % thực đơn và dự toán E3; không bình quân tỷ lệ hoặc suy từ số giao. Chờ định nghĩa tổng hợp có nguồn. |
| E12-Q09 | [Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì?](../../phan-hoi-bao-cao/review/questions.md#L34) | chưa rõ | R12 | [DEC-176](decision-pack/decision-groups.md#dec-176) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Allowlist đọc theo người hỏi; mọi thay món/định lượng kiểm lại ba nguồn cùng hash; không cấp apply. |
| E12-Q10 | [Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì?](../../phan-hoi-bao-cao/review/questions.md#L35) | chưa rõ | R12 | [DEC-177](decision-pack/decision-groups.md#dec-177) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: So nguồn cùng căn cứ và để ngưỡng trống; không mượn BO-02/NFR-COST-002. |
| E12-Q11 | [FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp?](../../phan-hoi-bao-cao/review/questions.md#L36) | chưa rõ | R12 | [DEC-178](decision-pack/decision-groups.md#dec-178) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Chỉ đọc projection E10 theo quyền; không tạo task/quote, gửi hoặc cam kết giá. |
| E12-Q12 | [FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm?](../../phan-hoi-bao-cao/review/questions.md#L37) | chưa rõ | R12 | [DEC-179](decision-pack/decision-groups.md#dec-179) | Đề xuất: Catalog câu hỏi/chỉ số có nguồn, kiểm từng công cụ và output; thiếu định nghĩa thì không trả số. |
| E12-Q13 | [Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì?](../../phan-hoi-bao-cao/review/questions.md#L38) | chưa rõ | R12 | [DEC-180](decision-pack/decision-groups.md#dec-180) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Mục tiêu cấp nhóm, không theo bệnh lý/cá nhân; số cụ thể chờ NUTR-Q01–04. |
| E12-Q14 | [Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không?](../../phan-hoi-bao-cao/review/questions.md#L39) | chưa rõ | R12 | [DEC-181](decision-pack/decision-groups.md#dec-181) | Đề xuất: Mục tiêu nháp có phiên bản; chưa thêm cổng MENU hoặc chọn ưu tiên bản mới. |
| E12-Q15 | [Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào?](../../phan-hoi-bao-cao/review/questions.md#L40) | chưa rõ | R12 | [DEC-182](decision-pack/decision-groups.md#dec-182) | Chặn: 5 ca (gate trực tiếp)<br>Đề xuất: Đồng ý tự nguyện riêng cho bữa đã ăn; không chọn sẵn, không ảnh hưởng chọn món; không hồ sơ sức khỏe. |
| E12-Q16 | [Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào?](../../phan-hoi-bao-cao/review/questions.md#L41) | chưa rõ | R12 | [DEC-183](decision-pack/decision-groups.md#dec-183) | Đề xuất: Kế thừa xóa ≤ 72 giờ của nền; tách receipt/hoàn tất; không đặt retention hoặc xóa giao dịch nguồn. |
| E12-Q17 | [Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào?](../../phan-hoi-bao-cao/review/questions.md#L42) | chưa rõ | R12 | [DEC-184](decision-pack/decision-groups.md#dec-184) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Cân nhắc xác nhận tự nguyện của người ăn có scope và snapshot; chưa chọn làm chính sách. Không suy từ order/giao/chọn món. |
| E12-Q18 | [Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào?](../../phan-hoi-bao-cao/review/questions.md#L43) | chưa rõ | R12 | [DEC-185](decision-pack/decision-groups.md#dec-185) | Chặn: 4 ca (gate trực tiếp)<br>Đề xuất: Adapter theo nguồn, quyền hiện tại và provenance; không tự đặt TTL, retry, quota hoặc chọn hạ tầng. |

## E13 · Chi phí & lợi nhuận

### 🟢 Thấp — 14 câu

| Mã | Câu hỏi | Người quyết định | Release | Nhóm | Ghi chú |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E13-Q01 | [Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì?](../../chi-phi-loi-nhuan/review/questions.md#L26) | chưa rõ | R13 | [DEC-186](decision-pack/decision-groups.md#dec-186) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Duyệt danh mục có phiên bản; mỗi khoản chỉ thuộc một nguồn và một nhóm trong cùng báo cáo. |
| E13-Q02 | [Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào?](../../chi-phi-loi-nhuan/review/questions.md#L27) | chưa rõ | R13 | [DEC-187](decision-pack/decision-groups.md#dec-187) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Chốt cùng scope đối soát; không mặc định tháng hoặc người khóa. |
| E13-Q03 | [Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì?](../../chi-phi-loi-nhuan/review/questions.md#L28) | chưa rõ | R13 | [DEC-188](decision-pack/decision-groups.md#dec-188) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Giữ tham chiếu phân ca E11 riêng với giờ thực tế có chứng cứ; không mặc định phần mềm chấm công. |
| E13-Q04 | [Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao?](../../chi-phi-loi-nhuan/review/questions.md#L29) | chưa rõ | R13 | [DEC-189](decision-pack/decision-groups.md#dec-189) | Đề xuất: Tham chiếu phiên bản nguồn được duyệt; không xây quy trình tính lương. |
| E13-Q05 | [Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao?](../../chi-phi-loi-nhuan/review/questions.md#L30) | Giám đốc | R13 | [DEC-190](decision-pack/decision-groups.md#dec-190) | Chặn: 5 ca (gate trực tiếp)<br>Đề xuất: Trình các lựa chọn theo suất/doanh thu/giờ công/diện tích/kết hợp cùng dữ liệu đối chiếu; không chọn sẵn. |
| E13-Q06 | [Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào?](../../chi-phi-loi-nhuan/review/questions.md#L31) | chưa rõ | R13 | [DEC-191](decision-pack/decision-groups.md#dec-191) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Tách pool cấp công ty, chưa phân bổ không giấu vào cơ sở hoặc khách; chỉ dùng sau quyết định. |
| E13-Q07 | [Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào?](../../chi-phi-loi-nhuan/review/questions.md#L32) | chưa rõ | R13 | [DEC-192](decision-pack/decision-groups.md#dec-192) | Chặn: 1 ca (gate trực tiếp)<br>Đề xuất: Giữ customerRef gốc, kitchenRef và revision nguồn; tổng hợp sau đối chiếu từng cơ sở. |
| E13-Q08 | [Kết quả kinh doanh cơ sở gồm khoản nào, nguồn chuẩn nào, ghi nhận điều chỉnh và CK ra sao?](../../chi-phi-loi-nhuan/review/questions.md#L33) | chưa rõ | R13 | [DEC-219](decision-pack/decision-groups.md#dec-219) | Đề xuất: Cần manifest thành phần và định nghĩa có phiên bản; không suy lợi nhuận bằng doanh thu trừ riêng cost nguyên liệu. |
| E13-Q09 | [Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào?](../../chi-phi-loi-nhuan/review/questions.md#L34) | chưa rõ | R13 | [DEC-193](decision-pack/decision-groups.md#dec-193) | Đề xuất: Đối chiếu số gốc decimal; phần dư hiện riêng, không tự dồn cho khách cuối; chặn nếu chưa có quy tắc. |
| E13-Q10 | [Ai duyệt điều chỉnh sau khóa, ghi vào kỳ nào và bằng chứng nào bắt buộc?](../../chi-phi-loi-nhuan/review/questions.md#L35) | chưa rõ | R13 | [DEC-210](decision-pack/decision-groups.md#dec-210) | Chặn: 2 ca (gate trực tiếp)<br>Đề xuất: Bút toán riêng gắn bản gốc, lý do và người duyệt khác người lập/sửa cuối; không mở khóa tại E13. |
| E13-Q11 | [Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào?](../../chi-phi-loi-nhuan/review/questions.md#L36) | chưa rõ | R13 | [DEC-194](decision-pack/decision-groups.md#dec-194) | Đề xuất: Deny by default; chỉ cấp từng quyền cần dùng cho hai persona, không suy mọi kế toán đều thấy mọi cơ sở. |
| E13-Q12 | [Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào?](../../chi-phi-loi-nhuan/review/questions.md#L37) | chưa rõ | R13 | [DEC-195](decision-pack/decision-groups.md#dec-195) | Chặn: 3 ca (gate trực tiếp)<br>Đề xuất: Nguồn không đầy đủ thì BLOCKED; chụp manifest và không ghi lại snapshot cũ; chưa đặt TTL, SLA, định dạng xuất. |
| E13-Q13 | [Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào?](../../chi-phi-loi-nhuan/review/questions.md#L38) | chưa rõ | R13 | [DEC-196](decision-pack/decision-groups.md#dec-196) | Đề xuất: Đề xuất chỉ đọc tổng hợp có version và trạng thái; không thay cost % E12, không chốt E10-Q15. |
| E13-Q14 | [Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu?](../../chi-phi-loi-nhuan/review/questions.md#L39) | chưa rõ | R13 | [DEC-197](decision-pack/decision-groups.md#dec-197) | Đề xuất: Lập bộ chứng từ cùng kỳ/cơ sở, số chuẩn độc lập; Giám đốc xác nhận phương pháp rồi đối chiếu. |
