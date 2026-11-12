# Báo cáo kiểm gói BA nháp E9

12/11/2026 · Chỉ tài liệu và mock tĩnh; 0 backend, 0 migration, 0 lời gọi mô hình AI.

## Phạm vi bàn giao

Đúng FEAT-060→065: 5 P0 có thiết kế nháp có điều kiện; FEAT-063 P1 chỉ gate. Độ phủ tài liệu nháp **56/78 ≈ 71,8%** = 51 hiện có + 5 E9. Ba feature gate-only FEAT-046/047/063 ghi riêng. Không phải BA được duyệt, tiến độ phần mềm hoặc nghiệm thu R9/G-Next.

- 13 FR/UC/story; 39 AC và ca chức năng (12 BLOCKED, 27 NOT RUN); 13 ca hệ thống (5 BLOCKED, 8 NOT RUN), có overlap.
- 11 HTTP endpoint và 4 port đề xuất; 3 tool model-callable trong allowlist, tách các control port và lệnh gửi nháp do khách xác nhận.
- Mapping schema hiện có và 6 cấu trúc delta sơ bộ, không merge DBML 65 bảng.
- 7 màn wireframe, 3 state diagram và 2 user flow; 35 tài liệu nội dung trong preview.
- Khung 4 bộ nghiệm thu R9; ví dụ synthetic chưa duyệt, chưa chạy bộ 30/20/20 hoặc đo chi phí ngày.
- 14 câu hỏi E9-Q01–14 CHỜ TRẢ LỜI, cột trả lời/nguồn/người/ngày trống.

## Kiểm thực hiện

| Kiểm | Bằng chứng | Phạm vi |
| :--- | :--- | :--- |
| `node validation/check-e9.cjs` | [structure-result.json](structure-result.json): 1.302 kiểm đạt, 0 lỗi | Cấu trúc, mã/RTM/AC/test/catalog, liên kết, câu hỏi trống, R9/G-Next nguyên văn,65 bảng, hash/inventory producer và prefix4 file append |
| `node validation/render-e9.cjs` | [diagram-render-result.json](diagram-render-result.json) | 5/5 Mermaid render cục bộ, 0 lỗi; preview35 tài liệu; không mạng |
| `node validation/check-ui-e9.cjs` | [ui-result.json](ui-result.json) | 116 kiểm mock, 0 lỗi;7 màn tại1440/390/360px; không tràn toàn trang; trạng thái ẩn candidate, điều hướng preview;0 request mạng |
| Kiểm trực quan | [desktop01–03](screenshots/desktop-sheet-1.png), [04–06](screenshots/desktop-sheet-2.png), [07](screenshots/desktop-sheet-3.png); [mobile01–03](screenshots/mobile-sheet-1.png), [04–06](screenshots/mobile-sheet-2.png), [07](screenshots/mobile-sheet-3.png) | Đã xem cả7 màn ở desktop/mobile qua6 ảnh ghép. Nhãn, bảng, form, thông báo và nội dung đọc được; không cắt nội dung chính. Nav mobile cuộn trong vùng riêng |
| Bảo toàn | [protected-baseline.json](protected-baseline.json) | 617 file SHA256 chụp trước viết tài liệu; toàn bộ E1–E8 + PRD/roadmap không đổi; không thêm/xóa file producer;4 file tổng quan giữ byte prefix |

Kết quả kiểm cấu trúc cuối cùng đọc trực tiếp ở structure-result.json; chỉ coi hoàn tất khi errors rỗng. Checker/renderer riêng E9 chỉ ghi output trong E9. Renderer được chuẩn bị từ khung đọc của E8 rồi đổi target; không chạy hoặc sửa generator/checker/renderer E6/E7/E8. Không tìm thấy AGENTS.md trong workspace. `rg` không có, dùng PowerShell/Node; đọc rules bản `.claude/ba-kit` và quy ước E8. Skill áp dụng: prd-epic, srs, wireframe-html.

Lần kiểm cấu trúc đầu phát hiện link đến structure-result.json chưa tồn tại trước khi checker ghi output đầu tiên; chạy lại sau khi có file đạt toàn bộ. Không sửa/reset baseline để làm pass. Workspace không phải Git repository, nên bảo toàn dựa trên SHA256 và inventory/prefix trực tiếp, không dựa vào git diff.

## File tạo/cập nhật

[Manifest file và SHA256](files-created.json) liệt kê 84 file E9; cộng manifest là 85 file mới, không tự hash chính manifest. Ngoài E9 chỉ append 4 file tổng quan được yêu cầu. Nhóm nội dung:

| Nhóm | Điểm vào |
| :--- | :--- |
| Epic/SRS | [epic](../epic-spec.md), [spec](../srs/spec.md), [states](../srs/states.md), [lỗi](../srs/error-matrix.md), [từ điển](../srs/data-dictionary.md) |
| UC/story/AC | [13 UC](../usecases/index.md), [backlog](../userstories/backlog.md), [39 AC](../userstories/acceptance-criteria.md) |
| API/data | [spec + allowlist](../api/api-spec.md), [catalog](../api/endpoint-catalog.json), [mapping](../api/data-mapping.md) |
| UI/preview | [7 màn](../html-wireframe/agent-workbench.html), [screens](../ui/screens.md), [flow](../ui/user-flow.md), [preview](../preview.html), [sơ đồ SVG](../srs/diagrams/index.html) |
| Test | [checklist](../test/checklist.md), [ca FR](../test/test-cases.md), [hệ thống](../test/system-cases.md), [RTM](../test/traceability.md), [R9](../test/r9-acceptance.md), [evidence](../test/evidence-protocol.md), [fixtures](../test/fixtures/README.md) |
| Review | [questions](../review/questions.md), [dependencies](../review/dependencies.md), [handoff](../review/handoff.md) |
| Validation | scripts riêng E9, baseline/index/results/manifest,14 ảnh riêng +6 ảnh ghép |

Chỉ append mốc12/11/2026 vào [OVERVIEW](../../OVERVIEW.md), [dashboard](../../project-dashboard.md), [progress-assessment](../../gia-phat/review/progress-assessment.md), [next-session-prompt](../../gia-phat/review/next-session-prompt.md). Không sửa lịch sử hay E1–E8/PRD/roadmap/schema.

## Giới hạn và tiếp nối

R5/R6/R8 chưa có bằng chứng hoàn tất; không xác nhận R9 hoặc G-Next đạt. API/quyền/adapter/delta là nháp; test sản phẩm đều NOT RUN/BLOCKED, Actual/Evidence trống. Kiểm HTML không chứng minh DB grants, chặn leakage, admission ngân sách, E2 validator, lưu nháp thật, consent hay xóa dữ liệu. Chưa audit WCAG đầy đủ hoặc thử thiết bị thật.

Provider/hạ tầng/nơi xử lý, identity, danh mục khẩu vị/kiêng kỵ, giá public, hành vi vượt cost, điểm nhận/người duyệt/SLA, quota/cap/đơn vị/ngày, lưu/xóa hội thoại, bộ thử/lời nhắc bệnh lý còn mở. Không có lời khuyên y tế được phê duyệt trong gói. FEAT-063 không có thuật toán/gợi ý/thu hoặc suy luận sức khỏe.

E6 CG01/08/05/06, E7 Q-13/E7-Q01–08, E8-Q01–12 giữ CHỜ TRẢ LỜI;14/14 CG OPEN;E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04 và AIO-Q01–06 không tự đóng. Cost gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn không đồng nghĩa VAT0%; chiết khấu khoản riêng theo đơn không giảm tiền phải trả. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 không đổi.

Prompt tiếp nối ở cuối next-session-prompt: chỉ bổ sung E9 theo phản hồi/nguồn mới hoặc sai lệch cụ thể; giữ phần thiếu BLOCKED, không hỏi lại producer đang chờ và không mở E10–E13. Không chạy lại helper author/capture để reset baseline hoặc ghi đè phiên lịch sử.
