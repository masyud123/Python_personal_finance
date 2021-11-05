from tkinter import *
import io
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import errorcode
import pymysql
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PersonalFinance:
    def __init__(self,parent, title):
        self.parent = parent
        self.parent.title(title)
        self.layoutLogin()
        self.cnx = mysql.connector.connect(
            user='root', 
            password='',
            host='127.0.0.1',
            database='finansial')
        self.my_cursor = self.cnx.cursor()

#Login
    def layoutLogin(self):
        self.lyLogin = Frame(self.parent, bg="grey")
        self.lyLogin.pack(fill=BOTH, expand=1)

        self.frm_login = Frame(self.lyLogin, width=500, height=400, bg="white", highlightbackground="black", highlightthicknes=1) 
        self.frm_login.place(relx=.35, rely=.2)

        Label(self.frm_login, font= "Arial 17 bold", text = "Selamat Datang", bg = "white").place(relx=.5, y=45, anchor="center")

        Label(self.frm_login, font= "Arial 10 normal", text = "Masukkan Email", bg = "white").place(relx=.1, y=100)
        self.akun = Entry(self.frm_login, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.akun.place(relx=.1, y=140, height=35)

        Label(self.frm_login, font= "Arial 10 normal", text = "Masukkan Password", bg = "white").place(relx=.1, y=200)
        self.passwd = Entry(self.frm_login, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.passwd.default_show_val = self.passwd["show"]
        self.passwd["show"]="*"
        self.passwd.place(relx=.1, y=240, height=35)

        def showpassword():
            if self.tampil.var.get():
                self.passwd['show'] = "*"
            else:
                self.passwd['show'] = ""
        self.tampil = Checkbutton(self.frm_login, bd=0, text="Tampil Password",bg ="white",command=showpassword,onvalue=False,offvalue=True)
        self.tampil.var = BooleanVar(value=1)
        self.tampil['variable'] = self.tampil.var
        self.tampil.place(relx=.21, y=295, anchor="center")

        def login():
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="finansial")
                cur=con.cursor()
                cur.execute("select * from t_user where email=%s and password=%s", (self.akun.get(),self.passwd.get()))
                self.row2 = cur.fetchone()
                if self.row2==None:
                    messagebox.showerror("Error", "Username atau Password Salah")
                else:
                    self.lyLogin.pack_forget()
                    self.layoutKomponen()
                con.close()
            except Exception as es:
                print(es)
       
        self.masuk = Button(self.frm_login, bg="blue", text="Masuk", command=login, font="Arial 11 bold", fg='white', bd=1)
        self.masuk.place(relx=.5, y=325, anchor="center")

        self.buat_akun = Button(self.frm_login, bg="white", text="Belum punya akun ? Buat akun", command=self.layoutRegistrasi, font="Arial 9 normal", fg='blue', bd=0)
        self.buat_akun.place(relx=.5, y=365, anchor="center")

#buat akun    
    def layoutRegistrasi(self):
        self.lyLogin.pack_forget()
        self.registrasi = Frame(self.parent, bg="grey")
        self.registrasi.pack(fill=BOTH, expand=1)

        self.frm_regis = Frame(self.registrasi, width=500, height=650, bg="white", highlightbackground="black", highlightthicknes=1) 
        self.frm_regis.place(relx=.35, rely=.05)

        Label(self.frm_regis, font= "Arial 17 bold", text = "Silakan Registrasi", bg = "white").place(relx=.5, y=45, anchor="center")

        Label(self.frm_regis, font= "Arial 10 normal", text = "Masukkan Nama", bg = "white").place(relx=.1, y=100)
        self.nama = Entry(self.frm_regis, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.nama.place(relx=.1, y=140, height=35)

        Label(self.frm_regis, font= "Arial 10 normal", text = "Masukkan NO. HP", bg = "white").place(relx=.1, y=200)
        self.NoHP = Entry(self.frm_regis, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.NoHP.place(relx=.1, y=240, height=35)

        Label(self.frm_regis, font= "Arial 10 normal", text = "Masukkan Password", bg = "white").place(relx=.1, y=300)
        self.pasword = Entry(self.frm_regis, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.pasword.place(relx=.1, y=340, height=35)

        Label(self.frm_regis, font= "Arial 10 normal", text = "Masukkan Email", bg = "white").place(relx=.1, y=400)
        self.email = Entry(self.frm_regis, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.email.place(relx=.1, y=440, height=35)

        Label(self.frm_regis, font= "Arial 10 normal", text = "Masukkan Pekerjaan", bg = "white").place(relx=.1, y=500)
        self.pekerjaan = Entry(self.frm_regis, bg="#e9eceb", width=44, font="arial 12 normal", highlightbackground="black", highlightthicknes=1)
        self.pekerjaan.place(relx=.1, y=540, height=35)

        self.simpan11 = Button(self.frm_regis, bg="blue", text="Simpan", font="Arial 11 bold", command=self.Registrasii, fg='white', bd=1)
        self.simpan11.place(relx=.35, y=610, anchor="center")

        self.batal22 = Button(self.frm_regis, bg="red", text="Batal", command=self.batall, font="Arial 11 bold", fg='white', bd=1)
        self.batal22.place(relx=.65, y=610, anchor="center")

    def Registrasii(self):
        self.my_cursor.execute("INSERT INTO `t_user` (NoHP, password, nama, pekerjaan, email) VALUES (%s,%s, %s, %s, %s)",
            (self.NoHP.get(), self.pasword.get(), self.nama.get(), self.pekerjaan.get(), self.email.get()))
        self.cnx.commit()
        self.nama.delete(0,END)
        self.NoHP.delete(0,END)
        self.pasword.delete(0,END)
        self.email.delete(0,END)
        self.pekerjaan.delete(0,END)
        self.registrasi.pack_forget()
        self.lyLogin.pack(fill=BOTH, expand=1)

    def batall(self, event=None):
        self.registrasi.pack_forget()
        self.lyLogin.pack(fill=BOTH, expand=1)
    
    def layoutKomponen(self):
        self.mainfr = Frame(self.parent, bg="white")
        self.mainfr.pack(fill=BOTH, expand=1)

    #navbar
        self.frame1 = Frame(self.mainfr, width=1256, height=70, bg="white", highlightbackground="black", highlightthicknes=1)
        self.frame1.place(x=99, y=10)
        self.frame1.propagate(False)
        iduser = self.row2[0]
        self.my_cursor.execute("SELECT nama FROM t_user where idUser = %s", (str(iduser),))
        result = self.my_cursor.fetchone()[0]

        load = Image.open("user.png")
        load = load.resize((35, 35), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.frame1, image=render, bd=0,bg ="white")
        img.image = render
        img.place(x=60, rely=.5, anchor="center")
        self.txtUser = Label(self.frame1, font= "Arial 9 normal", text = result, bg = "white")
        self.txtUser.place(x=87, y=15)

    #sidebar
        frame2 = Frame(self.mainfr, width=88, height=766, bg="white", highlightbackground="black", highlightthicknes=1)
        frame2.place(x=12, y=10)
        frame2.propagate(False)

        load = Image.open("home.png")
        load = load.resize((30, 30), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(frame2, image=render, bd=0, command=self.home, bg ="white")
        img.image = render
        img.place(relx=.5, y=37, anchor="center")
        Label(frame2, font= "Arial 10 normal", text = "Dashboard", bg = "white").place(relx=.5, y=68, anchor="center")

        load = Image.open("dompet.png")
        load = load.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.img = Button(frame2, image=render, bd=0, command=self.dompet, bg ="white", fg = "#1aa333")
        self.img.image = render
        self.img.place(relx=.5, y=130, anchor="center")
        Label(frame2, font= "Arial 10 normal", text = "Transaksi", bg = "white").place(relx=.5, y=160, anchor="center")

        load = Image.open("report.png")
        load = load.resize((27, 27), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.img1 = Button(frame2, image=render, command=self.diagram, bd=0,bg ="white")
        self.img1.image = render
        self.img1.place(relx=.5, y=223, anchor="center")
        Label(frame2, font= "Arial 10 normal", text = "Laporan", bg = "white").place(relx=.5, y=250, anchor="center")

        load = Image.open("history.png")
        load = load.resize((29, 29), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.img = Button(frame2, image=render,command=self.history, bd=0,bg ="white")
        self.img.image = render
        self.img.place(relx=.5, y=315, anchor="center")
        Label(frame2, font= "Arial 10 normal", text = "Riwayat", bg = "white").place(relx=.5, y=345, anchor="center")
        Label(frame2, font= "Arial 10 normal", text = "Transaksi", bg = "white").place(relx=.5, y=365, anchor="center")

    #frame kosong/utama
        self.frame3 = Frame(self.mainfr, width=1256, height=766, bg="#e9eceb", highlightbackground="black", highlightthicknes=1)
        self.frame3.place(x=99, y=79)
        self.frame3.propagate(False)

    #frame bulan ini
        self.frame_bl_ini = Frame(self.frame3, width=550, height=430, bg="white", highlightbackground="black", highlightthicknes=1)

    #frame transaksi
        self.frametrans = Frame(self.frame3, width=550, height=70, bg="white", highlightbackground="black", highlightthicknes=1)

    #logika perhitungan    
        self.selesai()
        self.btnTransaksi = Button(self.frame_bl_ini, bg="#1aa333", text="Tambah Transaksi", command=self.tambah, font="Arial 11 bold", fg='white', bd=1)
        self.btnTransaksi.place(relx=.5, rely=.38, anchor="center")

    #tambah transaksi
        self.frame6 = Frame(self.frame3, width=550, height=300, bg="white", highlightbackground="black", highlightthicknes=1)

        Label(self.frame6, text = "Pemasukan", bg = "white", font= "Arial 10 bold").place(x=30, y=20)
        Label(self.frame6, text = "Pengeluaran", bg = "white", font= "Arial 10 bold").place(x=30, y=80)
        Label(self.frame6, text = "Tanggal", bg = "white", font= "Arial 10 bold").place(relx=.2, y=145, anchor="center")
        Label(self.frame6, text = "Bulan", bg = "white", font= "Arial 10 bold").place(relx=.5, y=145, anchor="center")
        Label(self.frame6, text = "Tahun", bg = "white", font= "Arial 10 bold").place(relx=.8, y=145, anchor="center")
        Label(self.frame6, text = "Rp.", bg = "white", font= "Arial 10 bold").place(x=330, y=20)
        Label(self.frame6, text = "Rp.", bg = "white", font= "Arial 10 bold").place(x=330, y=80)

        self.isian1 = ttk.Combobox(self.frame6, values = ("Gaji", "Tunjangan", "Hadiah", "Lainya"))
        self.isian1.place(x=200, y=30, anchor="center")

        self.duwet1 = Entry(self.frame6)
        self.duwet1.place(relx=.8, y=30, anchor="center")

        self.isian2 = ttk.Combobox(self.frame6, values = ("Tagihan", "Keluarga", "Kesehatan", "Hiburan", "Lainya"))
        self.isian2.place(x=200, y=90, anchor="center")

        self.duwet2 = Entry(self.frame6)
        self.duwet2.place(relx=.8, y=90, anchor="center")

        self.tgl = Entry(self.frame6)
        self.tgl.place(relx=.2, y=170, anchor="center")

        self.bulan = ttk.Combobox(self.frame6, values = ("Januari", "Februari", "Maret", "April", "Mei",
         "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"))
        self.bulan.place(relx=.5, y=170, anchor="center")

        self.tahun = Entry(self.frame6)
        self.tahun.place(relx=.8, y=170, anchor="center")

        self.btnbatal = Button(self.frame6, bg="red", text="Batal", command=self.batal, font="Arial 11 bold", fg='white', bd=1)
        self.btnbatal.place(relx=.4, rely=.8, anchor="center")

        self.btnselesai = Button(self.frame6, bg="#1aa333", text="Selesai", font="Arial 11 bold", fg='white', bd=1, command=self.tambahtransaksi)
        self.btnselesai.place(relx=.6, rely=.8, anchor="center")

    #frame home
        self.framerumah = Frame(self.frame3, width=400, height=520, bg="white", highlightbackground="black", highlightthicknes=1) 
        self.framerumah.place(relx=.5, y=310, anchor=CENTER)   

        self.my_cursor.execute("SELECT nama FROM t_user where idUser = %s", (str(iduser),))
        text1 = self.my_cursor.fetchone()[0]
        self.my_cursor.execute("SELECT email FROM t_user where idUser = %s", (str(iduser),))
        text2 = self.my_cursor.fetchone()[0]
        self.my_cursor.execute("SELECT pekerjaan FROM t_user where idUser = %s", (str(iduser),))
        text3 = self.my_cursor.fetchone()[0]
        self.my_cursor.execute("SELECT NoHP FROM t_user where idUser = %s", (str(iduser),))
        text4 = self.my_cursor.fetchone()[0]

        load = Image.open("usr.png")
        load = load.resize((125, 125), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self.framerumah, image=render, bd=0,bg ="white")
        img.image = render
        img.place(relx=.5, y=80, anchor="center")

        self.txtUser = Label(self.framerumah, font= "Arial 15 bold", text = text1, bg = "white")
        self.txtUser.place(relx=.5, y=155, anchor="center")

        framegr1 = Frame(self.framerumah, width=400, height=1.5, bg="black", highlightbackground="grey", highlightthicknes=1) 
        framegr1.place(relx=.5, y=197, anchor=CENTER)

        load = Image.open("user.png")
        load = load.resize((28, 28), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.framerumah, image=render, bd=0,bg ="white", command=self.saya)
        img.image = render
        img.place(x=40, y=225, anchor="center")
        self.btnakun = Button(self.framerumah, bg="white", text="Akun Saya", font="Arial 12 bold", fg='black', relief=FLAT, command=self.saya)
        self.btnakun.place(x=130, y=225, anchor="center")

        framegr2 = Frame(self.framerumah, width=350, height=1.5, bg="black", highlightbackground="grey", highlightthicknes=1) 
        framegr2.place(x=85, y=255)

        load = Image.open("dompet.png")
        load = load.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.framerumah, image=render, bd=0,bg ="white", command=self.dompet_saya)
        img.image = render
        img.place(x=40, y=285, anchor="center")
        self.btndompet = Button(self.framerumah, bg="white", text="Dompet Saya", font="Arial 12 bold", fg='black', relief=FLAT, command=self.dompet_saya)
        self.btndompet.place(x=137, y=285, anchor="center")

        framegr3 = Frame(self.framerumah, width=350, height=1.5, bg="black", highlightbackground="grey", highlightthicknes=1) 
        framegr3.place(x=85, y=315)

        load = Image.open("kategori.png")
        load = load.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.framerumah, image=render, bd=0,bg ="white")
        img.image = render
        img.place(x=40, y=345, anchor="center")
        self.btnkategori = Button(self.framerumah, bg="white", text="Kategori", font="Arial 12 bold", fg='black', relief=FLAT)
        self.btnkategori.place(x=121, y=345, anchor="center")

        framegr4 = Frame(self.framerumah, width=350, height=1.5, bg="black", highlightbackground="grey", highlightthicknes=1) 
        framegr4.place(x=85, y=375)

        load = Image.open("link.png")
        load = load.resize((25, 25), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.framerumah, image=render, bd=0,bg ="white")
        img.image = render
        img.place(x=40, y=405, anchor="center")
        self.btnbank = Button(self.framerumah, bg="white", text="Sambungkan ke Bank", font="Arial 12 bold", fg='black', relief=FLAT)
        self.btnbank.place(x=170, y=405, anchor="center")

        framegr5 = Frame(self.framerumah, width=350, height=1.5, bg="black", highlightbackground="grey", highlightthicknes=1) 
        framegr5.place(x=85, y=435)

    #frame akun saya
        self.frm_akun = Frame(self.frame3, width=400, height=520, bg="white", highlightbackground="black", highlightthicknes=0) 
        self.frm_head = Frame(self.frm_akun, width=400, height=50, bg="#cccdcd", highlightbackground="black", highlightthicknes=1)
        self.frm_head.place(x=0, y=0)

        load = Image.open("back.png")
        load = load.resize((20, 20), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Button(self.frm_head, command=self.back, image=render, bd=0,bg ="#cccdcd")
        img.image = render
        img.place(x=30, y=14)

        Label(self.frm_head, text = "AKUN SAYA", bg = "#cccdcd", font = "Arial 14 bold").place(relx=.5, rely=.5, anchor="center")

        load = Image.open("usr.png")
        load = load.resize((140, 140), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self.frm_akun, image=render, bd=0,bg ="white")
        img.image = render
        img.place(relx=.5, y=120, anchor="center")

        Label(self.frm_akun, text = "Nama", bg = "white", font = "Arial 13 bold").place(relx=.07, y=200)
        Label(self.frm_akun, text = ":", bg = "white", font = "Arial 13 bold").place(relx=.33, y=200)
        self.namaa = Label(self.frm_akun, font= "Arial 13 bold", text = text1, bg = "white")
        self.namaa.place(relx=.37, y=200)

        Label(self.frm_akun, text = "Pekerjaan", bg = "white", font = "Arial 13 bold").place(relx=.07, y=260)
        Label(self.frm_akun, text = ":", bg = "white", font = "Arial 13 bold").place(relx=.33, y=260)
        self.pkrj = Label(self.frm_akun, font= "Arial 13 bold", text = text3, bg = "white")
        self.pkrj.place(relx=.37, y=260)

        Label(self.frm_akun, text = "Email", bg = "white", font = "Arial 13 bold").place(relx=.07, y=320)
        Label(self.frm_akun, text = ":", bg = "white", font = "Arial 13 bold").place(relx=.33, y=320)
        self.pkrj = Label(self.frm_akun, font= "Arial 13 bold", text = text2, bg = "white")
        self.pkrj.place(relx=.37, y=320)

        Label(self.frm_akun, text = "NO. HP", bg = "white", font = "Arial 13 bold").place(relx=.07, y=380)
        Label(self.frm_akun, text = ":", bg = "white", font = "Arial 13 bold").place(relx=.33, y=380)
        self.no = Label(self.frm_akun, font= "Arial 13 bold", text = text4, bg = "white")
        self.no.place(relx=.37, y=380)

        self.btnlogout = Button(self.frm_akun, bg="grey", text="LOGOUT", command=self.logout, font="Arial 12 bold", fg='black', relief=FLAT)
        self.btnlogout.place(relx=.5, y=470, anchor="center")

    #frame dompet saya
        self.frm_dompet = Frame(self.frame3, width=500, height=200, bg="white", highlightbackground="black", highlightthicknes=0) 
        self.frm_head = Frame(self.frm_dompet, width=500, height=50, bg="#cccdcd", highlightbackground="black", highlightthicknes=1)
        self.frm_head.place(x=0, y=0)

        # load = Image.open("back.png")
        # load = load.resize((20, 20), Image.ANTIALIAS)
        # render = ImageTk.PhotoImage(load)
        # img = Button(self.frm_head, command=self.back1, image=render, bd=0,bg ="#cccdcd")
        # img.image = render
        # img.place(x=30, y=14)
        Label(self.frm_head, text = "DOMPET SAYA", bg = "#cccdcd", font = "Arial 14 bold").place(relx=.5, rely=.5, anchor="center")

        # load = Image.open("user.png")
        # load = load.resize((50, 50), Image.ANTIALIAS)
        # render = ImageTk.PhotoImage(load)
        # img = Label(self.frm_dompet, image=render, bd=0,bg ="white")
        # img.image = render
        # img.place(x=50, y=120, anchor="center")
        self.txtUser = Label(self.frm_dompet, font= "Arial 10 bold", text = result, bg = "white")
        self.txtUser.place(x=87, y=100)
        Label(self.frm_dompet, font= "Arial 10 bold", text = str(self.format4), bg = "white").place(x=87, y=120)

    #Frame Diagram
        self.frame_diagram = Frame(self.frame3, width=800, height=400, bg="white", highlightbackground="black", highlightthicknes=1)
        self.frame_diagram_head = Frame(self.frame_diagram, width=800, height=100, bg="grey", highlightbackground="black", highlightthicknes=0)
        Label(self.frame_diagram_head, text = "Diagram Pendapatan dan Pengeluaran", bg = "grey", font = "Arial 18 bold").place(relx=.5, rely=.75, anchor="center")
        
        # self.chart1()
     
        Label(self.frame_diagram, text = "PENDAPATAN", bg = "white", font = "Arial 15 bold").place(relx=.35, y=320, anchor="center")
        Label(self.frame_diagram, font= "Arial 15 bold", text = str(self.format2), fg="blue", bg = "white").place(relx=.35, y=350, anchor="center")
        Label(self.frame_diagram, text = "PENGELUARAN", bg = "white", font = "Arial 15 bold").place(relx=.65, y=320, anchor="center")
        Label(self.frame_diagram, font= "Arial 15 bold", text = str(self.format3), fg="red", bg = "white").place(relx=.65, y=350, anchor="center")

    #Frame History
        self.framehistor = Frame(self.frame3, width=800, height=70, bg="white", highlightbackground="black", highlightthicknes=1)
        Label(self.framehistor, text = "RIWAYAT TRANSAKSI", bg = "white", font = "Arial 18 bold").place(relx=.5, rely=.5, anchor="center")

        self.frame_history = Frame(self.frame3, width=800, height=430, bg="white", highlightbackground="black", highlightthicknes=1)
        
        self.table_frame = Frame(self.frame_history, bg ="white")
        self.table_frame.place(x=0, y=0, width=798,height=370)
        self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.tbl_history2 = ttk.Treeview(self.frame_history, 
            columns=("ID","Pengeluaran","Pendapatan","Kategori Pengeluran","Kategori Pendapatan", "tgl", "bulan", "tahun"),
            xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command=self.tbl_history2.yview)
        self.tbl_history2.heading("ID", text="ID")
        self.tbl_history2.heading("Pengeluaran", text="Pengeluaran")
        self.tbl_history2.heading("Pendapatan", text="Pendapatan")
        self.tbl_history2.heading("Kategori Pengeluran", text="Kategori Pengeluran")
        self.tbl_history2.heading("Kategori Pendapatan", text="Kategori Pendapatan")
        self.tbl_history2.heading("tgl", text="Tgl")
        self.tbl_history2.heading("bulan", text="Bulan")
        self.tbl_history2.heading("tahun", text="Tahun")
        self.tbl_history2['show']='headings'
        self.tbl_history2.column("ID",width=30,anchor=CENTER)
        self.tbl_history2.column("Pengeluaran",width=100,anchor=CENTER)
        self.tbl_history2.column("Pendapatan",width=100,anchor=CENTER)
        self.tbl_history2.column("Kategori Pengeluran",width=145)
        self.tbl_history2.column("Kategori Pendapatan",width=145)
        self.tbl_history2.column("tgl", width=50, anchor=CENTER)
        self.tbl_history2.column("bulan", width=80, anchor=CENTER)
        self.tbl_history2.column("tahun", width=70, anchor=CENTER)
        self.tbl_history2.place(x=0, y=0, width=780,height=370)
        self.tbl_history2.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data2()

        self.btnedit = Button(self.frame_history, bg="#4682b4", text="EDIT RIWAYAT", command=self.edit, font="Arial 12 bold", fg='black', relief=FLAT)
        self.btnedit.place(relx=.5, rely=.93, anchor=CENTER)

    #edit histori    
        self.frm_edit = Frame(self.frame3, width=400, height=70, bg="white", highlightbackground="black", highlightthicknes=1)
        Label(self.frm_edit, text = "EDIT TRANSAKSI", bg = "white", font = "Arial 18 bold").place(relx=.5, rely=.5, anchor="center")

        self.frm_edit1 = Frame(self.frame3, width=400, height=430, bg="white", highlightbackground="black", highlightthicknes=1)

        Label(self.frm_edit1, text = "Id Transaksi", bg = "white", font= "Arial 12 bold").place(relx=.1, y=20)
        Label(self.frm_edit1, text = "Pemasukan", bg = "white", font= "Arial 12 bold").place(relx=.1, y=67)
        Label(self.frm_edit1, text = "Rp.", bg = "white", font= "Arial 12 bold").place(relx=.1, y=114)
        Label(self.frm_edit1, text = "Pengeluaran", bg = "white", font= "Arial 12 bold").place(relx=.1, y=161)
        Label(self.frm_edit1, text = "Rp.", bg = "white", font= "Arial 12 bold").place(relx=.1, y=208)
        Label(self.frm_edit1, text = "Tanggal", bg = "white", font= "Arial 12 bold").place(relx=.1, y=255)
        Label(self.frm_edit1, text = "Bulan", bg = "white", font= "Arial 12 bold").place(relx=.1, y=302)
        Label(self.frm_edit1, text = "Tahun", bg = "white", font= "Arial 12 bold").place(relx=.1, y=349)
        self.idTransaksi = StringVar()
        self.kategoriPendapatan_Var = StringVar()
        self.kategoriPengeluaran_Var = StringVar()
        self.pendapatan_Var = StringVar()
        self.pengeluaran_Var = StringVar()
        self.tanggal = StringVar()
        self.bulan2 = StringVar()
        self.tahun2 = StringVar()

        self.IDTransaksi = Entry(self.frm_edit1, bg="#e9eceb", textvariable= self.idTransaksi)
        self.IDTransaksi.place(relx=.5, y=20)
        
        self.isian3 = ttk.Combobox(self.frm_edit1, values = ("Gaji", "Tunjangan", "Hadiah", "Lainya"), textvariable = self.kategoriPendapatan_Var)
        self.isian3.place(relx=.5, y=67)

        self.duwet3 = Entry(self.frm_edit1, bg="#e9eceb", textvariable = self.pendapatan_Var)
        self.duwet3.place(relx=.5, y=114)

        self.isian4 = ttk.Combobox(self.frm_edit1, values = ("Tagihan", "Keluarga", "Kesehatan", "Hiburan", "Lainya"), 
            textvariable = self.kategoriPengeluaran_Var)
        self.isian4.place(relx=.5, y=161)

        self.duwet4 = Entry(self.frm_edit1, bg="#e9eceb", textvariable = self.pengeluaran_Var)
        self.duwet4.place(relx=.5, y=208)

        self.tgl3 = Entry(self.frm_edit1, bg="#e9eceb", textvariable = self.tanggal)
        self.tgl3.place(relx=.5, y=255)

        self.bulan3 = ttk.Combobox(self.frm_edit1, values = ("Januari", "Februari", "Maret", "April", "Mei",
         "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"),textvariable=self.bulan2)
        self.bulan3.place(relx=.5, y=302)

        self.tahun3 = Entry(self.frm_edit1, bg="#e9eceb", textvariable = self.tahun2)
        self.tahun3.place(relx=.5, y=349)

        self.btnupdate = Button(self.frm_edit1, bg="#1aa333", text="UPDATE", font="Arial 12 bold", fg='black', relief=FLAT, command=self.updatetabel)
        self.btnupdate.place(relx=.2, rely=.9)

        self.btnhapus = Button(self.frm_edit1, bg="red", text="HAPUS", font="Arial 12 bold", fg='black', relief=FLAT, command=self.hapustabel)
        self.btnhapus.place(relx=.6, rely=.9)
    
    #frame dompet
    def selesai(self, event=None):
        self.frame4 = Frame(self.frame3, width=550, height=70, bg="white", highlightbackground="black", highlightthicknes=1)

        Label(self.frame4, text = "DAFTAR TRANSAKSI", bg = "white", font = "Arial 18 bold").place(relx=.5, rely=.5, anchor="center")
        Label(self.frametrans, text = "TAMBAH TRANSAKSI", bg = "white", font = "Arial 18 bold").place(relx=.5, rely=.5, anchor="center")

        Label(self.frame_bl_ini, text = "Pemasukan", bg = "white", font= "Arial 15 bold").place(x=35, y=10)
        Label(self.frame_bl_ini, text = "Pengeluaran", bg = "white", font= "Arial 15 bold").place(x=35, y=60)
        Label(self.frame_bl_ini, text = "Uang Saat Ini", bg = "white", font= "Arial 15 bold").place(x=35, y=110)

        self.labelDompet()
        self.label1a.place_forget()
        self.label1a = Label(self.frame_bl_ini, text = self.format2, bg = "white", fg = "blue",font= "Arial 15 normal")
        self.label1a.place(x=335, y=10)

        self.label2a.place_forget()
        self.label2a= Label(self.frame_bl_ini, text = str(self.format3), bg = "white", fg = "red",font= "Arial 15 normal")
        self.label2a.place(x=335, y=60)

        self.label3a.place_forget()
        self.label3a = Label(self.frame_bl_ini, text = self.format4, bg = "white", fg = "grey",font= "Arial 15 normal")
        self.label3a.place(x=353, y=110)        

    #Treeview
        self.table_frame = Frame(self.frame_bl_ini, bg ="white")
        self.table_frame.place(x=0, y=200, width=548,height=228)
        self.scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.tbl_history = ttk.Treeview(self.frame_bl_ini, 
            columns=("Pendapatan","Pengeluaran","Kategori Pendapatan","Kategori Pengeluaran", "tgl", "bulan", "tahun"),
            xscrollcommand=self.scroll_x.set,yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x.config(command=self.tbl_history.xview)
        self.scroll_y.config(command=self.tbl_history.yview)
        self.tbl_history.heading("Pendapatan", text="Pendapatan")
        self.tbl_history.heading("Pengeluaran", text="Pengeluaran")
        self.tbl_history.heading("Kategori Pendapatan", text="Kategori Pendapatan")
        self.tbl_history.heading("Kategori Pengeluaran", text="Kategori Pengeluaran")
        self.tbl_history.heading("tgl", text="Tgl")
        self.tbl_history.heading("bulan", text="Bulan")
        self.tbl_history.heading("tahun", text="Tahun")
        self.tbl_history['show']='headings'
        self.tbl_history.column("Pendapatan",width=100,anchor=CENTER)
        self.tbl_history.column("Pendapatan",width=100,anchor=CENTER)
        self.tbl_history.column("Kategori Pendapatan",width=145)
        self.tbl_history.column("Kategori Pengeluaran",width=145)
        self.tbl_history.column("tgl", width=50, anchor=CENTER)
        self.tbl_history.column("bulan", width=80, anchor=CENTER)
        self.tbl_history.column("tahun", width=70, anchor=CENTER)
        self.tbl_history.place(x=0, y=200, width=533,height=213)
        self.fetch_data()

#controler
    def tambahtransaksi(self, event=None):
        self.my_cursor.execute("INSERT INTO `t_transaksi` (idUser,kategoriPendapatan, pendapatan, kategoriPengeluaran, pengeluaran,`tgl`, `bulan`, `tahun`) VALUES (%s,%s, %s, %s, %s, %s, %s, %s)",
            (self.iduser, self.isian1.get(), self.duwet1.get(), self.isian2.get(), self.duwet2.get(), self.tgl.get(), self.bulan.get(), self.tahun.get()))
        self.cnx.commit()
        self.isian1.set('')
        self.duwet1.delete(0, END)
        self.isian2.set('')
        self.duwet2.delete(0, END)
        self.tgl.delete(0, END)
        self.bulan.set('')
        self.tahun.delete(0, END)
        self.frame6.place_forget()
        self.frame4.place_forget()
        self.selesai()
        self.frame4.place_forget()
        self.frame4.place(relx=.5, y=102, anchor=CENTER) 
        self.frame_bl_ini.place_forget()
        self.frame_bl_ini.place(relx=.5, y=350, anchor=CENTER)
        self.frametrans.place_forget()
        self.frame_history.place_forget()
        self.framehistor.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()

    def batal(self, event=None):
        self.frame6.place_forget()
        self.frame_history.place_forget()
        self.framehistor.place_forget()
        self.frametrans.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()
        self.frame4.place(relx=.5, y=102, anchor=CENTER) 
        self.frame_bl_ini.place(relx=.5, y=350, anchor=CENTER)
    
    def tambah(self, event=None):
        self.frame4.place_forget()
        self.frametrans.place_forget()
        self.frame_history.place_forget()
        self.framehistor.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()
        self.frame4.place(x=50, y=65) 
        self.frametrans.place(x=650, y=65)
        self.frame_bl_ini.place_forget()
        self.frame_bl_ini.place(x=50, y=130)
        self.frame6.place(x=650, y=130)
    
    def home(self, event=None):
        self.frame4.place_forget()
        self.frame_history.place_forget()
        self.framehistor.place_forget()
        self.frame_bl_ini.place_forget()
        self.frame6.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frametrans.place_forget()
        self.frm_akun.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()
        self.framerumah.place(relx=.5, y=310, anchor=CENTER)

    def saya(self, event=None):
        self.frm_akun.place(relx=.5, y=310, anchor=CENTER)
        self.framerumah.place_forget()

    def logout(self, event=None):
        self.mainfr.pack_forget()
        self.lyLogin.pack(fill=BOTH, expand=1)

    def back(self, event=None):
        self.framerumah.place(relx=.5, y=310, anchor=CENTER)
        self.frm_akun.place_forget()

    def dompet_saya(self, event=None):
        self.frm_dompet.place(relx=.5, y=200, anchor=CENTER)
        self.framerumah.place_forget()
        Label(self.frm_dompet, font= "Arial 10 bold", text = str(self.format4), bg = "white").place(x=87, y=120)
    
    def back1(self, event=None):
        self.framerumah.place(relx=.5, y=310, anchor=CENTER)
        self.frm_dompet.place_forget()

    def dompet(self, event=None):
        self.frame6.place_forget()
        self.frametrans.place_forget()
        self.framehistor.place_forget()
        self.frame_history.place_forget()
        self.framerumah.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()
        self.frame4.place(relx=.5, y=102, anchor=CENTER) 
        self.fetch_data()
        self.frame_bl_ini.place(relx=.5, y=350, anchor=CENTER)
        self.labelDompet()
        
    def labelDompet(self):
        self.iduser=self.row2[0]
        self.my_cursor.execute("SELECT SUM(pendapatan) AS total2 FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.result3 = self.my_cursor.fetchone()[0]
        if self.result3==None:
            label1= Label(self.frame_bl_ini, text = ('+ Rp {:0,.0f},- '.format(0)), bg = "white", fg = "blue",font= "Arial 15 normal")
            label1.place(x=335, y=10)
        else:
            self.format2 = '+ Rp {:0,.0f},- '.format(self.result3)
            self.label1a = Label(self.frame_bl_ini, text = self.format2, bg = "white", fg = "blue",font= "Arial 15 normal")
            self.label1a.place(x=335, y=10)
        self.my_cursor.execute("SELECT SUM(pengeluaran) AS total2 FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.result4 = self.my_cursor.fetchone()[0]
        if self.result4==None:
            label2 = Label(self.frame_bl_ini, text = ('-  Rp {:0,.0f},- '.format(0)), bg = "white", fg = "red",font= "Arial 15 normal")
            label2.place(x=335, y=60)
        else:
            self.format3 = '-  Rp {:0,.0f},- '.format(self.result4)
            self.label2a= Label(self.frame_bl_ini, text = str(self.format3), bg = "white", fg = "red",font= "Arial 15 normal")
            self.label2a.place(x=335, y=60)
        if self.result3 == None and self.result4 == None:
            label3 = Label(self.frame1, font= "Arial 10 bold", text = ('Rp {:0,.0f},- '.format(0)), bg = "white")
            label3.place(x=87, y=33)
        else :
            self.jumlah = self.result3 - self.result4
            self.format4 = 'Rp {:0,.0f},- '.format(self.jumlah)
            self.label3a = Label(self.frame_bl_ini, text = self.format4, bg = "white", fg = "grey",font= "Arial 15 normal")
            self.label3a.place(x=353, y=110)
            Label(self.frame1, font= "Arial 10 bold", text = str(self.format4), bg = "white").place(x=87, y=33)
    
    def diagram(self, event=None): 
        self.frame4.place_forget()
        self.frame_bl_ini.place_forget()
        self.frame6.place_forget()
        self.framerumah.place_forget()
        self.frametrans.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_history.place_forget()
        self.framehistor.place_forget()
        self.my_cursor.execute("SELECT SUM(pendapatan) AS total2 FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.result3 = self.my_cursor.fetchone()[0]
        self.my_cursor.execute("SELECT SUM(pengeluaran) AS total2 FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.result4 = self.my_cursor.fetchone()[0]
        self.chart1()
        Label(self.frame_diagram, font= "Arial 15 bold", text = str(self.format2), fg="blue", bg = "white").place(relx=.35, y=350, anchor="center")
        Label(self.frame_diagram, font= "Arial 15 bold", text = str(self.format3), fg="red", bg = "white").place(relx=.65, y=350, anchor="center")
        self.frame_diagram.place(relx=.5, y=250, anchor=CENTER)
        self.frame_diagram_head.place(relx=.5, y=0, anchor=CENTER)

    def history(self, event=None):
        self.frame4.place_forget()
        self.frame_bl_ini.place_forget()
        self.frame6.place_forget()
        self.framerumah.place_forget()
        self.frametrans.place_forget()
        self.frm_edit.place_forget()
        self.frm_edit1.place_forget()
        self.frm_akun.place_forget()
        self.frm_dompet.place_forget()
        self.frame_diagram.place_forget()
        self.frame_diagram_head.place_forget()
        self.framehistor.place(relx=.5, y=102, anchor=CENTER)
        self.frame_history.place(relx=.5, y=350, anchor=CENTER)
        self.fetch_data2()

    def edit(self, event=None):
        self.framehistor.place(relx=.67, y=102, anchor=CENTER)
        self.frame_history.place(relx=.67, y=350, anchor=CENTER)
        self.frm_edit.place(relx=.18, y=102, anchor=CENTER)
        self.frm_edit1.place(relx=.18, y=350, anchor=CENTER)
    
    def getData(self, event=None):
        self.my_cursor.execute("SELECT nama FROM t_user where idUser = %s", (str(self.iduser),))
        result = self.my_cursor.fetchone()[0]
        self.txtUser = Label(self.frame1, font= "Arial 9 normal", text = result, bg = "white")
        self.txtUser.place(x=87, y=15)

    def fetch_data2(self):
        self.my_cursor.execute("SELECT idTransaksi, pendapatan, pengeluaran, kategoriPendapatan, kategoriPengeluaran, tgl, bulan, tahun  FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.tbl_history2.delete(*self.tbl_history2.get_children())
            for row in self.rows :
                self.tbl_history2.insert('',END,values=row)

    def fetch_data(self):
        self.my_cursor.execute("SELECT pendapatan, pengeluaran, kategoriPendapatan, kategoriPengeluaran, tgl, bulan, tahun  FROM t_transaksi where idUser = %s", (str(self.iduser),))
        self.rows=self.my_cursor.fetchall()
        if len(self.rows)!=0:
            self.tbl_history.delete(*self.tbl_history.get_children())
            for row in self.rows :
                self.tbl_history.insert('',END,values=row)
            self.cnx.commit()
            
    def hapustabel(self):
        value1 = (self.idTransaksi.get(),)
        query = "DELETE FROM t_transaksi WHERE idTransaksi =  %s"  
        self.my_cursor.execute(query, value1)
        self.cnx.commit()
        self.fetch_data2()
        self.idTransaksi.set("")
        self.kategoriPendapatan_Var.set("")
        self.pendapatan_Var.set("")
        self.kategoriPengeluaran_Var.set("")
        self.pengeluaran_Var.set("")
        self.tanggal.set("")
        self.bulan2.set("")
        self.tahun2.set("")
        self.framehistor.place(relx=.5, y=102, anchor=CENTER)
        self.frame_history.place(relx=.5, y=350, anchor=CENTER)
        self.frm_edit1.place_forget()
        self.frm_edit.place_forget()

    def get_cursor(self,ev):
        cursor_row=self.tbl_history2.focus()
        contents=self.tbl_history2.item(cursor_row)
        row=contents['values']  
        self.idTransaksi.set(row[0])
        self.kategoriPendapatan_Var.set(row[3])
        self.pendapatan_Var.set(row[1])
        self.kategoriPengeluaran_Var.set(row[4])
        self.pengeluaran_Var.set(row[2])
        self.tanggal.set(row[5])
        self.bulan2.set(row[6])
        self.tahun2.set(row[7])

    def updatetabel(self):
        query1 = ("UPDATE `t_transaksi` SET `pendapatan` = %s, `pengeluaran` = %s, `kategoriPendapatan` = %s, `kategoriPengeluaran` = %s, `tgl` = %s, `bulan` = %s, `tahun` = %s WHERE `t_transaksi`.`idTransaksi` = %s;")
        values = (self.pendapatan_Var.get(), self.pengeluaran_Var.get(),self.kategoriPendapatan_Var.get(), self.kategoriPengeluaran_Var.get(), self.tanggal.get(), self.bulan2.get(), self.tahun2.get(), self.idTransaksi.get())
        self.my_cursor.execute(query1, values)
        self.cnx.commit()
        self.fetch_data2()
        self.idTransaksi.set("")
        self.kategoriPendapatan_Var.set("")
        self.pendapatan_Var.set("")
        self.kategoriPengeluaran_Var.set("")
        self.pengeluaran_Var.set("")
        self.tanggal.set("")
        self.bulan2.set("")
        self.tahun2.set("")
        self.framehistor.place(relx=.5, y=102, anchor=CENTER)
        self.frame_history.place(relx=.5, y=350, anchor=CENTER)
        self.frm_edit1.place_forget()
        self.frm_edit.place_forget()      
        self.labelDompet()

    def chart1(self):
        listpie = [self.result3,self.result4]
        stockListExp = ["Pendapatan","Pengeluaran"]
        fig = Figure(figsize=(10,10))
        fig.patch.set_facecolor('white') 
        ax = fig.add_subplot(111) 
        ax.pie(listpie, 
            radius=1, 
            labels=stockListExp,
            autopct='%i%%')
        chart1 = FigureCanvasTkAgg(fig,self.frame_diagram)
        chart1.get_tk_widget().configure(background='white', highlightcolor='black', highlightbackground='black')
        chart1.get_tk_widget().place(relx=.5, y=180, anchor="center", width = 400, height=240)

if __name__ == '__main__':
    root = Tk()
    jdl = PersonalFinance(root, "Manajemen Keuangan Pribadi")
    root.state("zoomed")
    root.mainloop()