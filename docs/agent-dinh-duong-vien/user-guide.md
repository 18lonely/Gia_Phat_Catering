---
id: DOC-E9-USER-GUIDE
title: Hướng dẫn vận hành E9
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e9]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E9: Agent Dinh dưỡng viên

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Khách, quản trị hạn mức AI. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-AIN-001: Mở phiên yêu cầu

[Use case gốc](usecases/UC-AIN-001.md)

1. Khách bắt đầu yêu cầu tại UI-AIN-01 và cung cấp channelRef cùng bằng chứng xác minh/consent được policy yêu cầu.
2. Hệ thống kiểm policy truy cập của kênh và phiên bản consent đã được duyệt.
3. Hệ thống xác minh chủ thể và lấy nhóm/quyền từ server, không dùng userId/group/role do khách tự gán.
4. Khi đủ điều kiện, hệ thống cấp sessionRef opaque gắn với chủ thể và phạm vi được phép.
5. Hệ thống trả tham chiếu phiên để khách tiếp tục yêu cầu tập thể, ghi metadata an toàn cùng requestId theo quyền.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Chưa chốt loại người dùng/consent: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q02/E9-Q10; chưa mở phiên thật, không lưu hội thoại.
- 3a. Bằng chứng phiên thiếu/hết hạn/thu hồi: hệ thống trả ERR-AIN-401-01; không cấp hoặc khôi phục phiên.
- 3b. Khách đọc lại phiên của người khác: hệ thống trả ERR-AIN-404-01 đồng nhất; không phục hồi dữ liệu ngoài quyền.
- 4a. Lỗi ghi hoặc mất phản hồi: hệ thống báo ERR-AIN-500-01, yêu cầu đối soát cùng key; trạng thái tạo phiên chưa rõ, không báo hoàn tất giả.

### UC-AIN-002: Yêu cầu thực đơn tập thể

[Use case gốc](usecases/UC-AIN-002.md)

1. Khách gửi sessionRef, loại suất, số suất nguyên dương, tuần/ngày và lựa chọn khẩu vị/kiêng kỵ tại UI-AIN-01.
2. Hệ thống xác minh chủ thể/scope và kiểm các trường đầu vào, làm rõ phần chưa có nghĩa xác định.
3. Hệ thống kiểm policy, nguồn đã duyệt và giữ hạn mức lượt/ngân sách trước khi nhận lượt có chi phí.
4. Hệ thống ghi run bền vững theo key/body của yêu cầu và trả tham chiếu theo dõi.
5. Worker dựng candidate qua công cụ được phép, chỉ dùng món/công thức đã duyệt; phép tính dinh dưỡng/cost không do model tự tính.
6. Worker gắn candidate revision/hash và nguồn vào trạng thái chờ CHK; hệ thống chưa trình bày candidate chưa kiểm là hợp lệ.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu/trường hoặc số suất âm/lẻ: hệ thống trả ERR-AIN-400-01/ERR-AIN-422-01 theo nguyên nhân; chưa dựng candidate.
- 2b. Kiêng kỵ chưa rõ: hệ thống trả NEEDS_INPUT để khách làm rõ nhu cầu không kèm sức khỏe; không tự đoán phương án.
- 3a. Thiếu policy/nguồn: hệ thống trả ERR-AIN-503-01 kèm gate; không gọi provider.
- 3b. Không đủ hạn mức/ngân sách: hệ thống trả ERR-AIN-429-01; chưa nhận lượt có chi phí.
- 4a. Gửi lại cùng key/body sau mất mạng: hệ thống trả cùng run theo quyền hiện tại; không reserve hoặc tính lượt lần hai. Cùng key khác body trả ERR-AIN-409-02, không tạo run mới.
- 4b. Lỗi ghi/mất phản hồi chưa đối soát được: hệ thống báo ERR-AIN-500-01; kết quả lưu chưa rõ, khách giữ key gốc.

### UC-AIN-003: Kiểm và xem phương án

[Use case gốc](usecases/UC-AIN-003.md)

1. Worker lấy candidate canonical của run, revision/hash và phiên bản nguồn cần kiểm.
2. Orchestrator gọi FR-MENU-RUL-002 để kiểm toàn phương án không lưu MENU, đối chiếu hash và ruleVersion của evidence.
3. Worker xác định kết quả kiểm từ nguồn/evidence; không đánh dấu hợp lệ nếu có vi phạm cứng, thiếu nguồn hoặc máy kiểm lỗi.
4. Adapter lọc kết quả nhạy cảm trước model/UI, giữ bảng kiểm public an toàn gắn với candidate revision.
5. Khách tra runRef tại UI-AIN-02; hệ thống kiểm quyền sở hữu rồi đọc trạng thái và evidence đã có.
6. Hệ thống trả nháp đã kiểm cùng version/bảng kiểm an toàn hoặc trạng thái chặn; GET không gọi model/validator hay sinh candidate.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Máy kiểm lỗi/không khả dụng: hệ thống giữ trạng thái chặn, lỗi nguyên nhân ERR-AIN-503-01; candidate không VALID và không được gửi.
- 3a. Vi phạm quy tắc cứng: hệ thống ghi kết quả không đạt theo ERR-AIN-422-01; không trình bày candidate như phương án hợp lệ.
- 5a. Nguồn/ruleVersion đổi sau kiểm: hệ thống đánh dấu stale, báo ERR-AIN-409-01 khi cần kiểm lại; không dùng evidence cũ cho bản mới, GET không tự chạy kiểm.
- 5b. Run ngoài quyền: hệ thống trả ERR-AIN-404-01; không lộ phương án của chủ thể khác.
- 4a. Chưa chốt cách phản hồi nhánh kinh tế: hệ thống giữ BLOCKED E9-Q05; không đưa lý do/giá trị cost ra model hoặc khách.

### UC-AIN-004: Giải thích thực đơn

[Use case gốc](usecases/UC-AIN-004.md)

1. Khách chọn mục cần giải thích tại UI-AIN-02, gửi candidateRef/revision và topic được phép.
2. Hệ thống kiểm quyền sở hữu, revision và evidence của candidate, chặn chủ đề ngoài phạm vi trước khi diễn giải.
3. Hệ thống lấy projection món/định lượng/bảng kiểm public cùng 4 chỉ số từ E4 và provenance tương ứng.
4. Hệ thống chỉ diễn giải các giá trị đã được cung cấp, gắn đơn vị, nguồn và nhãn “ước tính từ định lượng sống”.
5. Hệ thống lọc lời giải thích trước khi trả cho khách; không nêu nguyên nhân cost hoặc đưa giá suất chưa có nguồn được duyệt.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Dinh dưỡng thiếu/stale: hệ thống ghi chưa đủ/cũ và giữ tổng thiếu là null; không bịa số hoặc báo kết quả đầy đủ.
- 2a. Khách yêu cầu suy giá nhập từ giá suất/định lượng: hệ thống từ chối an toàn ERR-AIN-403-01; không gọi tool cấm, không tạo phép suy ngược.
- 2b. Candidate ngoài scope hoặc revision đã đổi: hệ thống trả ERR-AIN-404-01/ERR-AIN-409-01 tương ứng; chưa có giải thích mới hợp lệ.
- 3b. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-AIN-503-01 kèm gate; không giả kết quả hoặc tự hiển thị giá.

### UC-AIN-005: Chỉnh thực đơn và kiểm lại

[Use case gốc](usecases/UC-AIN-005.md)

1. Khách gửi candidateRef, baseRevision và chỉ dẫn chỉnh ngày/vị trí/món tại UI-AIN-03.
2. Hệ thống kiểm quyền sở hữu và baseRevision, đối chiếu chỉ dẫn với các vị trí/món được phép.
3. Khi yêu cầu rõ và đủ điều kiện quyền/hạn mức, hệ thống tạo revision candidate mới cùng diff từ bản gốc.
4. Worker kiểm lại máy E2 trên toàn tuần và kiểm phiên bản nguồn cho candidate mới, không dùng kết quả pass của bản cũ.
5. Hệ thống gắn evidence đúng revision/hash vào kết quả, lọc bảng kiểm trước khi cho model/UI đọc.
6. Hệ thống trả diff và bản mới đã kiểm hoặc trạng thái không đạt; bản cũ chỉ được giữ làm lịch sử.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Chỉ dẫn mơ hồ: hệ thống yêu cầu làm rõ qua ERR-AIN-422-01/NEEDS_INPUT; chưa tự đổi món, không hỏi thêm bệnh lý.
- 2b. Hai tab gửi cùng baseRevision: một revision tiến; lệnh cũ nhận ERR-AIN-409-01, không ghi đè bản mới.
- 4a. Bản đổi vi phạm quy tắc cứng: hệ thống ghi không đạt theo ERR-AIN-422-01; bản mới bị chặn, không trình bày hợp lệ hoặc thay bằng pass cũ.
- 4b. Máy kiểm/nguồn/policy chưa sẵn sàng: hệ thống trả ERR-AIN-503-01; bản mới chưa có evidence đạt.
- 3a. Mất phản hồi ghi revision: hệ thống báo ERR-AIN-500-01 và yêu cầu đối soát cùng key; chưa xác định đã ghi hay chưa, không tạo bản sửa trùng.

### UC-AIN-006: Gửi đề xuất về Gia Phát

[Use case gốc](usecases/UC-AIN-006.md)

1. Khách rà candidateRef/revision tại UI-AIN-04, nguồn kênh và thông tin liên hệ được phép gửi.
2. Khách thể hiện consent và xác nhận lệnh gửi; ứng dụng nhận clientConfirmation, không để model tự gửi.
3. Hệ thống kiểm lại quyền sở hữu, revision/hash và evidence hiện hành, cùng policy nơi lưu/đầu nhận.
4. Hệ thống ghi proposal, nguồn, revision và receipt bền vững theo key/body của lệnh.
5. Hệ thống chỉ trả mã tiếp nhận sau khi xác định đã lưu; trạng thái là CHỜ XEM XÉT bởi người thật.
6. Ứng dụng chuyển qua port tối thiểu khi có đầu nhận được duyệt, theo dõi receipt bàn giao riêng; không gọi applyDraft.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa chọn nơi lưu/đầu nhận: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q06; không báo tiếp nhận thành công.
- 3b. Revision/nguồn/evidence thay đổi: hệ thống trả ERR-AIN-409-01, yêu cầu kiểm lại; chưa gửi nháp đó.
- 4a. Đã lưu nhưng mất phản hồi hoặc nhận lại cùng key/body: hệ thống đối soát và trả cùng proposal/receipt theo quyền hiện tại; không tạo lead/đề xuất trùng.
- 4b. Cùng key khác body: hệ thống trả ERR-AIN-409-02; giữ yêu cầu gốc, không ghi đề xuất mới.
- 4c. Lỗi ghi chưa xác định kết quả: hệ thống báo ERR-AIN-500-01; khách giữ key để đối soát, chưa coi đã tiếp nhận.
- 6a. Chưa có receipt bàn giao: hệ thống giữ trạng thái chờ/lỗi có căn cứ; proposal đã lưu không bị xóa và không được coi đã duyệt.

### UC-AIN-007: Xem trạng thái đề xuất

[Use case gốc](usecases/UC-AIN-007.md)

1. Khách chọn proposalRef tại UI-AIN-04 để tra tình trạng đề xuất.
2. Hệ thống xác minh phiên và quyền sở hữu proposal; mã opaque không tự thay bằng chứng quyền.
3. Hệ thống đọc receipt tiếp nhận cùng trạng thái và evidence đã có từ nơi nhận.
4. Hệ thống phân biệt tiếp nhận bền vững, chờ bàn giao và trạng thái có evidence; không dùng thông báo làm bằng chứng bàn giao.
5. Hệ thống trả trạng thái an toàn để khách theo dõi; proposal mới tiếp nhận vẫn chờ người thật xem xét.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Proposal ngoài quyền hoặc không có: hệ thống trả ERR-AIN-404-01 đồng nhất; không lộ tồn tại, dữ liệu không đổi.
- 2b. Phiên hết hạn/thu hồi: hệ thống trả ERR-AIN-401-01; không phục hồi dữ liệu ngoài quyền.
- 3a. Chưa có receipt bàn giao hoặc trạng thái đến muộn: hệ thống giữ trạng thái có evidence hiện tại; không tự chuyển đã bàn giao/đã duyệt.
- 3b. Nơi nhận/policy không sẵn sàng: hệ thống trả ERR-AIN-503-01 cho phần chưa thể đọc/xác nhận; proposal không bị mất và không giả kết quả.

### UC-AIN-008: Từ chối gợi ý cá nhân khi gate đóng

[Use case gốc](usecases/UC-AIN-008.md)

1. Người ăn yêu cầu xem khả dụng của gợi ý cá nhân tại UI-AIN-07.
2. Hệ thống kiểm yêu cầu chỉ thuộc đường đọc khả dụng, không nhận trường hồ sơ/sức khỏe.
3. Hệ thống đọc trạng thái gate từ server, xác định O-03 chưa mở và FEAT-047 chưa có luồng được phép.
4. Hệ thống trả CLOSED cùng lý do khả dụng chung; không gọi recommendation hoặc đọc hồ sơ.
5. Giao diện hiển thị tính năng chưa khả dụng, không có biểu mẫu hồ sơ hay thao tác nhận gợi ý.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Client gửi trường bệnh lý/hồ sơ hoặc gọi đường không hỗ trợ: hệ thống từ chối yêu cầu sai schema bằng ERR-AIN-400-01; không lưu hoặc chuyển payload tới tool/model.
- 3a. Client tự khai gate đã mở: hệ thống bỏ tuyên bố quyền từ client và giữ CLOSED; không tạo gợi ý hay quyền mới.
- 3b. Không đọc được điều kiện khả dụng: hệ thống trả ERR-AIN-503-01 an toàn; tính năng không được mở, không dùng thiếu dữ liệu làm quyết định cho phép.

### UC-AIN-009: Kiểm và giữ hạn mức lượt/ngân sách

[Use case gốc](usecases/UC-AIN-009.md)

1. Orchestrator gửi principal/group, policyVersion, requestKey và upper bound của bước cần nhận tới PORT-AIN-ADMISSION.
2. Admission kiểm policy hiện hành, đơn vị/ngày ngân sách, quyền chủ thể và upper bound có xác định/cưỡng chế được hay không.
3. Admission đối chiếu lượt còn lại và tổng spentConfirmed + outstandingReserved + upperBound với cap.
4. Khi đủ điều kiện, admission giữ chỗ nguyên tử cả lượt và ngân sách trước mọi phát sinh chi phí, gắn reservationRef với yêu cầu.
5. Orchestrator nhận ADMITTED và chỉ cho bước tiếp tục khi quyền cùng budget lease còn hiệu lực; mỗi bước có chi phí phải được kiểm lại điều kiện.
6. Hệ thống trả trạng thái an toàn cho UI-AIN-06 khi cần, giữ metadata phục vụ đối soát; không đưa chi tiết trần nội bộ cho khách.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Hết lượt/chạm cap: admission trả QUOTA_BLOCKED/BUDGET_BLOCKED với ERR-AIN-429-01; không nhận lượt hoặc gọi provider.
- 2a. Không xác định upper bound hoặc còn usage chưa rõ: admission giữ UNKNOWN_BLOCKED và không giải phóng phần reserve chưa xác định; không phát sinh bước chi phí mới theo giả định 0.
- 2b. Policy/provider chưa sẵn sàng: hệ thống trả ERR-AIN-503-01 kèm gate; chưa có admission hợp lệ.
- 4a. Nhiều yêu cầu sát trần hoặc retry cùng yêu cầu: admission kiểm/giữ chỗ nguyên tử và trả kết quả yêu cầu gốc theo policy; không tính lượt hai lần hoặc overspend.
- 5a. Lease/quyền không còn hợp lệ: hệ thống chặn bước tiếp theo; reservation/usage đã có không bị tự xóa để giả còn ngân sách.

### UC-AIN-010: Xem và đề nghị đổi hạn mức

[Use case gốc](usecases/UC-AIN-010.md)

1. Giám đốc xem nhóm và policyVersion tại UI-AIN-05, cùng đơn vị và thời gian áp dụng được phép đọc.
2. Giám đốc đề nghị giới hạn lượt, cửa sổ đếm, cap ngày, đơn vị/múi giờ, hiệu lực và lý do thay đổi.
3. Hệ thống kiểm quyền server, version hiện tại và các giá trị theo policy đã được duyệt.
4. Hệ thống đối chiếu đề nghị với spent/reserved hiện có, không hồi tố xóa chi phí hoặc reservation.
5. Nếu policy yêu cầu duyệt, hệ thống tạo đề nghị và tách người tạo/sửa cuối khỏi người duyệt theo E1; nếu không, áp dụng theo workflow đã được xác nhận.
6. Hệ thống lưu audit trước/sau/lý do/version và trả cấu hình hoặc đề nghị cùng trạng thái hiệu lực.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Thiếu quyền: hệ thống trả ERR-AIN-403-01; cấu hình/quota chưa đổi.
- 3b. Chưa quyết định policy/duyệt: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q07/E9-Q08/E9-Q13; không kích hoạt cấu hình.
- 3c. Version cũ: hệ thống trả ERR-AIN-409-01 để tải lại; không ghi đè policy mới.
- 4a. Cap đề nghị thấp hơn spent + reserved: khi thay đổi có hiệu lực hợp lệ, hệ thống chặn admission mới và báo quản trị; không hủy debt, giả hoàn tiền hoặc sửa quá khứ.
- 6a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-AIN-500-01, yêu cầu đối soát; chưa xác định thay đổi đã lưu, không báo tăng quota thành công.

### UC-AIN-011: Chặn truy cập dữ liệu kinh tế nội bộ

[Use case gốc](usecases/UC-AIN-011.md)

1. Registry/API adapter nhận tool request trước truy cập, đối chiếu tên canonical với allowlist.
2. Hệ thống kiểm giao quyền chủ thể và service identity AIN theo scope; không nâng quyền từ nội dung hội thoại hoặc quyền cost của người hỏi.
3. Hệ thống chỉ cho công cụ được phép đọc projection qua API/service/DB grants giới hạn; không cấp SELECT giá nhập/cost hoặc proxy AIO.
4. Adapter kiểm allowlist đệ quy của kết quả trước model và response, bao gồm dữ liệu lồng nhau, metadata, lỗi, log và cache.
5. Hệ thống trả projection sạch hoặc từ chối an toàn tại UI-AIN-07; sự kiện chỉ chứa metadata/mã tổng quát, không payload nhạy cảm.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Injection, alias, SQL/URL tùy ý hoặc yêu cầu cost gián tiếp: guard từ chối ERR-AIN-403-01 trước truy cập; công cụ cấm không chạy.
- 2a. Người hỏi có quyền cost nội bộ nhưng AIN không có: hệ thống vẫn từ chối ERR-AIN-403-01; quyền dịch vụ không được mở rộng.
- 4a. Có cost/ratio/CK trong nested error, log, giải thích hoặc cache: hệ thống chặn dữ liệu đó trước biên; không phát tán qua kênh phụ và không lưu payload nhạy cảm vào log an toàn.
- 4b. Giải thích đòi suy giá nhập từ giá suất/định lượng: hệ thống từ chối an toàn, không tạo phép suy ngược hoặc gọi công cụ cấm.
- 3a. Policy/adapter chưa đủ: hệ thống trả ERR-AIN-503-01 kèm gate; mặc định từ chối, không nới quyền để tiếp tục.

### UC-AIN-012: Giữ ranh giới câu hỏi bệnh lý

[Use case gốc](usecases/UC-AIN-012.md)

1. Biên an toàn kiểm yêu cầu trước khi đưa nội dung vào công cụ/model hoặc lưu hội thoại.
2. Hệ thống nhận diện nhánh ngoài phạm vi chẩn đoán/điều trị/cá nhân hóa sức khỏe mà không tạo hoặc suy luận hồ sơ.
3. Hệ thống chặn xử lý nhánh đó, không hỏi thêm bệnh và không chuyển dữ liệu thô sức khỏe tới tool/model.
4. Hệ thống kiểm trạng thái phê duyệt lời nhắc bắt buộc; chỉ khi có nội dung được duyệt mới dùng đúng nội dung đó trong phản hồi.
5. Hệ thống trả trạng thái ngoài phạm vi tại UI-AIN-07 và chỉ ghi metadata an toàn; mock khi chưa duyệt chỉ thể hiện placeholder chờ xác nhận.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Chưa duyệt lời nhắc: hệ thống giữ BLOCKED E9-Q09, runtime trả ERR-AIN-503-01; không mở hội thoại thật, placeholder mock không là lời nhắc đã duyệt.
- 1a. Sức khỏe xen trong yêu cầu đổi món: hệ thống chặn phần ngoài phạm vi; không tự coi là kiêng nguyên liệu thông thường, không tạo hồ sơ hoặc chuyển payload tới model.
- 3a. Khách muốn mở gợi ý theo bệnh bằng chỉ dẫn trong chat: hệ thống giữ gate O-03/E9-Q14 đóng; không nhận consent sức khỏe để vượt gate và không sinh gợi ý.

### UC-AIN-013: Đối soát lượt và chi phí AI

[Use case gốc](usecases/UC-AIN-013.md)

1. Bộ xử lý usage đối chiếu sự kiện theo run/eventId duy nhất với reservation và policyVersion tương ứng.
2. Bộ xử lý tách confirmed, estimated, unknown và reserved; chỉ chuyển reserve sang confirmed một lần khi có bằng chứng xác nhận.
3. Bộ xử lý giữ phần chưa rõ và gắn ngày/đơn vị theo policy được duyệt; không xóa debt qua ranh giới ngày.
4. Giám đốc chọn ngày/group và runRef cần rà tại UI-AIN-05; hệ thống kiểm quyền đọc báo cáo AIN.
5. Hệ thống đọc ledger đã có và trả tổng chi phí AI, reservation cùng sai lệch chưa xử lý; GET không thực hiện lại quyết toán hay gọi provider.
6. Giám đốc đối chiếu báo cáo với provenance được phép đọc, không xem raw hội thoại hoặc log AIO.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Sự kiện trùng: bộ xử lý nhận diện eventId đã có và không cộng lại; tổng confirmed/reserved không tăng lần hai.
- 2a. Usage thiếu/provider lỗi hoặc timeout: hệ thống giữ UNKNOWN cùng reservation; không báo còn đủ tiền giả hoặc tự hoàn chỗ.
- 3a. Sự kiện đến muộn qua ngày: hệ thống đối chiếu theo ngày của policy được duyệt; debt cũ còn nguyên, chưa có policy thì BLOCKED E9-Q07/E9-Q13.
- 4a. Thiếu quyền: hệ thống trả ERR-AIN-403-01; báo cáo không lộ cho khách/model và ledger không đổi.
- 5a. Nguồn/policy không khả dụng: hệ thống trả ERR-AIN-503-01; không dựng tổng giả hoặc lấy log AIO thay nguồn AIN.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-AIN-400-01 | Yêu cầu chưa đúng định dạng. | Sửa trường được chỉ ra |
| ERR-AIN-401-01 | Phiên chưa hợp lệ. | Xác minh theo cơ chế được duyệt |
| ERR-AIN-403-01 | Không được thực hiện yêu cầu này. | Không thử vượt quyền |
| ERR-AIN-404-01 | Không tìm thấy dữ liệu. | Kiểm mã thuộc phiên của bạn |
| ERR-AIN-409-01 | Phương án cần kiểm lại. | Tải lại và kiểm trước gửi |
| ERR-AIN-409-02 | Mã yêu cầu đã được sử dụng. | Đối soát yêu cầu gốc |
| ERR-AIN-422-01 | Chưa có phương án hợp lệ cho yêu cầu này. | Làm rõ/chỉnh yêu cầu không kèm sức khỏe |
| ERR-AIN-429-01 | Hiện chưa thể nhận thêm yêu cầu. | Xem thời điểm khả dụng nếu policy có; không đổi identity |
| ERR-AIN-503-01 | Chức năng hiện chưa khả dụng. | Giữ mã yêu cầu để kiểm lại; không coi đã tiếp nhận |
| ERR-AIN-500-01 | Chưa thể xác nhận hoàn tất. | Đối soát cùng key trước thử lại |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
