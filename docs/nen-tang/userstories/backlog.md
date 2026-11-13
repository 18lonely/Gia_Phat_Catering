---
id: DOC-NEN-TANG-USERSTORIES-BACKLOG
title: Backlog E1
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Backlog E1

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Story point chưa ước lượng (O-04). P1 giữ trạng thái phụ thuộc, không tự đưa vào cam kết MVP. Mỗi story có3 AC; xem test riêng cho BR/ERR/NFR.

| Story | Nội dung | FR | Ưu tiên | UC / UI |
| :--- | :--- | :--- | :--- | :--- |
| US-CORE-001 | Là một nhân viên nội bộ, tôi muốn đăng nhập nội bộ để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-LGN-001 | P0 | [UC-CORE-001](../usecases/UC-CORE-001.md) / UI-CORE-01 |
| US-CORE-002 | Là một nhân viên nội bộ, tôi muốn làm mới phiên để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-LGN-002 | P0 | [UC-CORE-002](../usecases/UC-CORE-002.md) / UI-CORE-01 |
| US-CORE-003 | Là một nhân viên nội bộ, tôi muốn đăng xuất để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-LGN-003 | P0 | [UC-CORE-003](../usecases/UC-CORE-003.md) / UI-CORE-01 |
| US-CORE-004 | Là một nhân viên nội bộ, tôi muốn xác thực 2 bước để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-LGN-004 | P1 | [UC-CORE-004](../usecases/UC-CORE-004.md) / UI-CORE-01 |
| US-CORE-005 | Là một nhân viên nội bộ, tôi muốn đổi mật khẩu để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-PWD-001 | P0 | [UC-CORE-005](../usecases/UC-CORE-005.md) / UI-CORE-01 |
| US-CORE-006 | Là một nhân viên nội bộ, tôi muốn cấp lại mật khẩu để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-PWD-002 | P0 | [UC-CORE-006](../usecases/UC-CORE-006.md) / UI-CORE-01 |
| US-CORE-007 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tạo tài khoản nội bộ để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-ACC-001 | P0 | [UC-CORE-007](../usecases/UC-CORE-007.md) / UI-CORE-02 |
| US-CORE-008 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn khoá / mở khoá tài khoản để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-ACC-002 | P0 | [UC-CORE-008](../usecases/UC-CORE-008.md) / UI-CORE-02 |
| US-CORE-009 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn sửa vai trò và cơ sở để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-ACC-003 | P0 | [UC-CORE-009](../usecases/UC-CORE-009.md) / UI-CORE-02 |
| US-CORE-010 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn xem nhật ký đăng nhập để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-ACC-004 | P0 | [UC-CORE-010](../usecases/UC-CORE-010.md) / UI-CORE-02 |
| US-CORE-011 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn kiểm quyền mỗi yêu cầu để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-RBAC-001 | P0 | [UC-CORE-011](../usecases/UC-CORE-011.md) / UI-CORE-02 |
| US-CORE-012 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn xem ma trận vai trò – quyền để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-RBAC-002 | P0 | [UC-CORE-012](../usecases/UC-CORE-012.md) / UI-CORE-02 |
| US-CORE-013 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn uỷ quyền duyệt khi vắng để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-RBAC-003 | P1 | [UC-CORE-013](../usecases/UC-CORE-013.md) / UI-CORE-02 |
| US-CORE-014 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tài khoản dịch vụ cho agent để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-AUTH-SVC-001 | P0 | [UC-CORE-014](../usecases/UC-CORE-014.md) / UI-CORE-02 |
| US-CORE-015 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn ghi nhật ký thay đổi để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-AUD-001 | P0 | [UC-CORE-015](../usecases/UC-CORE-015.md) / UI-CORE-03 |
| US-CORE-016 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tra cứu nhật ký để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-AUD-002 | P0 | [UC-CORE-016](../usecases/UC-CORE-016.md) / UI-CORE-03 |
| US-CORE-017 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn bắt buộc lý do để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-AUD-003 | P0 | [UC-CORE-017](../usecases/UC-CORE-017.md) / UI-CORE-03 |
| US-CORE-018 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn huỷ thay cho xoá để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-AUD-004 | P0 | [UC-CORE-018](../usecases/UC-CORE-018.md) / UI-CORE-03 |
| US-CORE-019 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn quản lý tham số để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-PRM-001 | P0 | [UC-CORE-019](../usecases/UC-CORE-019.md) / UI-CORE-04 |
| US-CORE-020 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn duyệt thay đổi tham số để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-PRM-002 | P0 | [UC-CORE-020](../usecases/UC-CORE-020.md) / UI-CORE-04 |
| US-CORE-021 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tạo thông báo trong hệ thống để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-NTF-001 | P0 | [UC-CORE-021](../usecases/UC-CORE-021.md) / UI-CORE-05 |
| US-CORE-022 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn trạng thái thông báo để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-NTF-002 | P0 | [UC-CORE-022](../usecases/UC-CORE-022.md) / UI-CORE-05 |
| US-CORE-023 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn gửi qua kênh ngoài để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-NTF-003 | P1 | [UC-CORE-023](../usecases/UC-CORE-023.md) / UI-CORE-05 |
| US-CORE-024 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tải tệp lên để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-FILE-001 | P0 | [UC-CORE-024](../usecases/UC-CORE-024.md) / UI-CORE-06 |
| US-CORE-025 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn tác vụ nền để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-JOB-001 | P0 | [UC-CORE-025](../usecases/UC-CORE-025.md) / UI-CORE-06 |
| US-CORE-026 | Là một quản trị hoặc người được cấp quyền theo SRS, tôi muốn kiểm tra sức khoẻ để thao tác được kiểm soát và truy vết đúng phạm vi. | FR-SYS-HLT-001 | P0 | [UC-CORE-026](../usecases/UC-CORE-026.md) / UI-CORE-06 |
