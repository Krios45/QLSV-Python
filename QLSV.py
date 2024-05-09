from tkinter import *
from tkinter import messagebox
from datetime import date
from tkinter.ttk import Combobox
import json

class SinhVien:
    
    __name = str
    __mssv = int
    __class_name = str
    __dob = str
    __gender = str
    __phone = int
    __email = str
    __address = str

    def __init__(self, name='', mssv=0, class_name='', dob='', gender='', phone=0, email='', address=''):
        self.__name = name
        self.__mssv = mssv
        self.__class_name = class_name
        self.__dob = dob
        self.__gender = gender
        self.__phone = phone
        self.__email = email
        self.__address = address
    
    def __str__(self):
        return f"Tên: {self.__name}\nMSSV: {self.__mssv}\nNgành: {self.__class_name}\nNgày sinh: {self.__dob}\nGiới tính: {self.__gender}\nSô điện thoại: {self.__phone}\nEmail: {self.__email}\nĐịa chỉ: {self.__address}"
          
    def add(self):
        self.__name = Name.get()
        self.__mssv = Id.get()
        self.__class_name = Class.get()
        self.__dob = Dob.get()
        self.__gender = radio.get()
        self.__phone = Number.get()
        self.__email = Email.get()
        self.__address = Address.get()
           
class PhuHuynh:
    
        __dad_name = str
        __dad_dob = str
        __dad_job = str
        __mom_name = str
        __mom_dob = str
        __mom_job = str
    
        def __init__(self, dad_name='', dad_dob='', dad_job='', mom_name='', mom_dob='', mom_job=''):
            self.__dad_name = dad_name
            self.__dad_dob = dad_dob
            self.__dad_job = dad_job
            self.__mom_name = mom_name
            self.__mom_dob = mom_dob
            self.__mom_job = mom_job
        
        def __str__(self):
            return f"Tên bố: {self.__dad_name}\nNgày sinh bố: {self.__dad_dob}\nCông việc bố: {self.__dad_job}\nTên mẹ: {self.__mom_name}\nNgày sinh mẹ: {self.__mom_dob}\nCông việc mẹ: {self.__mom_job}"

        def add(self):
            self.__dad_name = Dad_name.get()
            self.__dad_dob = Dad_birth.get()
            self.__dad_job = Dad_job.get()
            self.__mom_name = Mom_name.get()
            self.__mom_dob = Mom_birth.get()
            self.__mom_job = Mom_job.get()

Danh_sach_sinh_vien = []
Danh_sach_phu_huynh = []
class QuanLySinhVien:

    def add(self):
        sv = SinhVien()
        sv.add()
        sv.__dict__["STT"] = len(Danh_sach_sinh_vien) + 1
        ph = PhuHuynh()
        ph.add()
        ph.__dict__["STT"] = len(Danh_sach_phu_huynh) + 1
        Danh_sach_sinh_vien.append(sv.__dict__)
        Danh_sach_phu_huynh.append(ph.__dict__)
        with open("Danh_sach_sinh_vien.json", "w") as f:
            f.write(json.dumps(Danh_sach_sinh_vien, indent=4))
        with open("Danh_sach_sinh_vien.json", "r") as f:
            data = json.load(f)
        for student in data:
            if student["_SinhVien__gender"] == 1:
                student["_SinhVien__gender"] = "Nam"
            else:
                student["_SinhVien__gender"] = "Nu"
        with open("Danh_sach_sinh_vien.json", "w") as f:
            f.write(json.dumps(data, indent=4))     
        with open("Danh_sach_phu_huynh.json", "w") as f:
            f.write(json.dumps(Danh_sach_phu_huynh, indent=4))
       
    def delete(self):
        n = Delete.get()
        with open("Danh_sach_sinh_vien.json", "r") as f:
            data = json.load(f)
        for student in data:
            if student["_SinhVien__mssv"] == n:
                data.remove(student)  
                messagebox.showinfo("Thông báo", "Xoá thành công!")
                with open("Danh_sach_sinh_vien.json", "w") as f:
                    f.write(json.dumps(data, indent=4))
                    Delete.set("")
                return
        messagebox.showerror("Lỗi", "Không tìm thấy sinh viên")  
        Delete.set("")          
        
    def search(self):
        n = Search.get()
        with open("Danh_sach_sinh_vien.json", "r") as f:
            data = json.load(f)
        for student in data:
            if student["_SinhVien__mssv"] == n:
                # STUDENT'S INFOMATION
                student_info = LabelFrame(show_window, text="SINH VIÊN", font="Arial 25", bd=2, width=650, height=300, fg="tomato", bg=framebg, relief=GROOVE)
                student_info.place(x=30,y=30)
                Label(student_info, text= f"- Tên: {student["_SinhVien__name"]}", font="Arial 15").place(x=20,y=20)
                Label(student_info, text= f"- Mã số sinh viên: {student["_SinhVien__mssv"]}", font="Arial 15").place(x=20,y=80)
                Label(student_info, text= f"- Ngành học: {student["_SinhVien__class_name"]}", font="Arial 15").place(x=20,y=140)
                Label(student_info, text= f"- Ngày sinh: {student["_SinhVien__dob"]}", font="Arial 15").place(x=20,y=200)
                Label(student_info, text= f"- Giới tính: {student["_SinhVien__gender"]}", font="Arial 15").place(x=320,y=20)
                Label(student_info, text= f"- Số điện thoại: {student["_SinhVien__phone"]}", font="Arial 15").place(x=320,y=80)
                Label(student_info, text= f"- Email: {student["_SinhVien__email"]}", font="Arial 15").place(x=320,y=140)
                Label(student_info, text= f"- Địa chỉ: {student["_SinhVien__address"]}", font="Arial 15").place(x=320,y=200)      
                Search.set("")
                return
        messagebox.showerror("Lỗi", "Không tìm thấy sinh viên")
        Search.set("")         
        
# GUI - Python
def Them():
    fields = [Name, Id, Dob, radio, Number, Email, Address, Class, Dad_name, Dad_birth, Dad_job, Mom_name, Mom_birth, Mom_job]
    for field in fields:
        if field.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
    sinhvien = QuanLySinhVien()
    sinhvien.add()
    messagebox.showinfo("Thông báo", "Thêm thành công")
    Name.set("")
    Id.set("")
    Dob.set("")
    radio.set(0)
    Number.set("")
    Email.set("")
    Address.set("")
    Class.set("")
    Dad_name.set("")
    Dad_birth.set("")
    Dad_job.set("")
    Mom_name.set("")
    Mom_birth.set("")
    Mom_job.set("")
                
def Thoat():
    root.quit()

# SEARCH WINDOW
search_window = None

def on_closing_search_window():
    global search_window
    search_window.destroy()
    search_window = None

def create_search_window():
    global search_window
    if search_window is None:
        search_window = Toplevel()
        search_window.title("Tìm kiếm sinh viên")
        search_window.geometry("500x200+550+250")
        Label(search_window, text="Nhập mã số sinh viên để tìm kiếm!", font="Arial 15").place(x=110,y=40)
        search_entry = Entry(search_window, textvariable=Search, width=25, font="Arial 13").place(x=150,y=80)
        Button(search_window, text="Tìm kiếm", width=10, height=2, font="Arial 13", bg="light blue", fg="black", command=create_show_window).place(x=200,y=120)
        search_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_search_window())
    else:
        search_window.lift()

# SHOW STUDENT'S INFORMATION
show_window = None

def on_closing_show_window():
    global show_window
    show_window.destroy()
    show_window = None

def create_show_window():
    global show_window
    if show_window is None:
        show_window = Toplevel()
        show_window.title("Thông tin sinh viên")
        show_window.geometry("700x350+450+200")
        sinhvien = QuanLySinhVien()
        sinhvien.search()
        show_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_show_window())
    else:
        show_window.lift()

# DELETE WINDOW
delete_window = None

def Xoa():
    sinhvien = QuanLySinhVien()
    sinhvien.delete()
    
def on_closing_delete_window():
    global delete_window
    delete_window.destroy()
    delete_window = None

def create_delete_window():
    global delete_window
    if delete_window is None:
        delete_window = Toplevel()
        delete_window.title("Xoá sinh viên")
        delete_window.geometry("500x200+550+250")
        Label(delete_window, text="Nhập mã số sinh viên để xoá!", font="Arial 15").place(x=130,y=40)
        delete_entry = Entry(delete_window, textvariable=Delete, width=17, font="Arial 13").place(x=175,y=80)
        Button(delete_window, text="Xoá", width=10, height=2, font="Arial 13", bg="light blue", fg="black", command=Xoa).place(x=200,y=120)
        delete_window.protocol("WM_DELETE_WINDOW", lambda: on_closing_delete_window())
    else:
        delete_window.lift()
                       
background="sky blue"
framebg="white"
framefg="#06283D"

root = Tk()
root.title("Đăng kí sinh viên")
root.geometry("1250x750+100+20")
root.config(bg=background)

# Top Frame
Label(root, text="Email: 23110311@st.vju.ac.vn", width=10, height=3, bg="#f0687c", anchor="e").pack(side=TOP, fill=X)
Label(root, text="Đăng kí sinh viên", width=10, height=2, bg="yellow", fg="blue", font=("Arial 20 bold")).pack(side=TOP, fill=X)

# Registration and Date
Label(root, text="Date:", font="Arial 20", fg=framebg, bg=background).place(x=100,y=140)

Registration = StringVar()
Date = StringVar()

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="Arial 15")
date_entry.place(x=180,y=147)
Date.set(d1)

# Student Information
student = LabelFrame(root, text="Thông tin sinh viên", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
student.place(x=30,y=200)

Label(student, text="Họ và tên:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=20)
Label(student, text="Ngày sinh:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=70)
Label(student, text="Giới tính:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=120)
Label(student, text="Ngành học:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=170)
Label(student, text="Mã số:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=20)
Label(student, text="Số ĐT:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=70)
Label(student, text="Email:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=120)
Label(student, text="Địa chỉ:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=170)

Name = StringVar()
name_entry = Entry(student, textvariable=Name, width=30, font="Arial 13").place(x=130, y=20)

Dob = StringVar()
dob_entry = Entry(student, textvariable=Dob, width=30, font="Arial 13").place(x=130, y=70)

radio = IntVar()
r1 = Radiobutton(student, text="Nam", variable=radio, value=1, font="Arial 13", bg=framebg, fg=framefg).place(x=130, y=120)
r2 = Radiobutton(student, text="Nữ", variable=radio, value=2, font="Arial 13", bg=framebg, fg=framefg).place(x=200, y=120)


Id=StringVar()
string_entry = Entry(student, textvariable=Id, width=30, font="Arial 13").place(x=550, y=20)

Number = StringVar()
number_entry = Entry(student, textvariable=Number, width=30, font="Arial 13").place(x=550, y=70)

Email = StringVar()
email_entry = Entry(student, textvariable=Email, width=30, font="Arial 13").place(x=550, y=120)

Address = StringVar()
address_entry = Entry(student, textvariable=Address, width=30, font="Arial 13").place(x=550, y=170)

Class = Combobox(student, values=["BSCE", "BJS", "ECE", "ESAS", "FTH", "MJM"], font="Arial 13", width=17, state="r")
Class.place(x=130, y=170)

# Parents Information
parent = LabelFrame(root, text="Thông tin phụ huynh", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
parent.place(x=30,y=470)

Label(parent, text="Họ tên bố:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=30)
Label(parent, text="Ngày sinh:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=80)
Label(parent, text="Công việc:", font="Arial 13", fg=framefg, bg=framebg).place(x=30, y=130)

Label(parent, text="Họ tên mẹ:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=30)
Label(parent, text="Ngày sinh:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=80)
Label(parent, text="Công việc:", font="Arial 13", fg=framefg, bg=framebg).place(x=450, y=130)

Dad_name = StringVar()
dad_entry = Entry(parent, textvariable=Dad_name, width=30, font="Arial 13").place(x=130, y=30)

Dad_birth = StringVar()
dad_entry = Entry(parent, textvariable=Dad_birth, width=30, font="Arial 13").place(x=130, y=80)

Dad_job = StringVar()
dad_entry = Entry(parent, textvariable=Dad_job, width=30, font="Arial 13").place(x=130, y=130)


Mom_name = StringVar()
mom_entry = Entry(parent, textvariable=Mom_name, width=30, font="Arial 13").place(x=550, y=30)

Mom_birth = StringVar()
mom_entry = Entry(parent, textvariable=Mom_birth, width=30, font="Arial 13").place(x=550, y=80)

Mom_job = StringVar()
mom_entry = Entry(parent, textvariable=Mom_job, width=30, font="Arial 13").place(x=550, y=130)

Delete = StringVar()
Search = StringVar()

# Button
Button(root, text = "Lưu sinh viên", width = 20, height = 2, font="Arial 12", bg="light blue", command=Them).place(x=1000, y=250)
Button(root, text = "Xoá sinh viên", width = 20, height = 2, font="Arial 12", bg="light blue", command=create_delete_window).place(x=1000, y=350)
Button(root, text = "Thoát chương trình", width = 20, height = 2, font="Arial 12", bg="light blue", command=Thoat).place(x=1000, y=550)
Button(root, text = "Tìm kiếm sinh viên", width = 20, height = 2, font="Arial 12", bg="light blue", command=create_search_window).place(x=1000, y=450)


root.mainloop()





