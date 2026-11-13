const fs=require('fs'),path=require('path'),crypto=require('crypto'),base=path.resolve(__dirname,'..'),root=path.resolve(base,'../..');
const sources=[
 ['docs/OVERVIEW.md','Mốc E12: 74/78, không coi nguồn được duyệt'],
 ['docs/gia-phat/review/progress-status-2026-11-12.md','Ảnh tiến độ cũ 60/78, không ghi đè; đối chiếu mốc E12 mới hơn'],
 ['docs/gia-phat/01-prd.md','FEAT-088, BO-01/02, PER-07/08, O-01/O-06'],
 ['docs/gia-phat/02-roadmap.md','R13: R7/R11 xong, Giám đốc duyệt; tiêu chí đối chiếu cơ sở'],
 ['docs/phan-hoi-bao-cao/review/handoff.md','Gói mẫu gần nhất; phạm vi và giới hạn hash lịch sử'],
 ['docs/phan-hoi-bao-cao/validation/report.md','Mẫu bàn giao/checker, không thay bằng chứng E12'],
 ['docs/cost/srs/spec.md','Giá, snapshot, dự toán, quyền cost, NFR-COST-002; đọc các mục liên quan'],
 ['docs/cost/accounting/business-rules.md','ACC-CONF-02 VAT phải trả, cờ hóa đơn và CK riêng'],
 ['docs/cost/review/decision-register.md','Câu Cost/CK/DATA-COST chưa đóng; không tự chọn thành phần'],
 ['docs/giao-nhan-doanh-thu/srs/spec.md','FR-FIN-REV/VIEW/REC/AGRE/LOCK; bản đối soát và căn cứ'],
 ['docs/giao-nhan-doanh-thu/review/questions.md','Q-13/E7-Q01–08; doanh thu/VAT/rounding/kỳ và contract chưa chốt'],
 ['docs/crm-ban-hang/srs/spec.md','Khách, snapshot giá/hợp đồng, quote nội bộ và projection khách'],
 ['docs/crm-ban-hang/review/questions.md','E10-Q15 chưa có công thức margin, không suy cost thành lợi nhuận'],
 ['docs/mua-hang-san-xuat/srs/spec.md','FR-COST-BUY-001; FR-PLAN-SHF-001; phân ca khác giờ công'],
 ['docs/mua-hang-san-xuat/review/questions.md','E11-Q07/08/09/13 và nguồn mua/công nợ giữ mở'],
 ['docs/phan-hoi-bao-cao/srs/spec.md','FR-RPT-CPCT-001, chỉ số/nguồn/projection; không thay cost %'],
 ['docs/phan-hoi-bao-cao/review/questions.md','E12-Q06/07/08/18 và toàn bộ câu nguồn còn mở'],
 ['docs/nen-tang/srs/spec.md','Quyền cơ sở, BR-SEC-008, audit, NFR nền'],
 ['docs/nen-tang/srs/erd.md','Mục khung/phạm vi bảng, khóa BIGINT, thời điểm và dữ liệu đề xuất'],
 ['docs/nen-tang/srs/schema.dbml','65 bảng; kitchens/users/customers có thật, EXP chưa có'],
];
const skillNames=['prd-epic','srs','usecase','userstory','ac','state','user-flow','api-design','api-map','wireframe-html','test-checklist','test-cases','preview'];
const scripts=fs.readdirSync(path.join(root,'docs/phan-hoi-bao-cao/validation')).filter(x=>x.endsWith('.cjs'));
const register={readScope:'Nội dung nguồn theo các mục/mã liên quan; script mẫu đọc cấu trúc, entry point và logic kiểm/render, không chạy generator lịch sử',sources:sources.map(([p,note])=>({path:p,note})),rules:fs.readdirSync(path.join(root,'.claude/ba-kit/rules')).map(x=>'.claude/ba-kit/rules/'+x),templates:['07-prd-epic.md','08-srs.md','19-state-diagram.md','26-usecase-cockburn.md','27-userstory.md','28-acceptance-criteria.md','29-user-flow.md','31-wireframe-html.html','37-api-design.md','38-api-map.md','42-test-checklist.md','43-test-cases.md'].map(x=>'.claude/ba-kit/_templates/'+x),skills:skillNames.map(x=>'.agents/skills/'+x+'/SKILL.md'),sampleScripts:scripts.map(x=>'docs/phan-hoi-bao-cao/validation/'+x)};
fs.writeFileSync(path.join(__dirname,'source-register.json'),JSON.stringify(register,null,2));
const table=(headers,rs)=>'| '+headers.join(' | ')+' |\n| '+headers.map(()=>':---').join(' | ')+' |\n'+rs.map(r=>'| '+r.join(' | ')+' |').join('\n');
const dep=fs.readFileSync(path.join(base,'review/dependencies.md'),'utf8').split('| Gói |')[1].split('\n## Nền')[0];
const report=`---
id: DOC-E13-VALIDATION-REPORT
title: Báo cáo kiểm và bàn giao E13
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [e13, validation, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Báo cáo kiểm và bàn giao E13

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở và kiểm gói tài liệu FEAT-088 |

## Phạm vi và số liệu

Đúng FEAT-088, EXP / M10, P2, PER-07/PER-08. Có thiết kế nháp có điều kiện, không chỉ gate: 12 FR / 12 UC Cockburn / 12 story; 36 AC và 36 ca chức năng (16 BLOCKED, 20 NOT RUN). Có 13 ca hệ thống overlap (4 BLOCKED, 9 NOT RUN), 4 dòng R13 BLOCKED. Mọi Actual/Evidence trống. Không ca sản phẩm đã chạy.

18 endpoint đề xuất nối về FR; 5 port ranh giới; 8 màn, 5 sơ đồ trạng thái và 2 luồng; 14 câu E13-Q01–14 để trống Trả lời. Chuỗi FR → UC → story → AC → test → API → màn nằm trong [RTM](../test/traceability.md). Khóa và kiểu đề xuất bám nền, không migration.

Độ phủ **thiết kế tài liệu nháp (74 + 1) / 78 = 75/78 ≈ 96,2 %**. Ba feature FEAT-046/047/063 chỉ gate O-03 ghi riêng. Không phải BA được duyệt, effort hoặc tiến độ phần mềm. E13 là epic cuối theo PRD; việc tiếp theo là review/chốt câu hỏi với stakeholder. R13 cần R7/R11 xong và Giám đốc duyệt nguyên tắc phân bổ; chưa có bằng chứng cả ba, chưa nghiệm thu.

## Bước 0: Nguồn đã đọc

Đọc nguồn theo mục nghiệp vụ và mã liên quan E13; không coi nháp là hợp đồng được duyệt. Đã xem cây thư mục E12 và các script validation; không chạy generator lịch sử. Danh sách chi tiết máy đọc: [source-register.json](source-register.json).

${table(['Nguồn','Nội dung áp dụng'],sources.map(([p,n])=>['['+p+']('+path.relative(__dirname,path.join(root,p)).replaceAll('\\','/')+')',n]))}

Đã đọc 19 quy tắc trong .claude/ba-kit/rules và liệt kê thư mục template; đọc các mẫu 07, 08, 19, 26, 27, 28, 29, 31, 37, 38, 42, 43. Đọc skill tương ứng tại .agents/skills. Không thấy AGENTS.md trong workspace. rg không có, dùng PowerShell/Node để tìm và đọc.

## Bảng điểm nối E13 ↔ E3/E7/E10/E11/E12

| Gói |${dep}

Lưu ý nguồn: báo cáo tiến độ 12/11 còn 60/78 vì lập trước E11/E12; lấy mốc E12 74/78 làm nền độ phủ, không sửa báo cáo cũ. ERD có diễn đạt VAT cũ; áp dụng xác nhận ACC-CONF-02 và chỉ dẫn người dùng, không thay file nguồn. E12 có 4 sai lệch hash lịch sử đã ghi trong report E12; không coi baseline E13 là cách xóa hoặc miễn sai lệch đó.

## Skill và thứ tự thực hiện

prd-epic → srs → usecase → userstory + ac → state + user-flow → api-design + api-map → wireframe-html → test-checklist + test-cases → preview → review. Dùng quy tắc tại .claude/ba-kit. Không gán story point; checklist/ca chi tiết là nháp theo yêu cầu, chưa có BA/QA phê duyệt. Renderer riêng dùng thư viện Mermaid/marked/Playwright cục bộ như gói mẫu; không chạy scripts/render_diagrams.py không có trong workspace, không dùng dịch vụ mạng hoặc mô hình AI.

## Baseline và phạm vi ghi

[baseline.json](baseline.json) chụp SHA256/kích thước của toàn bộ **1070 file cũ** trong docs trước khi viết gói; chỉ tạo một lần. [baseline-double-check.json](baseline-double-check.json) là lần chụp đối chiếu ngay sau: 0 file thay đổi, 0 file cũ thêm/xóa trong khoảng chụp. Không ghi lại baseline để bỏ sai lệch.

Chỉ hai file OVERVIEW/dashboard được append mốc E13 bằng byte UTF-8 mới, prefix cũ kiểm theo hash/kích thước baseline. 1068 file cũ còn lại giữ toàn bộ SHA256; không file cũ bị xóa, không file mới ngoài gói trong docs. PRD/roadmap/schema và baseline/manifest/report/result E6–E12 giữ nguyên; schema vẫn 65 bảng. Danh sách file mới đầy đủ: [files-created.json](files-created.json).

## Kết quả checker và bằng chứng

${table(['Checker','Phạm vi','Kết quả / bằng chứng'],[
 ['check-e13.cjs','Cấu trúc, front-matter, truy vết hai chiều, endpoint, mã mới không trùng nguồn, link Markdown/anchor, số dính chữ, câu trả lời và kết quả ca trống, manifest','0 lỗi; [structure-result.json](structure-result.json)'],
 ['render-e13.cjs','Mọi Mermaid trong tài liệu nội dung, SVG/HTML offline; preview nhúng tài liệu','7/7 sơ đồ, 32 tài liệu nội dung; 0 lỗi; [diagram-render-result.json](diagram-render-result.json)'],
 ['check-ui-e13.cjs','8 màn × 3 chiều rộng 1440/390/360 px, 6 trạng thái, form/dialog, preview, request mạng','327 kiểm, 0 lỗi, 0 request mạng; [ui-result.json](ui-result.json)'],
 ['hash-check-e13.cjs','Mọi file baseline, hai ngoại lệ append-only, file mới và số bảng','0 lỗi, 1068 file giữ hash, 2 file chỉ append; [hash-result.json](hash-result.json)']
 ])}

Đã xem ảnh desktop và mobile cho cả 8 màn. Bố cục tự xuống dòng; bảng cầu nối chuyển cột dọc ở mobile, nhãn gate đọc được, không che/chồng nội dung. Sau rà soát đã bổ sung trường nghiệp vụ vào wireframe; xem lại ảnh sau sửa. 24 ảnh từng màn và 8 ảnh ghép trong screenshots. Desktop: [1–2](screenshots/1440-sheet-1.png), [3–4](screenshots/1440-sheet-2.png), [5–6](screenshots/1440-sheet-3.png), [7–8](screenshots/1440-sheet-4.png). Mobile: [1–2](screenshots/360-sheet-1.png), [3–4](screenshots/360-sheet-2.png), [5–6](screenshots/360-sheet-3.png), [7–8](screenshots/360-sheet-4.png).

Chạy lại cả bốn checker sau lần sửa nội dung cuối; file JSON là kết quả máy, không gán trạng thái sản phẩm từ kiểm tài liệu. Checker số dính chữ chỉ quét văn xuôi E13, bỏ mã định danh/code/URL; không sửa lỗi cũ trong nguồn đã khóa.

## Giới hạn và điều kiện chưa đóng

Không tự chọn phương pháp, driver, công thức lợi nhuận/biên lợi nhuận, cách hạch toán CK hoặc chi phí cấp công ty. Khi chưa có bản duyệt, báo cáo khách BLOCKED và chỉ cho xem chi phí trực tiếp. Mọi run ghi methodVersionRef hoặc null có lý do khi BLOCKED. Phần chưa phân bổ hiển thị riêng; cầu nối khớp khi còn phần chưa phân bổ chưa đủ R13. Cần U = 0 và D = 0 trên cùng số chuẩn độc lập và đủ nguồn để hoàn tất đối chiếu theo khách.

Lương là dữ liệu nhạy cảm, chỉ PER-07/PER-08 được cấp quyền cần thiết theo scope; báo cáo khách nội bộ chỉ tổng hợp nhân công. Lợi nhuận/biên lợi nhuận không có trên tài liệu gửi khách. Kỳ khóa bất biến; điều chỉnh là bút toán riêng có lý do và người duyệt, chính sách kỳ đích còn chờ. Không tính lương/bảo hiểm/thuế TNCN.

Giữ VAT phải trả NCC trong cost, cờ hóa đơn riêng, CK riêng theo đơn không giảm phải trả NCC/khách. Giữ NFR-COST-002 (≤ 1 đ; ≤ 0,01 điểm phần trăm), tách BO-01 ≤ 52 % và BO-02 ≤ 3 điểm phần trăm. Không đóng O-02/O-03 hoặc câu nguồn. Bảng điểm nối và sổ câu hỏi ghi rõ từng phần BLOCKED.

Kiểm mock không chứng minh quyền server/DB, persistence, tính toán thực, tải, audit thật, khả năng xuất hay nghiệm thu R13. Chưa audit WCAG đầy đủ/thiết bị thật; chưa có quyết định hoặc dữ liệu thật. Preview nhúng 32 tài liệu nội dung, liên kết report/manifest bên ngoài để tránh vòng lặp. Ngày 12/11/2026 là ngày lập hồ sơ, không là ngày triển khai.

Không backend, migration, gọi mô hình AI, commit hoặc xóa file. Các script trong validation chỉ tạo/kiểm tài liệu và mock. [Handoff và prompt tiếp nối](../review/handoff.md).
`;
fs.writeFileSync(path.join(__dirname,'report.md'),report);
console.log('Prepared source register and final report.');
