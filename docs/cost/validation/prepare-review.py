"""Build a review register and synthetic fixtures; never marks business decisions approved."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
def save(p,s):
    path=B/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(s,encoding='utf-8')
def dump(p,d):save(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
catalog=json.loads((B/'test/scenario-catalog.json').read_text(encoding='utf-8'))
decisions={}
for source in ['srs/spec.md','ui/user-flow.md']:
    source_text=(B/source).read_text(encoding='utf-8')
    if source=='srs/spec.md': source_text=source_text.split('### 4.4 Điểm mở',1)[1].split('### 4.6',1)[0]
    for line in source_text.splitlines():
        cells=[x.strip() for x in line.strip('|').split('|')]
        if not cells or not re.fullmatch(r'(?:O-01|E[23]-Q\d+|DL-01|FLOW-COST-Q\d+)',cells[0]):continue
        code=cells[0]
        if code in decisions:continue
        # These rows are the open-questions tables, not FR tables.
        if code.startswith('FLOW-'): question,owner,current=cells[1],cells[3],cells[4]
        elif code in ['E3-Q14','E3-Q15','E3-Q16']:question,current,owner=cells[1:4]
        else:question,owner,current=cells[1:4]
        decisions[code]=dict(id=code,question=question,owner=owner,current=current,source=source,status='OPEN',decision=None,approvedBy=None,approvedAt=None)
for code,question,owner,current,source in [
 ('O-06','Ai duyệt và ai thay khi vắng?','Giám đốc','Giữ phân tách người tạo/người sửa cuối và người duyệt','../nen-tang/srs/spec.md'),
 ('E2-Q5','Nguồn khoảng định lượng chuẩn và mức chất độn?','Dinh dưỡng viên, Giám đốc','Test dùng ngưỡng fixture, chưa làm cấu hình thật','../thuc-don-dinh-luong/srs/spec.md'),
 ('QA-COST-Q01','NCC tồn tại INACTIVE trả 404-01 hay 422-02?','BA, Tech lead','Cả hai mô tả trùng điều kiện, chưa đổi mã lỗi','validation/backlog-report.md')]:
    decisions[code]=dict(id=code,question=question,owner=owner,current=current,source=source,status='OPEN',decision=None,approvedBy=None,approvedAt=None)
proposals={
 'O-01':('Chốt riêng VAT bán ra, thành phần cost, khoản khoán và cách hiểu giá nhập; yêu cầu bảng kế toán làm nguồn.','Không lấy VAT8% của mẫu làm mặc định; thiếu VAT vẫn chặn tính%.','SRS3.3, params SYS, seed dữ liệu, fixture kế toán'),
 'E3-Q1':('Cân nhắc DAT_NHAT giai đoạn đầu; so với BINH_QUAN/MAC_DINH trên10 ngày thực tế trước khi chọn.','DAT_NHAT thận trọng nhưng có thể cao hơn cơ cấu chọn thực tế.','BR-CALC-004, tham số, AC-COST-015-04'),
 'E3-Q2':('Xác nhận định lượng sống là trước hay sau loại xương/vỏ; chỉ áp hao hụt một lần.','Áp hai lần sẽ tăng lượng mua sai; tắt hao hụt khi định lượng đã bao gồm phần bỏ.','SRS3.3.1/3.3.4 và dữ liệu công thức'),
 'E3-Q14':('Giữ giá đã hiệu lực bất biến, chỉ đổi tham chiếu tương lai; nếu cần hồi tố phải thiết kế nghiệp vụ riêng.','Dễ kiểm toán nhưng kế toán không sửa cờ lịch sử trực tiếp.','BR-PRC-004/005, API-COST-008, UC-COST-002'),
 'E3-Q15':('R3 giới hạn K=1; chỉ mở K>1 khi xác nhận tổng lượt chọn chia hết K và cách xử lý phần dư.','Giảm rủi ro suy ra sai số suất; hạn chế loại suất nhiều món chính.','BR-EST-001, API EstimateInput, TC-COST-022-04'),
 'E3-Q16':('Cân nhắc cùng món/cỡ/cơ sở, ngày lập đến ngày phục vụ <=N ngày; chốt riêng công thức đổi có làm hết hiệu lực không.','Không tái dùng bảng khác cơ sở nếu chưa có quy tắc; tăng số bảng cần duyệt.','BR-CALC-007, bộ lọc bảng, test89/90/91ngày'),
 'FLOW-COST-Q01':('Yêu cầu chọn giá thay thế trong cùng giao dịch hủy, nếu còn báo giá khác cùng nhóm.','Không tự chọn NCC; lỗi ở một bước rollback cả hai thay đổi.','API hủy/tham chiếu, unique constraint, UC-COST-002'),
 'FLOW-COST-Q02':('Review phương án API hiện có: key/hash theo actor/method/path, TTL24h, đối soát, commit nguyên tử.','Cần kho bền vững và migration; retry không được vượt quyền hiện tại.','API mục2/7, schema request store, test concurrency'),
 'FLOW-COST-Q03':('Tạo thiết kế cảnh báo nguyên liệu riêng, không dùng cost_alerts bắt buộc menu_day_id.','Chốt khóa chống trùng theo nguyên liệu hay nguyên liệu/cơ sở trước thiết kế bảng.','SRS PRC009, schema, worker giá cũ, thông báo NCC ngừng'),
 'FLOW-COST-Q04':('Hiện dấu — và ghi Không áp dụng khi mẫu số0; giữ delta tiền nếu tính được.','Không trả Infinity/NaN, không biến delta% thành0 gây hiểu nhầm.','API Decimal nullable, bảng phân rã/so sánh, AC'),
 'FLOW-COST-Q05':('Xác nhận ma trận đọc danh mục quản trị riêng với quyền xem khoản trong phân rã cost.','Cần phân biệt số liệu người xem cost được biết với quyền xem đề nghị quản trị.','SRS2.2, API khoản khoán, wireframe11'),
 'FLOW-COST-Q06':('Cân nhắc kiểm lại tại duyệt cuối; nếu đủ điều kiện thì chụp bộ vừa kiểm cùng transaction.','Khi mới vượt ở CHAN cần trả lại hoặc giữ PENDING? phải chốt trạng thái; không tự chuyển.','MENU/SRS Cost, transaction approve, snapshot, TC-COST-018-02'),
 'FLOW-COST-Q07':('Cân nhắc all-or-nothing cho cả batch tuần; trả lỗi theo ngày, không ghi ngày hợp lệ khi có lỗi.','Dễ đối soát/retry nhưng phải sửa mọi ngày lỗi trước khi có kết quả tuần.','API batch success/error, transaction, version/batch key, UC012'),
 'FLOW-COST-Q08':('Tách hai tình huống: vốn vượt khi duyệt và phục hồi rồi vượt lại; xác định có mở cảnh báo mới hay cập nhật lịch sử.','Không dùng mức tăng tùy ý để phát thông báo; cần tránh lặp cảnh báo đang mở.','SRS ALR001/002, state/worker và test P1'),
 'FLOW-COST-Q09':('Cân nhắc KHONG_XAC_DINH ưu tiên khi bất kỳ ngày/cơ sở không tính được, kể cả thiếu VAT.','Tránh kết luận toàn bộ đã đánh giá, nhưng che mất một vi phạm đã chắc chắn; PO phải chọn.','BR-CALC-011, budget contract, quota/log, TC-COST-021-04'),
 'FLOW-COST-Q10':('Giữ P2; chốt vai trò, phạm vi cơ sở, trạng thái thực đơn và cửa sổ ngày trước khi mở.','Không tăng phạm vi R3 để hoàn tất một màn mẫu.','API simulation, role matrix, US-COST-028'),
 'QA-COST-Q01':('Cân nhắc422-02 khi NCC tồn tại nhưng INACTIVE;404-01 chỉ tham chiếu không tồn tại hoặc nguyên liệu không dùng.','Phải sửa câu chữ404-01 và đồng bộ các client; ngoài phạm vi vẫn dùng404 theo SYS.','SRS ma trận lỗi, API và TC-COST-002-06')
}
for code,d in decisions.items():
    d['proposal'],d['tradeoff'],d['updateTargets']=proposals.get(code,('Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.','Chưa có bằng chứng để tự quyết thay nghiệp vụ.','SRS, use case, API và AC bị ảnh hưởng'))
    d['explicitBlockedTests']=[c['tc'] for s in catalog['stories'] for c in s['cases'] if code in re.findall(r'(?:FLOW-COST-Q\d+|QA-COST-Q\d+|E[23]-Q\d+|O-\d+|DL-\d+)',c['gate'])]
decisions['O-01']['status']='PARTIALLY_CONFIRMED'
decisions['O-01']['confirmedFacts']='Người dùng xác nhận 11/11/2026: cost nguyên liệu gồm VAT phải trả; khách không lấy VAT là không yêu cầu hóa đơn. Chi tiết ACC-CONF-01 đến05 tại accounting/business-rules.md. VAT cụ thể/thành phần khoán/cơ sở doanh thu còn mở.'
dump('review/decision-register.json',list(decisions.values()))
head='Phiên bản 0.1.0 · 11/11/2026 · Draft; O-01 được xác nhận một phần trong phiên, các chi tiết còn lại chờ review.\n\n'
md='# Sổ quyết định cần review Cost\n\n'+head+'''Mỗi dòng giữ nguyên mã điểm mở của nguồn. Phương án dưới đây là đề xuất thảo luận, không sửa SRS, không cấu hình hệ thống và không thay chữ ký chủ sở hữu. Danh sách test chỉ lấy mã xuất hiện trực tiếp trong gate, không phải toàn bộ tác động gián tiếp. Không cộng số test giữa các điểm vì một ca có thể phụ thuộc nhiều quyết định.

Thứ tự phiên review đề xuất: (1) kế toán/Giám đốc chốt O-01, E3-Q1/Q2/Q4/Q14/Q15/Q16; (2) BA/Tech lead chốt FLOW-Q01–Q07 và QA-Q01; (3) xử lý agent/P1/P2 theo release. Mốc ngày họp, tên người phụ trách cụ thể và thời hạn chưa được ấn định.

| Mã | Câu hỏi | Chủ sở hữu theo tài liệu | Trạng thái |
| :--- | :--- | :--- | :--- |
'''
for d in decisions.values():md+=f"| [{d['id']}](#{d['id'].lower()}) | {d['question']} | {d['owner']} | {d['status']} |\n"
for d in decisions.values():
    md+=f"\n<a id=\"{d['id'].lower()}\"></a>\n\n## {d['id']}\n\n- Nguồn: [{d['source']}](../{d['source']}).\n- Thông tin xác nhận bổ sung: {d.get('confirmedFacts','Chưa có xác nhận mới trong đợt kế toán')}.\n- Hiện tại theo nguồn: {d['current']}\n- Đề xuất để review: {d['proposal']}\n- Đánh đổi/cần làm rõ: {d['tradeoff']}\n- Sau quyết định phải cập nhật: {d['updateTargets']}.\n- Test bị chặn có gate nêu đích danh: {', '.join(d['explicitBlockedTests']) or 'Không nêu trực tiếp; vẫn kiểm tác động theo story/FR nguồn'}.\n- Quyết định / người duyệt / ngày / bằng chứng: **Chưa có / Chưa có / Chưa có / Chưa có**.\n"
save('review/decision-register.md',md)
blocked='# Danh sách điều kiện mở khóa test\n\n'+head+'Mọi ca vẫn giữ BLOCKED trong catalog; tài liệu này chỉ giúp phân công. Nhóm người xử lý là đề xuất phân công, không phải giao việc đã gửi.\n\n| Test | Điều kiện đang thiếu | Nhóm xử lý đề xuất | Bằng chứng để mở khóa |\n| :--- | :--- | :--- | :--- |\n'
for s in catalog['stories']:
    for c in s['cases']:
        if not c['status'].startswith('BLOCKED'):continue
        g=c['gate']
        owner='BA và chủ sở hữu trong sổ quyết định';evidence='Quyết định có người/ngày/nguồn; cập nhật expected và review AC'
        if 'môi trường backend' in g:owner='Tech lead, QA';evidence='Build/URL môi trường, tài khoản test, seed/reset và cấu hình tải'
        elif 'dữ liệu kế toán' in g:owner='Kế toán, BA';evidence='10 món/10 ngày thực tế có nguồn giá/công thức/params và xác nhận kế toán'
        elif 'review API' in g:owner='Tech lead, BA';evidence='Hợp đồng và mã lỗi được review; thiết kế migration/concurrency nhất quán'
        blocked+=f"| {c['tc']} | {g} | {owner} | {evidence} |\n"
save('review/blocked-tests.md',blocked)

def line(q,price,factor='1000',waste='0',include=True):return dict(qty=q,priceVnd=price,conversionFactor=factor,wastePct=waste,includeInCost=include)
dishes=[]
def dish(name,lines,expected,waste=False):dishes.append(dict(id=f'MOCK-DISH-{len(dishes)+1:02}',name=name,date='2026-11-16',kitchenId='A',applyWaste=waste,lines=lines,expectedExactCost=expected))
dish('Thịt và trứng mẫu',[line('70','120000'),line('3','800','1')],'10800')
dish('Thịt đơn mẫu',[line('70','120000')],'8400')
dish('Thịt hao hụt20% mẫu',[line('70','120000',waste='20')],'10500',True)
dish('Nước không tính cost mẫu',[line('70','120000'),line('100','0',include=False)],'8400')
dish('Phần lẻ ba dòng mẫu',[line('0.4','1','1') for _ in range(3)],'1.2')
dish('Không có thành phần tính cost',[line('100','0',include=False)],'0')
dish('Định lượng80g mẫu',[line('80','120000')],'9600')
dish('Giá cơ sở B mẫu',[line('70','126000')],'8820');dishes[-1]['kitchenId']='B'
dish('Trứng mẫu',[line('3','800','1')],'2400')
dish('Hải sản hao hụt20% mẫu',[line('100','100000',waste='20')],'12500',True)
days=[]
def day(main,method,k,other,allowance,price,vat,total,pct,result,default=0,kitchen='A'):
    i=len(days)+1;days.append(dict(id=f'MOCK-DAY-{i:02}',date=f'2026-11-{15+i:02}',kitchenId=kitchen,mainCosts=main,method=method,mainPick=k,defaultIndex=default,otherCost=other,allowance=allowance,mealPrice=price,vatPct=vat,thresholdPct='52',expectedCost=total,expectedPct=pct,expectedResult=result))
day(['10800'],'DAT_NHAT',1,'6500','1500','40000','8','18800','50.76','DAT')
day(['13000'],'DAT_NHAT',1,'6500','1500','40000','8','21000','56.70','KHONG_DAT')
day(['12000'],'DAT_NHAT',1,'6500','1500','40000','0','20000','50.00','DAT')
day(['52004'],'DAT_NHAT',1,'0','0','100000','0','52004','52.00','DAT')
day(['52005'],'DAT_NHAT',1,'0','0','100000','0','52005','52.01','KHONG_DAT')
day(['8000','10000','12000'],'DAT_NHAT',2,'6500','1500','80000','0','32000','40.00','DAT')
day(['8000','10000','12000'],'BINH_QUAN',2,'6500','1500','80000','0','28000','35.00','DAT')
day(['8000','10000','12000'],'MAC_DINH',2,'6500','1500','80000','0','24000','30.00','DAT')
day(['0'],'DAT_NHAT',1,'0','0','40000','8','0','0.00','DAT')
day(['13000'],'DAT_NHAT',1,'6500','1500','40000','8','21000','56.70','KHONG_DAT',kitchen='B')
dump('test/fixtures/synthetic-cost.json',dict(version='0.1.0',status='SYNTHETIC_NOT_ACCOUNTANT_APPROVED',description='Cost main inputs in days are supplied fixture numbers, not references to dishes or real menus. No price selection/approval workflow is implemented here.',dishes=dishes,days=days))
table='# Bộ số liệu đối soát giả định\n\n'+head+'''**Không phải dữ liệu Gia Phát, chưa có kế toán xác nhận.** 10 món minh họa công thức định lượng × đơn giá, chuyển đơn vị và hao hụt; 10 ngày dùng cost món chính đầu vào độc lập để kiểm cách gộp, VAT và làm tròn. Đây không phải 10 thực đơn hoàn chỉnh hay seed database, không kiểm chọn giá theo ngày, chọn công thức, duyệt, RBAC hoặc engine production.

JSON lưu số tiền/định lượng dạng chuỗi decimal; expected được nhập tường minh để so với phép tính. [Script kiểm](../../validation/check-reconciliation.py) dùng Decimal và chỉ kiểm công thức mẫu. Thay bằng dữ liệu thật phải giữ bản nguồn, ghi VAT/cơ sở/ngày/giá và người xác nhận; không sửa file này thành bằng chứng NFR-COST-002 đã đạt.

| Món mẫu | Tên | Cost chính xác kỳ vọng (đ) |
| :--- | :--- | ---: |
'''
for d in dishes:table+=f"| {d['id']} | {d['name']} | {d['expectedExactCost']} |\n"
table+='\n| Ngày mẫu | Cơ sở | Cách tính | Cost suất (đ) | VAT% | Cost% sau làm tròn | Kết quả |\n| :--- | :--- | :--- | ---: | ---: | ---: | :--- |\n'
for d in days:table+=f"| {d['date']} | {d['kitchenId']} | {d['method']} | {d['expectedCost']} | {d['vatPct']} | {d['expectedPct']} | {d['expectedResult']} |\n"
table+='\nNgưỡng52% trong fixture; dữ liệu K=2 chỉ kiểm công thức BR-CALC-004, không quyết định mở dự toán K>1 đang chờ E3-Q15. Cost0 không kiểm cách hiển thị tỷ trọng đang chờ Q04. Bộ thực tế cho NFR-COST-002 vẫn chưa có.\n'
save('test/fixtures/README.md',table)
print(f'{len(decisions)} review items (O-01 partially confirmed); 46 blocked-test rows expected from catalog; 10 synthetic dishes + 10 synthetic days')
