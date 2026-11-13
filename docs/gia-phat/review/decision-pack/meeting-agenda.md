---
id: DOC-DECISION-PACK-MEET
title: Chương trình họp theo vai trò
version: 0.1.1
phase: Review
domain: Gia Phát
tags: [decision-pack, draft, review]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Chương trình họp theo vai trò

Nháp · 13/11/2026 · Chuẩn bị quyết định, chưa phê duyệt.

| Phiên bản | Ngày | Vai trò | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | DEC-27; BA-Q; XC-05/12 |
| 0.1.0 | 13/11/2026 | BA | Hợp nhất nguồn để review; giữ câu mở |

Theo skill meet và mẫu 48: phân biệt nội dung thảo luận, quyết định có chữ ký và việc theo sau. Đây là chương trình cùng biên bản trống, không phải biên bản cuộc họp đã diễn ra. Không đặt lịch triển khai, tên người hoặc thời lượng ước đoán.

**Chốt các nhóm trong buổi 1–3 là điều kiện để chuyển MVP E1–E5 sang trạng thái có thể duyệt.** Còn cần evidence dữ liệu và review artifact bị ảnh hưởng; không tự chuyển sang đã duyệt. Các nhóm P-MVP đều được xếp trong ba buổi này. E1-Q được rà tiếp kỹ thuật ở buổi 4.

E6-EVID-001 chỉ xác nhận có danh sách và quản lý xác nhận. E6-EVID-002 yêu cầu giữ mở scope nhiều công ty, C→S và vượt T: chỉ đọc lại evidence; không yêu cầu trả lời lại khi chưa có yêu cầu chốt hoặc thông tin mới. Các nhóm liên quan vẫn có chỗ trong chương trình để theo dõi, không ép biểu quyết.

<a id="buoi-1"></a>

## Buổi 1 — Giám đốc — phạm vi và quyền quyết định

Mục tiêu: Chốt phạm vi O-03, nguồn lực O-04, người duyệt/người thay O-06; rà quyền và các gate nền của MVP.

Tham dự: Giám đốc, Tech lead, Kế toán, BA, phụ trách dữ liệu. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Ma trận quyền hiện hành; cơ chế thay người; ranh giới dữ liệu được phép; nhu cầu nguồn lực và trần ngân sách chưa điền.

Các nhóm cần review:

- [DEC-01 — Gợi ý cá nhân có xét bệnh lý không](decision-groups.md#dec-01) (O-03).
- [DEC-02 — Đội phát triển, hạ tầng, nhà cung cấp AI, ngân sách](decision-groups.md#dec-02) (O-04).
- [DEC-03 — Ai duyệt ngoại lệ và ai thay khi vắng](decision-groups.md#dec-03) (O-06).
- [DEC-06 — Chuẩn envelope giữa các phân hệ](decision-groups.md#dec-06) (E1-Q01, E6-CG-09).
- [DEC-16 — Trường học, bệnh viện, tiệc cỗ có trong bản đầu không](decision-groups.md#dec-16) (O-05).
- [DEC-17 — Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không?](decision-groups.md#dec-17) (E1-Q02).
- [DEC-18 — MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể?](decision-groups.md#dec-18) (E1-Q03).
- [DEC-19 — Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu?](decision-groups.md#dec-19) (E1-Q04).
- [DEC-20 — Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào?](decision-groups.md#dec-20) (E1-Q05).
- [DEC-21 — Nhân viên đăng nhập bằng số điện thoại, email, hay tên do quản trị đặt? (Bếp trưởng có thể không có email công việc.)](decision-groups.md#dec-21) (N-01).
- [DEC-22 — Ai giữ vai trò quản trị hệ thống: người của Gia Phát hay đội phát triển?](decision-groups.md#dec-22) (N-02).
- [DEC-23 — Thời gian lưu nhật ký thay đổi (đề xuất 5 năm) và nhật ký đăng nhập (đề xuất 1 năm)](decision-groups.md#dec-23) (N-03).
- [DEC-24 — Có bắt buộc xác thực 2 bước cho Giám đốc, kế toán doanh thu, quản trị không?](decision-groups.md#dec-24) (N-04).
- [DEC-26 — Số người ăn, số công ty, số điểm giao mỗi ngày](decision-groups.md#dec-26) (Q-18).
- [DEC-198 — NFR-PERF-003 đo ký tự nội dung đầu hay phản hồi tiến trình đầu; mốc bắt đầu, kết thúc và cách đo với polling là gì?](decision-groups.md#dec-198) (E1-Q06).
- [DEC-199 — E5 phải cung cấp bằng chứng nào để đối chiếu phép đo phản hồi đầu NFR-PERF-003 với polling và thời gian dựng thực đơn?](decision-groups.md#dec-199) (AIO-Q07).
- [DEC-203 — Nếu mở O-03: consent/version, rút đồng ý, thời hạn xóa/lưu log, phạm vi bệnh lý và tiêu chí gợi ý cụ thể?](decision-groups.md#dec-203) (ORD-Q15).
- [DEC-204 — Mở FEAT-063 cần phê duyệt nào sau O-03/FEAT-046/047; PER-04 không tài khoản có được dùng không?](decision-groups.md#dec-204) (E9-Q14).
- [DEC-205 — Nhà cung cấp/model, ngân sách, concurrency, số lần thử, token tối đa và cách ghi chi phí/tỷ giá nào?](decision-groups.md#dec-205) (AIO-Q01).
- [DEC-206 — O-04: nhà cung cấp mô hình, hạ tầng, vùng/nơi xử lý dữ liệu và đường chuyển dữ liệu nào được duyệt?](decision-groups.md#dec-206) (E9-Q01).
- [DEC-207 — Ai lập/sửa, ai duyệt chiết khấu; phân cấp tiền/tỷ lệ, tự duyệt và người thay khi vắng thế nào?](decision-groups.md#dec-207) (CK-Q04).
- [DEC-208 — Ai lập, ai duyệt gộp/hoàn tác; có người thay và kiểm tách nhiệm vụ thế nào?](decision-groups.md#dec-208) (E10-Q03).
- [DEC-209 — Ai lập, duyệt, phát hành đơn mua; xử lý sửa/hủy và người thay thế thế nào?](decision-groups.md#dec-209) (E11-Q02).
- [DEC-210 — Ai duyệt điều chỉnh sau khóa, ghi vào kỳ nào và bằng chứng nào bắt buộc?](decision-groups.md#dec-210) (E13-Q10).

Đọc trước:

- [docs/gia-phat/01-prd.md](../../01-prd.md).
- [docs/chon-mon-order/review/questions.md](../../../chon-mon-order/review/questions.md).
- [docs/agent-dinh-duong-vien/review/questions.md](../../../agent-dinh-duong-vien/review/questions.md).
- [docs/agent-noi-bo/review/questions.md](../../../agent-noi-bo/review/questions.md).
- [docs/mua-hang-san-xuat/review/questions.md](../../../mua-hang-san-xuat/review/questions.md).
- [docs/chi-phi-loi-nhuan/review/questions.md](../../../chi-phi-loi-nhuan/review/questions.md).
- [docs/crm-ban-hang/review/questions.md](../../../crm-ban-hang/review/questions.md).
- [docs/cost/accounting/business-rules.md](../../../cost/accounting/business-rules.md).
- [docs/nen-tang/review/questions.md](../../../nen-tang/review/questions.md).
- [docs/chon-mon-order/review/contract-gap-register.md](../../../chon-mon-order/review/contract-gap-register.md).
- [docs/nen-tang/srs/spec.md](../../../nen-tang/srs/spec.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-2"></a>

## Buổi 2 — Dinh dưỡng viên / bếp trưởng — quy tắc và dữ liệu MVP

Mục tiêu: Chốt DL-01, O-02, NUTR-Q và đầu vào/tiêu chí agent nội bộ.

Tham dự: Dinh dưỡng viên, Bếp trưởng, người soạn docx, QA, Chủ sản phẩm, Tech lead, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Bản 43 quy tắc; danh mục 30 món và công thức; đơn vị, hao hụt; nguồn dinh dưỡng; 5 suất tính tay; bộ 20 yêu cầu và cách đo thời gian trước MVP.

Các nhóm cần review:

- [DEC-04 — Cỡ định lượng của một món](decision-groups.md#dec-04) (O-02, H-9).
- [DEC-27 — Phiên bản quy tắc được duyệt: biên tuần, Healthy, lặp nhóm nguyên liệu, cặp loại trừ và phương pháp chế biến](decision-groups.md#dec-27) (DL-01, E2-Q2, H-1, H-2, H-3, H-4, H-8).
- [DEC-28 — Cách kiểm ngưỡng giá suất](decision-groups.md#dec-28) (E2-Q1).
- [DEC-30 — Tuần phục vụ gồm những ngày nào](decision-groups.md#dec-30) (E2-Q3).
- [DEC-31 — Thực đơn chung hay riêng theo khách](decision-groups.md#dec-31) (E2-Q4).
- [DEC-32 — Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)](decision-groups.md#dec-32) (E2-Q6).
- [DEC-33 — Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?](decision-groups.md#dec-33) (E2-Q7).
- [DEC-34 — Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?](decision-groups.md#dec-34) (E2-Q8).
- [DEC-35 — Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)](decision-groups.md#dec-35) (E2-Q9).
- [DEC-36 — Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)](decision-groups.md#dec-36) (E2-Q10).
- [DEC-37 — Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)](decision-groups.md#dec-37) (E2-Q11).
- [DEC-38 — Khoảng định lượng và chất độn dùng chuẩn từng món hay bảng theo nguyên liệu/kiểu món; lưu ở đâu?](decision-groups.md#dec-38) (E2-Q5).
- [DEC-43 — Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào?](decision-groups.md#dec-43) (H-5).
- [DEC-86 — Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu?](decision-groups.md#dec-86) (NUTR-Q01).
- [DEC-87 — Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi?](decision-groups.md#dec-87) (NUTR-Q03).
- [DEC-88 — Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.](decision-groups.md#dec-88) (NUTR-Q04).
- [DEC-89 — Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp.](decision-groups.md#dec-89) (DATA-NUTR-Q01).
- [DEC-90 — Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không?](decision-groups.md#dec-90) (AIO-Q02).
- [DEC-91 — 20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao?](decision-groups.md#dec-91) (AIO-Q03).
- [DEC-92 — Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào?](decision-groups.md#dec-92) (AIO-Q04).
- [DEC-93 — Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào?](decision-groups.md#dec-93) (AIO-Q05).
- [DEC-94 — Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout?](decision-groups.md#dec-94) (AIO-Q06).

Đọc trước:

- [docs/thuc-don-dinh-luong/srs/spec.md](../../../thuc-don-dinh-luong/srs/spec.md).
- [docs/gia-phat/01-prd.md](../../01-prd.md).
- [docs/gia-phat/brainstorms/quy-tac-thuc-don.md](../../brainstorms/quy-tac-thuc-don.md).
- [docs/dinh-duong/review/questions.md](../../../dinh-duong/review/questions.md).
- [docs/cost/review/decision-register.md](../../../cost/review/decision-register.md).
- [docs/agent-noi-bo/review/questions.md](../../../agent-noi-bo/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-3"></a>

## Buổi 3 — Kế toán — cost, chiết khấu và bộ đối chiếu

Mục tiêu: Chốt O-01, CK-Q01–10, DATA-COST-Q01–06 và các gate Cost còn mở.

Tham dự: Kế toán, Giám đốc, phụ trách thỏa thuận khách, Dinh dưỡng viên, Bếp trưởng, Tech lead, QA, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: 10 món / 10 ngày thật: công thức, đơn vị/quy đổi, giá báo/giá cuối gồm VAT, chứng từ, VAT bán ra, khoản khoán, cách tính món chính, kết quả chưa/sau làm tròn; đơn gốc và khoản chiết khấu riêng.

Các nhóm cần review:

- [DEC-05 — Thành phần cost và VAT bán ra còn thiếu](decision-groups.md#dec-05) (O-01, H-6, H-7).
- [DEC-09 — Định lượng sống đã gồm xương, vỏ chưa](decision-groups.md#dec-09) (E3-Q2).
- [DEC-45 — Cost phần món chính](decision-groups.md#dec-45) (E3-Q1).
- [DEC-46 — Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào](decision-groups.md#dec-46) (E3-Q3).
- [DEC-47 — Giá nào là giá tham chiếu](decision-groups.md#dec-47) (E3-Q4).
- [DEC-48 — Tần suất cập nhật giá thực tế](decision-groups.md#dec-48) (E3-Q5).
- [DEC-49 — Giá nhập có cần duyệt](decision-groups.md#dec-49) (E3-Q6).
- [DEC-50 — Định nghĩa cost cao / thấp](decision-groups.md#dec-50) (E3-Q7).
- [DEC-51 — Nguồn số suất trước khi có order](decision-groups.md#dec-51) (E3-Q8).
- [DEC-52 — Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ](decision-groups.md#dec-52) (E3-Q9).
- [DEC-53 — Chặn chuyển bếp](decision-groups.md#dec-53) (E3-Q10).
- [DEC-54 — Bếp trưởng có xem giá và cost](decision-groups.md#dec-54) (E3-Q11).
- [DEC-55 — Khi tính BINH_QUAN hoặc DAT_NHAT, món chính Healthy (thường rẻ hơn) có được tính vào không](decision-groups.md#dec-55) (E3-Q12).
- [DEC-56 — Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không](decision-groups.md#dec-56) (E3-Q13).
- [DEC-57 — FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không?](decision-groups.md#dec-57) (E3-Q14).
- [DEC-58 — Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick](decision-groups.md#dec-58) (E3-Q15).
- [DEC-59 — Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá?](decision-groups.md#dec-59) (E3-Q16).
- [DEC-60 — Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào?](decision-groups.md#dec-60) (FLOW-COST-Q01).
- [DEC-61 — Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào?](decision-groups.md#dec-61) (FLOW-COST-Q02).
- [DEC-62 — Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào?](decision-groups.md#dec-62) (FLOW-COST-Q03).
- [DEC-63 — Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào?](decision-groups.md#dec-63) (FLOW-COST-Q04).
- [DEC-64 — Ai được đọc danh sách/chi tiết khoản khoán?](decision-groups.md#dec-64) (FLOW-COST-Q05).
- [DEC-65 — Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào?](decision-groups.md#dec-65) (FLOW-COST-Q06).
- [DEC-66 — Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ?](decision-groups.md#dec-66) (FLOW-COST-Q07).
- [DEC-67 — Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao?](decision-groups.md#dec-67) (FLOW-COST-Q08).
- [DEC-68 — Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không?](decision-groups.md#dec-68) (FLOW-COST-Q09).
- [DEC-69 — Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào?](decision-groups.md#dec-69) (FLOW-COST-Q10).
- [DEC-70 — NCC tồn tại INACTIVE trả 404-01 hay 422-02?](decision-groups.md#dec-70) (QA-COST-Q01).
- [DEC-71 — Chiết khấu % tính trên tiền suất đã gồm VAT hay chưa VAT? Cơ sở tính có bao gồm khoản phụ thu nào không?](decision-groups.md#dec-71) (CK-Q01).
- [DEC-72 — Chiết khấu áp dụng mọi suất hay từng loại/dòng; số lượng căn cứ đặt, giao hay khách xác nhận?](decision-groups.md#dec-72) (CK-Q02).
- [DEC-73 — Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào?](decision-groups.md#dec-73) (CK-Q03).
- [DEC-74 — Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai?](decision-groups.md#dec-74) (CK-Q05).
- [DEC-75 — Xác nhận/xử lý chiết khấu lúc chốt, giao, thanh toán hay cuối kỳ; xử lý một phần và chứng từ thế nào?](decision-groups.md#dec-75) (CK-Q06).
- [DEC-76 — Đơn đổi suất/giá/loại khi chiết khấu chưa xử lý: tự tính lại, duyệt lại và giữ phiên bản cũ thế nào?](decision-groups.md#dec-76) (CK-Q07).
- [DEC-77 — Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không?](decision-groups.md#dec-77) (CK-Q08).
- [DEC-78 — Đơn đổi/hủy sau chi trả/bù trừ: thu hồi, bù kỳ sau hay điều chỉnh riêng; ai duyệt, chứng từ nào?](decision-groups.md#dec-78) (CK-Q09).
- [DEC-79 — Một đơn hưởng đồng thời chiết khấu %/tiền mỗi suất hoặc nhiều chương trình được không; cộng dồn, ưu tiên, trần thế nào?](decision-groups.md#dec-79) (CK-Q10).
- [DEC-80 — Ai phụ trách cung cấp và xác nhận 10 món/10 ngày thực tế? Khi nào có dữ liệu?](decision-groups.md#dec-80) (DATA-COST-Q01).
- [DEC-81 — File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào?](decision-groups.md#dec-81) (DATA-COST-Q02).
- [DEC-82 — Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào?](decision-groups.md#dec-82) (DATA-COST-Q03).
- [DEC-83 — Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào?](decision-groups.md#dec-83) (DATA-COST-Q04).
- [DEC-84 — Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập?](decision-groups.md#dec-84) (DATA-COST-Q05).
- [DEC-85 — Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào?](decision-groups.md#dec-85) (DATA-COST-Q06).
- [DEC-213 — qty_std là gram sống còn xương/vỏ hay gram phần ăn được? Xác nhận edible_pct và quy đổi theo từng nguyên liệu để không trừ hai lần.](decision-groups.md#dec-213) (NUTR-Q02).

Đọc trước:

- [docs/gia-phat/01-prd.md](../../01-prd.md).
- [docs/gia-phat/brainstorms/quy-tac-thuc-don.md](../../brainstorms/quy-tac-thuc-don.md).
- [docs/cost/accounting/business-rules.md](../../../cost/accounting/business-rules.md).
- [docs/mua-hang-san-xuat/review/questions.md](../../../mua-hang-san-xuat/review/questions.md).
- [docs/chi-phi-loi-nhuan/review/questions.md](../../../chi-phi-loi-nhuan/review/questions.md).
- [docs/crm-ban-hang/review/questions.md](../../../crm-ban-hang/review/questions.md).
- [docs/cost/review/accountant-input.md](../../../cost/review/accountant-input.md).
- [docs/cost/review/decision-register.md](../../../cost/review/decision-register.md).
- [docs/dinh-duong/review/questions.md](../../../dinh-duong/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-4"></a>

## Buổi 4 — Phụ trách khách + Tech lead — cổng E6 và chuẩn nền

Mục tiêu: Theo thứ tự E6-CG-01, E6-CG-08, E6-CG-05, E6-CG-06 rồi E6-CG-12; đối chiếu E1-Q.

Tham dự: Phụ trách khách, Tech lead/Auth, Vận hành, Bếp trưởng, Chủ sản phẩm, QA, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Danh sách người ăn có quản lý xác nhận; ví dụ account/guest; nguồn khách/điểm; ca sát hạn và thiếu nguồn; bản kế hoạch và evidence nhận revision.

Các nhóm cần review:

- [DEC-07 — Định danh duy nhất người ăn có tài khoản/QR bằng gì; xử lý nhiều thiết bị/QR chia sẻ và account trùng ra sao?](decision-groups.md#dec-07) (ORD-Q01).
- [DEC-08 — Người đặt tổng có thể quản lý nhiều khách/điểm không; role customer scope và audit QR guest/service lưu thế nào khi user_roles/sessions/audit_logs hiện yêu cầu user?](decision-groups.md#dec-08) (ORD-Q11).
- [DEC-10 — Ngưỡng đổi sau chốt, vai trò duyệt, delta âm và khi bếp đã sản xuất xử lý thế nào?](decision-groups.md#dec-10) (ORD-Q08).
- [DEC-11 — Bếp phải xác nhận nhận phiên bản kế hoạch mới không; ai phát hành/cho IN_PRODUCTION và xử lý bản in cũ?](decision-groups.md#dec-11) (ORD-Q14).
- [DEC-25 — Kênh thông báo ngoài (Zalo OA, SMS, email)](decision-groups.md#dec-25) (Q-14).
- [DEC-95 — Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa?](decision-groups.md#dec-95) (ORD-Q02).
- [DEC-96 — Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order?](decision-groups.md#dec-96) (ORD-Q03).
- [DEC-97 — Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào?](decision-groups.md#dec-97) (ORD-Q04).
- [DEC-98 — Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào?](decision-groups.md#dec-98) (ORD-Q05).
- [DEC-99 — T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món?](decision-groups.md#dec-99) (ORD-Q06).
- [DEC-100 — Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao?](decision-groups.md#dec-100) (ORD-Q07).
- [DEC-101 — Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi?](decision-groups.md#dec-101) (ORD-Q09).
- [DEC-102 — R6 luôn 1 MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao?](decision-groups.md#dec-102) (ORD-Q10).
- [DEC-103 — MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn?](decision-groups.md#dec-103) (ORD-Q12).
- [DEC-104 — Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày?](decision-groups.md#dec-104) (ORD-Q13).
- [DEC-105 — C có danh tính/gộp, C→S, vượtT, hủy/zero; RV02/03, ORD-Q06/13, EVID002](decision-groups.md#dec-105) (E6-CG-03).
- [DEC-106 — Summary token, receipt, outbox transaction/retention; RV04, E1-Q02](decision-groups.md#dec-106) (E6-CG-04).
- [DEC-107 — Delta line identity, unit/role/portion và món mới; RV07, ORD-Q04/08/10/12, O-02](decision-groups.md#dec-107) (E6-CG-07).
- [DEC-108 — Customer master/account/service lifecycle; ORD-Q03/11](decision-groups.md#dec-108) (E6-CG-08).
- [DEC-109 — NUTR provenance/kind/stale, refresh/cache/fallback; NUTR-Q03/04, ORD-Q04/12](decision-groups.md#dec-109) (E6-CG-10).
- [DEC-110 — Required/optional/null, limits, enum/query, create-version chưa rõ](decision-groups.md#dec-110) (E6-CG-11).
- [DEC-111 — Tuần/mode/reminder policy; ORD-Q05/09, Q-14/E1-Q04](decision-groups.md#dec-111) (E6-CG-12).
- [DEC-112 — Wireframe chỉ mô phỏng một nguồn/version đồng bộ](decision-groups.md#dec-112) (E6-CG-13).
- [DEC-113 — Gate sức khỏe và dữ liệu/QA môi trường chưa có](decision-groups.md#dec-113) (E6-CG-14).
- [DEC-211 — Identity/binding/credential/guest audit; RV01, ORD-Q01/02/11; EVID001 chỉ xác nhận danh sách](decision-groups.md#dec-211) (E6-CG-01).
- [DEC-212 — Scope người đặt tổng một/nhiều công ty; ORD-Q11, EVID002](decision-groups.md#dec-212) (E6-CG-02).
- [DEC-214 — Hạn, thiếu nguồn, remediation, quyền/ngưỡng đổi; RV08, ORD-Q07/08/12, Q-16/O-06](decision-groups.md#dec-214) (E6-CG-05).
- [DEC-215 — Hạn 15:00 ngày D-1, ngưỡng 5 %/10 suất/trước 06:00 đúng thực tế không; chọn ngưỡng nhỏ hơn hay lớn hơn?](decision-groups.md#dec-215) (Q-16).
- [DEC-216 — Expected source/completeness, publish/ack/start; RV05/06, ORD-Q03/13/14](decision-groups.md#dec-216) (E6-CG-06).

Đọc trước:

- [docs/chon-mon-order/review/questions.md](../../../chon-mon-order/review/questions.md).
- [docs/chon-mon-order/review/contract-gap-register.md](../../../chon-mon-order/review/contract-gap-register.md).
- [docs/gia-phat/00-ke-hoach-tong-the.md](../../00-ke-hoach-tong-the.md).
- [docs/nen-tang/srs/spec.md](../../../nen-tang/srs/spec.md).
- [docs/nen-tang/review/questions.md](../../../nen-tang/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-5"></a>

## Buổi 5 — Kế toán / Giám đốc — doanh thu và lợi nhuận Next/Later

Mục tiêu: Chốt số tính tiền, đối soát, MISA, phân bổ và nguồn kết quả kinh doanh.

Tham dự: Kế toán, Giám đốc, người nhận phía khách, phụ trách dữ liệu, Tech lead, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Biên bản đối soát 2 khách, mẫu MISA chính thức có phiên bản, chứng từ thu/điều chỉnh, nguồn chi phí và giờ công, bộ đối chiếu từng cơ sở.

Các nhóm cần review:

- [DEC-14 — Biên lợi nhuận nội bộ trên báo giá dùng công thức, thành phần và nguồn phiên bản nào; ai được xem?](decision-groups.md#dec-14) (E10-Q15).
- [DEC-114 — Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?](decision-groups.md#dec-114) (Q-13).
- [DEC-115 — Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?](decision-groups.md#dec-115) (E7-Q01).
- [DEC-116 — Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?](decision-groups.md#dec-116) (E7-Q02).
- [DEC-117 — Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?](decision-groups.md#dec-117) (E7-Q03).
- [DEC-118 — Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?](decision-groups.md#dec-118) (E7-Q04).
- [DEC-119 — Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?](decision-groups.md#dec-119) (E7-Q05).
- [DEC-120 — Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?](decision-groups.md#dec-120) (E7-Q06).
- [DEC-121 — Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?](decision-groups.md#dec-121) (E7-Q07).
- [DEC-122 — Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?](decision-groups.md#dec-122) (E7-Q08).
- [DEC-186 — Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì?](decision-groups.md#dec-186) (E13-Q01).
- [DEC-187 — Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào?](decision-groups.md#dec-187) (E13-Q02).
- [DEC-188 — Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì?](decision-groups.md#dec-188) (E13-Q03).
- [DEC-189 — Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao?](decision-groups.md#dec-189) (E13-Q04).
- [DEC-190 — Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao?](decision-groups.md#dec-190) (E13-Q05).
- [DEC-191 — Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào?](decision-groups.md#dec-191) (E13-Q06).
- [DEC-192 — Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào?](decision-groups.md#dec-192) (E13-Q07).
- [DEC-193 — Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào?](decision-groups.md#dec-193) (E13-Q09).
- [DEC-194 — Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào?](decision-groups.md#dec-194) (E13-Q11).
- [DEC-195 — Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào?](decision-groups.md#dec-195) (E13-Q12).
- [DEC-196 — Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào?](decision-groups.md#dec-196) (E13-Q13).
- [DEC-197 — Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu?](decision-groups.md#dec-197) (E13-Q14).
- [DEC-219 — Kết quả kinh doanh cơ sở gồm khoản nào, nguồn chuẩn nào, ghi nhận điều chỉnh và CK ra sao?](decision-groups.md#dec-219) (E13-Q08).

Đọc trước:

- [docs/crm-ban-hang/review/questions.md](../../../crm-ban-hang/review/questions.md).
- [docs/chi-phi-loi-nhuan/review/questions.md](../../../chi-phi-loi-nhuan/review/questions.md).
- [docs/giao-nhan-doanh-thu/review/questions.md](../../../giao-nhan-doanh-thu/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-6"></a>

## Buổi 6 — Mua hàng / bếp trưởng — mua hàng và sản xuất Later

Mục tiêu: Rà nhu cầu mua, tồn, nhận hàng, công nợ, BO-02, phân ca, QC và mẫu lưu.

Tham dự: Mua hàng, Bếp trưởng, Vận hành, Kế toán, Giám đốc, Dinh dưỡng viên, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Đơn mua/phiếu nhận nhiều lần, dữ liệu lô, nguồn phân bổ thực mua, checklist QC, căn cứ mẫu lưu và nguồn thay món.

Các nhóm cần review:

- [DEC-154 — Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng?](decision-groups.md#dec-154) (E11-Q01).
- [DEC-155 — Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào?](decision-groups.md#dec-155) (E11-Q03).
- [DEC-156 — Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao?](decision-groups.md#dec-156) (E11-Q04).
- [DEC-157 — Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không?](decision-groups.md#dec-157) (E11-Q05).
- [DEC-158 — Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào?](decision-groups.md#dec-158) (E11-Q06).
- [DEC-159 — Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung?](decision-groups.md#dec-159) (E11-Q07).
- [DEC-160 — BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào?](decision-groups.md#dec-160) (E11-Q08).
- [DEC-161 — Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào?](decision-groups.md#dec-161) (E11-Q09).
- [DEC-162 — Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi?](decision-groups.md#dec-162) (E11-Q10).
- [DEC-163 — Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì?](decision-groups.md#dec-163) (E11-Q11).
- [DEC-164 — Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào?](decision-groups.md#dec-164) (E11-Q12).
- [DEC-165 — Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt?](decision-groups.md#dec-165) (E11-Q13).
- [DEC-166 — Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào?](decision-groups.md#dec-166) (E11-Q14).
- [DEC-167 — Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân?](decision-groups.md#dec-167) (E11-Q15).

Đọc trước:

- [docs/mua-hang-san-xuat/review/questions.md](../../../mua-hang-san-xuat/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-7"></a>

## Buổi 7 — Kinh doanh / quản trị website — website và CRM

Mục tiêu: Chốt công khai nội dung/giá, lead, URL, khách trùng, báo giá và hợp đồng.

Tham dự: Kinh doanh, Chăm sóc khách, quản trị website, Giám đốc, Kế toán, Tech lead, phụ trách dữ liệu, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Inventory URL/media, quyền tên miền, nguồn giá công khai, consent lead, hồ sơ khách/hợp đồng, bản báo giá và bằng chứng chấp thuận.

Các nhóm cần review:

- [DEC-12 — Giá suất nào được công khai; ai duyệt, thời hạn hiệu lực và cách ghi VAT/giá tham khảo ra sao?](decision-groups.md#dec-12) (E8-Q03).
- [DEC-13 — FEAT-057 sinh mẫu từ thư viện, thuật toán hay cách khác; có phải qua máy kiểm E2; giới hạn loại suất/số suất/kiêng kỵ/ngày/lượt là gì?](decision-groups.md#dec-13) (E8-Q05).
- [DEC-15 — Nguồn E2/E4 ở trạng thái nào đủ điều kiện hiển thị định lượng, 4 chỉ số và dị ứng; làm gì khi stale/thu hồi/thiếu?](decision-groups.md#dec-15) (E8-Q04).
- [DEC-123 — DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ?](decision-groups.md#dec-123) (E8-Q01).
- [DEC-124 — Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback?](decision-groups.md#dec-124) (E8-Q02).
- [DEC-125 — Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào?](decision-groups.md#dec-125) (E8-Q06).
- [DEC-126 — Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao?](decision-groups.md#dec-126) (E8-Q07).
- [DEC-127 — Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào?](decision-groups.md#dec-127) (E8-Q08).
- [DEC-128 — Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào?](decision-groups.md#dec-128) (E8-Q09).
- [DEC-129 — BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo?](decision-groups.md#dec-129) (E8-Q10).
- [DEC-130 — Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04?](decision-groups.md#dec-130) (E8-Q11).
- [DEC-131 — Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì?](decision-groups.md#dec-131) (E8-Q12).
- [DEC-141 — Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?](decision-groups.md#dec-141) (E10-Q01).
- [DEC-142 — Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?](decision-groups.md#dec-142) (E10-Q02).
- [DEC-143 — Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?](decision-groups.md#dec-143) (E10-Q04).
- [DEC-144 — Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?](decision-groups.md#dec-144) (E10-Q05).
- [DEC-145 — Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?](decision-groups.md#dec-145) (E10-Q06).
- [DEC-146 — Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?](decision-groups.md#dec-146) (E10-Q07).
- [DEC-147 — Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?](decision-groups.md#dec-147) (E10-Q08).
- [DEC-148 — Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?](decision-groups.md#dec-148) (E10-Q09).
- [DEC-149 — Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?](decision-groups.md#dec-149) (E10-Q10).
- [DEC-150 — Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?](decision-groups.md#dec-150) (E10-Q11).
- [DEC-151 — Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?](decision-groups.md#dec-151) (E10-Q12).
- [DEC-152 — Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?](decision-groups.md#dec-152) (E10-Q13).
- [DEC-153 — Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?](decision-groups.md#dec-153) (E10-Q14).
- [DEC-200 — Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](decision-groups.md#dec-200) (E8-Q13).
- [DEC-201 — Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](decision-groups.md#dec-201) (E9-Q15).
- [DEC-202 — Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại?](decision-groups.md#dec-202) (E10-Q16).
- [DEC-217 — Có hiển thị giá suất cho khách không, nguồn/hiệu lực/nhãn giá nào được duyệt?](decision-groups.md#dec-217) (E9-Q04).
- [DEC-218 — FEAT-057 E8 và FEAT-060 E9 dùng chung bộ dựng hay tách; contract kiểm nguồn/quy tắc và quyền public thế nào?](decision-groups.md#dec-218) (E9-Q11).
- [DEC-220 — Nguồn nào đủ điều kiện public; stale/thu hồi/thiếu dinh dưỡng/dị ứng xử lý ra sao; tuần/ngày phục vụ và nhiều cỡ?](decision-groups.md#dec-220) (E9-Q12).

Đọc trước:

- [docs/website-cong-khai/review/questions.md](../../../website-cong-khai/review/questions.md).
- [docs/agent-dinh-duong-vien/review/questions.md](../../../agent-dinh-duong-vien/review/questions.md).
- [docs/crm-ban-hang/review/questions.md](../../../crm-ban-hang/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-8"></a>

## Buổi 8 — Dinh dưỡng viên / phụ trách dữ liệu / Tech lead — agent khách

Mục tiêu: Chốt phạm vi người dùng, dữ liệu công khai, quota, lưu/xóa và bộ nghiệm thu R9.

Tham dự: Dinh dưỡng viên, phụ trách dữ liệu, Giám đốc, Tech lead, QA, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Manifest 30 yêu cầu, 20 câu dò cost, 20 câu bệnh lý; nguồn công khai; policy lượt/ngân sách và consent; không mang dữ liệu sức khỏe để thu vào hệ thống.

Các nhóm cần review:

- [DEC-132 — Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền?](decision-groups.md#dec-132) (E9-Q02).
- [DEC-133 — Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào?](decision-groups.md#dec-133) (E9-Q03).
- [DEC-134 — Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không?](decision-groups.md#dec-134) (E9-Q05).
- [DEC-135 — FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào?](decision-groups.md#dec-135) (E9-Q06).
- [DEC-136 — FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần?](decision-groups.md#dec-136) (E9-Q07).
- [DEC-137 — Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy?](decision-groups.md#dec-137) (E9-Q08).
- [DEC-138 — Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì?](decision-groups.md#dec-138) (E9-Q09).
- [DEC-139 — Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider?](decision-groups.md#dec-139) (E9-Q10).
- [DEC-140 — Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9?](decision-groups.md#dec-140) (E9-Q13).

Đọc trước:

- [docs/agent-dinh-duong-vien/review/questions.md](../../../agent-dinh-duong-vien/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

<a id="buoi-9"></a>

## Buổi 9 — Chủ dashboard / phụ trách dữ liệu — phản hồi và nhật ký Later

Mục tiêu: Chốt mẫu số, quyền chỉ số, phản hồi, mục tiêu nhóm và consent/bằng chứng bữa đã ăn.

Tham dự: Giám đốc, Kế toán, Dinh dưỡng viên, Bếp trưởng, Chăm sóc khách, phụ trách dữ liệu, Tech lead, QA, BA. Vai trò tham dự không tự trở thành người có quyền ký; ô người quyết định “chưa rõ” phải được xác nhận trước khi ký.

Dữ liệu cần mang: Catalog chỉ số từng vai trò, lựa chọn thật có nguồn, mẫu phản hồi, căn cứ mục tiêu nhóm, consent nhật ký và quy trình chứng minh xóa.

Các nhóm cần review:

- [DEC-168 — Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì?](decision-groups.md#dec-168) (E12-Q01).
- [DEC-169 — Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao?](decision-groups.md#dec-169) (E12-Q02).
- [DEC-170 — Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào?](decision-groups.md#dec-170) (E12-Q03).
- [DEC-171 — Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào?](decision-groups.md#dec-171) (E12-Q04).
- [DEC-172 — Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao?](decision-groups.md#dec-172) (E12-Q05).
- [DEC-173 — Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào?](decision-groups.md#dec-173) (E12-Q06).
- [DEC-174 — Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope?](decision-groups.md#dec-174) (E12-Q07).
- [DEC-175 — Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào?](decision-groups.md#dec-175) (E12-Q08).
- [DEC-176 — Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì?](decision-groups.md#dec-176) (E12-Q09).
- [DEC-177 — Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì?](decision-groups.md#dec-177) (E12-Q10).
- [DEC-178 — FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp?](decision-groups.md#dec-178) (E12-Q11).
- [DEC-179 — FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm?](decision-groups.md#dec-179) (E12-Q12).
- [DEC-180 — Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì?](decision-groups.md#dec-180) (E12-Q13).
- [DEC-181 — Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không?](decision-groups.md#dec-181) (E12-Q14).
- [DEC-182 — Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào?](decision-groups.md#dec-182) (E12-Q15).
- [DEC-183 — Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào?](decision-groups.md#dec-183) (E12-Q16).
- [DEC-184 — Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào?](decision-groups.md#dec-184) (E12-Q17).
- [DEC-185 — Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào?](decision-groups.md#dec-185) (E12-Q18).

Đọc trước:

- [docs/phan-hoi-bao-cao/review/questions.md](../../../phan-hoi-bao-cao/review/questions.md).

Biên bản mẫu — ghi từng nhóm và phạm vi sau cuộc họp:

| Quyết định | Người ký | Ngày | Nguồn |
| :--- | :--- | :--- | :--- |
|  |  |  |  |

| Việc sau quyết định | Vai trò phụ trách | Hạn được thống nhất | Bằng chứng hoàn tất |
| :--- | :--- | :--- | :--- |
|  |  |  |  |


Thẩm quyền cần hỏi trước chữ ký: [BA-Q](ba-open-questions.md). Không lấy danh sách tham dự thay thẩm quyền quyết định.
