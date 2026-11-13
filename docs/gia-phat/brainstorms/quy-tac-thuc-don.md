# Bảng quy tắc xây dựng thực đơn & kiểm soát cost: bản đề xuất để duyệt

| Trường | Giá trị |
|---|---|
| Phiên bản | v0.1.0: **bản đề xuất, chưa có hiệu lực** |
| Ngày | 10/11/2026 |
| Nguồn | `Yêu cầu về thực đơn và cost tp.docx` |
| Người duyệt | Người soạn file docx (dinh dưỡng viên / bếp trưởng): riêng nhóm COST cần thêm kế toán |
| Dùng cho | Bộ kiểm quy tắc MENU-06, bộ kiểm cost COST-03, và cả hai AI agent |

## Cách duyệt

Mỗi dòng là một câu trong file docx đã được viết lại thành dạng máy kiểm được. Mọi **con số trong cột "Đề xuất" là do tôi đề nghị**, chưa phải số của Gia Phát. Với từng dòng, người duyệt đánh dấu một trong ba:

- **Đ**: đồng ý nguyên văn
- **S**: sửa (ghi con số hoặc loại mới vào cột "Sửa thành")
- **B**: bỏ, không đưa vào hệ thống

**Loại quy tắc**

| Loại | Hệ thống làm gì khi vi phạm |
|---|---|
| **Cứng** | Chặn: không cho gửi duyệt/công bố thực đơn. AI agent không được đề xuất thực đơn vi phạm. |
| **Mềm – nặng** | Cảnh báo đỏ, trừ 3 điểm; muốn công bố phải ghi lý do. |
| **Mềm – vừa** | Cảnh báo vàng, trừ 2 điểm. |
| **Mềm – nhẹ** | Ghi chú, trừ 1 điểm. |

Mỗi thực đơn tuần bắt đầu từ 100 điểm. Đề xuất: dưới 80 điểm phải có người thứ hai duyệt. ☐ Đ ☐ S: ____

**Phạm vi kiểm tra**: "ngày" = thực đơn một ngày của một loại suất (các món chính đưa ra để chọn + món phụ + rau + canh). "Tuần" = các ngày phục vụ từ thứ Hai đến thứ Bảy.

---

## A. Cơ cấu món trong ngày

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-001 | Số món chính đưa ra mỗi ngày đúng bằng số cấu hình của loại suất | "Mỗi ngày bố trí 03 món chính" | Cứng | Mặc định 3 | ☐ | |
| BR-MENU-002 | Trong các món chính của ngày có đúng 1 món gắn cờ Healthy | "01 món chính là món luộc theo định hướng Healthy" | Cứng | Đúng 1 | ☐ | |
| BR-MENU-003 | Món Healthy phải dùng phương pháp chế biến thuộc danh sách ít dầu mỡ | "ưu tiên các phương pháp chế biến ít dầu mỡ" | Cứng | Luộc, hấp (xem câu hỏi H-1) | ☐ | |
| BR-MENU-004 | Mỗi ngày có đủ rau và canh | Mục I.3 | Cứng | 1 rau + 1 canh | ☐ | |
| BR-MENU-005 | Số món phụ mỗi ngày đúng bằng số cấu hình của loại suất | Mục I.2 | Cứng | Theo loại suất | ☐ | |

## B. Đa dạng nguyên liệu

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-010 | Các món chính trong cùng ngày không trùng nhóm nguyên liệu chính | "đa dạng về nguyên liệu… không trùng lặp" | Cứng | 0 cặp trùng | ☐ | |
| BR-MENU-011 | Nguyên liệu chính của món phụ không trùng với món chính cùng ngày | "Hạn chế tối đa… trùng lặp nguyên liệu chính giữa các món trong cùng một ngày" | Mềm – vừa | Tối đa 1 cặp trùng/ngày | ☐ | |
| BR-MENU-012 | Cùng một nhóm nguyên liệu chính không xuất hiện ở món chính quá N ngày liên tiếp | "Không nên bố trí cùng một nguyên liệu chính trong nhiều ngày liên tiếp" | Mềm – nặng | N = 2 ngày (xem H-2) | ☐ | |
| BR-MENU-013 | Một món không lặp lại trong tuần | "Hạn chế lặp lại cùng một món trong tuần" | Mềm – nặng | Mỗi món tối đa 1 lần/tuần | ☐ | |
| BR-MENU-014 | Hai món cùng "món gốc" (đổi tên/trình bày) tính là một món khi kiểm BR-MENU-013 | "kể cả khi thay đổi tên gọi hoặc cách trình bày" | Cứng (cách đếm) | Món có trường "món gốc" | ☐ | |
| BR-MENU-015 | Trong tuần, món chính phải phủ tối thiểu K nhóm nguyên liệu | "Luân phiên sử dụng các nhóm nguyên liệu như: thịt lợn, gà, bò, ếch, tôm, cá" | Mềm – vừa | K = 4 nhóm/tuần | ☐ | |
| BR-MENU-016 | Rau không lặp ngày liền kề | "Rau và canh cần được thay đổi hàng ngày" | Mềm – vừa | Cùng loại rau cách nhau ≥ 2 ngày | ☐ | |
| BR-MENU-017 | Canh không lặp ngày liền kề | Như trên | Mềm – vừa | Cùng loại canh cách nhau ≥ 2 ngày | ☐ | |
| BR-MENU-018 | Ưu tiên rau đang trong mùa | "Ưu tiên rau theo mùa" | Mềm – nhẹ | Trừ điểm khi chọn rau trái mùa | ☐ | |
| BR-MENU-019 | Món phụ không lặp trong tuần | "tránh lặp lại thường xuyên" | Mềm – vừa | Mỗi món phụ tối đa 2 lần/tuần | ☐ | |

## C. Phương pháp chế biến

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-020 | Hai món chính không phải Healthy trong ngày không cùng phương pháp chế biến | "Hạn chế tối đa việc bố trí 02 món chính cùng phương pháp chế biến trong một ngày" | Mềm – nặng | 0 cặp trùng | ☐ | |
| BR-MENU-021 | Số món phụ chiên trong ngày | "Hạn chế tối đa… 02 món phụ cùng có phương pháp chế biến chiên" | Mềm – nặng | Tối đa 1 | ☐ | |
| BR-MENU-022 | Tổng số món chiên/rán trong ngày (chính + phụ) | "Hạn chế… quá nhiều món chiên rán, nhiều dầu mỡ trong cùng một bữa" | Mềm – nặng | Tối đa 2 | ☐ | |
| BR-MENU-023 | Số món cùng một phương pháp trong ngày, tính mọi món | "Không bố trí quá nhiều món có cùng phương pháp chế biến trong một ngày" | Mềm – vừa | Tối đa 2 món/phương pháp | ☐ | |

## D. Khẩu vị, kết cấu

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-030 | Số món có vị chua trong ngày | "Hạn chế kết hợp các món có cùng vị chua" (sốt cà chua + dưa chua) | Mềm – nặng | Tối đa 1 | ☐ | |
| BR-MENU-031 | Số món có nước sốt trong ngày | "Tránh… quá nhiều món sử dụng nước sốt" | Mềm – vừa | Tối đa 2 | ☐ | |
| BR-MENU-032 | Số món khô trong ngày (không tính rau luộc) | "Tránh thực đơn có quá nhiều món khô" | Mềm – vừa | Tối đa 2 | ☐ | |
| BR-MENU-033 | Trong ngày có ít nhất 1 món thanh nhẹ ngoài rau và canh | "Cân đối giữa các món đậm đà, món thanh nhẹ" | Mềm – nhẹ | ≥ 1 (món Healthy được tính) | ☐ | |
| BR-MENU-034 | Cặp món kỵ nhau không xuất hiện cùng ngày | "Không bố trí nem và nộm cùng một ngày" | Cứng | Theo danh sách cặp kỵ (xem H-4) | ☐ | |

"Hài hòa về hương vị, màu sắc và kết cấu" không viết thành quy tắc máy kiểm được. Đề xuất: để người duyệt thực đơn tự đánh giá, không đưa vào hệ thống. ☐ Đ ☐ S: ____

## E. Tính khả thi bếp và vận chuyển

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-040 | Số món cầu kỳ (nhiều công đoạn sơ chế: nộm, cuốn, hấp…) trong ngày | "Hạn chế các món đòi hỏi nhiều công đoạn sơ chế, chế biến cầu kỳ" | Mềm – nặng | Tối đa 1 món/ngày | ☐ | |
| BR-MENU-041 | Số món cầu kỳ trong tuần | Như trên | Mềm – vừa | Tối đa 3 món/tuần | ☐ | |
| BR-MENU-042 | Món đánh dấu "kém chịu vận chuyển" (dễ dai, khô, nhũn) không dùng cho điểm giao xa | "Hạn chế các món dễ bị dai, khô, nhũn… sau một khoảng thời gian" | Mềm – nặng | Không dùng khi từ nấu xong đến giờ ăn > 2 giờ | ☐ | |
| BR-MENU-043 | Chỉ dùng món đã được đánh dấu phù hợp bếp số lượng lớn | "Ưu tiên các món phù hợp với mô hình bếp suất ăn số lượng lớn" | Cứng | Cờ bật/tắt trên từng món | ☐ | |
| BR-MENU-044 | Nguyên liệu chính có nguồn cung không ổn định | "Ưu tiên sử dụng nguyên liệu có nguồn cung ổn định" | Mềm – nhẹ | Trừ điểm khi dùng | ☐ | |

## F. Dinh dưỡng

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-MENU-050 | Trong tuần, nguồn đạm của món chính + món phụ phủ đủ các nhóm | "Đảm bảo nguồn đạm đa dạng từ thịt, cá, trứng, tôm, đậu" | Mềm – vừa | ≥ 4 trong 5 nhóm: thịt, cá, trứng, thuỷ sản, đậu | ☐ | |
| BR-MENU-051 | Mỗi suất đạt mức năng lượng tối thiểu | Docx không có con số | Chưa đề xuất | Cần dinh dưỡng viên cho số (xem H-5) | ☐ | |

## G. Cost và định lượng

| Mã | Quy tắc | Câu gốc (docx) | Loại | Đề xuất | Duyệt | Sửa thành |
|---|---|---|---|---|---|---|
| BR-COST-001 | Cost thực phẩm mỗi ngày ÷ doanh thu suất ăn không vượt ngưỡng | "không vượt quá 52% doanh thu suất ăn" | Cứng | ≤ 52% | ☐ | |
| BR-COST-002 | Doanh thu dùng làm mẫu số là giá suất **đã trừ VAT** | Docx không nói; anh xác nhận 40.000đ đã gồm VAT | Cứng (cách tính) | Giá suất ÷ (1 + thuế suất VAT) (xem H-6) | ☐ | |
| BR-COST-003 | Thành phần tính vào cost | Docx không nói | Cứng (cách tính) | Gồm: món chính, phụ, rau, canh, gạo, gia vị + dầu (khoán đ/suất). Không gồm: gas, hộp/khay, nhân công (xem H-7) | ☐ | |
| BR-COST-004 | Giá dùng để tính là giá nhập có hiệu lực mới nhất của nhà cung cấp | "căn cứ vào bảng giá thực phẩm thực tế từ nhà cung cấp" | Cứng | Giá có ngày hiệu lực ≤ ngày phục vụ | ☐ | |
| BR-COST-005 | Giá nhập quá cũ thì cảnh báo | "cập nhật khi có biến động" | Mềm – vừa | Cảnh báo khi giá chưa cập nhật > 7 ngày (hàng tươi), > 30 ngày (hàng khô, đông lạnh) | ☐ | |
| BR-COST-006 | Món chính cost cao đi với món phụ cost thấp và ngược lại | "Món chính có cost cao thì ưu tiên món phụ có cost thấp" | Mềm – vừa | Không xếp món chính nhóm cost cao cùng món phụ nhóm cost cao | ☐ | |
| BR-COST-007 | Món dùng nguyên liệu giá cao phải có bảng tính cost được duyệt trước khi vào thực đơn | "bò, tôm, cá và các thực phẩm đặc thù cần được tính cost riêng" | Cứng | Áp dụng cho nhóm: bò, tôm, cá, và món gắn cờ "đặc thù" | ☐ | |
| BR-COST-008 | Định lượng sống của nguyên liệu chính nằm trong khoảng chuẩn của công thức | Bảng định lượng mục II | Cứng | Trong khoảng min–max của bảng | ☐ | |
| BR-COST-009 | Tỷ lệ nguyên liệu phụ/chất độn so với nguyên liệu chính | "tránh sử dụng quá nhiều nguyên liệu phụ làm giảm tỷ lệ nguyên liệu chính" | Mềm – nặng | Chất độn không vượt mức trong bảng (ví dụ bò 65–70g đi với chất độn 50–55g) | ☐ | |
| BR-COST-010 | Nguyên liệu có xương/vỏ phải khai tỷ lệ hao hụt trước khi dùng trong công thức | "thực phẩm có phần xương, vỏ hoặc tỷ lệ hao hụt cao" | Cứng | Bắt buộc có tỷ lệ hao hụt | ☐ | |
| BR-COST-011 | Khi giá nhập đổi làm thực đơn đã duyệt vượt ngưỡng thì báo người phụ trách | "Trường hợp cost vượt ngưỡng 52%, cần rà soát lại" | Cứng | Báo ngay; chặn chuyển bếp cho đến khi xử lý | ☐ | |
| BR-COST-012 | Tổng giá bán các món người ăn chọn không vượt định mức suất của công ty | Quyết định D-12 (không có trong docx) | Cứng | Chặn lựa chọn làm vượt định mức | ☐ | |

---

## H. Câu hỏi cần người duyệt trả lời trực tiếp

| Mã | Câu hỏi |
|---|---|
| H-1 | Món Healthy chỉ được **luộc**, hay hấp / áp chảo ít dầu / nướng cũng được tính? |
| H-2 | "Nhiều ngày liên tiếp" là mấy ngày? Thịt lợn có được nới hơn các nhóm khác không (vì dùng nhiều nhất)? |
| H-3 | Danh sách **nhóm nguyên liệu chính** để máy so trùng: đề xuất: lợn, gà, bò, ếch, tôm, cá, sườn, trứng, đậu phụ, giò/chả, khác. Sườn tính riêng hay gộp vào lợn? |
| H-4 | Ngoài "nem – nộm" còn những cặp món nào không được xếp cùng ngày? |
| H-5 | Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào? |
| H-6 | Suất ăn đang xuất hoá đơn với thuế suất VAT bao nhiêu? (Cần kế toán trả lời.) |
| H-7 | Hiện tại khi tính 52%, kế toán/bếp đang cộng những khoản nào? Gạo, gia vị, dầu ăn, tráng miệng có tính không? |
| H-8 | Danh sách **phương pháp chế biến**: đề xuất: luộc, hấp, kho, rang, xào, sốt, chiên/rán, áp chảo, nướng, nộm/trộn, cuốn. Thiếu hoặc thừa gì? |
| H-9 | Bảng định lượng hiện chỉ có 23 dòng cho mức 40k. Khi dinh dưỡng viên tạo loại suất giá khác, định lượng **giữ nguyên theo món** (giá suất khác nhau do số món khác nhau), hay cùng một món có **nhiều cỡ định lượng** với giá khác nhau? |

## Thuộc tính mỗi món phải có để máy kiểm được các quy tắc trên

| Thuộc tính | Dùng cho quy tắc |
|---|---|
| Vai trò: chính / phụ / rau / canh | 001, 004, 005 |
| Cờ Healthy | 002, 003, 033 |
| Nhóm nguyên liệu chính | 010–015, 050 |
| Món gốc | 013, 014 |
| Phương pháp chế biến | 003, 020–023 |
| Vị chua (có/không), có sốt / khô | 030–032 |
| Mức cầu kỳ sơ chế | 040, 041 |
| Mức chịu vận chuyển | 042 |
| Phù hợp bếp số lượng lớn | 043 |
| Nhóm cost: thấp / cao; cờ "đặc thù" | BR-COST-006, 007 |
| Mùa vụ (với rau) | 018 |
| Giá bán của món | BR-COST-012 |
