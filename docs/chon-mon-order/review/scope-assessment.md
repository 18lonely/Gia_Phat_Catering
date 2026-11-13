---
id: DOC-E6-REVIEW-SCOPE-ASSESSMENT
title: Đối chiếu phạm vi FEAT-030–048
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Đối chiếu phạm vi FEAT-030–048

**Draft để review · 11/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |

Nguồn: [PRD](../../gia-phat/01-prd.md), [roadmap](../../gia-phat/02-roadmap.md), [D-03/04/14/19/21](../../gia-phat/00-ke-hoach-tong-the.md). **14 P0 + 5 P1**, giữ nguyên 19 capability gốc. Đủ căn cứ để viết hành vi không đồng nghĩa đủ căn cứ để build trọn tính năng.

| Feature | FR | Ưu tiên | Đủ căn cứ / phần tiếp tục | Chặn / điều kiện |
| :--- | :--- | :--- | :--- | :--- |
| FEAT-030 | FR-AUTH-EXT-001 | P0 | Cấp quyền người đặt tổng: tài khoản công ty | ORD-Q01; PARTIAL (thiết kế có điều kiện) |
| FEAT-031 | FR-AUTH-QREG-001 | P0 | Đăng ký qua QR công ty: user/eater đã liên kết | ORD-Q01; PARTIAL (thiết kế có điều kiện) |
| FEAT-032 | FR-AUTH-QSES-001 | P0 | Mở phiên QR giới hạn: phiên có scope và expiry | ORD-Q01; PARTIAL (thiết kế có điều kiện) |
| FEAT-033 | FR-AUTH-QRM-001 | P0 | Quản lý QR và danh sách người ăn: QR/người ăn trạng thái mới | ORD-Q02; PARTIAL (thiết kế có điều kiện) |
| FEAT-034 | FR-CUS-SVC-001 | P0 | Quản lý dữ liệu phục vụ: dữ liệu phục vụ có version | ORD-Q03; PARTIAL (thiết kế có điều kiện) |
| FEAT-035 | FR-ORD-QTA-001 | P0 | Đặt định mức công ty: quota version | ORD-Q04; PARTIAL (thiết kế có điều kiện) |
| FEAT-036 | FR-ORD-SEL-001 | P0 | Chọn và đổi một món chính: selection/version và tổng đúng | ORD-Q01, ORD-Q04; PARTIAL (thiết kế có điều kiện) |
| FEAT-037 | FR-ORD-WEEK-001 | P1 | Gửi lựa chọn cả tuần: kết quả từng ngày có trạng thái | ORD-Q05; PARTIAL (thiết kế có điều kiện) |
| FEAT-038 | FR-ORD-SUB-001 | P0 | Chốt tổng suất và phân bổ: order SUBMITTED và breakdown | ORD-Q06; PARTIAL (thiết kế có điều kiện) |
| FEAT-039 | FR-ORD-DEF-001 | P0 | Gán món mặc định khi khóa: qty_default và snapshot | ORD-Q06, ORD-Q07; PARTIAL (thiết kế có điều kiện) |
| FEAT-040 | FR-ORD-LOCK-001 | P0 | Khóa tại hạn và phát hành nguồn kế hoạch: order LOCKED,plan v1 | Q-16, ORD-Q07; PARTIAL (thiết kế có điều kiện) |
| FEAT-041 | FR-ORD-CHG-001 | P0 | Đề nghị và duyệt thay đổi sau khóa: change request và revision nếu duyệt | Q-16, O-06, ORD-Q08; PARTIAL (thiết kế có điều kiện) |
| FEAT-042 | FR-ORD-PXY-001 | P0 | Điều phối nhập hộ: order có nguồn nhập hộ | ORD-Q06; PARTIAL (thiết kế có điều kiện) |
| FEAT-043 | FR-ORD-REM-001 | P1 | Nhắc người chưa chọn: notification/integration outcome | Q-14; PARTIAL (thiết kế có điều kiện) |
| FEAT-044 | FR-ORD-MODE-001 | P1 | Đổi chế độ chọn món: mode version | ORD-Q09; PARTIAL (thiết kế có điều kiện) |
| FEAT-045 | FR-NUTR-DSP-001 | P0 | Xem thông tin món công bố: public-safe meal DTO | NUTR-Q03; PARTIAL (thiết kế có điều kiện) |
| FEAT-046 | FR-NUTR-PROF-001 | P1 | Giữ cổng hồ sơ sức khỏe: chưa mở contract triển khai | O-03; GATED toàn nghiệp vụ |
| FEAT-047 | FR-NUTR-REC-001 | P1 | Giữ cổng gợi ý cá nhân: gợi ý chưa đặc tả thuật toán | O-03; GATED toàn nghiệp vụ |
| FEAT-048 | FR-PLAN-MEAL-001 | P0 | Đọc kế hoạch sản xuất phiên bản: phiếu sản xuất theo món | ORD-Q10; PARTIAL (thiết kế có điều kiện) |

## Ngoài phạm vi phiên này

E7 giao/nhận/doanh thu/đối soát/MISA; E8 website công khai (chỉ dùng lại DTO món); E9 agent phía khách; E10 CRM đầy đủ; E11 mua nguyên liệu/phân ca/QC; E12–E13 báo cáo/lợi nhuận. Không triển khai backend, migration, provider thông báo hay thuật toán sức khỏe. ORD-Q10 không tự mở nhiều MAIN trong R6 khi D-04 đang là cơ sở luồng chọn 1/3.

G-Now vẫn là cổng release; việc viết trước tài liệu không chứng minh đã vượt cổng. Không đổi lịch/ước lượng O-04.

