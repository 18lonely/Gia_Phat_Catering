---
id: DOC-E13-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## AC-EXP-001-1 — Luồng kỳ vọng

US-EXP-001 · FR-EXP-PER-001 · UC-EXP-001 · TC-EXP-001-1 · BLOCKED; E13-Q02.

```gherkin
Scenario: Quản lý và khóa kỳ chi phí — 1
  Given kỳ mở có bộ nguồn và quyết định khóa hợp lệ
  When gửi yêu cầu khóa
  Then kỳ LOCKED, snapshot và audit giữ nguyên nguồn
```

## AC-EXP-001-2 — Lỗi nghiệp vụ

US-EXP-001 · FR-EXP-PER-001 · UC-EXP-001 · TC-EXP-001-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Quản lý và khóa kỳ chi phí — 2
  Given kỳ đã LOCKED
  When gửi sửa trực tiếp kỳ
  Then ERR-EXP-409-01; không đổi byte dữ liệu gốc
```

## AC-EXP-001-3 — Biên và bảo toàn

US-EXP-001 · FR-EXP-PER-001 · UC-EXP-001 · TC-EXP-001-3 · BLOCKED; E13-Q02.

```gherkin
Scenario: Quản lý và khóa kỳ chi phí — 3
  Given hai thao tác cùng version cũ
  When gửi khóa đồng thời với ghi chi phí
  Then chỉ một version hợp lệ; thao tác còn lại ERR-EXP-409-02
```

## AC-EXP-002-1 — Luồng kỳ vọng

US-EXP-002 · FR-EXP-COST-001 · UC-EXP-002 · TC-EXP-002-1 · BLOCKED; E13-Q01.

```gherkin
Scenario: Ghi chi phí theo cơ sở và loại — 1
  Given kỳ mở, loại được duyệt, chứng từ synthetic 120000 đ
  When ghi khoản trực tiếp cho khách A tại cơ sở A
  Then dòng nháp giữ 120000 đ, khách/cơ sở/nguồn; không phân bổ lại
```

## AC-EXP-002-2 — Lỗi nghiệp vụ

US-EXP-002 · FR-EXP-COST-001 · UC-EXP-002 · TC-EXP-002-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Ghi chi phí theo cơ sở và loại — 2
  Given dòng chi phí thiếu chứng từ hoặc loại
  When gửi lưu
  Then ERR-EXP-422-01 và chỉ ra trường thiếu; không ghi dòng
```

## AC-EXP-002-3 — Biên và bảo toàn

US-EXP-002 · FR-EXP-COST-001 · UC-EXP-002 · TC-EXP-002-3 · BLOCKED; E13-Q01.

```gherkin
Scenario: Ghi chi phí theo cơ sở và loại — 3
  Given sourceKey đã nằm trong cost E3/E11 của cùng kỳ
  When nhập lại khoản đó
  Then ERR-EXP-409-03; không cộng hai lần
```

## AC-EXP-003-1 — Luồng kỳ vọng

US-EXP-003 · FR-EXP-TIME-001 · UC-EXP-003 · TC-EXP-003-1 · BLOCKED; E13-Q03; E11-Q09.

```gherkin
Scenario: Ghi giờ công thực tế theo ca — 1
  Given ca E11 và nguồn giờ 8 giờ có căn cứ được duyệt
  When ghi giờ thực tế của người synthetic P-A
  Then giữ người/cơ sở/ca/revision/bằng chứng, không tạo bảng lương
```

## AC-EXP-003-2 — Lỗi nghiệp vụ

US-EXP-003 · FR-EXP-TIME-001 · UC-EXP-003 · TC-EXP-003-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Ghi giờ công thực tế theo ca — 2
  Given chỉ có phân ca E11, không có giờ thực tế
  When yêu cầu xác nhận chấm công
  Then ERR-EXP-422-02; không suy đã làm đủ giờ
```

## AC-EXP-003-3 — Biên và bảo toàn

US-EXP-003 · FR-EXP-TIME-001 · UC-EXP-003 · TC-EXP-003-3 · BLOCKED; E13-Q03; E11-Q09.

```gherkin
Scenario: Ghi giờ công thực tế theo ca — 3
  Given một người có hai dòng cùng nguồn ca
  When gửi lại dòng chấm công
  Then không cộng đôi giờ; conflict hoặc receipt theo contract được duyệt
```

## AC-EXP-004-1 — Luồng kỳ vọng

US-EXP-004 · FR-EXP-LAB-001 · UC-EXP-004 · TC-EXP-004-1 · BLOCKED; E13-Q03/04.

```gherkin
Scenario: Tham chiếu chi phí nhân công — 1
  Given nguồn chi phí nhân công đã duyệt và cùng cơ sở/kỳ
  When liên kết nguồn với bảng công
  Then giữ amount và sourceVersion; không sinh bảng lương mới
```

## AC-EXP-004-2 — Lỗi nghiệp vụ

US-EXP-004 · FR-EXP-LAB-001 · UC-EXP-004 · TC-EXP-004-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Tham chiếu chi phí nhân công — 2
  Given có giờ công nhưng chưa có đơn giá hay nguồn tiền công
  When yêu cầu tính chi phí
  Then ERR-EXP-422-02; amount null, không mặc định 0
```

## AC-EXP-004-3 — Biên và bảo toàn

US-EXP-004 · FR-EXP-LAB-001 · UC-EXP-004 · TC-EXP-004-3 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Tham chiếu chi phí nhân công — 3
  Given đơn giá nguồn thay phiên bản sau kỳ khóa
  When đọc báo cáo cũ
  Then giữ phiên bản đã chụp; thay đổi chỉ qua điều chỉnh
```

## AC-EXP-005-1 — Luồng kỳ vọng

US-EXP-005 · FR-EXP-METH-001 · UC-EXP-005 · TC-EXP-005-1 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Soạn phiên bản phương pháp phân bổ — 1
  Given kế toán có phương án kèm căn cứ
  When lưu nháp phương pháp
  Then tạo DRAFT và revision; không tự APPROVED
```

## AC-EXP-005-2 — Lỗi nghiệp vụ

US-EXP-005 · FR-EXP-METH-001 · UC-EXP-005 · TC-EXP-005-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Soạn phiên bản phương pháp phân bổ — 2
  Given bản phương pháp đã APPROVED
  When sửa nội dung trên cùng version
  Then ERR-EXP-409-01; cần phiên bản mới
```

## AC-EXP-005-3 — Biên và bảo toàn

US-EXP-005 · FR-EXP-METH-001 · UC-EXP-005 · TC-EXP-005-3 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Soạn phiên bản phương pháp phân bổ — 3
  Given chưa chọn phương pháp nào
  When mở form mới
  Then không có driver mặc định, không tính tỷ trọng hoặc lợi nhuận
```

## AC-EXP-006-1 — Luồng kỳ vọng

US-EXP-006 · FR-EXP-APRV-001 · UC-EXP-006 · TC-EXP-006-1 · BLOCKED; E13-Q05; O-06.

```gherkin
Scenario: Ghi duyệt phương pháp của Giám đốc — 1
  Given Giám đốc độc lập có bằng chứng duyệt đúng hash
  When ghi chấp thuận phiên bản
  Then APPROVED có người duyệt, thời điểm, evidence và phạm vi; không áp vào báo cáo cũ
```

## AC-EXP-006-2 — Lỗi nghiệp vụ

US-EXP-006 · FR-EXP-APRV-001 · UC-EXP-006 · TC-EXP-006-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Ghi duyệt phương pháp của Giám đốc — 2
  Given người duyệt cũng là người lập/sửa cuối
  When gửi chấp thuận
  Then ERR-EXP-403-01; không có quyết định hiệu lực
```

## AC-EXP-006-3 — Biên và bảo toàn

US-EXP-006 · FR-EXP-APRV-001 · UC-EXP-006 · TC-EXP-006-3 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Ghi duyệt phương pháp của Giám đốc — 3
  Given hash nội dung thay đổi từ lúc mở màn duyệt
  When gửi duyệt hash cũ
  Then ERR-EXP-409-02; yêu cầu đọc lại, không duyệt nhầm bản
```

## AC-EXP-007-1 — Luồng kỳ vọng

US-EXP-007 · FR-EXP-ALLOC-001 · UC-EXP-007 · TC-EXP-007-1 · BLOCKED; E13-Q05/06/09/12.

```gherkin
Scenario: Kiểm cổng và lập lần phân bổ — 1
  Given phương pháp đã duyệt và nguồn đầy đủ theo manifest
  When lập lần phân bổ
  Then snapshot mới ghi methodVersionRef, từng nguồn và phần chưa phân bổ; không sửa lần cũ
```

## AC-EXP-007-2 — Lỗi nghiệp vụ

US-EXP-007 · FR-EXP-ALLOC-001 · UC-EXP-007 · TC-EXP-007-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Kiểm cổng và lập lần phân bổ — 2
  Given không có phương pháp APPROVED
  When yêu cầu lợi nhuận theo khách
  Then ERR-EXP-422-03 và BLOCKED; chỉ xem chi phí trực tiếp
```

## AC-EXP-007-3 — Biên và bảo toàn

US-EXP-007 · FR-EXP-ALLOC-001 · UC-EXP-007 · TC-EXP-007-3 · BLOCKED; E13-Q05/06/09/12.

```gherkin
Scenario: Kiểm cổng và lập lần phân bổ — 3
  Given driver thiếu hoặc tổng driver bằng 0
  When yêu cầu phân bổ
  Then không chia 0, không dồn cho khách bất kỳ; giữ khoản chưa phân bổ và lý do
```

## AC-EXP-008-1 — Luồng kỳ vọng

US-EXP-008 · FR-EXP-PROF-001 · UC-EXP-008 · TC-EXP-008-1 · BLOCKED; E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15.

```gherkin
Scenario: Tra cứu lợi nhuận theo khách — 1
  Given bộ nguồn được duyệt, doanh thu E7 đã đối soát
  When xem khách trong một cơ sở/kỳ
  Then hiện đúng snapshot và methodVersion; không thay số bằng giá hợp đồng mới
```

## AC-EXP-008-2 — Lỗi nghiệp vụ

US-EXP-008 · FR-EXP-PROF-001 · UC-EXP-008 · TC-EXP-008-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Tra cứu lợi nhuận theo khách — 2
  Given doanh thu chưa đối soát hoặc không có căn cứ thành phần lợi nhuận
  When mở báo cáo khách
  Then ERR-EXP-422-02; BLOCKED, không gọi chênh thu trừ nguyên liệu là lợi nhuận
```

## AC-EXP-008-3 — Biên và bảo toàn

US-EXP-008 · FR-EXP-PROF-001 · UC-EXP-008 · TC-EXP-008-3 · BLOCKED; E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15.

```gherkin
Scenario: Tra cứu lợi nhuận theo khách — 3
  Given khách có nguồn ở hai cơ sở
  When lọc theo từng cơ sở rồi tổng khách
  Then không trộn khóa; không cộng nguồn trùng; chỉ tổng khi từng phần đủ căn cứ
```

## AC-EXP-009-1 — Luồng kỳ vọng

US-EXP-009 · FR-EXP-RECON-001 · UC-EXP-009 · TC-EXP-009-1 · BLOCKED; E13-Q06/08/09/14.

```gherkin
Scenario: Đối chiếu lợi nhuận với từng cơ sở — 1
  Given fixture đối chiếu cùng cơ sở: doanh thu 1000, trực tiếp 600, chung 200, mọi khoản đã phân bổ
  When so tổng khách 120 + 80 với kết quả cơ sở 200
  Then delta 0, chưa phân bổ 0; chỉ đủ một điều kiện R13, không tự nghiệm thu
```

## AC-EXP-009-2 — Lỗi nghiệp vụ

US-EXP-009 · FR-EXP-RECON-001 · UC-EXP-009 · TC-EXP-009-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Đối chiếu lợi nhuận với từng cơ sở — 2
  Given cơ sở 200, tổng khách 250, chưa phân bổ có tác động -50
  When mở đối chiếu
  Then hiện cầu nối 250 - 50 = 200, nhưng R13 vẫn chưa đạt vì khách chưa phân bổ hết
```

## AC-EXP-009-3 — Biên và bảo toàn

US-EXP-009 · FR-EXP-RECON-001 · UC-EXP-009 · TC-EXP-009-3 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Đối chiếu lợi nhuận với từng cơ sở — 3
  Given cơ sở 200, tổng khách 250, phần chưa phân bổ -40
  When mở đối chiếu
  Then delta -10 hiện rõ; không giấu 10 vào khách cuối, không dùng dung sai Cost
```

## AC-EXP-010-1 — Luồng kỳ vọng

US-EXP-010 · FR-EXP-ADJ-001 · UC-EXP-010 · TC-EXP-010-1 · BLOCKED; E13-Q10; O-06.

```gherkin
Scenario: Lập điều chỉnh sau khóa có phê duyệt — 1
  Given kỳ khóa và chính sách kỳ đích/duyệt đã được xác nhận
  When tạo rồi trình điều chỉnh -20000 đ có chứng từ
  Then dòng riêng gắn nguồn gốc, chỉ ghi nhận sau duyệt; snapshot cũ giữ nguyên
```

## AC-EXP-010-2 — Lỗi nghiệp vụ

US-EXP-010 · FR-EXP-ADJ-001 · UC-EXP-010 · TC-EXP-010-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Lập điều chỉnh sau khóa có phê duyệt — 2
  Given đề nghị không có lý do hoặc người duyệt hợp lệ
  When yêu cầu ghi nhận điều chỉnh
  Then ERR-EXP-422-04; kỳ và số liệu gốc không đổi
```

## AC-EXP-010-3 — Biên và bảo toàn

US-EXP-010 · FR-EXP-ADJ-001 · UC-EXP-010 · TC-EXP-010-3 · BLOCKED; E13-Q10; O-06.

```gherkin
Scenario: Lập điều chỉnh sau khóa có phê duyệt — 3
  Given đề nghị đã được ghi nhận
  When gửi lại cùng khóa nghiệp vụ
  Then không ghi bút toán lần hai; trả receipt hoặc conflict theo contract đã duyệt
```

## AC-EXP-011-1 — Luồng kỳ vọng

US-EXP-011 · FR-EXP-SAFE-001 · UC-EXP-011 · TC-EXP-011-1 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Bảo vệ lương và đầu ra nội bộ — 1
  Given kế toán được cấp quyền đúng cơ sở
  When xem báo cáo theo khách nội bộ
  Then chỉ tổng nhân công; không có personRef, giờ hay đơn giá trong payload này
```

## AC-EXP-011-2 — Lỗi nghiệp vụ

US-EXP-011 · FR-EXP-SAFE-001 · UC-EXP-011 · TC-EXP-011-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Bảo vệ lương và đầu ra nội bộ — 2
  Given người ngoài PER-07/PER-08 hoặc phiên phía khách
  When truy cập chi tiết công/lương/lợi nhuận hoặc xuất
  Then ERR-EXP-403-01; không lộ qua payload, lỗi, log, cache, file hoặc metadata
```

## AC-EXP-011-3 — Biên và bảo toàn

US-EXP-011 · FR-EXP-SAFE-001 · UC-EXP-011 · TC-EXP-011-3 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Bảo vệ lương và đầu ra nội bộ — 3
  Given người vừa bị thu hồi quyền nhưng có runRef đã biết
  When đọc lại hoặc yêu cầu bản xuất
  Then từ chối theo quyền hiện tại; không dùng cache quyền cũ
```

## AC-EXP-012-1 — Luồng kỳ vọng

US-EXP-012 · FR-EXP-SRC-001 · UC-EXP-012 · TC-EXP-012-1 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Kiểm nguồn và truy nguyên lần báo cáo — 1
  Given run có manifest và quyền đúng scope
  When mở nguồn báo cáo
  Then hiện từng nguồn/revision/cơ sở/kỳ và methodVersion; không gọi lại số giao để tính thu
```

## AC-EXP-012-2 — Lỗi nghiệp vụ

US-EXP-012 · FR-EXP-SRC-001 · UC-EXP-012 · TC-EXP-012-2 · NOT RUN; Chưa có sản phẩm để chạy.

```gherkin
Scenario: Kiểm nguồn và truy nguyên lần báo cáo — 2
  Given thiếu một nguồn trong manifest cần thiết
  When yêu cầu đánh dấu đủ dữ liệu
  Then ERR-EXP-422-02; nguồn thiếu không có giá trị 0 thay thế
```

## AC-EXP-012-3 — Biên và bảo toàn

US-EXP-012 · FR-EXP-SRC-001 · UC-EXP-012 · TC-EXP-012-3 · BLOCKED; E13-Q12/13.

```gherkin
Scenario: Kiểm nguồn và truy nguyên lần báo cáo — 3
  Given nguồn E7 có revision mới sau lần chạy
  When đọc lần chạy cũ và đề nghị làm mới
  Then bản cũ bất biến; lần mới phải kiểm lại gate và có id khác
```

