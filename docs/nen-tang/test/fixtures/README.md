---
id: DOC-NEN-TANG-TEST-FIXTURES-README
title: Fixture giả lập E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, fixture, e1]
author: BA
last_updated: 2026-11-16
---
# Fixture giả lập E1: Nền tảng

Draft · 16/11/2026 · Dữ liệu giả lập, không phải tài khoản thật.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo bộ tài khoản, cơ sở, ủy quyền, tham số giả lập theo khuôn chung các epic |

[synthetic.json](synthetic.json) gồm hai cơ sở A, B; một tài khoản cho mỗi vai trò nội bộ, trong đó hai quản lý cơ sở thuộc hai cơ sở khác nhau để thử cách ly phạm vi (tiêu chí R1); hai tài khoản dịch vụ cho agent; một ủy quyền có hạn; một tham số.

- Không có mật khẩu, token hay secret trong file. Môi trường test tự cấp và không ghi vào evidence.
- Tên đăng nhập chỉ là ví dụ; hình thức đăng nhập chờ N-01, người giữ quyền quản trị chờ N-02.
- Không phải seed runtime. Ca dùng fixture: [ca hệ thống E1](../system-cases.md) và [test case E1](../test-cases.md).
