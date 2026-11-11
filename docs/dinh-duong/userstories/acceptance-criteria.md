# Acceptance criteria — NUTR

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Expected là hợp đồng nháp; scenario phụ thuộc câu hỏi chưa phải tiêu chí đã duyệt. Dữ liệu I1/I2/A/B và tiền/token thử đều giả định, không phải dữ liệu Gia Phát.

## AC-NUTR-001 — US-NUTR-001, scenario 1

```gherkin
Scenario: Quản lý bảng thành phần — 1
  Given bảng thử nguyên liệu I1 chưa có, nguồn ghi rõ GIẢ ĐỊNH, kcal=100; đạm=10; béo=2; carb=15; ediblePct=80; unit=g
  When PUT đủ trường với version=0
  Then 201; version=1; 1 revision và audit; số liệu giữ đúng, không đổi công thức món
```

Truy vết: FR-NUTR-REF-001; BR-NUTR-001; TC-NUTR-001. Trạng thái: NOT RUN.

## AC-NUTR-002 — US-NUTR-001, scenario 2

```gherkin
Scenario: Quản lý bảng thành phần — 2
  Given I1 có version=1
  When PUT energyKcal=-1 hoặc proteinG=null hoặc thiếu sourceLocator
  Then 422; ERR-NUTR-422-01; không ghi bất kỳ bảng nào
```

Truy vết: FR-NUTR-REF-001; BR-NUTR-001; TC-NUTR-002. Trạng thái: NOT RUN.

## AC-NUTR-003 — US-NUTR-001, scenario 3

```gherkin
Scenario: Quản lý bảng thành phần — 3
  Given hai người cùng đọc I1 version=1; người thứ nhất đã ghi version=2
  When người thứ hai PUT version=1
  Then 409 ERR-NUTR-409-01; giá trị version=2 không bị ghi đè
```

Truy vết: FR-NUTR-REF-001; BR-NUTR-001; TC-NUTR-003. Trạng thái: NOT RUN.

## AC-NUTR-004 — US-NUTR-002, scenario 1

```gherkin
Scenario: Kiểm độ phủ nguyên liệu — 1
  Given hai công thức thử dùng chung I1 và I2 đều đủ dữ liệu
  When POST recipeIds của hai công thức
  Then 200; complete=2,total=2; không đếm lặp I1
```

Truy vết: FR-NUTR-REF-002; BR-NUTR-002; TC-NUTR-004. Trạng thái: NOT RUN.

## AC-NUTR-005 — US-NUTR-002, scenario 2

```gherkin
Scenario: Kiểm độ phủ nguyên liệu — 2
  Given I2 chưa có bảng thành phần
  When kiểm độ phủ hai công thức có I2
  Then 200; complete=1,total=2; missing ghi I2 và cả hai recipeId; không thay null bằng 0
```

Truy vết: FR-NUTR-REF-002; BR-NUTR-002; TC-NUTR-005. Trạng thái: NOT RUN.

## AC-NUTR-006 — US-NUTR-002, scenario 3

```gherkin
Scenario: Kiểm độ phủ nguyên liệu — 3
  Given I1 có cả bốn chỉ số bằng 0 và nguồn đầy đủ
  When kiểm I1 rồi gửi lại khi thiếu đăng nhập
  Then lần đầu complete=1; lần sau 401 ERR-NUTR-401-01; không trả dữ liệu
```

Truy vết: FR-NUTR-REF-002; BR-NUTR-002; TC-NUTR-006. Trạng thái: NOT RUN.

## AC-NUTR-007 — US-NUTR-003, scenario 1

```gherkin
Scenario: Tính dinh dưỡng món — 1
  Given fixture I1: qty=50g, edible=80%, kcal=100/P10/F2/C15 trên 100g; chỉ một dòng
  When tính món với công thức ACTIVE
  Then totals=40.00 kcal,4.00g đạm,0.80g béo,6.00g carb; có nhãn ước tính từ định lượng sống
```

Truy vết: FR-NUTR-CALC-001; BR-NUTR-003; TC-NUTR-007. Trạng thái: BLOCKED: NUTR-Q02.

## AC-NUTR-008 — US-NUTR-003, scenario 2

```gherkin
Scenario: Tính dinh dưỡng món — 2
  Given công thức dùng 1 quả nhưng gramsPerUnit thiếu
  When tính món
  Then 422 ERR-NUTR-422-02; totals=null; chỉ rõ nguyên liệu thiếu quy đổi, không trả tổng một phần
```

Truy vết: FR-NUTR-CALC-001; BR-NUTR-003; TC-NUTR-008. Trạng thái: NOT RUN.

## AC-NUTR-009 — US-NUTR-003, scenario 3

```gherkin
Scenario: Tính dinh dưỡng món — 3
  Given qty=1 quả; gramsPerUnit=50; edible=80%; cùng thành phần I1
  When tính rồi đổi COST_AP_HAO_HUT và tính lại
  Then hai kết quả bằng nhau:40.00/4.00/0.80/6.00; không nhân hao hụt Cost
```

Truy vết: FR-NUTR-CALC-001; BR-NUTR-003; TC-NUTR-009. Trạng thái: BLOCKED: NUTR-Q02.

## AC-NUTR-010 — US-NUTR-004, scenario 1

```gherkin
Scenario: Tính dinh dưỡng tổ hợp suất — 1
  Given suất thử yêu cầu 1 chính; chính A=40/4/0.8/6, B=80/8/1.6/12; phụ cố định=10/1/0.2/1.5
  When chọn A và phụ rồi tính
  Then 50.00 kcal,5.00g đạm,1.00g béo,7.50g carb; không cộng B; lưu danh sách món đã chọn
```

Truy vết: FR-NUTR-CALC-002; BR-NUTR-004; TC-NUTR-010. Trạng thái: BLOCKED: NUTR-Q03.

## AC-NUTR-011 — US-NUTR-004, scenario 2

```gherkin
Scenario: Tính dinh dưỡng tổ hợp suất — 2
  Given suất cần 1 chính, người dùng chọn A và B
  When POST tổ hợp có 2 chính hoặc trùng itemId
  Then 422 ERR-NUTR-422-03; không tính tổng
```

Truy vết: FR-NUTR-CALC-002; BR-NUTR-004; TC-NUTR-011. Trạng thái: NOT RUN.

## AC-NUTR-012 — US-NUTR-004, scenario 3

```gherkin
Scenario: Tính dinh dưỡng tổ hợp suất — 3
  Given đang xem menuVersion=2, một người sửa thành 3
  When POST menuVersion=2 hoặc itemId thuộc cơ sở không có quyền
  Then 409 ERR-NUTR-409-01 hoặc 404 ERR-NUTR-404-01 tương ứng; không lộ dữ liệu ngoài quyền
```

Truy vết: FR-NUTR-CALC-002; BR-NUTR-004; TC-NUTR-012. Trạng thái: NOT RUN.

## AC-NUTR-013 — US-NUTR-005, scenario 1

```gherkin
Scenario: Xem kết quả và nguồn lịch sử — 1
  Given calculation C1 ghi I1 version=1; I1 đổi thành version=2
  When GET C1
  Then 200; giữ totals/source version=1; isStale=true; đề nghị tính lại
```

Truy vết: FR-NUTR-SNAP-001; BR-NUTR-005; TC-NUTR-013. Trạng thái: NOT RUN.

## AC-NUTR-014 — US-NUTR-005, scenario 2

```gherkin
Scenario: Xem kết quả và nguồn lịch sử — 2
  Given người dùng không có quyền cơ sở của C1
  When GET C1
  Then 404 ERR-NUTR-404-01; không trả totals hoặc nguồn
```

Truy vết: FR-NUTR-SNAP-001; BR-NUTR-005; TC-NUTR-014. Trạng thái: NOT RUN.

## AC-NUTR-015 — US-NUTR-005, scenario 3

```gherkin
Scenario: Xem kết quả và nguồn lịch sử — 3
  Given C1 và C2 là hai lần tính, clientRevision 1 và 2
  When phản hồi C1 tới sau C2
  Then UI giữ C2; lịch sử vẫn xem C1; cả hai có nhãn ước tính từ định lượng sống
```

Truy vết: FR-NUTR-SNAP-001; BR-NUTR-005; TC-NUTR-015. Trạng thái: NOT RUN.
