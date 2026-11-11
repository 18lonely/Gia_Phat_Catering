# Thiết kế các nhánh Cost còn mở

Phiên bản0.1.0 · 11/11/2026 · Phương án thiết kế để review; chưa tự đóng quyết định nghiệp vụ.

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | Cụ thể hóa4 nhóm nhánh, giao dịch, kết quả lỗi và câu hỏi phải xác nhận |

Người dùng yêu cầu tiếp tục hoàn thiện thiết kế; các câu chiết khấu CK-Q01–10 vẫn để hỏi sau. Bảng này chọn **phương án đề xuất cụ thể** để dev đánh giá, không ghi là chủ sở hữu đã phê duyệt. Nhánh còn gate chưa mở production; không đổi các ca BLOCKED thành PASS.

## 1. Giá/tham số đổi khi PENDING — FLOW-COST-Q06

Đề xuất: khi duyệt cuối, đọc lại giá/params theo ngày phục vụ nhưng giữ công thức đã gắn vào MENU; kiểm đủ cơ sở và khóa revision đầu vào. Nếu giá tiếp tục đổi trong transaction thì không commit trên bộ số hỗn hợp: retry có giới hạn/đối soát theo hợp đồng Tech lead. Snapshot và APPROVED phải commit cùng giao dịch.

| Kết quả kiểm mới | Hành vi đề xuất | Dữ liệu giữ |
| :--- | :--- | :--- |
| Đủ dữ liệu và đạt | Duyệt, chụp bộ giá/params vừa kiểm | Lịch sử kiểm lúc gửi và snapshot lúc duyệt phân biệt |
| Vượt ở CHAN | Từ chối quyết định duyệt, giữ PENDING để người có quyền xử lý | Không tạo snapshot giả, không tự chuyển DRAFT |
| Vượt ở CANH_BAO | Hiện cảnh báo mới theo quyền; sau xác nhận quyết định thì duyệt và chụp số vượt | Không xóa dấu vết đã vượt khi duyệt |
| Thiếu giá/VAT/bảng đặc thù | Không duyệt dù CANH_BAO | Chi tiết lỗi theo quyền, giữ PENDING |

**Cần trả lời:** có chấp nhận kiểm lại tại duyệt cuối không; giữ PENDING hay trả DRAFT; có yêu cầu người duyệt xác nhận lại khi số thay đổi? Chủ sở hữu: Giám đốc/kế toán. Liên quan TC-COST-018-02, MEAL005/006, snapshot transaction. Không sửa snapshot vòng duyệt cũ.

## 2. Dự toán tuần có ngày lỗi — FLOW-COST-Q07

Đề xuất all-or-nothing toàn batch: validate toàn bộ ngày, chụp version inputs, tính rồi commit tất cả bản ngày và khóa batch cùng giao dịch. Bất kỳ ngày lỗi trả lỗi theo ngày và `committedCount:0`. Batch retry cùng key/body trả cùng kết quả; không cấp version bản ngày bằng MAX+1 ngoài khóa transaction.

Thành công đề xuất: batchKey,items[{date,estimateId,version}],weeklyLines có phân rã ngày/giá; không nhân tổng lượng tuần với một giá cuối tuần. Timeout sau gửi không chứng minh committedCount0; đối soát cùng key. Khi lượng mua cần làm tròn, tổng tuần lấy tổng lượng mua đã chụp từng ngày để khớp bản ngày, không gộp lượng thô rồi làm tròn lại nếu chưa có quyết định khác.

**Cần trả lời:** cả tuần nguyên tử hay cho lưu ngày hợp lệ; cách gộp/làm tròn bảng tuần có được chốt như trên không? Chủ sở hữu: kế toán/DD. Chưa cập nhật success contract cuối của API-COST batch và TC-COST-023 sang sẵn sàng chạy khi chưa trả lời.

## 3. Bảng món đặc thù — E3-Q16

Đề xuất chỉ nhận APPROVED cùng dish/portion/kitchen, công thức đúng phiên bản dự kiến dùng, ngày lập không sau ngày phục vụ và tuổi tính theo ngày lập <=N ngày (N từ cấu hình có hiệu lực). Lưu rõ ngày lập và ngày tính giá; không dùng hai ngày thay thế nhau. Bảng A không tự hợp lệ cho B. Ranh giới89/90/91 khi N90: đề xuất hợp lệ/hợp lệ/không hợp lệ.

**Cần trả lời:** tuổi bắt đầu từ ngày lập hay ngày tính giá; ngày hết hạn có bao gồm mốcN; có được dùng chéo cơ sở không; công thức thay đổi có buộc duyệt bảng mới không? Chủ sở hữu: Giám đốc/kế toán. Cần xác nhận đầy đủ trước khi bật bộ lọc hiệu lực, không coi việc lưu đủ field là đã có quy tắc hợp lệ.

## 4. Quyền xem và quyết định

| Nội dung | Hiện có / đề xuất | Gate |
| :--- | :--- | :--- |
| Cost/giá/dự toán nội bộ | Giữ SRS2.2, QL chỉ cơ sở mình, quyền ghi không tự cấp quyền đọc mọi nguồn | Không mở rộng phạm vi từ client |
| Bếp | Giữ thiết kế chỉ lượng, không tiền trong JSON/UI/file | E3-Q11 vẫn cần xác nhận |
| Danh mục khoản khoán quản trị | Đề xuất KT mua hàng và GD; người xem cost chỉ thấy phần khoản áp vào phân rã của mình | FLOW-COST-Q05 |
| Duyệt bảng/tham số | Giữ tách người tạo/người sửa cuối và người duyệt theo SYS | O-06 người thay thế |
| Context giá khách và draft chiết khấu | Permission đề xuất riêng, deny khi chưa cấp; không dùng cost.allowance.write thay | CK-Q04 và quyết định quyền kế toán |

Mọi nhánh cần deny server-side, dữ liệu ngoài scope404, thiếu quyền403; lỗi cũng lọc tiền. Mẫu UI có chọn vai trò chỉ phục vụ review, không chứng minh phân quyền backend.

## 5. Cách đóng từng nhánh

Ghi câu trả lời, người/ngày/nguồn → sửa SRS/UC/API/schema/UI/AC có liên quan → review ví dụ happy/error/biên → chuyển test BLOCKED sang NOT RUN nếu đủ đầu vào. Chưa có quyết định của chủ sở hữu thì giữ gate, không ghi “đã chốt” trong báo cáo bàn giao.
