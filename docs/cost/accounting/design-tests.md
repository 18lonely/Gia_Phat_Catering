# AC và test thiết kế kế toán

Phiên bản0.1.0 ·11/11/2026 ·18 ca, chưa chạy backend. Khác12 ca TC-ACC-001–012: bộ này truy vết hợp đồng/dữ liệu/UI; không cộng hai bộ thành số ca độc lập đã nghiệm thu.

## US-ACC-001: FR-ACC-001

Nguồn: API-COST-005/006/007/012/013/014; API-ACC-001; ingredient_prices; SCR-ACC-01. Gate: Rounding giá mua; policy migration.

### TC-ACC-D01-01: Giá hai cách ghi cho cùng cost

```gherkin
Scenario: AC-ACC-D01-01
  Given 100000 EXCLUSIVE VAT8% và108000 INCLUSIVE, có nguồn
  When preview rồi tạo hai fixture độc lập
  Then cùng giá cost108000;70g cùng7560, không cộng VAT hai lần
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Rounding giá mua); policy migration; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D01-02: Thiếu VAT và phần lẻ

```gherkin
Scenario: AC-ACC-D01-02
  Given EXCLUSIVE thiếu rate/amount; fixture khác quote1 rate8%
  When thử commit
  Then không ghi giá ở cả hai; báo thiếu VAT hoặc rounding-unresolved, không tự làm tròn
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Rounding giá mua); policy migration; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D01-03: Lô nguyên tử và legacy

```gherkin
Scenario: AC-ACC-D01-03
  Given lô2 dòng một dòng UNKNOWN; lịch sử giá legacy có snapshot
  When kiểm/commit lô và đọc lịch sử
  Then không ghi lô; legacy gắn cờ, snapshot không bị chuẩn hóa lại
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Rounding giá mua); policy migration; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

## US-ACC-002: FR-ACC-002

Nguồn: API-ACC-002; order_pricing_snapshots; SCR-ACC-02. Gate: Sale context và quyền mới.

### TC-ACC-D02-01: Cờ hóa đơn độc lập

```gherkin
Scenario: AC-ACC-D02-01
  Given đơn100×40000 đã gồmVAT8%; context đầy đủ
  When đổi cờ hóa đơn trên hai fixture trước chụp
  Then amountDue đều4000000; revenueExVat=4000000/1.08, không đổi do cờ
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Sale context và quyền mới); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D02-02: Không suy diễn doanh thu

```gherkin
Scenario: AC-ACC-D02-02
  Given priceBasis UNKNOWN hoặc VAT chưa rõ
  When đọc context
  Then UNRESOLVED; revenueExVat=null; không trả doanh thu0 hoặc gross giả là net
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Sale context và quyền mới); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D02-03: Phạm vi order/snapshot

```gherkin
Scenario: AC-ACC-D02-03
  Given kế toán chỉ kháchA; orderB ngoài quyền
  When gọi contextB và gán snapshotB cho draftA
  Then 404 ngoài scope hoặc409 snapshot không thuộc order; không lộ dữ liệuB
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Sale context và quyền mới); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

## US-ACC-003: FR-ACC-003

Nguồn: API-ACC-003; Không ghi; đọc order_pricing_snapshots; SCR-ACC-03. Gate: CK-Q01/02/03/04/10.

### TC-ACC-D03-01: Hai cách tính

```gherkin
Scenario: AC-ACC-D03-01
  Given đơn100×40000; giả định base GROSS;5% hoặc2000/suất
  When tính từng cách
  Then khoản thử200000;amountDue4000000;canConfirm=false, chưa thanh toán
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q01/02/03/04/10); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D03-02: Basis chưa chốt

```gherkin
Scenario: AC-ACC-D03-02
  Given PERCENT5% nhưng baseUNRESOLVED
  When preview
  Then calculatedAmount=null và câuCK-Q01; không thay bằng0
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q01/02/03/04/10); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D03-03: Không cộng hai kiểu

```gherkin
Scenario: AC-ACC-D03-03
  Given request có cả ratePct và amountPerServing
  When preview
  Then 422; không tự cộng hai khoản; preview không ghi order/draft
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q01/02/03/04/10); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

## US-ACC-004: FR-ACC-004

Nguồn: API-ACC-004/005/006; order_discount_records; order_discount_events; SCR-ACC-03/04. Gate: CK-Q04; chưa duyệt/chi trả.

### TC-ACC-D04-01: Lưu draft có lịch sử

```gherkin
Scenario: AC-ACC-D04-01
  Given snapshot đúng version, fixed2000×100, keyK
  When tạo draft
  Then DRAFT khoản thử200000;event DRAFT_CREATED;amountDue không đổi
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q04); chưa duyệt/chi trả; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D04-02: Retry không tạo trùng

```gherkin
Scenario: AC-ACC-D04-02
  Given draft đã commit nhưng phản hồi mất
  When retry cùng key/hash; sau đó khác hash
  Then lần cùng trả bản cũ; khác hash409; chỉ một draft/event tạo
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q04); chưa duyệt/chi trả; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D04-03: Không vượt gate

```gherkin
Scenario: AC-ACC-D04-03
  Given draft tồn tại, CK chưa trả lời
  When gửi statusCONFIRMED hoặc gọi thao tác thanh toán
  Then không chuyển trạng thái/không ghi thanh toán; thiếu quyền bị403
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q04); chưa duyệt/chi trả; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

## US-ACC-005: FR-ACC-005

Nguồn: API-ACC-007/008; customer_price_terms; SCR-ACC-02. Gate: Quyền terms và activation sales policy.

### TC-ACC-D05-01: Nháp chưa đủ vẫn thể hiện thiếu

```gherkin
Scenario: AC-ACC-D05-01
  Given kháchA,mealType1,quote40000,basisUNKNOWN,invoice=false,rate=null
  When tạo term draft
  Then DRAFT; không kích hoạt; không tự gánrate0
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Quyền terms và activation sales policy); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D05-02: Khoảng ngày sai

```gherkin
Scenario: AC-ACC-D05-02
  Given effectiveTo trước effectiveFrom
  When lưu
  Then 422 và không tạo term
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Quyền terms và activation sales policy); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D05-03: Không hồi tố context

```gherkin
Scenario: AC-ACC-D05-03
  Given term draft mới của khách; order cũ có snapshot
  When sửa điều kiện tương lai
  Then snapshot order cũ giữ nguyên; không tự đổi tiền phải trả
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (Quyền terms và activation sales policy); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

## US-ACC-006: FR-ACC-006

Nguồn: Sự kiện nội bộ order.changed; order_discount_records; order_discount_events; order_pricing_snapshots; SCR-ACC-04. Gate: CK-Q07/08/09; chỉ cơ chế đánh dấu review.

### TC-ACC-D06-01: Đổi số suất

```gherkin
Scenario: AC-ACC-D06-01
  Given draft dựa trênorder v1=100suất;order v2=80suất
  When xử lý order.changed một lần
  Then draft NEEDS_REVIEW; giữ giá trị cũ để so, không tự sửa200000 thành160000 và không chi tiền
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q07/08/09); chỉ cơ chế đánh dấu review; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D06-02: Sự kiện lặp

```gherkin
Scenario: AC-ACC-D06-02
  Given eventKeyE đã xử lý
  When nhận E lần hai
  Then không thêm event duplicate, không nhân khoản chiết khấu
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q07/08/09); chỉ cơ chế đánh dấu review; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

### TC-ACC-D06-03: Hủy khi chưa rõ chính sách

```gherkin
Scenario: AC-ACC-D06-03
  Given order bị hủy; khoản đang cần review
  When worker nhận sự kiện
  Then giữ dấu vết, yêu cầuCK-Q08/09; không xóa khoản hoặc tự thu hồi/bù trừ
```

Bước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED (chờ CK-Q07/08/09); chỉ cơ chế đánh dấu review; chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.

