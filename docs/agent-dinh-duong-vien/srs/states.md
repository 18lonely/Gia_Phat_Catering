# Trạng thái E9

Draft · 12/11/2026 · Tên trạng thái đề xuất; không trạng thái triển khai. Mọi mũi tên thành công đều có điều kiện policy/quyền/nguồn được duyệt. Gate chưa đủ thì không thực thi.

## Phiên hội thoại và yêu cầu thực đơn

```mermaid
stateDiagram-v2
  [*] --> CLOSED
  CLOSED --> ACTIVE: policy identity consent duoc duyet
  ACTIVE --> NEEDS_INPUT: yeu cau chua ro
  NEEDS_INPUT --> ACTIVE: lam ro khong thu suc khoe
  ACTIVE --> RESERVED: admission atomic dat
  ACTIVE --> BLOCKED: gate hoac quota dong
  RESERVED --> RUNNING: nhan run ben vung
  RUNNING --> CHECKING: candidate moi
  CHECKING --> CHECKED: E2 dat cung va source fresh
  CHECKING --> INVALID: vi pham cung
  CHECKING --> FAILED: validator loi
  RUNNING --> FAILED: provider loi hoac timeout
  CHECKED --> STALE: source doi
  CHECKED --> RESERVED: chinh revision moi
  STALE --> RESERVED: yeu cau kiem lai
  INVALID --> NEEDS_INPUT: sua yeu cau
  ACTIVE --> CLOSED: het phien hoac thu hoi
  CHECKED --> CLOSED: het phien hoac thu hoi
```

SESS là lifecycle quyền truy cập; run con có QUEUED/RUNNING/DONE/FAILED/REJECTED tương thích metadata nền, outcome phân biệt NEEDS_INPUT/INVALID/BLOCKED/STALE. Đồ thị là góc nhìn tổng hợp phiên và run, không ép hai lifecycle vào một cột status. Đóng/thu hồi phiên ở bất kỳ trạng thái nào chặn tool mới; lượt tính phí đang dở vẫn đối soát reservation. Candidate sau chỉnh phải CHECKING; không chuyển CHECKED bằng câu trả lời model. Chỉ tín hiệu tiến độ an toàn được hiện trước kiểm, không stream thực đơn chưa kiểm cho khách.

## Bản nháp gửi về Gia Phát

```mermaid
stateDiagram-v2
  [*] --> LOCAL_DRAFT
  LOCAL_DRAFT --> BLOCKED: gate nguon consent noi nhan chua du
  LOCAL_DRAFT --> ACCEPTED: khach xac nhan va luu ben vung
  ACCEPTED --> HANDOFF_PENDING: cho dau nhan
  HANDOFF_PENDING --> RECEIVED: co receipt dau nhan
  HANDOFF_PENDING --> HANDOFF_ERROR: loi chuyen
  HANDOFF_ERROR --> HANDOFF_PENDING: retry cung identity
  RECEIVED --> HUMAN_REVIEW: nguoi that tiep nhan
  HUMAN_REVIEW --> NEEDS_CLARIFICATION: yeu cau lam ro
  HUMAN_REVIEW --> DECLINED: nguoi that tu choi
  HUMAN_REVIEW --> REVIEWED_PROPOSAL: quyet dinh co bang chung
```

E9-Q06 chặn nơi nhận, vai trò, SLA, wording/status sau ACCEPTED; các trạng thái sau là phương án review, không cam kết runtime. Không có cạnh tự động tới MENU/ORDER/QUOTE. Ngay REVIEWED_PROPOSAL vẫn là đề xuất; nếu triển khai áp dụng về sau phải người thật và luồng FEAT-013, ngoài thao tác agent E9. ACK lưu và ACK bàn giao là hai bằng chứng riêng. Chưa có nơi lưu thì không ACCEPTED giả.

## Lượt/ngân sách AI

```mermaid
stateDiagram-v2
  [*] --> POLICY_CLOSED
  POLICY_CLOSED --> AVAILABLE: policy duyet du tham so
  AVAILABLE --> RESERVED: atomic check and reserve
  AVAILABLE --> QUOTA_BLOCKED: het luot
  AVAILABLE --> BUDGET_BLOCKED: vuot cap
  AVAILABLE --> UNKNOWN_BLOCKED: khong xac dinh upper bound
  RESERVED --> SETTLED: usage confirmed mot lan
  RESERVED --> UNKNOWN_HELD: timeout hoac usage chua ro
  UNKNOWN_HELD --> SETTLED: doi soat co bang chung
  RESERVED --> RELEASED: chung minh khong phat sinh phi
  SETTLED --> AVAILABLE: policy con cho phep
  RELEASED --> AVAILABLE: policy con cho phep
  QUOTA_BLOCKED --> AVAILABLE: reset theo policy da duyet
  BUDGET_BLOCKED --> AVAILABLE: ky moi theo policy va doi soat
```

Không tự release khi timeout, không lấy confirmed=null làm0. Reset/ngày mới không bỏ nợ/reserve cũ, không cộng quota AIO. Quy trình đổi policy: đề nghị→duyệt nếu yêu cầu→hiệu lực theo version; khi cơ chế duyệt chưa chốt thì POLICY_CLOSED. Mỗi lần thay đổi có audit theo E1. Mức số/đơn vị/reset/định nghĩa lượt vẫn E9-Q07/08/13.
