import tkinter as tk

"""
Tham số Sticky	Tác dụng căn chỉnh	Ứng dụng thực tế
sticky="w"	Bám lề trái	Dùng cho nhãn (Label) văn bản.
sticky="e"	Bám lề phải	Dùng cho các con số hoặc nút "Hủy".
sticky="ew"	Dãn hết chiều ngang	Dùng cho ô nhập liệu (Entry).
sticky="nsew"	Lấp đầy mọi hướng	Dùng cho các bảng dữ liệu lớn (Treeview).

"""


root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")

# --- ĐIỂM MỚI 1: Cấu hình trọng số cho cột 1 ---
# Lệnh này nói rằng: Cột 1 có quyền chiếm lấy không gian thừa (weight=1)
root.columnconfigure(1, weight=1)


# 1. Tạo các thành phần (nhưng chưa hiện lên)
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)

'''
1.	sticky="w": Bắt các chữ phải bám sát lề bên trái (West - hướng Tây).
2.	padx / pady: Tạo khoảng cách đệm để các ô không dính vào nhau.
3.	grid(row=0, column=0): Đặt nhãn mã sinh viên ở hàng 0, cột 0.
4.	grid(row=0, column=1): Đặt ô nhập mã sinh viên ở hàng 0, cột 1.
'''

""" code cũ
# Hàng 0
nhan_ma_sv.grid(row=0, column=0)
o_nhap_ma_sv.grid(row=0, column=1)

# Hàng 1
nhan_ho_ten.grid(row=1, column=0)
o_nhap_ho_ten.grid(row=1, column=1)

"""

# Hàng 0 với căn lề trái (sticky="w") và khoảng cách (padx, pady)
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10)

# --- ĐIỂM MỚI 2: Dùng sticky="ew" cho ô nhập ---
# "ew" (East-West) nghĩa là kéo giãn từ hướng Đông sang hướng Tây
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
#o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10)


# Hàng 1
nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


root.mainloop()
