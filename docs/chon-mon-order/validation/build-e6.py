"""Author the additive E6 review package. Not product code or migration."""
from pathlib import Path
import re,json
B=Path(__file__).resolve().parents[1]
def write(p,title,body):
 f=B/p; f.parent.mkdir(parents=True,exist_ok=True)
 f.write_text(f'---\nid: DOC-E6-{p.upper().replace("/","-").replace(".MD","")}\ntitle: {title}\nversion: 0.2.0\nphase: Specification\ndomain: Gia Phát\nauthor: BA\nlast_updated: 2026-11-11\n---\n# {title}\n\n**Draft để review · 11/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**\n\n| Phiên bản | Ngày | Thay đổi |\n| :--- | :--- | :--- |\n| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |\n\n'+body+'\n',encoding='utf-8')
def append(p,s):
 f=B/p; f.write_text(f.read_text(encoding='utf-8')+'\n'+s+'\n',encoding='utf-8')
rows=[]
for line in (B/'srs/spec.md').read_text(encoding='utf-8').splitlines():
 if line.startswith('| FR-'):
  c=[x.strip() for x in line.split('|')[1:-1]]
  if len(c)==7: rows.append(c)
# Scenarios are concrete review expectations, not results of software execution.
# title, API ids, data, screen, happy Given/When/Then, negative G/W/T, boundary G/W/T
cases=[
('Cấp quyền người đặt tổng','006,007','users,user_roles,customers','01',
 ('nhân viên được cấp quyền quản trị khách A và hợp đồng hợp lệ','cấp vai trò người đặt tổng cho user U ở A','tài khoản chỉ có quyền A; audit ghi người cấp và phạm vi'),
 ('U là người đặt tổng A','U cấp quyền nội bộ cho mình','403 ERR-ORD-403-01; không thay user_roles'),
 ('quản trị chỉ được giao A','gửi customerId B','404 ERR-ORD-404-01; không tiết lộ B')),
('Đăng ký qua QR công ty','008','customer_qr_codes,eaters,users','02',
 ('QR A ACTIVE và identity policy đã được duyệt','xác minh và đăng ký với identity hợp lệ','liên kết eater với tài khoản và A; không cấp quyền người đặt tổng'),
 ('QR đã ROTATED','đăng ký bằng token cũ','401 ERR-ORD-401-01; không tạo eater'),
 ('identity đã có trên thiết bị khác','đăng ký lần nữa','kết quả theo ORD-Q01; không tuyên bố cookie ngăn trùng người')),
('Mở phiên QR giới hạn','009','customer_qr_codes,eaters; delta qr_sessions','02',
 ('QR A ACTIVE, policy định danh đã chốt','mở phiên guest ngày 2026-11-16 tại điểm A1','phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần'),
 ('phiên guest thuộc A1 ngày 16','gọi ngày 17 hoặc điểm B1','404 ERR-ORD-404-01; không trả thực đơn ngoài scope'),
 ('phiên đã hết hạn','gửi lựa chọn','401 ERR-ORD-401-01; không tăng bộ đếm')),
('Quản lý QR và danh sách người ăn','010,011,012','customer_qr_codes,eaters','03',
 ('người đặt tổng A có QR ACTIVE version hiện tại','quay vòng QR với lý do','token cũ ROTATED; chỉ trả token mới một lần; lịch sử giữ nguyên'),
 ('danh sách thuộc khách B','người đặt tổng A đọc danh sách','404 ERR-ORD-404-01; không lộ tên người ăn B'),
 ('eater đã có order khóa','gỡ eater','giữ lịch sử; tác động phiên/lựa chọn chưa khóa BLOCKED ORD-Q02')),
('Quản lý dữ liệu phục vụ','013,014','customers,service_points,service_schedules,eaters','04',
 ('DDV được phân công khách A','lưu điểm A1, bếp K1 và lịch thứ Hai ca LUNCH','điểm thuộc A, lịch duy nhất theo điểm/ca/thứ, version tăng'),
 ('A1 thuộc A','lưu lịch với customer B','422 ERR-ORD-422-04; không tạo quan hệ chéo khách'),
 ('order cũ khóa ở K1','đề xuất đổi bếp sang K2','snapshot cũ giữ K1; hiệu lực tương lai chờ ORD-Q03')),
('Đặt định mức công ty','015,016','customer_quotas,meal_types,dish_prices','05',
 ('loại suất đã duyệt và policy hiệu lực đã xác nhận','người đặt tổng lưu định mức chung','version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người'),
 ('chưa có định mức hiệu lực','người ăn chọn món','422 ERR-ORD-422-01; không ghi lựa chọn'),
 ('đã có lựa chọn theo quota v1','lưu quota v2 giữa ngày','không âm thầm tính lại v1; xử lý theo ORD-Q04')),
('Chọn và đổi một món chính','001,002,017','meal_selections,selection_counters,menu_days','06',
 ('eater E chọn A version 1 trước hạn, giá tổ hợp B hợp lệ','đổi A sang B version 1 và replay cùng key/body','version 2; A giảm 1, B tăng 1 đúng một lần'),
 ('định mức synthetic 40000đ, tổ hợp 40001đ','gửi chọn tổ hợp','422 ERR-ORD-422-01; lựa chọn/counter không đổi'),
 ('định mức synthetic 40000đ, tổ hợp đúng 40000đ và đủ cơ cấu','gửi chọn trước hạn với version hiện tại','được nhận; không yêu cầu người ăn bù tiền')),
('Gửi lựa chọn cả tuần','018','meal_selections; delta weekly submission receipt','07',
 ('tài khoản có 5 ngày công bố còn mở, ORD-Q05 đã chốt','gửi lựa chọn tuần kèm version từng ngày','trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt'),
 ('guest QR chỉ có phạm vi ngày','gửi lựa chọn tuần','403 ERR-ORD-403-01; không ghi ngày nào'),
 ('4 ngày hợp lệ và 1 ngày đã khóa','gửi tuần','không báo thành công toàn tuần; atomic rollback hoặc partial receipt chờ ORD-Q05')),
('Chốt tổng suất và phân bổ','003,004,019','orders,order_dish_lines,selection_counters','08',
 ('synthetic S=60,C=10,T=100 và ORD-Q06 đã duyệt','gửi tổng','SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa'),
 ('synthetic S=60,C=10,T=65','gửi tổng','đề xuất 422 ERR-ORD-422-02; không xóa 5 lựa chọn; chờ ORD-Q06'),
 ('synthetic S=60,C=10,T=70','gửi tổng rồi khóa đủ điều kiện','D=0; không tạo dòng default ảo')),
('Gán món mặc định khi khóa','PORT-LOCK','order_revisions,order_revision_lines (delta)','09',
 ('synthetic T=100,S=60,C=10; default A hợp lệ','scheduler khóa','D=30 cho A; MAIN tổng 100; không tạo 30 eater giả'),
 ('default không thuộc MAIN ngày công bố','scheduler khóa','422 ERR-ORD-422-03; không phát hành kế hoạch'),
 ('chưa có total; có 100 người đăng ký','scheduler khóa','total vẫn chưa xác định; không tự coi T=100; xử lý ORD-Q07')),
('Khóa tại hạn và phát hành nguồn kế hoạch','PORT-LOCK,020','orders,order_revisions,production_plan_revisions (delta)','09',
 ('đã gửi tổng và đủ snapshot, deadline cấu hình hợp lệ','scheduler khóa scope điểm/ngày/ca','order LOCKED; một revision và một outbox event bền vững'),
 ('clock server đúng bằng deadline','người ăn gửi PUT','đề xuất 409 ERR-ORD-409-01; không ghi; biên deadline chờ ORD-Q07'),
 ('lock event đã xử lý, worker mất phản hồi','retry cùng eventKey','trả revision cũ; không tăng plan revision lần hai')),
('Đề nghị và duyệt thay đổi sau khóa','005,021,022','order_change_requests,order_revisions,approvals (delta/existing)','10',
 ('order LOCKED rev1; ngưỡng và người duyệt đã chốt','người khác người tạo/sửa cuối duyệt delta hợp lệ','tạo rev2, giữ rev1; bếp nhận delta có nguồn rev2'),
 ('đề nghị PENDING do U tạo','U tự duyệt','403 ERR-ORD-403-01; order vẫn rev1'),
 ('đề nghị dựa rev1 nhưng hiện hành rev2','duyệt đề nghị cũ','409 ERR-ORD-409-01; không áp delta lên sai baseline')),
('Điều phối nhập hộ','003,004','orders,order_dish_lines,files,audit_logs','11',
 ('DDV được giao A có chứng cứ synthetic điện thoại','nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason','order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân'),
 ('người ăn tự chọn có phiên hợp lệ','gửi source ZALO để giả vai DDV','403 ERR-ORD-403-01; không ghi order'),
 ('người đặt tổng và DDV cùng đọc version 1','cả hai gửi tổng','một commit version 2; bên sau 409; không ghi đè mù')),
('Nhắc người chưa chọn','PORT-REM,023','notifications; delta outbox/dedupe','09',
 ('kênh đã được duyệt, người nhận có định danh và còn đủ điều kiện','scheduler lập nhắc trước hạn','chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi'),
 ('Q-14 chưa chốt hoặc thiếu cấu hình kênh','job nhắc chạy','BLOCKED_CONFIGURATION; không gọi SMS/Zalo/email'),
 ('event nhắc đã thành công','worker nhận lại eventId','không gửi lần hai; đối soát kết quả không tạo thông báo trùng')),
('Đổi chế độ chọn món','024','customers; delta choice_mode_versions','05',
 ('khách chưa có lựa chọn và policy ngày hiệu lực đã duyệt','người đặt tổng tắt chọn món','người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền'),
 ('khách đã tắt chọn từ đầu ngày','người ăn PUT trực tiếp','409 ERR-ORD-409-01; không thay số suất'),
 ('đã có 60 lựa chọn','đề nghị tắt giữa ngày','giữ 60 lựa chọn và lịch sử; tác động chờ ORD-Q09')),
('Xem thông tin món công bố','001','menu_day_items,recipes,dish_allergens,nutrition_calculations','06',
 ('món thuộc menu PUBLISHED có nguồn dinh dưỡng đủ','người ăn mở chi tiết','hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính'),
 ('thiếu dữ liệu dinh dưỡng một nguyên liệu','mở tổ hợp','totals=null và lý do thiếu; không hiển thị 0 như kết quả thật'),
 ('client dò field cost và id khách khác','gọi available-meals','DTO chỉ allowlist; ngoài scope 404; lỗi không lộ cost/giá nhập')),
('Giữ cổng hồ sơ sức khỏe','GATE-046','eater_health_profiles tồn tại nhưng gated','12',
 ('O-03 còn mở','người dùng mở hồ sơ','thấy chưa mở tính năng; không có form hoặc request thu sức khỏe'),
 ('client cố gửi bệnh lý khi gate đóng','gọi đường ghi chưa công bố','không ghi dữ liệu; không tạo consent ngầm; contract chưa mở'),
 ('người dùng không đồng ý hoặc rút đồng ý trong thiết kế tương lai','review hồ sơ','chưa được thu thập; tiêu chí xóa/lưu vết cần O-03 và ORD-Q15')),
('Giữ cổng gợi ý cá nhân','GATE-047','không thêm dữ liệu hồ sơ/gợi ý','12',
 ('O-03 còn mở','người ăn mở gợi ý','tính năng chưa mở; chọn món thủ công vẫn có theo quyền'),
 ('không có consent/hồ sơ hợp lệ','yêu cầu suy bệnh từ lịch sử chọn','không suy diễn và không tự tạo hồ sơ'),
 ('gợi ý tương lai được duyệt','review hành vi áp dụng','phải có lựa chọn tường minh; không tự ghi selection hoặc đổi order')),
('Đọc kế hoạch sản xuất phiên bản','020,025','production_plan_revisions,order_revisions (delta)','13',
 ('2 order khóa cùng bếp/ca, MAIN A lần lượt 60 và 40','worker tổng hợp và bếp đọc kế hoạch','A=100; hiện source revision từng order, plan revision và thời điểm'),
 ('bếp K1 yêu cầu kế hoạch K2','GET theo id K2','404 ERR-ORD-404-01; không lộ tổng K2'),
 ('một nguồn đổi rev1 sang rev2 tăng A 5 suất','tạo kế hoạch kế tiếp','A tăng 5 đúng một lần; plan cũ bất biến; không cộng cả hai source revisions')),
]
assert len(rows)==len(cases)==19
rtm='Mỗi dòng là liên kết tài liệu, không chứng minh tính năng hoàn tất. 17 capability có thiết kế luồng có điều kiện; 2 capability chỉ đặc tả gate O-03. P1 không tự được đưa lên P0.\n\n| Feature / ưu tiên | FR | UC | API / port / gate | Data | UI | Story | AC | Test | Gate |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n'
ac='Mọi số liệu ví dụ là **synthetic**. Với nghiệp vụ còn mở, Then là **kỳ vọng đề xuất để review**, không phải quyết định đã duyệt. AC của FEAT-046/047 chỉ kiểm gate; happy path nghiệp vụ sức khỏe vẫn BLOCKED O-03.\n'
tests='Giữ nguyên [10 ca khởi đầu](test-cases.md). Bộ dưới đây bổ sung 57 ca liên kết AC; không cộng 10 ca cũ thành độ phủ độc lập vì có mục tiêu trùng. **Actual/Evidence: chưa có cho tất cả ca. Không ca nào PASS phần mềm.**\n\nQuy trình mỗi ca: (1) tạo fixture synthetic theo Given trong môi trường test; (2) đăng nhập đúng actor UC và ghi version ban đầu; (3) gọi API/port ghi trong UC với hành động When; (4) kiểm HTTP/DTO/UI và đọc lại resource/counter/audit/snapshot theo Then; (5) lưu requestId, trước/sau, log và actual. Ca gate chỉ kiểm không phát sinh request/ghi; không thử thu sức khỏe thật.\n'
scope='Nguồn: [PRD](../../gia-phat/01-prd.md), [roadmap](../../gia-phat/02-roadmap.md), [D-03/04/14/19/21](../../gia-phat/00-ke-hoach-tong-the.md). **14 P0 + 5 P1**, giữ nguyên 19 capability gốc. Đủ căn cứ để viết hành vi không đồng nghĩa đủ căn cứ để build trọn tính năng.\n\n| Feature | FR | Ưu tiên | Đủ căn cứ / phần tiếp tục | Chặn / điều kiện |\n| :--- | :--- | :--- | :--- | :--- |\n'
index='Các UC là đặc tả review có điều kiện; không gắn nhãn ready khi gate chưa chốt.\n\n'
for i,(r,c) in enumerate(zip(rows,cases),1):
 fr,feat,actor,inp,logic,out,gate=r; title,api,data,screen,h,n,e=c
 num=f'{i:03}'; uc=f'UC-ORD-{num}'; us=f'US-E6-{num}'
 apis=', '.join('API-ORD-'+a if a.isdigit() else a for a in api.split(','))
 acids=[f'AC-E6-{num}-{j}' for j in range(1,4)]; tcids=[f'TC-E6-{num}-{j}' for j in range(1,4)]
 scope+=f'| {feat.split(" / ")[0]} | {fr} | {feat.split(" / ")[1]} | {title}: {out} | {gate}; '+('GATED toàn nghiệp vụ' if i in (17,18) else 'PARTIAL (thiết kế có điều kiện)')+' |\n'
 rtm+=f'| {feat} | {fr} | [{uc}](../usecases/{uc}.md) | {apis} | {data} | [UI-ORD-{screen}](../ui/screen-catalog.md) | {us} | '+', '.join(acids)+' | '+', '.join(tcids)+f' | {gate} |\n'
 ucbody=f'''- **ID / mức:** {uc} / {'Fish (kiểm cổng)' if i in (17,18) else 'Sea (mục tiêu nghiệp vụ)'}.
- **Truy vết:** {feat}; {fr}; {us}; {apis}; UI-ORD-{screen}.
- **Actor chính:** {actor.split(';')[-1].strip()}. Actor hỗ trợ: AUTH/SYS kiểm quyền/audit; MENU cung cấp bản công bố; các port trong API.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** {h[1]}.
- **Tiền điều kiện:** {h[0]}. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào {gate}; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** {h[2]}.

## Luồng chính

1. Actor mở UI-ORD-{screen}; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: {inp}.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: {logic}
4. Hệ thống thực hiện {h[1]}; kết quả theo điều kiện review: {h[2]}.
5. Hệ thống trả {out}; UI chỉ báo đã ghi khi có biên nhận. Với thao tác đọc/gate không phát sinh mutation; với ghi lưu audit cùng giao dịch.

## Nhánh rẽ và ngoại lệ

- **2a. Đầu vào/quyền nghiệp vụ:** Given {n[0]}; When {n[1]}; Then {n[2]}.
- **3a. Biên/đồng thời:** Given {e[0]}; When {e[1]}; Then {e[2]}.
- **3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a. Mất phản hồi:** không khẳng định thất bại hay tự đổi key; đọc biên nhận/resource trước retry cùng key. Gate O-03 không có write contract để retry.
- **4b. Version đổi:** ERR-ORD-409-01; tải lại, hiển thị khác biệt, người dùng quyết định gửi lại. Không tự ghi đè.
- **4c. Phụ thuộc gián đoạn:** ERR-ORD-503-01; không báo thành công khi chưa có commit; đối soát bằng requestId.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: {data}. Bộ ba AC: {', '.join(acids)}; test: {', '.join(tcids)}. Gate {gate} giữ CHỜ XÁC NHẬN.
'''
 write(f'usecases/{uc}.md',f'{uc}: {title}',ucbody)
 index+=f'- [{uc}: {title}](../usecases/{uc}.md): {fr}.\n'
 ac+=f'\n## {us}: {title}\n\n{fr}; {feat}; gate {gate}.\n'
 tests+=f'\n## {us} / {uc}\n\nAPI/port: {apis}; UI-ORD-{screen}. Priority {feat.split(" / ")[1]}.\n\n| TC / AC | Given (fixture / tiền điều kiện) | When (thao tác) | Then (expected) | Status |\n| :--- | :--- | :--- | :--- | :--- |\n'
 for j,(label,s) in enumerate(zip(['Thành công có điều kiện / gate','Lỗi nghiệp vụ','Biên và bảo mật'],[h,n,e]),1):
  ac+=f'\n### {acids[j-1]}: {label}\n\n```gherkin\nScenario: {title} ({label})\n  Given {s[0]}\n  When {s[1]}\n  Then {s[2]}\n```\n'
  status='BLOCKED '+gate if j==1 and i not in (16,17,18) or 'chờ' in s[2] or 'ORD-Q' in s[2] or i in (17,18) and j==3 else 'NOT RUN'
  tests+=f'| {tcids[j-1]} / {acids[j-1]} | {s[0]} | {s[1]} | {s[2]} | {status} |\n'
write('review/scope-assessment.md','Đối chiếu phạm vi FEAT-030–048',scope+'''\n## Ngoài phạm vi phiên này

E7 giao/nhận/doanh thu/đối soát/MISA; E8 website công khai (chỉ dùng lại DTO món); E9 agent phía khách; E10 CRM đầy đủ; E11 mua nguyên liệu/phân ca/QC; E12–E13 báo cáo/lợi nhuận. Không triển khai backend, migration, provider thông báo hay thuật toán sức khỏe. ORD-Q10 không tự mở nhiều MAIN trong R6 khi D-04 đang là cơ sở luồng chọn 1/3.

G-Now vẫn là cổng release; việc viết trước tài liệu không chứng minh đã vượt cổng. Không đổi lịch/ước lượng O-04.
''')
write('srs/usecase-diagram.md','Chỉ mục và sơ đồ use case E6',index+'''
```mermaid
flowchart LR
  E[Người ăn tài khoản] --> CH[Chọn ngày và xem món]
  Q[Người ăn QR] --> CH
  E --> W[Chọn tuần P1]
  C[Người đặt tổng] --> T[QR - định mức - tổng suất]
  D[DDV] --> P[Phục vụ và nhập hộ]
  J[Scheduler] --> L[Mặc định và khóa]
  L --> B[Kế hoạch có phiên bản]
  K[Bếp theo cơ sở] --> B
  C --> R[Đề nghị đổi]
  A[Người duyệt chờ O-06] --> R
  E -. O-03 đóng .-> H[Hồ sơ và gợi ý chưa mở]
```
''')
write('userstories/acceptance-criteria.md','57 AC Given / When / Then E6',ac)
write('test/review-test-cases.md','57 ca thiết kế liên kết AC E6',tests)
write('test/traceability.md','Ma trận truy vết E6',rtm)
(B/'validation/capability-map.json').write_text(json.dumps([{'feature':r[1].split(' / ')[0],'priority':r[1].split(' / ')[1],'fr':r[0],'uc':f'UC-ORD-{i:03}','story':f'US-E6-{i:03}','api':c[1],'screen':'UI-ORD-'+c[3],'gate':r[6]} for i,(r,c) in enumerate(zip(rows,cases),1)],ensure_ascii=False,indent=2),encoding='utf-8')
