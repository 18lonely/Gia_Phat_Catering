// Chỉ tạo tài liệu trong gói mới. Không ghi nguồn hoặc baseline.
const c=require('./common.cjs');const {read,tableRows,clean,json,md,link}=c;
const epicDirs=['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo','chon-mon-order','giao-nhan-doanh-thu','website-cong-khai','agent-dinh-duong-vien','crm-ban-hang','mua-hang-san-xuat','phan-hoi-bao-cao','chi-phi-loi-nhuan'];
const configs=[
 ['docs/gia-phat/01-prd.md','PRD','^O-0[1-6]$',2],
 ['docs/nen-tang/review/questions.md','E1','^E1-Q',2,3],
 ['docs/nen-tang/srs/spec.md','E1','^(N-0[1-4]|Q-14|Q-18)$',2],
 ['docs/thuc-don-dinh-luong/srs/spec.md','E2','^(DL-01|E2-Q[0-9]+)$',2],
 ['docs/gia-phat/brainstorms/quy-tac-thuc-don.md','E2','^H-[1-9]$'],
 ['docs/cost/review/decision-register.md','E3','^(E3-Q[0-9]+|FLOW-COST-Q[0-9]+|QA-COST-Q01)$',2],
 ['docs/cost/accounting/business-rules.md','E3','^CK-Q[0-9]+$',3],
 ['docs/cost/review/accountant-input.md','E3','^DATA-COST-Q[0-9]+$'],
 ['docs/dinh-duong/review/questions.md','E4','^(NUTR-Q|DATA-NUTR-Q)',2],
 ['docs/agent-noi-bo/review/questions.md','E5','^AIO-Q',2],
 ['docs/chon-mon-order/review/questions.md','E6','^ORD-Q',2],
 ['docs/chon-mon-order/review/contract-gap-register.md','E6','^E6-CG-',2],
 ['docs/gia-phat/00-ke-hoach-tong-the.md','E6','^Q-16$'],
 ...epicDirs.slice(6).map((d,i)=>[`docs/${d}/review/questions.md`,`E${i+7}`,i===0?'^(Q-13|E7-Q)':'^E'+(i+7)+'-Q',i===3?3:undefined,i===3?5:2])
];
let rows=[],inventory=[];
for(const [file,epic,pattern,ownerCol,recCol] of configs){
 const selected=tableRows(file).filter(r=>new RegExp(pattern).test(clean(r.cells[0])));inventory.push({file,epic,count:selected.length,codes:selected.map(r=>clean(r.cells[0]))});
 for(const r of selected){const id=clean(r.cells[0]);if(rows.some(x=>x.sourceCode===id))throw Error('Duplicate '+id);
 let recommendation=recCol===undefined?'':r.cells[recCol], alternatives='',effects='',blocked='',owner=ownerCol===undefined?'chưa rõ':clean(r.cells[ownerCol]);
 if(epic==='E10'){alternatives=r.cells[6];effects=r.cells[4];}
 else if(Number(epic.slice(1))>=7)effects=r.cells[3];
 if(/^NUTR-|^DATA-NUTR-|^AIO-/.test(id)){effects=r.cells[3];const m=r.cells[3].match(/đề xuất[^;|]*/i);recommendation=m?m[0]:'';}
 if(/^E3-|^FLOW-COST-|^QA-COST-/.test(id)){
 const section=read(file).split('## '+id+'\n')[1]?.split('\n## ')[0]||read(file).split('## '+id+'\r\n')[1]?.split('\r\n## ')[0]||'';
 const field=label=>(section.match(new RegExp('- '+label+': (.*)'))||[])[1]||'';
 recommendation=field('Đề xuất để review');effects=field('Đánh đổi/cần làm rõ');
 const tests=field('Test bị chặn có gate nêu đích danh').match(/TC-[A-Z0-9-]+/g)||[];blocked=tests.length?`${new Set(tests).size} ca (gate trực tiếp)`:'';
 }
 if(id.startsWith('E6-CG-')){
 const n=id.slice(-2);const proposal=tableRows(file).find(x=>new RegExp('^CG'+n+'(?::|$)').test(x.cells[0])&&x.line>50&&x.cells.length>=4);
 if(proposal){recommendation=proposal.cells[1];alternatives=proposal.cells.length===5?proposal.cells[3]:proposal.cells[2];effects=proposal.cells.length===5?proposal.cells[2]:proposal.cells[3];}
 }
 if(id==='DL-01')blocked='86 ca rule; 2 ca Cost (khác bộ)';
 let releases=epic==='PRD'?({'O-01':['R3'],'O-02':['R2'],'O-03':['R6','R9'],'O-04':['R1','R5'],'O-05':['R6'],'O-06':['R1']}[id]):['R'+epic.slice(1)];
 let priority=epic==='PRD'?(['O-01','O-02','O-04','O-06'].includes(id)?'P-MVP':'P-NEXT'):Number(epic.slice(1))<=5?'P-MVP':Number(epic.slice(1))<=9?'P-NEXT':'P-LATER';
 if(['E1-Q03','N-04','FLOW-COST-Q10','E3-Q15'].includes(id)){releases=['chưa rõ'];priority='P-NOW';}
 if(id==='Q-14')releases=['R6'];
 if(id==='Q-14')priority='P-NEXT';
 if(/^H-/.test(id)){owner=['H-6','H-7'].includes(id)?'Kế toán':['H-5','H-9'].includes(id)?'Dinh dưỡng viên':'Người soạn docx';}
 rows.push({sourceCode:id,epic,question:clean(r.cells[1]),sourceFile:file,sourceLine:r.line,sourceText:r.cells[1],decisionGroup:'',decisionOwner:owner,blockedReleases:releases,priority,blockedCount:blocked,recommendation:recommendation||'',answer:'',alternatives,effects,releaseEvidence:'docs/gia-phat/02-roadmap.md',releaseNote:'Release trực tiếp của phạm vi epic theo roadmap; không cộng bắc cầu. Nếu P1/P2 chưa rõ gate release thì giữ chưa rõ.'});
 }
}
// Chỉ gộp khi cùng quyết định; các câu nhiều nhánh giữ đầy đủ phạm vi ở nguồn.
const merges=[
 ['Phạm vi sức khỏe và điều kiện mở gợi ý cá nhân','O-03','ORD-Q15','E9-Q14'],
 ['Nguồn lực, hạ tầng và cấu hình ngân sách AI','O-04','AIO-Q01','E9-Q01'],
 ['Người duyệt ngoại lệ và cơ chế thay thế','O-06','E11-Q02','E13-Q10','E10-Q03','CK-Q04'],
 ['Cỡ định lượng của một món','O-02','H-9'],
 ['Thành phần cost và VAT bán ra còn thiếu','O-01','H-6','H-7'],
 ['Chuẩn envelope giữa các phân hệ','E1-Q01','E6-CG-09'],
 ['Xác minh người ăn và binding danh tính','ORD-Q01','E6-CG-01'],
 ['Scope người đặt tổng một hoặc nhiều khách','ORD-Q11','E6-CG-02'],
 ['Nguồn định lượng sống, phần ăn được và hao hụt','E3-Q2','NUTR-Q02'],
 ['Chính sách hạn chốt và xử lý nguồn sau hạn','Q-16','ORD-Q08','E6-CG-05'],
 ['Phát hành, xác nhận revision và bắt đầu sản xuất','ORD-Q14','E6-CG-06'],
 ['Giá công khai cho website và agent khách','E8-Q03','E9-Q04'],
 ['Dựng thực đơn public và tái dùng bộ kiểm','E8-Q05','E9-Q11'],
 ['Lợi nhuận báo giá và công thức kết quả kinh doanh','E10-Q15','E13-Q08'],
 ['Nguồn công khai, độ đầy đủ và tính mới','E8-Q04','E9-Q12']
];
let groups=[];for(const [title,...ids]of merges){const members=ids.map(id=>rows.find(x=>x.sourceCode===id));if(members.some(x=>!x))throw Error(title);groups.push({title,members:ids});}
for(const r of rows)if(!groups.some(g=>g.members.includes(r.sourceCode)))groups.push({title:r.question,members:[r.sourceCode]});
groups.forEach((g,i)=>{g.id='DEC-'+String(i+1).padStart(2,'0');for(const id of g.members)rows.find(r=>r.sourceCode===id).decisionGroup=g.id;});
json('validation/source-inventory.json',{configs,registers:inventory,excludedEvidence:['E6-EVID-001','E6-EVID-002'],excludedFindings:'E6-RV-01–08 được truy vết trong CG; không tạo câu nghiệp vụ mới.',rows:rows.length});
json('validation/draft-register.json',{rows,groups,epicDirs});
console.log(JSON.stringify({rows:rows.length,groups:groups.length,inventory:inventory.map(x=>[x.epic,x.count]),long:rows.filter(r=>r.question.split(/\s+/).length>30).map(r=>[r.sourceCode,r.question])},null,2));
