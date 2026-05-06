# Hệ Thống Quản Lý Bãi Giữ Xe Sinh Viên (QLDoXeV1)

Một ứng dụng quản lý bãi đỗ xe dành cho sinh viên được viết bằng Python. Dự án cung cấp cả giao diện dòng lệnh (CLI) và giao diện đồ họa người dùng (GUI - Tkinter), giúp quản lý việc ra vào bãi đỗ xe, tính phí tự động dựa trên số dư tài khoản, và theo dõi tình trạng bãi xe trong thời gian thực.

## 🚀 Tính Năng Chính

1. **Quản lý Sinh viên & Tài khoản:** 
   - Thêm sinh viên mới vào hệ thống.
   - Hỗ trợ 2 loại vé: **Vé ngày** (thanh toán theo lượt) và **Vé tháng** (trọn gói).
   - Quản lý số dư tài khoản của từng sinh viên.

2. **Kiểm soát Xe Ra/Vào (Quẹt thẻ):**
   - Quẹt thẻ để cho xe vào/ra bãi.
   - Tự động kiểm tra sức chứa của bãi xe trước khi cho xe vào.
   - **Tự động trừ tiền** vào số dư tài khoản đối với sinh viên dùng vé ngày. Cảnh báo nếu số dư không đủ.

3. **Nạp Tiền & Nâng Cấp Vé:**
   - Nạp thêm tiền vào tài khoản sinh viên.
   - Nâng cấp từ vé ngày lên vé tháng tự động (phí sẽ được trừ trực tiếp vào số dư).

4. **Thống Kê (Dashboard):**
   - Theo dõi doanh thu trong ngày.
   - Hiển thị số lượng xe đang nằm trong bãi và số chỗ còn trống.
   - Danh sách chi tiết các xe đang có mặt tại bãi xe lúc hiện tại.

5. **Nhập/Xuất Dữ liệu (Import/Export):**
   - Hỗ trợ xuất danh sách sinh viên ra file CSV.
   - Nhập danh sách sinh viên từ file CSV để hỗ trợ quá trình di chuyển dữ liệu hàng loạt.

6. **Tạo Dữ Liệu Mẫu (Seed Data):**
   - Tự động sinh danh sách sinh viên giả lập, nhật ký ra vào xe, và giao dịch để người dùng có thể trải nghiệm ngay hệ thống.

## 🛠️ Công Nghệ Sử Dụng

- **Ngôn Ngữ:** Python 3.x
- **Giao Diện:** Tkinter (cho GUI), Console (cho CLI)
- **Cơ Sở Dữ Liệu:** SQLite (`parking.db`) kết hợp với lưu trữ dạng CSV để dễ quản lý dữ liệu tĩnh (`students.csv`, `parking_logs.csv`).

## 📁 Cấu Trúc Thư Mục

- `main.py` : Điểm khởi chạy chính của chương trình. Điều hướng giữa các chế độ CLI, GUI, và Seed.
- `gui.py` : Chứa code của giao diện đồ họa Tkinter.
- `cli.py` : Chứa code của giao diện dòng lệnh.
- `services.py` : Tầng nghiệp vụ xử lý các logic như vào bãi, tính phí, nâng cấp vé.
- `database.py` : Xử lý giao tiếp với CSDL SQLite (query, transaction).
- `models.py` : Định nghĩa các lớp và kiểu dữ liệu.
- `seed_data.py` : Script tự động tạo dữ liệu mẫu.

## 💻 Hướng Dẫn Chạy Cài Đặt

1. **Cài đặt Python:** Yêu cầu máy tính đã cài đặt sẵn Python 3.x.
2. **Khởi tạo dữ liệu mẫu** *(Khuyên dùng cho lần đầu chạy)*:
   Mở terminal / command prompt và chạy:
   ```bash
   python main.py seed
   ```
3. **Chạy ứng dụng với giao diện (GUI):**
   ```bash
   python main.py gui
   ```
4. **Chạy ứng dụng với dòng lệnh (CLI):**
   ```bash
   python main.py cli
   ```
   *(Lưu ý: Nếu chỉ gõ `python main.py`, chương trình sẽ mặc định chạy chế độ CLI)*

## 📄 Quy Trình Hoạt Động Cơ Bản
- **Bước 1:** Khởi tạo dữ liệu bằng lệnh `seed`.
- **Bước 2:** Bật GUI lên, vào mục Quản lý sinh viên để xem danh sách hoặc nạp tiền nếu cần.
- **Bước 3:** Sử dụng tính năng "Quẹt thẻ" bằng mã sinh viên để giả lập việc xe chạy qua cổng.
- **Bước 4:** Xem mục "Bãi xe & Thống kê" để thấy số liệu biến động, vị trí chỗ trống giảm đi và doanh thu tăng lên.
