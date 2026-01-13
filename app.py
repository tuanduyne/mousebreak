import tkinter as tk
import random
from tkinter import messagebox

SO_HANG = 3
SO_COT = 3
THOI_GIAN_CHOI = 30      
TOC_DO_CHUOT = 1500      

diem = 0
thoi_gian_con = THOI_GIAN_CHOI
vi_tri_chuot = (-1, -1)

def hien_chuot():
    global vi_tri_chuot

 
    for i in range(SO_HANG):
        for j in range(SO_COT):
            nut[i][j].config(text="")


    hang = random.randint(0, SO_HANG - 1)
    cot = random.randint(0, SO_COT - 1)
    vi_tri_chuot = (hang, cot)

    nut[hang][cot].config(text="🐭")

def bam_o(hang, cot):
    global diem

    if (hang, cot) == vi_tri_chuot:
        diem += 1
        nhan_diem.config(text=f"Điểm: {diem}")
        hien_chuot()

def dem_nguoc():
    global thoi_gian_con

    if thoi_gian_con > 0:
        thoi_gian_con -= 1
        nhan_thoi_gian.config(text=f"Thời gian: {thoi_gian_con}s")
        cua_so.after(1000, dem_nguoc)
    else:
        ket_thuc_game()

def ket_thuc_game():
    messagebox.showinfo("Kết thúc", f"Hết giờ!\nĐiểm của bạn: {diem}")
    khoa_game()

def khoa_game():
    for i in range(SO_HANG):
        for j in range(SO_COT):
            nut[i][j].config(state="disabled")

cua_so = tk.Tk()
cua_so.title("Game Đập Chuột")
cua_so.geometry("300x350")

nhan_diem = tk.Label(cua_so, text="Điểm: 0", font=("Arial", 12))
nhan_diem.pack()

nhan_thoi_gian = tk.Label(
    cua_so,
    text=f"Thời gian: {THOI_GIAN_CHOI}s",
    font=("Arial", 12)
)
nhan_thoi_gian.pack()

khung = tk.Frame(cua_so)
khung.pack(pady=10)

nut = [[None for _ in range(SO_COT)] for _ in range(SO_HANG)]

for i in range(SO_HANG):
    for j in range(SO_COT):
        nut[i][j] = tk.Button(
            khung,
            text="",
            font=("Arial", 18),
            width=4,
            height=2,
            command=lambda h=i, c=j: bam_o(h, c)
        )
        nut[i][j].grid(row=i, column=j, padx=5, pady=5)

hien_chuot()
dem_nguoc()

def lap_chuot():
    if thoi_gian_con > 0:
        hien_chuot()
        cua_so.after(TOC_DO_CHUOT, lap_chuot)

lap_chuot()

cua_so.mainloop()
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)