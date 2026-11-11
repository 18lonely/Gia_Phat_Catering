"""Rebuild the Cost review package from explicit BA scenarios, not runtime tests."""
from pathlib import Path
import re, json

BASE=Path(__file__).resolve().parents[1]
stories=[]
def story(title,actor,goal,value,fr,uc,priority,points,gates='—'):
    stories.append(dict(id=f'US-COST-{len(stories)+1:03}',title=title,actor=actor,goal=goal,value=value,fr=['FR-COST-'+x for x in fr.split()],uc=uc,priority=priority,points=points,gates=gates,cases=[]))
def case(title,given,when,then,refs='',gate='—',kind='Functional'):
    stories[-1]['cases'].append(dict(title=title,given=given,when=when,then=then,refs=refs.split(),gate=gate,kind=kind))

story('Danh mục nhà cung cấp','kế toán mua hàng','tạo, sửa, tìm và ngừng nhà cung cấp','quản lý nguồn giá mà vẫn giữ lịch sử','SUP-001 SUP-002 SUP-003','001','P0',3,'FLOW-COST-Q03')
case('Tạo, sửa và lọc NCC','KT có quyền ghi; chưa có NCC An Bình','tạo An Bình loại REGULAR; sửa điện thoại; lọc tên An Bình, loại REGULAR và ACTIVE','có đúng một NCC ACTIVE với điện thoại mới, lịch sử ghi người thao tác và nội dung thay đổi','BR-PRC-001')
case('Tên trùng sau chuẩn hóa','đã có NCC An Bình chưa huỷ','tạo NCC có tên "  AN   BÌNH  "','HTTP 409 ERR-COST-409-01; không thêm NCC','BR-PRC-001 BR-CAT-001 ERR-COST-409-01')
case('Ngừng không xóa giá cũ','NCC An Bình có giá tham chiếu 120000 ngày 10/11/2026','ngừng NCC với lý do "Không tiếp tục mua hàng"; tính giá tại 10/11; thử nhập giá mới','giá lịch sử vẫn dùng; giá mới bị từ chối; cảnh báo tham chiếu đang dùng được ghi nhận theo thiết kế Q03','BR-PRC-007 ERR-COST-422-02','FLOW-COST-Q03')

story('Nhập giá nguyên liệu','kế toán mua hàng','thêm giá trên đơn vị mua và ngày hiệu lực','có dữ liệu giá truy vết được','PRC-001','002','P0',3,'E3-Q13; E3-Q6')
case('Giá đầu tiên','nguyên liệu I1 và NCC S1 ACTIVE; chưa có giá; ngày hệ thống 11/11/2026','nhập I1/S1/A giá 120000 ngày 11/11','tạo một dòng giá, tự đánh dấu tham chiếu, ghi audit; không có bước duyệt giá thứ hai trong thiết kế hiện tại','BR-PRC-002 BR-PRC-005')
case('Giá không hợp lệ','I1/S1 ACTIVE','lần lượt nhập giá 0, -1, 1.5; mỗi lần dùng khóa yêu cầu mới','mỗi lần HTTP 422 ERR-COST-422-01; không tạo dòng','BR-PRC-002 ERR-COST-422-01')
case('Biên ngày và khóa trùng','hôm nay 11/11/2026; hồi tố cấu hình 7 ngày','nhập từng bản độc lập tại 04/11, 11/12 rồi tại 03/11, 12/12; gửi lại tuple I1/S1/A/ngày đã tồn tại bằng khóa mới','hai ngày biên hợp lệ; hai ngày ngoài biên trả ERR-COST-422-02; tuple trùng trả ERR-COST-409-02','BR-PRC-003 BR-PRC-005 ERR-COST-422-02 ERR-COST-409-02','E3-Q13','Boundary')
case('Tham chiếu không tồn tại','không có nguyên liệu I999','nhập giá cho I999 hoặc NCC không tồn tại','HTTP 404 ERR-COST-404-01; không tạo giá','ERR-COST-404-01')

story('Chọn và tra giá tham chiếu','kế toán mua hàng','chọn giá và tra theo ngày, cơ sở','tính cost theo đúng nguồn giá','PRC-002 PRC-003','002','P0',3,'E3-Q4; E3-Q14; FLOW-COST-Q01')
case('Ưu tiên giá cơ sở','I1 có giá chung 100000 ngày 10/11 và giá A 120000 ngày 01/11; không có giá B','tra I1 tại 11/11 cho A và B','A nhận 120000 dù giá chung mới hơn; B nhận 100000 kèm NCC/ngày giá','BR-PRC-006 BR-COST-004')
case('Không dùng giá tương lai','I2 chỉ có giá hiệu lực 16/11','tra I2 ngày 11/11','HTTP 404 ERR-COST-404-02; không dùng giá tương lai','BR-PRC-006 ERR-COST-404-02')
case('Chuyển cờ trong cùng nhóm tương lai','hai giá I1/A/16-11 thuộc hai NCC; chỉ giá thứ nhất tham chiếu','chọn giá thứ hai làm tham chiếu; tra I1/A/16-11','chỉ giá thứ hai còn cờ trong nhóm; giá nhóm ngày/cơ sở khác giữ nguyên; đổi cờ giá đã hiệu lực chờ quyết định riêng','BR-PRC-005','E3-Q4; E3-Q14','Boundary')

story('Nhập lưới nguyên tử','kế toán mua hàng','lưu nhiều giá trong một lượt','giảm thao tác mà không ghi dở dang','PRC-004','003','P0',3)
case('Bỏ qua dòng không đổi','lưới có hai nguyên liệu; I1=100000, I2=20000','lọc nhóm/bảo quản/đang dùng; đổi I1 thành 110000, giữ I2; lưu ngày hợp lệ','tạo đúng một giá I1; I2 không thêm lịch sử')
case('Một dòng sai rollback','lô có I1 giá 110000 và I2 giá 0','lưu lô; kiểm số giá trước/sau','báo ERR-COST-422-01 gắn dòng I2; không tạo giá I1 hoặc I2','BR-PRC-002 ERR-COST-422-01')
case('Mất phản hồi sau commit','lô hợp lệ và key K; gateway làm mất phản hồi sau commit','đối soát K rồi retry cùng key/body trong 24 giờ','trả kết quả đã lưu; số dòng không tăng lần hai; không tạo key mới chỉ vì timeout','', 'FLOW-COST-Q02','Integration')

story('Nhập XLSX giá','kế toán mua hàng','kiểm tệp trước khi nhập','xử lý dữ liệu hàng loạt có báo lỗi theo dòng','PRC-005','004','P0',5)
case('Đọc đúng tên cột','mẫu giá XLSX không mật khẩu, hai dòng hợp lệ; đổi thứ tự cột, thêm cột Ghi chú lạ, dòng trắng','kiểm tệp; xác nhận nhập','kiểm không ghi; bỏ dòng trắng và cảnh báo cột lạ; xác nhận mới tạo hai dòng','BR-CAT-023')
case('Tệp lỗi không ghi','tệp thiếu cột bắt buộc hoặc giá dòng 2 bằng 0','kiểm và thử xác nhận tệp chưa đạt','ERR-MENU-422-20, lỗi có dòng/cột; không tạo giá','BR-CAT-023 ERR-MENU-422-20')
case('Giới hạn dòng và đọc số','hai tệp mẫu có 2000 và 2001 dòng hợp lệ; số văn bản "120000"; tệp phụ có "120,000"','kiểm từng tệp; không xác nhận nhập','2000 dòng được kiểm; 2001 trả ERR-MENU-422-20; số nguyên văn bản được đọc; "120,000" là thập phân 120, không được hiểu là 120000','BR-CAT-023 ERR-MENU-422-20','—','Boundary')

story('Lịch sử và hủy giá tương lai','kế toán mua hàng','xem lịch sử và hủy giá chưa hiệu lực','sửa kế hoạch giá mà không sửa dữ liệu quá khứ','PRC-006 PRC-007','002,005','P0',3,'FLOW-COST-Q01; E3-Q14')
case('Hủy giá tương lai độc lập','giá I1/A/16-11 là dòng duy nhất của ngày; hôm nay 11/11','xem lịch sử rồi hủy với lý do từ 10 ký tự','dòng được đánh dấu hủy, giữ audit, không còn được chọn khi tra giá; các dòng cũ giữ nguyên','BR-PRC-004 BR-AUD-001')
case('Giá đã hiệu lực','giá ngày 10/11 và ngày 11/11; hôm nay 11/11','thử sửa hoặc hủy từng giá','HTTP 409 ERR-COST-409-03; dữ liệu và cờ tham chiếu không bị đổi ngầm','BR-PRC-004 ERR-COST-409-03')
case('Phạm vi lịch sử','QL chỉ thuộc A; tồn tại giá riêng B','gọi trực tiếp chi tiết giá B bằng ID và lọc lịch sử B','ERR-SYS-404-01 cho tài nguyên ngoài phạm vi; không lộ giá B','ERR-SYS-404-01','—','Security')

story('Theo dõi giá thiếu và giá cũ','kế toán mua hàng','nhận danh sách nguyên liệu cần cập nhật','ưu tiên cập nhật giá đang ảnh hưởng thực đơn','PRC-008 PRC-009','005','P0',3,'E3-Q5; FLOW-COST-Q03; DL-01')
case('Thiếu giá theo cơ sở','I1 dùng ở hai công thức ACTIVE; chỉ có giá riêng A','tra danh sách thiếu giá B và A','B có I1, số món ảnh hưởng 2; A không liệt kê I1; không lấy giá riêng A cho B','BR-PRC-006')
case('Chạy lại không nhân cảnh báo','I1 tươi có giá 8 ngày tuổi; ngưỡng 7','chạy worker giá cũ hai lần cùng ngày','một cảnh báo đang mở cho I1 gửi KT; lần hai không tạo cảnh báo mở thứ hai','BR-PRC-008 BR-COST-005','FLOW-COST-Q03')
case('Biên tuổi giá','tươi có giá 7/8 ngày tuổi; khô và đông lạnh có giá 30/31 ngày tuổi; cấu hình 7/30','chạy kiểm tuổi giá','7 và 30 chưa cảnh báo; 8 và 31 cảnh báo; nguyên liệu ngoài công thức ACTIVE không bị đưa vào tập kiểm','BR-PRC-008 BR-COST-005','DL-01','Boundary')

story('Xác nhận biến động giá','kế toán mua hàng','xác nhận giá thay đổi lớn','tránh nhập nhầm mà vẫn cho lưu giá thực tế','PRC-010','002','P1',2,'E3-Q6')
case('Xác nhận rồi lưu','giá trước 100000; ngưỡng lệch 30%','nhập 131000; xác nhận cảnh báo','trước xác nhận chưa có dòng mới; sau xác nhận tạo đúng một dòng','BR-PRC-009')
case('Hủy xác nhận','giá trước 100000','nhập 69000; chọn hủy cảnh báo','không tạo dòng giá; có thể sửa dữ liệu nhập','BR-PRC-009')
case('Đúng ngưỡng và giá đầu tiên','giá trước 100000; ngưỡng 30%; I2 chưa có giá','thử giá 130000, 70000 ở các fixture độc lập; nhập giá đầu I2','đúng 30% không hỏi vì quy tắc là vượt 30%; I2 không có cơ sở so sánh nên không hỏi','BR-PRC-009','—','Boundary')

story('Chứng từ giá','kế toán mua hàng','gắn chứng từ cho giá hoặc lô giá','truy lại nguồn nhập','PRC-011','002','P1',2)
case('Gắn PDF hợp lệ','KT có quyền và PDF thật 1 MB','upload rồi gắn vào giá hoặc một lô; mở bằng quyền hợp lệ','truy lại cùng chứng từ; URL nội bộ có chữ ký hết hạn 15 phút')
case('Sai nội dung và quá dung lượng','tệp executable đổi đuôi .pdf; PDF lớn hơn 10 MB','upload từng tệp','tệp giả trả ERR-SYS-415-01; tệp quá cỡ trả ERR-SYS-413-01; không tạo liên kết chứng từ','ERR-SYS-415-01 ERR-SYS-413-01')
case('Thu hồi quyền và URL hết hạn','chứng từ giá thuộc B; QL thuộc A; URL đã hết hạn','thử tải bằng QL A; thử tải URL hết hạn','không trả bytes chứng từ; không rò qua URL tải hoặc thông báo lỗi','', '—','Security')

story('Cost món và bảng phân rã','dinh dưỡng viên','xem cost món theo ngày và công thức','chọn món có căn cứ về chi phí','DISH-001 DISH-002 DISH-003 DISH-004','006','P0',5,'O-01; E3-Q2; FLOW-COST-Q04')
case('Tính chính xác theo đơn vị','thịt 70g giá 120000/kg hệ số1000; trứng 3 quả giá800; hao hụt KHONG; cả hai tính cost','tính món và mở picker tại cùng ngày/cơ sở','cost 10800; dòng thịt 8400, trứng 2400; có NCC/ngày giá/đơn vị/tỷ trọng; picker cùng ngày khớp 10800','BR-CALC-001 BR-CALC-002 BR-CALC-006')
case('Không trả tổng thiếu','thịt cần tính cost nhưng không có giá; trứng vẫn có giá; nước không tính cost và không có giá','tính món','ERR-COST-422-03 liệt kê thịt, không liệt kê nước; không trả 2400 như cost toàn món','BR-CALC-002 BR-CALC-003 ERR-COST-422-03')
case('Công thức theo ngày và quyền','R1 hiệu lực10/11 thịt70g; R2 hiệu lực16/11 thịt80g; giá120000; có thêm công thức đã gắn vào MENU PENDING','tính món tại15/11,16/11; kiểm MENU PENDING; gọi picker bằng người thiếu cost.cost.read','chọn R1 rồi R2 theo ngày; MENU PENDING giữ công thức gắn; picker của người thiếu quyền không có trường tiền','BR-CALC-001 BR-CAT-014','—','Security')
case('Món không tồn tại','không có mã món M999','tính M999','ERR-MENU-404-01; không trả kết quả số','ERR-MENU-404-01')
case('Hao hụt đúng một lần','thịt70g, giá120000/kg, hao hụt20%, chế độ CO','tính cost một suất; lập dự toán10 suất chỉ có món này không khoản khoán','cost thịt10500; lượng mua0.88kg sau làm tròn lên từ0.875; thành tiền105600; không chia hao hụt lần hai','BR-EST-002','E3-Q2','Boundary')

story('So sánh công thức','người duyệt công thức','so sánh cost hai phiên bản','thấy tác động trước quyết định','DISH-005','006','P1',2,'FLOW-COST-Q04')
case('So sánh cùng ngày','R1 cost10000, R2 cost11000 tại cùng D/A','so sánh R1 và R2','chênh1000 và10%; không ghi giá hay tự duyệt công thức')
case('Một bản thiếu giá','R2 có nguyên liệu chưa có giá','so sánh R1/R2','ERR-COST-422-03; không suy diễn R2 bằng0 và không trả delta sai','ERR-COST-422-03')
case('Cost gốc bằng0','R1 có mọi nguyên liệu không tính cost; R2 cost1000','so sánh hai bản','delta tiền1000; cách hiển thị delta% phải theo quyết định Q04; không trả Infinity/NaN','', 'FLOW-COST-Q04','Boundary')

story('Lập bảng món đặc thù','dinh dưỡng viên','chụp bảng cost và gửi duyệt','có căn cứ xét món đặc thù','DISH-006','007','P0',3,'E3-Q16')
case('Chụp bản pending','món đặc thù M1 đủ giá tại A/D','lập bảng có ghi chú và gửi','bảng PENDING giữ công thức, giá, cơ sở, ngày tính và người lập; thay giá sau đó không sửa nội dung chụp','BR-CALC-010')
case('Sai loại món','M2 không có cờ đặc thù','lập bảng đặc thù cho M2','ERR-COST-422-04; không tạo bảng','ERR-COST-422-04')
case('Thiếu một giá','M1 đặc thù thiếu giá thịt','gửi bảng M1','ERR-COST-422-03, danh sách thiếu; không tạo bản chụp thiếu rồi coi là đủ','BR-CALC-003 ERR-COST-422-03')

story('Duyệt bảng món đặc thù','Giám đốc','duyệt hoặc trả lại bảng tính','kiểm soát món đặc thù trước khi dùng','DISH-007','007','P0',3,'O-06; E3-Q16')
case('Duyệt bởi người khác','bảng PENDING do DD1 tạo/sửa; GD1 khác DD1','GD1 duyệt','APPROVED, có audit quyết định; dữ liệu chụp không bị tính lại','BR-SEC-008 BR-CALC-010')
case('Không tự duyệt hoặc thiếu lý do','người có quyền duyệt đồng thời là người tạo hoặc người sửa cuối của bảng; bảng khác do người khác tạo','tự duyệt bảng đầu; trả lại bảng thứ hai với lý do9 ký tự rồi10 ký tự','tự duyệt trả ERR-SYS-403-01; lý do9 trả ERR-SYS-422-01; lý do10 cho trả lại, giữ bản chụp','BR-SEC-008 ERR-SYS-403-01 ERR-SYS-422-01')
case('Hiệu lực và cơ sở','bảng M1 được duyệt ở A; ngày lập và ngày tính khác nhau; thời hạn cấu hình90','kiểm điều kiện M1 ở mốc89/90/91 ngày và cơ sở B','ghi nhận kết quả theo bộ lọc được chốt ở E3-Q16 trước khi chạy; không tự coi bảng A dùng được ở B','BR-CALC-007 BR-COST-007','E3-Q16','Boundary')

story('Gợi ý nhóm cost','dinh dưỡng viên','nhận gợi ý nhóm cao/thấp','phân loại món có tham khảo chi phí','DISH-008','006','P1',2,'E3-Q7')
case('Gợi ý không tự ghi','ngưỡng phân nhóm đã được duyệt trong fixture và món đủ giá','yêu cầu gợi ý','trả nhóm theo ngưỡng; nhóm đang lưu không đổi cho tới thao tác quyết định của người dùng','', 'E3-Q7')
case('Thiếu giá không phân nhóm','món có nguyên liệu thiếu giá','yêu cầu gợi ý','không đưa nhóm thấp do coi giá thiếu là0; trả chưa tính được','BR-CALC-003','E3-Q7')
case('Biên phân nhóm','có quyết định E3-Q7 về ngưỡng và dấu so sánh','thử cost dưới, đúng, trên ngưỡng một đồng','nhóm khớp quyết định được duyệt; chưa điền ngưỡng tự đặt vào production','', 'E3-Q7','Boundary')

story('Cost ngày trên thực đơn','dinh dưỡng viên','xem cost suất và phân rã theo ngày/cơ sở','điều chỉnh thực đơn trong ngân sách','MEAL-001 MEAL-002 MEAL-003','009','P0',5,'O-01; E3-Q1; E3-Q3; E2-Q1')
case('Ngày đủ món','fixture giá suất40000 VAT8%, phần chính10800, phụ/rau/canh6500, khoán1500; ngưỡng52','tính cost ngày và mở phân rã','cost18800; doanh thu chưa VAT=40000/1.08, cost50.76%, đạt; dư hiển thị459đ; có từng phần và cách tính','BR-CALC-005 BR-CALC-006 BR-COST-002 BR-COST-003','O-01; E2-Q1')
case('VAT thiếu hoặc mẫu số0','fixture không đặt VAT; fixture khác giá suất0','tính từng ngày','ERR-COST-422-05; không mặc định VAT0 hay trả cost%0','BR-CALC-005 ERR-COST-422-05')
case('Làm tròn rồi so ngưỡng','fixture VAT0, giá suất100000, ngưỡng52; cost52004 và52005 ở hai lần độc lập','tính cost% và kiểm ngưỡng','52.004% làm tròn52.00 đạt;52.005% làm tròn52.01 vượt; trung gian không làm tròn','BR-CALC-006 BR-COST-001','—','Boundary')
case('Ba phương pháp món chính','các món chính gồm Healthy có cost8000,10000,12000; K=2; món mặc định10000','tính từng cấu hình DAT_NHAT, BINH_QUAN, MAC_DINH','phần chính lần lượt24000,20000,20000; không bỏ Healthy khỏi trung bình','BR-CALC-004','E3-Q1; E3-Q12')
case('Ngày chưa đủ món và phản hồi cũ','ngày mới có món chính; hai lượt sửa có revision1 và2','tính phần có; trả phản hồi revision1 sau revision2','hiện chưa đủ món, không gắn nhãn đạt cho ngày hoàn chỉnh; không ghi đè kết quả revision2 bằng revision1','', 'FLOW-COST-Q02','Integration')

story('Khoản khoán','kế toán mua hàng','đề nghị khoản khoán để Giám đốc duyệt','tính đúng khoản cố định trên suất','MEAL-004','008','P0',3,'O-01; FLOW-COST-Q05')
case('Ưu tiên riêng thay chung','khoản Gia vị chung1000 đã duyệt; đề nghị riêng suất40K1500 ngày16/11','người khác duyệt đề nghị; tính ngày15/11 và16/11 cho suất40K','ngày15 dùng1000; ngày16 dùng1500 thay vì2500; không áp PENDING','BR-CALC-008 BR-SEC-008')
case('Khoản sai không nhận','KT có quyền','gửi khoản -1,1.5 hoặc thiếu ngày hiệu lực','mỗi đầu vào trả ERR-COST-422-06; không tạo đề nghị','BR-CALC-008 ERR-COST-422-06')
case('Số0 và người đề nghị','khoản giá0 ngày hợp lệ lý do đủ; người tạo có cả quyền duyệt trong fixture','gửi đề nghị0 rồi tự duyệt','đề nghị0 hợp lệ, tự duyệt ERR-SYS-403-01; giá0 của khoản không bị nhầm với giá nguyên liệu','BR-CALC-008 BR-SEC-008 ERR-SYS-403-01','—','Boundary')

story('Cổng gửi duyệt','dinh dưỡng viên','kiểm Cost trước gửi thực đơn','ngăn thiếu dữ liệu và tuân thủ chế độ ngưỡng','MEAL-005','010','P0',3,'E3-Q3; E3-Q9; E3-Q16')
case('Mọi cơ sở đều đạt','thực đơn đủ món, đủ giá/VAT, bảng đặc thù còn hiệu lực; A/B cùng dưới ngưỡng','gửi duyệt ở chế độ CHAN','Cost cho qua; MENU tiếp tục các điều kiện khác, không tự coi toàn bộ MENU đã được duyệt','BR-CALC-009')
case('Một cơ sở vượt','A cost50%, B cost54%, ngưỡng52; CHAN','gửi duyệt thực đơn chung A/B và thử bỏ B khỏi request','ERR-COST-422-07; không PENDING; server vẫn kiểm đủ cơ sở và trả chi tiết theo quyền','BR-CALC-009 BR-COST-001 ERR-COST-422-07')
case('Cảnh báo không bỏ qua dữ liệu thiếu','CANH_BAO; lần1 đủ giá cost54%; lần2 thiếu giá; lần3 đặc thù thiếu bảng; lần4 thiếu VAT','gửi duyệt từng fixture','lần1 Cost chỉ cảnh báo; lần2/3/4 vẫn chặn với ERR-COST-422-03/04/05 tương ứng; không có nút ngoại lệ CHAN','BR-CALC-003 BR-CALC-007 ERR-COST-422-03 ERR-COST-422-04 ERR-COST-422-05','—','Boundary')

story('Snapshot lúc duyệt','Giám đốc','lưu căn cứ cost cùng quyết định duyệt','truy lại số liệu đã dùng sau khi giá thay đổi','MEAL-006','010','P0',3,'FLOW-COST-Q06')
case('Chụp từng ngày/cơ sở','MENU PENDING đủ điều kiện, không có thay đổi đầu vào từ lần kiểm; 6 ngày,2 cơ sở','duyệt thành APPROVED','có12 snapshot cho vòng duyệt, chứa giá/nguồn/ngày/params; ghi APPROVED và snapshot cùng giao dịch đề xuất','BR-CALC-010','FLOW-COST-Q02')
case('Giá đổi trong lúc chờ','MENU PENDING đã kiểm bằng giá cũ; giá mới có hiệu lực trước khi duyệt','duyệt thực đơn','chưa xác định oracle số liệu chụp đến khi Q06 chốt chính sách kiểm lại; ca phải BLOCKED, không mặc nhiên chụp kết quả cũ hoặc mới','BR-CALC-010','FLOW-COST-Q06')
case('Bất biến và rollback','đã có snapshot vòng1; fixture khác cố ý gây lỗi khi lưu snapshot trước commit','đổi giá/công thức/params rồi đọc vòng1; thử duyệt fixture lỗi','vòng1 không đổi; giao dịch lỗi không để APPROVED thiếu snapshot; retry đối soát không tạo trùng vòng','BR-CALC-010','FLOW-COST-Q02','Integration')

story('Chế độ kiểm Cost','quản trị tham số','đề nghị chế độ kiểm để người khác duyệt','chuyển giai đoạn chạy thử sang kiểm soát chặn','MEAL-008','011','P0',2)
case('Duyệt thay đổi SYS','CANH_BAO hiện hành; QT đề nghị CHAN hiệu lực hôm nay','GD khác người tạo duyệt','trước duyệt vẫn CANH_BAO; sau duyệt CHAN áp dụng từ ngày hiệu lực','BR-SYS-002 BR-SEC-008')
case('Tự duyệt bị cấm','người đề nghị cũng có quyền duyệt','tự duyệt đề nghị hoặc người sửa cuối duyệt','ERR-SYS-403-01; tham số không thay','BR-SEC-008 ERR-SYS-403-01')
case('Hiệu lực tương lai','CHAN đã duyệt hiệu lực16/11, hiện11/11','kiểm ngày trước và đúng thời điểm có hiệu lực theo SYS','trước hiệu lực giữ chế độ cũ; tới hiệu lực áp CHAN; bản chụp quá khứ không đổi','BR-SYS-002 BR-CALC-010','—','Boundary')

story('Bộ kiểm và ẩn con số','người soạn thực đơn','xem quy tắc Cost theo quyền','biết vi phạm mà không lộ dữ liệu ngoài phạm vi','RUL-001 RUL-002','009','P0',3,'DL-01; E3-Q7')
case('Đăng ký đúng quy tắc','fixture có ngày vượt, giá cũ, cặp chính/phụ cost cao, đặc thù thiếu bảng','chạy bộ kiểm tích hợp MENU','có kết quả BR-COST-001/005/006/007 theo loại cấu hình; không đăng ký002/003/004 thành lỗi kiểm độc lập','BR-COST-001 BR-COST-005 BR-COST-006 BR-COST-007','DL-01; E3-Q7')
case('Không lộ tiền trong lỗi','tài khoản có quyền kiểm MENU nhưng thiếu cost.cost.read','kiểm ngày vượt và gửi duyệt ở CHAN; đọc JSON/network và UI','chỉ nhãn đạt/không đạt; ERR-COST-422-07 được rút gọn, không cost%, tiền, breakdown trong details','ERR-COST-422-07','—','Security')
case('Quyền thay đổi và agent nội bộ','agent nội bộ thay QL A; quyền cost bị thu hồi giữa hai yêu cầu','gọi cost B rồi lặp yêu cầu A sau thu hồi','không trả dữ liệu B; quyền hiệu lực là giao quyền dịch vụ/người; yêu cầu kế tiếp không replay dữ liệu đã mất quyền','BR-SEC-009','—','Security')

story('Ngân sách cho agent phía khách','agent dinh dưỡng viên phía khách','nhận trạng thái ngân sách tổng','hỗ trợ thực đơn mà không đọc giá nội bộ','RUL-003','015','P0',3,'FLOW-COST-Q09')
case('Chỉ một trạng thái','phiên còn quota; thực đơn hợp lệ mọi ngày đều đạt','gọi budget-check','chỉ result DAT; không ngày vượt, ngưỡng, cost, giá, snapshot trong body hoặc log','BR-CALC-011 BR-SEC-010')
case('Thực đơn lỗi','payload chứa món INACTIVE hoặc lặp món trong ngày','gọi budget-check','ERR-MENU-422-14; không trả dữ liệu tiền trong lỗi','ERR-MENU-422-14')
case('Quota lời gọi31','một phiên đã có29 lời gọi; payload hợp lệ','gọi lần30 rồi31, thử đổi key yêu cầu trong cùng phiên','lần30 xử lý; lần31 ERR-COST-429-01, không có con số; key mới không reset quota','ERR-COST-429-01','—','Boundary')
case('Thiếu giá và trạng thái hỗn hợp','fixture1 tất cả xác định và một ngày vượt; fixture2 thiếu giá nhưng không có ngày vượt; fixture3 vừa vượt vừa thiếu','gọi từng fixture','fixture1 KHONG_DAT; fixture2 KHONG_XAC_DINH; fixture3 BLOCKED chờ ưu tiên Q09, không tự chốt','BR-CALC-011','FLOW-COST-Q09')

story('Dự toán ngày','kế toán mua hàng','lập dự toán với số suất từng món','biết lượng mua và chi phí dự kiến','EST-001 EST-002 EST-004','012','P0',5,'E3-Q8; E3-Q15; E3-Q2; O-01')
case('Gộp nguyên liệu và đủ cột','K=1,10 suất; công thức mỗi suất thịt70g trứng3 quả; giá120000/kg và800/quả; khoán1500; VAT0,giá suất40000','lập dự toán ngày','thịt0.70kg=84000, trứng30quả=24000, khoán15000; tổng123000, doanh thu400000,cost30.75%; đủ phân rã món/giá/NCC/ngày/công thức','BR-EST-001 BR-EST-002 BR-EST-003')
case('Số suất sai','thực đơn đủ giá','lập từng fixture số suất -1,1.5 hoặc tất cả0','ERR-COST-422-08; không lưu bản dự toán','BR-EST-001 ERR-COST-422-08')
case('Làm tròn lên lượng mua','K=1; nguyên liệu tổng1001g, hệ số1000, giá100000/kg; không hao hụt/khoán','lập dự toán','lượng1.01kg, thành tiền101000; không làm tròn gần nhất thành1.00kg','BR-EST-002','—','Boundary')
case('K lớn hơn1','K=2; số lượt chọn món chính50 và30, fixture khác50 và31','lập dự toán với chính sách Q15 được duyệt','theo đề xuất chia K: N=40 cho fixture1; fixture2 không chia hết cần xử lý theo quyết định; ca BLOCKED trước khi Q15 chốt','BR-EST-001','E3-Q15')

story('Dự toán tuần','kế toán mua hàng','lập và gộp dự toán nhiều ngày','chuẩn bị nhu cầu nguyên liệu trong tuần','EST-003','012','P0',5,'FLOW-COST-Q07')
case('Tuần đủ dữ liệu','hai ngày cùng nguyên liệu I1; ngày1 dùng1kg,ngày2 dùng2kg; giá100000 và110000/kg; không khoán','lập tuần theo hợp đồng Q07 đã duyệt','có bản ngày; bảng tuần I1 tổng3kg, tiền320000; truy được giá/ngày từng phần, không nhân3kg với một giá duy nhất','BR-EST-003','FLOW-COST-Q07')
case('Một ngày thiếu giá','tuần có ngày2 thiếu giá, còn lại hợp lệ','lập tuần','báo lỗi ngày2; atomicity và số bản được phép ghi phải theo Q07; chưa chạy với oracle tự đặt','BR-CALC-003 ERR-COST-422-03','FLOW-COST-Q07')
case('Retry tuần và phiên bản','đã commit một batch nhưng mất phản hồi; giữ key cũ','đối soát rồi retry cùng key trong24h','không tạo thêm bản ngày hoặc batch; kết quả theo semantics Q07 được duyệt','BR-EST-004','FLOW-COST-Q02; FLOW-COST-Q07','Integration')

story('Lịch sử và bản chỉ lượng','bếp trưởng','xem dự toán thuộc cơ sở và lịch sử phù hợp quyền','nhận lượng cần chuẩn bị từ đúng phiên bản','EST-005 EST-006','013','P0',3,'E3-Q11')
case('Lập lại không sửa cũ','dự toán v1 giá100000; KT cập nhật giá110000','KT lập lại cùng ngày/cơ sở; đọc cả hai bản bằng quyền đầy đủ','v2 có người/thời điểm mới, v1 giữ giá100000; không sửa số suất hoặc dữ liệu chụp v1','BR-EST-004 BR-CALC-010')
case('Bếp không xem cơ sở khác','bếp A chỉ có cost.estimate.qty; tồn tại dự toán B','đổi ID/path/query sang B','ERR-SYS-404-01; không trả dòng của B','ERR-SYS-404-01','E3-Q11','Security')
case('Không có cột tiền ẩn','bếp A mở dự toán A','đọc raw JSON, DOM và đối soát mọi nested field','có số lượng/đơn vị/phân rã; không giá/thành tiền/tổng/cost%/inputsSnapshot chứa tiền, kể cả trường ẩn','NFR-COST-005','E3-Q11','Security')

story('Xuất dự toán','kế toán mua hàng','xuất XLSX hoặc PDF theo quyền','chia sẻ bảng chuẩn bị nguyên liệu','EST-007','013','P1',3,'E3-Q11')
case('Bản đủ giá','KT có quyền estimate.read và bản v1','xuất XLSX và PDF','hai tệp đúng v1, đủ dòng/tổng/đơn vị và metadata; số liệu khớp snapshot không tính lại theo giá mới','BR-CALC-010')
case('Quyền bị thu hồi trước tải','yêu cầu xuất hợp lệ đã được tạo; thu hồi quyền trước khi tải','tải tệp và retry URL cũ','không tải được dữ liệu ngoài quyền; phản hồi lỗi không chứa tiền','', '—','Security')
case('Bản chỉ lượng không giấu tiền trong tệp','bếp A có qty và dự toán A','xuất hai định dạng; giải nén XLSX kiểm sheets, hidden cells, sharedStrings, công thức; kiểm PDF text/metadata','không có tiền/cost trong bất kỳ thành phần nào; chỉ lượng của A','', 'E3-Q11','Security')

story('Tính lại và mở cảnh báo','dinh dưỡng viên','được báo khi giá mới khiến ngày đã duyệt vượt cost','kịp điều chỉnh thực đơn','ALR-001 ALR-002','014','P1',5,'FLOW-COST-Q08')
case('Tính lại đúng tập','100 giá đổi ảnh hưởng50 thực đơn APPROVED/PUBLISHED ngày phục vụ từ hôm nay; snapshot trước đạt','kích hoạt giá mới và đo đến khi lưu kết quả/cảnh báo','hoàn tất<=5phút; snapshot giữ nguyên; kết quả mới tách riêng; ngày chuyển đạt sang vượt có cảnh báo cho DD/GD','BR-COST-011 BR-CALC-010 NFR-COST-004')
case('Không tính lại ngày đã qua','có ngày hôm qua đã duyệt và ngày tương lai DRAFT không thuộc tập worker','đổi giá liên quan','không đưa hai bản đó vào tập tính lại FR-COST-ALR-001; không sửa snapshot của chúng','BR-COST-011')
case('Không trùng cảnh báo','ngày chung A/B đã có cảnh báo OPEN; giá tiếp tục đổi ở hai cơ sở','phát lặp sự kiện giá và xử lý đồng thời','một cảnh báo OPEN cho thực đơn/ngày, chi tiết A/B cập nhật; không tạo hai đầu mục; ngày vốn vượt lúc duyệt chờ Q08','BR-COST-011','FLOW-COST-Q08','Integration')

story('Xử lý cảnh báo','dinh dưỡng viên','xem và đóng cảnh báo với lý do','theo dõi việc xử lý biến động giá','ALR-003','014','P1',3)
case('Đóng tay có audit','DD có cost.alert.read; cảnh báo OPEN và thực đơn vẫn vượt','xem danh sách; đóng với lý do "Đã trao đổi để xử lý"','CLOSED; audit người/thời điểm/lý do; không biến kết quả vượt thành đạt hoặc sửa snapshot','BR-AUD-001')
case('Lý do ngắn hoặc thiếu quyền','cảnh báo OPEN; KT doanh thu không có alert.read; DD có quyền','KT doanh thu thử đóng; DD đóng với9 ký tự','thiếu quyền ERR-AUTH-403-02; lý do ngắn ERR-SYS-422-01; giữ OPEN','BR-AUD-001 ERR-SYS-422-01 ERR-AUTH-403-02')
case('Đóng theo sự kiện nghiệp vụ','hai fixture cảnh báo OPEN: giá đổi lại về đạt; thực đơn được thu hồi và sửa','xử lý từng sự kiện','cảnh báo tương ứng đóng; ghi nguồn xử lý và giữ lịch sử giá/snapshot','BR-AUD-001','—','Integration')

story('Mô phỏng giá','người nội bộ được cấp quyền mô phỏng','thử một giá giả định','đánh giá tác động trước khi nhập thật','ALR-005','016','P2',3,'FLOW-COST-Q10')
case('Mô phỏng không ghi','quyền/phạm vi Q10 đã chốt; giá thật100000; giả định130000','chạy mô phỏng rồi so số bản ghi giá/snapshot/estimate/alert trước sau','có danh sách ngày vượt trong phạm vi; các bảng nghiệp vụ không đổi; nhãn mô phỏng','', 'FLOW-COST-Q10')
case('Giá giả định sai','nguyên liệu hợp lệ','mô phỏng giá0 hoặc-1','ERR-COST-422-01, không chạy ghi nghiệp vụ','BR-PRC-002 ERR-COST-422-01','FLOW-COST-Q10')
case('Phạm vi và thiếu giá khác','chỉ được mô phỏng A; một ngày A thiếu giá nguyên liệu khác; có thực đơn B','mô phỏng A rồi cố yêu cầu B','ngày thiếu được ghi chưa tính được; không khẳng định đạt; không trả dữ liệu B','BR-CALC-003','FLOW-COST-Q10','Security')

# Supplemental checks share the story/AC/test chain, retaining explicit release priority.
def extra(index,*args,**kwargs):
    current=stories.pop(index-1); stories.append(current); case(*args,**kwargs); stories.pop(); stories.insert(index-1,current)
extra(10,'Đối soát bộ kế toán','kế toán cung cấp10 món và10 ngày đã ký xác nhận; cấu hình VAT/phương pháp ghi kèm','tính lặp từng bộ bằng decimal, so bảng tay và lần tính trước','sai lệch cost món<=1đ, cost%<=0.01 điểm phần trăm; lặp cùng đầu vào có cùng kết quả; lưu bảng actual/expected','NFR-COST-002','O-01; dữ liệu kế toán','Accuracy')
extra(10,'Decimal và không làm tròn trung gian','fixture0.1+0.2 đơn vị dùng; giá1đ/đơn vị; fixture có ba dòng cost0.4đ','rà kiểu dữ liệu engine và tính hai fixture','tổng chính xác0.3; tổng ba dòng1.2 hiển thị1đ, không làm tròn từng dòng thành0; không dùng float cho tiền/định lượng','NFR-COST-008 BR-CALC-006','—','Accuracy')
extra(15,'Hiệu năng tính thực đơn','fixture6 ngày x7 món, đủ giá; ghi môi trường, cơ sở, cache và cấu hình','chạy50 lần đo API cost và bộ kiểm đầy đủ, lưu từng mẫu; p95 theo thứ tự mẫu thứ48','p95 Cost<=1s; tổng bộ kiểm theo NFR-MENU-001<=2s; không tính thời gian render wireframe','NFR-COST-001','môi trường backend','Performance')
extra(4,'Hiệu năng lưới200 dòng','200 tuple giá mới hợp lệ, không cần xác nhận biến động; ghi cấu hình môi trường','gửi một lô200 dòng, đo từ gửi đến nhận xác nhận commit; đếm giá/audit','<=3giây và đủ200 dòng; thời gian và tính nguyên tử cùng đạt','NFR-COST-003','môi trường backend','Performance')
extra(21,'Không rò dữ liệu toàn API','bốn tài khoản: bếp A, người nội bộ không quyền giá/cost, svc khách, QL A truy B; danh mục MENU/COST','gọi success/error/list/detail/export/replay với từng tài khoản; kiểm JSON, file và cache','không con số hoặc trường giá/cost ngoài quyền trong mọi đường phản hồi; ghi endpoint x actor x outcome','NFR-COST-005','E3-Q11','Security')
extra(21,'Quyền DB agent khách','tài khoản DB thật dùng cho agent khách; danh mục15 bảng Cost từ DBML','kiểm grants rồi SELECT từng bảng Cost gồm bảng snapshot/allowance/alert mới; kiểm service không dùng tài khoản quyền cao để lách','mọi SELECT trực tiếp bị từ chối; không chỉ kiểm4 bảng cũ','NFR-COST-006 BR-SEC-010','môi trường backend','Security')
extra(21,'Log budget không chứa số','budget trả DAT,KHONG_DAT,KHONG_XAC_DINH và các lỗi; fixture cost có giá trị nhận dạng','gọi các nhánh; kiểm log ứng dụng, exception, trace của budget-check','không cost/giá/cost% trong log hoặc payload debug; vẫn có requestId cho đối soát','NFR-COST-007 BR-SEC-010','môi trường backend','Security')
extra(20,'Hồi quy quy tắc đã thuộc MENU','fixture chuẩn min70/max80g; phụ tối đa50g; nguyên liệu có xương chưa khai hao hụt; định mức40000','lưu công thức chính69g và81g, phụ51g; lưu nguyên liệu thiếu hao hụt; chọn món tổng40001','MENU chặn theo BR-COST-008/009/010/012; Cost không thay thế kiểm này; ngưỡng min/max/phụ là fixture chờ E2-Q5','BR-COST-008 BR-COST-009 BR-COST-010 BR-COST-012','E2-Q5','Integration')

extra(2,'Schema và trường do server quản lý','KT có token hợp lệ; chưa có giá tuple định tạo','gửi JSON thiếu priceVnd, enum sai, thêm createdBy hoặc totalCost client tự đặt','400 ERR-COST-400-01 theo hợp đồng đề xuất, details.path chỉ field sai; không ghi giá','ERR-COST-400-01','review API','Contract')
extra(4,'Key cùng body khác và đang xử lý','request K đã commit; request L được giữ ở trạng thái xử lý trong test','gửi K với giá khác; gửi đồng thời cùng L','K trả ERR-COST-409-04 không ghi; L trả ERR-COST-409-05 kèm Retry-After; đối soát sau hoàn tất chỉ một kết quả','ERR-COST-409-04 ERR-COST-409-05','FLOW-COST-Q02','Contract')
extra(8,'Token xác nhận stale','giá nền100000, đã cấp token cho giá131000; sau đó giá nền thay hoặc token hết hạn','xác nhận giá131000 bằng token cũ','ERR-COST-409-06; không ghi, yêu cầu kiểm lại dựa trên giá nền mới','ERR-COST-409-06','review API','Contract')
extra(5,'Import đã kiểm bị đổi','đã kiểm tệp và có token; thay bytes tệp hoặc dùng token hết hạn','commit token cũ với tệp mới','ERR-COST-409-07; không nhập một dòng nào; phải kiểm lại','ERR-COST-409-07','review API','Contract')
extra(13,'Hai quyết định cạnh tranh','cùng bảng PENDING v1; hai người có quyền duyệt khác người tạo/sửa','người1 duyệt v1; người2 gửi trả lại v1 với khóa mới','chỉ một quyết định được commit; version cũ ERR-SYS-409-02; nếu tải version mới nhưng trạng thái đã duyệt thì ERR-COST-409-07; không ghi đè quyết định trước','ERR-SYS-409-02 ERR-COST-409-07','review API và concurrency token','Contract')
extra(16,'Khoản trùng khi duyệt','đã có Gia vị/ALL/16-11 APPROVED; có đề nghị khác cùng tuple sau chuẩn hóa tên','duyệt đề nghị thứ hai','ERR-COST-409-08; không tạo hai khoản cùng tên/phạm vi/ngày hiệu lực','ERR-COST-409-08','review API','Contract')
extra(2,'NCC inactive có hai mã lỗi trong SRS','S1 tồn tại nhưng INACTIVE; I1 ACTIVE','nhập giá cho S1','không ghi giá; oracle mã lỗi BLOCKED vì ma trận404-01 nói tham chiếu không còn dùng,422-02 lại nói NCC ngừng; cần thống nhất trước nghiệm thu hợp đồng','ERR-COST-404-01 ERR-COST-422-02','QA-COST-Q01: BA/Tech lead thống nhất mã','Contract')
extra(5,'Số dạng văn bản và trang tính','mẫu đúng trang; giá văn bản120000.0 và120000,0; trang khác có dữ liệu; file khác đặt mật khẩu','kiểm từng tệp không commit','hai dạng số bằng120000 được đọc; bỏ trang khác kèm cảnh báo; tệp mật khẩu bị từ chối không ghi','BR-CAT-023','—','Boundary')
extra(10,'Tổng cost0 không chia cho0','mọi nguyên liệu món có cờ không tính cost','tính món và xem tỷ trọng từng dòng','tổng cost0; cách biểu diễn tỷ trọng chờ Q04; không NaN/Infinity và không suy ra giá nhập0','BR-CALC-002','FLOW-COST-Q04','Boundary')

catalog=json.loads((BASE/'api/endpoint-catalog.json').read_text(encoding='utf-8'))
for s in stories:
    s['apis']=[e['id'] for e in catalog['endpoints'] if set(e['fr'])&set(s['fr'])]
    s['screens']=sorted({screen for uc in s['uc'].split(',') for screen in re.findall(r'SCR-COST-\d+', (BASE/f'usecases/UC-COST-{uc}.md').read_text(encoding='utf-8'))})
    for i,c in enumerate(s['cases'],1):
        c['ac']=s['id'].replace('US-','AC-')+f'-{i:02}'
        c['tc']=s['id'].replace('US-','TC-')+f'-{i:02}'
        c['status']='BLOCKED — '+c['gate'] if c['gate']!='—' else 'NOT RUN — chưa có backend'

meta='Phiên bản 0.1.0 · 11/11/2026 · Draft để BA/QA/Tech lead review.\n\n'
sources='Nguồn: [SRS Cost](../srs/spec.md), [16 use case](../srs/usecase-diagram.md), [API đề xuất](../api/api-spec.md), [user flow](../ui/user-flow.md).\n\n'
history='\n## Lịch sử sửa đổi\n\n| Phiên bản | Ngày | Người | Nội dung |\n| :--- | :--- | :--- | :--- |\n| 0.1.0 | 2026-11-11 | BA | Khởi tạo bản nháp truy vết, giữ điểm mở và trạng thái chưa chạy |\n'
def write(relative,text):
    p=BASE/relative;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
back='# Backlog Cost\n\n'+meta+sources+'''Story Point là ước lượng sơ bộ của BA để thảo luận, chưa được đội dev cam kết; không dùng cộng điểm để suy ra tiến độ. P0/P1/P2 giữ theo SRS. Mỗi story có giá trị độc lập để review nhưng dùng nền MENU/SYS, engine và danh mục giá chung; chưa tuyên bố mọi story đủ INVEST để vào sprint.

Điều kiện đưa vào sprint: chốt điểm mở ảnh hưởng story, review hợp đồng API/migration, có fixture và người duyệt AC, đội dev ước lượng lại. Các story 5 điểm cần tách tiếp nếu vượt một sprint. Những kịch bản có oracle chưa xác định mang BLOCKED; kịch bản xác định theo SRS vẫn chỉ là NOT RUN và không tự phê duyệt đề xuất nghiệp vụ.

| Story | Nội dung | SP sơ bộ | Ưu tiên | FR | UC | Điểm mở |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
'''
for s in stories:
    back+=f"| [{s['id']}](#{s['id'].lower()}) | {s['title']} | {s['points']} | {s['priority']} | {', '.join(s['fr'])} | UC-COST-{s['uc']} | {s['gates']} |\n"
for s in stories:
    back+=f"\n<a id=\"{s['id'].lower()}\"></a>\n\n## {s['id']} — {s['title']}\n\nLà một **{s['actor']}**, tôi muốn **{s['goal']}** để **{s['value']}**.\n\n- Phạm vi: {', '.join(s['fr'])}; {'; '.join('[UC-COST-'+u+'](../usecases/UC-COST-'+u+'.md)' for u in s['uc'].split(','))}.\n- Giao tiếp đề xuất: {', '.join(s['apis']) or 'hook nội bộ/SYS theo API mục 7'}; màn: {', '.join(s['screens']) or 'SVC-COST-01 / tác vụ nền'}.\n- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: {s['gates']}.\n- Nghiệm thu: [AC](acceptance-criteria.md#{s['id'].lower()}) ({len(s['cases'])} kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.\n"
back+='''
## Hai mục hoãn, chưa đưa vào sprint

| Mục quyết định | FR | Chủ sở hữu | Điều kiện mở lại |
| :--- | :--- | :--- | :--- |
| DEC-COST-01 | FR-COST-MEAL-007 | Giám đốc, E3-Q9 | Chốt có ngoại lệ hay không, người duyệt/lý do/audit; sau đó mới viết story/AC thành công |
| DEC-COST-02 | FR-COST-ALR-004 | Giám đốc, E3-Q10 | Chốt luồng chuyển bếp và cơ chế chặn/cảnh báo; chưa có bước chuyển bếp ở R3 |

Hai mục này không được tính là story đã có AC/test hay chức năng hoàn tất. Chế độ CANH_BAO không phải duyệt ngoại lệ CHAN.
'''+history
write('userstories/backlog.md',back)
ac='# Tiêu chí nghiệm thu Cost\n\n'+meta+sources+'''Mỗi nhóm là Gherkin Given/When/Then, gồm thành công, lỗi và biên/quyền. Dữ liệu số là fixture giả định; VAT8% không phải quyết định của Gia Phát. Ca BLOCKED cần chốt oracle trước khi chạy; không chấm PASS chỉ vì hệ thống từ chối mọi thao tác. Một scenario có nhiều fixture phải chạy từng fixture và ghi từng kết quả.
\n'''
for s in stories:
    ac+=f"<a id=\"{s['id'].lower()}\"></a>\n\n## {s['id']} — {s['title']}\n\n"
    for c in s['cases']:
        ac+=f"### {c['ac']} — {c['title']}\n\nTruy vết: {', '.join(s['fr'])}; {', '.join(c['refs']) or 'FR/use case của story'}. Gate: {c['gate']}.\n\n```gherkin\nScenario: {c['ac']} {c['title']}\n  Given {c['given']}\n  When {c['when']}\n  Then {c['then']}\n```\n\n"
write('userstories/acceptance-criteria.md',ac+history)
check='# Checklist kiểm thử Cost\n\n'+meta+sources+'''Checklist đã được tự rà truy vết với SRS, chưa có BA/QA ký duyệt. Test case chi tiết được soạn song song làm bản nháp review theo yêu cầu tiếp tục công việc; chưa coi bước review con người đã hoàn tất.

| Nhóm | Story | Nội dung cần review | Số ca | Trạng thái review |
| :--- | :--- | :--- | :---: | :--- |
'''
for s in stories: check+=f"| CHK-COST-{s['id'][-3:]} | {s['id']} | {'; '.join(c['title'] for c in s['cases'])} | {len(s['cases'])} | Chờ BA/QA |\n"
check+='''
## Review xuyên suốt

- Chức năng và dữ liệu: 24 BR định nghĩa trong Cost, các quy tắc Cost/MENU/SYS phụ thuộc, lỗi nghiệp vụ, ranh giới ngày/số tiền/quota.
- Bảo mật: role × cơ sở × endpoint, success/error/export/replay, không giấu tiền bằng CSS; quyền người tạo và người sửa cuối khi duyệt.
- Giao diện: trạng thái loading/empty/error/offline, giữ bản sửa khi lỗi, không hiển thị phản hồi revision cũ. Wireframe chỉ là bằng chứng thiết kế; mobile/keyboard của app thật cần QA bổ sung sau khi có UI.
- Hiệu năng/chính xác: cả 8 NFR Cost có ca; cần môi trường thật và bộ đối soát 10 món/10 ngày của kế toán.
- Kỹ thuật API: idempotency/hash, xung đột phiên bản, xác nhận stale, import token stale và outbox cần test tích hợp sau Tech lead duyệt. Đây là phần bổ sung bên dưới, không thay14 lỗi SRS.
- Hoãn: FR-COST-MEAL-007 và FR-COST-ALR-004 chưa có test thực thi thành công; không tính vào độ phủ đã viết ca.

Người review cần điền: tên/ngày, quyết định chấp nhận hoặc yêu cầu sửa, điểm mở liên quan; trạng thái mặc định Chờ review.
'''+history
write('test/checklist.md',check)
tests='# Test case Cost\n\n'+meta+sources+'''## Chuẩn bị và cách ghi kết quả

Chỉ chạy trên môi trường test có MENU/SYS/COST và dữ liệu cô lập. Reset fixture trước mỗi ca/biến thể; không dùng dữ liệu thật. Đặt ngày máy chủ test 11/11/2026 theo Asia/Ho_Chi_Minh cho ca giá; mô phỏng mốc hiệu lực khi ca yêu cầu. Tạo KT/DD/GD/QT/QL A/bếp A và hai service account đúng quyền SRS; tài khoản kiêm quyền chỉ dùng kiểm phân tách tạo/duyệt.

Mỗi ca: (1) chuẩn bị tiền điều kiện/fixture; (2) thực hiện các hành động theo thứ tự trong ô bước; (3) kiểm phản hồi, dữ liệu trước/sau, audit và quyền; (4) ghi actual, PASS/FAIL/BLOCKED, requestId, build, môi trường và bằng chứng. Các bước ghi database dùng quyền QA phù hợp ở môi trường test. Không sửa dữ liệu production. Ngày/tiền trong bảng là số mẫu, không phải cấu hình mặc định đã chốt.

Tất cả Actual và Evidence đang để “Chưa chạy”. NOT RUN nghĩa có expected theo thiết kế nhưng chưa chạy trên backend; BLOCKED nghĩa cần quyết định hoặc đầu vào/môi trường bổ sung. Không có test chức năng nào được báo PASS từ việc kiểm cấu trúc Markdown.

'''
for s in stories:
    tests+=f"## {s['id']} — {s['title']}\n\nƯu tiên {s['priority']}; UC-COST-{s['uc']}; API: {', '.join(s['apis']) or 'hook nội bộ/SYS'}; {', '.join(s['fr'])}.\n\n"
    for c in s['cases']:
        tests+=f"### {c['tc']} — {c['title']}\n\n| Trường | Nội dung |\n| :--- | :--- |\n| Story / AC | {s['id']} / {c['ac']} |\n| Loại / nguồn | {c['kind']}; {', '.join(c['refs']) or 'FR/use case nêu trên'} |\n| Tiền điều kiện và dữ liệu | {c['given']} |\n| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. {c['when']}. 3. Đối chiếu kết quả và dữ liệu/audit. |\n| Kết quả mong đợi | {c['then']} |\n| Trạng thái | {c['status']} |\n| Actual / Evidence / Defect | Chưa chạy / Chưa có / — |\n\n"
write('test/test-cases.md',tests+history)
rtm='# Ma trận truy vết Cost\n\n'+meta+'Độ phủ dưới đây là **đã viết kịch bản**, không phải đã chạy hoặc đạt nghiệm thu. FR được liên kết tới nhóm AC/test của story; không có nghĩa từng ca đơn lẻ kiểm tất cả FR của nhóm. Xem Given/When/Then để xác định nhánh được kiểm.\n\n| FR | Story | AC | Test case | API / hook | Trạng thái |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n'
for s in stories:
    for fr in s['fr']:
        endpoints=[e['id'] for e in catalog['endpoints'] if fr in e['fr']]
        rtm+=f"| {fr} | {s['id']} | {', '.join(c['ac'] for c in s['cases'])} | {', '.join(c['tc'] for c in s['cases'])} | {', '.join(endpoints) or catalog['internalMappings'].get(fr,'—')} | Draft; xem gate từng ca |\n"
for fr in catalog['deferred']:rtm+=f'| {fr} | Hoãn — quyết định trong backlog | — | — | — | Chờ E3-Q9/Q10; không tính phủ test |\n'
rtm+='\n## Quy tắc, mã lỗi và NFR có kịch bản\n\n| Mã | Test case trực tiếp |\n| :--- | :--- |\n'
refs=sorted({r for s in stories for c in s['cases'] for r in c['refs']})
for r in refs:rtm+=f"| {r} | {', '.join(c['tc'] for s in stories for c in s['cases'] if r in c['refs'])} |\n"
write('test/traceability.md',rtm+history)
write('test/scenario-catalog.json',json.dumps(dict(version='0.1.0',status='draft-not-executed',stories=stories,deferred=catalog['deferred']),ensure_ascii=False,indent=2)+'\n')
print(f'{len(stories)} stories; {sum(len(s["cases"]) for s in stories)} scenarios; {len({f for s in stories for f in s["fr"]})} active FR')
