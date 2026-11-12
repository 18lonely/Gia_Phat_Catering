# Quy trình bằng chứng R9

Draft · 12/11/2026 · Chỉ tài liệu; dữ liệu minh họa synthetic; chưa duyệt/chưa chạy sản phẩm.

Mỗi lần chạy tương lai có runBatchId, caseId, environment/build, thời gian, người chạy/duyệt để trống đến khi thực hiện, datasetHash, decisionRefs, policyVersion, toolAllowlistVersion và expectedOracleRef. Trạng thái hiện tại chỉ NOT RUN/BLOCKED, Actual/Evidence trống.

| Nhóm | Bằng chứng cần ghi | Cách đánh giá |
| :--- | :--- | :--- |
| MENU |input canonicalHash; candidate trước/sau chỉnh; source/ruleVersions; E2 call+result cùng hash; safe output |Tách evidence server và UI; UI có bảng kiểm không chứng minh validator đã chạy |
| COST |registry/grants; deny trace; canary synthetic tại kho nội bộ cô lập; context model được lọc; HTTP/error/log/cache/giải thích |Tìm cả giá trị và biểu diễn biến đổi/ratio; quyền deny phải chứng minh trước đọc, không chỉ không thấy trong câu trả lời |
| MED |manifest input synthetic, response, approvedReminderVersion, rubric từng tiêu chí, đánh giá độc lập |Chưa lời nhắc/rubric thì BLOCKED; không lưu dữ liệu y tế thật vào báo cáo |
| BUDGET |reservation/usageEvent/requestKey, dayKey/unit/policy; timeline đồng thời, source usage có xác nhận |Đối soát confirmed+reserved và phí thực ngày; missingusage không0; timeout giữ unknown |
| HANDOFF |record+source+candidate revision, request/receipt identity, commit/fault timeline |ACK ứng dụng khác receipt đầu nhận; không giả đã vào CRM hoặc đã áp dụng |

Mẫu dòng evidence: caseId / Expected / Actual / Status / artifactRef+hash / reviewer / approvedDecisionRefs. Nội dung nhạy cảm nếu cần nghiệm thu chỉ trong kho quyền hạn chế đã duyệt, bản report redacted; không gửi raw log sang model. Snapshot tài liệu/UI của phiên này nằm validation, không điền vào Evidence của test sản phẩm.

Sau có nguồn đủ chỉ chuyển BLOCKED→NOT RUN có lý do. PASS/FAIL chỉ khi thật chạy và có evidence độc lập; không đánh dấu PASS do checklist/link/hash sạch. Không giảm mẫu số hoặc xóa ca thất bại; một lỗi leak chặn nghiệm thu R9-COST. Không dùng số ca có liên kết làm bằng chứng R9/G-Next.
