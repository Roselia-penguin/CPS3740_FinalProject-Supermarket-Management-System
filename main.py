from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import pandas as pd
import mysql.connector
from tkinter import messagebox
import pymysql

WINDOW_WIDTH = 920
WINDOW_HEIGHT = 530
TOP_WIDTH = 800
TOP_HEIGHT = 480
# Overall background color
BG_COLOR = '#5E95FF'
# Font for label
TK_L_FONT = ('', 28, 'bold')
# Font for entry
TK_E_FONT = ('', 18, 'bold')
# Font for button
TK_B_FONT = ('', 28, 'bold')

class TkinterMain():
    
    def __init__(self):
        #Initialize the window body
        self.window = Tk()
        self.window.config(background=BG_COLOR)
        self.window.title("Supermarket management System")

        # Get screen height and width
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set the window height and width and center it on the screen
        x = (screen_width - WINDOW_WIDTH) / 2
        y = (screen_height - WINDOW_HEIGHT) / 2
        root_size = '%dx%d+%d+%d' % ( WINDOW_WIDTH, WINDOW_HEIGHT, x, y)
        self.window.geometry(root_size)
        # Fixed size
        self.window.wm_resizable(False, False)

        #-------- Variables ----
        self.client_id_var=StringVar()
        self.client_name_var=StringVar()   
        self.mobile_var=StringVar() 
        self.home_address_var=StringVar()    
        self.email_var=StringVar() 

        self.goods_id_var=StringVar()
        self.goods_barcode_var=StringVar()
        self.goods_name_var=StringVar()
        self.Production_place_var=StringVar()
        self.del_var=StringVar()
        self.search_var=StringVar()
        self.co_var=StringVar() # add this variable for search combobox

        self.purchase_id_var=StringVar()
        #self.goods_id_var=StringVar()
        self.purchase_price_var=StringVar()
        self.purchase_number_var=StringVar()
        self.purchase_money_var=StringVar()
        self.purchase_date_var=StringVar()       
        #self.del_var=StringVar()
        #self.search_var=StringVar()
        #self.co_var=StringVar() # add this variable for search combobox

        self.sale_id_var=StringVar()
        #self.goods_id_var=StringVar()
        #self.client_id_var=StringVar()
        self.sale_price_var=StringVar()
        self.sale_number_var=StringVar()
        self.sale_sum_var=StringVar()
        self.sale_date_var=StringVar()

        # Sub window
        self.top_view = None
        #Create homepage window
        self.create_home_page_view()

    #Create homepage
    def create_home_page_view(self):
        # Home page background
        img = Image.open('bg.png').resize((650, 480))
        self.bg_png = ImageTk.PhotoImage(img)
        Label(self.window, image=self.bg_png, bd=0).place(x=0, y=30)
        # title
        Label(self.window, text='Supermarket\nManagement\nSystem\n-----------', 
              font=('', 24, 'bold'), bg=BG_COLOR).place(x=680, y=30)

        # Button frame
        btn_frame = Frame(self.window, bg=BG_COLOR)
        btn_frame.place(x=680, y=152, width=200, height=350)

        Button(btn_frame, text='Client', width=20,command=self.client, bg='white').pack(pady=6)
        Button(btn_frame, text='Goods', width=20,command=self.goods, bg='white').pack(pady=6)
        Button(btn_frame, text='Purchase', width=20,command=self.purchase, bg='white').pack(pady=6)
        Button(btn_frame, text='Sale', width=20,command=self.sale, bg='white').pack(pady=6)
        Button(btn_frame, text='About', width=20,command=self.about, bg='white').pack(pady=6)
        Button(btn_frame, text='Exit', width=20,command=self.quit, bg='white').pack(pady=6)
    
    def client(self):
        # display as the sub window
        self.show_top_view()

        Label(self.top_view, text='[Client Information]', bg=BG_COLOR, 
              font=('monospace', 14), fg='white').pack(fill=X)
        Manage_Frame = Frame(self.top_view, width=WINDOW_WIDTH, bg='white')
        Manage_Frame.place(x=5,y=30,width=175,height=400)

        # --------- Frame For Adding client Data-----------
        lbl_client_id = Label(Manage_Frame, bg='white', text='client_id')
        lbl_client_id.pack()
        client_id_Entry= Entry(Manage_Frame,textvariable=self.client_id_var, bd='2', justify='center')
        client_id_Entry.pack()

        lbl_client_name = Label(Manage_Frame, bg='white', text='client_name')
        lbl_client_name.pack()
        client_name_Entry= Entry(Manage_Frame,textvariable=self.client_name_var, bd='2', justify='center')
        client_name_Entry.pack()

        lbl_mobile = Label(Manage_Frame, bg='white', text='mobile')
        lbl_mobile.pack()
        mobile_Entry= Entry(Manage_Frame,textvariable=self.mobile_var, bd='2', justify='center')
        mobile_Entry.pack()

        lbl_home_address = Label(Manage_Frame, bg='white', text='home_address')
        lbl_home_address.pack()
        home_address_Entry= Entry(Manage_Frame,textvariable=self.home_address_var, bd='2', justify='center')
        home_address_Entry.pack()

        lbl_email = Label(Manage_Frame, bg='white', text='email')
        lbl_email.pack()
        email_Entry= Entry(Manage_Frame,textvariable=self.email_var, bd='2', justify='center')
        email_Entry.pack()

        lbl_delete = Label(Manage_Frame, bg='white', text='Delete Client by ID', fg='red')
        lbl_delete.pack()
        delete_Entry= Entry(Manage_Frame,textvariable=self.del_var, bd='2', justify='center')
        delete_Entry.pack()

        #--------- Button Frame------
        btn_Frame= Frame(self.top_view, bg='white')
        btn_Frame.place(x=740,y=25, width=175, height=405)

        title=Label(btn_Frame, text='Controls', font=('Deco', 14), fg='white',bg='#5E95FF')
        title.pack(fill=X)

        add_btn=Button(btn_Frame,text='Add Button', bg='#5E95FF', command=self.addClient)
        add_btn.place(x=15, y=30, width=150, height=33)

        del_btn=Button(btn_Frame, text='Delete Button', bg='#5E95FF', command=self.deleteClient) 
        del_btn.place(x=15, y=65, width=150, height=33)

        update_btn=Button(btn_Frame, text='Update Button', bg='#5E95FF', command=self.updateClient)
        update_btn.place(x=15, y=100, width=150, height=33)

        clear_btn=Button(btn_Frame, text='Clear Button', bg='#5E95FF', command=self.clearClient)
        clear_btn.place(x=15, y=135, width=150, height=33)

        display_btn=Button(btn_Frame, text='Display Button', bg='#5E95FF', command=self.displayClient)
        display_btn.place(x=15, y=170, width=150, height=33)

        exit_btn=Button(btn_Frame, text='Exit Button', bg='#5E95FF', command=self.quit)# command=self.about
        exit_btn.place(x=15, y=205, width=150, height=33)


        #--------- Search for Client Data----
        search_Frame = Frame (self.top_view, bg='#FAE5D3') 
        search_Frame.place (x=10,y=440,width=900, height=75)

        lbl_search=Label (search_Frame, text='Choose to search', bg='#FAE5D3', width=15)
        lbl_search.place (x=170, y=20)

        combo_search = ttk.Combobox (search_Frame, justify='right', textvariable=self.co_var) 
        combo_search['value']=('client_id','client_name', 'mobile', 'home_address','email')# modify it
        combo_search.place (x=280,y=20)

        search_Entry= Entry(search_Frame,textvariable=self.search_var, justify='right', bd='2')
        search_Entry.place (x=450, y=20)

        search_btn=Button(search_Frame, text='Search', bg='white', command=self.searchClient)
        search_btn.place(x=600, y=20, width=150, height=20)

        Details_Frame=Frame(self.top_view, bg="gray")
        Details_Frame.place(x=185, y=30, width=550, height=400)

        Scroll_X=Scrollbar(Details_Frame, orient=HORIZONTAL)
        Scroll_Y=Scrollbar(Details_Frame, orient=VERTICAL)

        self.client_table=ttk.Treeview(Details_Frame,
        columns=('client_id','client_name', 'mobile', 'home_address','email'),
        xscrollcommand=Scroll_X,
        yscrollcommand=Scroll_Y)

        self.client_table.place(x=10, y=10, width=514, height=365)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.client_table.xview)
        Scroll_Y.config(command=self.client_table.yview)

        self.client_table['show']='headings'
        self.client_table.heading('client_id', text='client_id')
        self.client_table.heading('client_name', text='client_name')
        self.client_table.heading('mobile', text='mobile')
        self.client_table.heading('home_address', text='home_address')
        self.client_table.heading('email', text='email')

        self.client_table.column('client_id', width=100)
        self.client_table.column('client_name', width=101)
        self.client_table.column('mobile', width=101)
        self.client_table.column('home_address', width=101)
        self.client_table.column('email', width=101)
        self.client_table.bind("<ButtonRelease-1>", self.get_cursorClient)

        self.fetch_allClient()

    
    def addClient(self): #-- pip install PyMySQL -- need to install----
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("insert into client values(%s,%s,%s,%s,%s) ",(
                                 self.client_id_var.get(),
                                 self.client_name_var.get(),
                                 self.mobile_var.get(),
                                 self.home_address_var.get(),
                                 self.email_var.get()                                
                                 )
                    )
        con.commit()
        self.fetch_allClient() # display all rows
        self.clearClient()# after added record need to clear all entries
        con.close()

    def fetch_allClient(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from client")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.client_table.delete(*self.client_table.get_children())
            for row in rows:
                self.client_table.insert("", END, values=row)
                con.commit()
            con.close()

    def displayClient(self):
        self.show_top_view()
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur=con.cursor()
        cur.execute("select * from client")
        rows=cur.fetchall()


        Label(self.top_view, text='Client', font=('', 60, 'bold'), bg=BG_COLOR).pack()
        info_frame = Frame(self.top_view, width=WINDOW_WIDTH)
        info_frame.pack(pady=(20, 0), expand=True, fill='y')
        Label(info_frame, text='client_id', font=('', 20)).place(x=10, y=0)
        Label(info_frame, text='client_name', font=('', 20)).place(x=180, y=0)
        Label(info_frame, text='mobile', font=('', 20)).place(x=420, y=0)
        Label(info_frame, text='home_address', font=('', 20)).place(x=580, y=0)
        Label(info_frame, text='email', font=('', 20)).place(x=780, y=0)

        info_all_frame = Frame(info_frame)
        info_all_frame.place(x=0, y=36, width=TOP_WIDTH, height=338)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                fund_info_label = tk.Label(info_frame, text=value)
                fund_info_label.place(x=(j * 180 + 65), y=((i + 3) * 20))
    
        btn_Frame= Frame(self.top_view, bg='#5E95FF')
        btn_Frame.place(x=0,y=450, width=920, height=100)
        export_btn=Button(btn_Frame, text='Export Button', bg='white', command=self.client_export_to_excel)
        export_btn.place(x=400, y=30, width=150, height=33)

    
    def client_export_to_excel(self):
        con = mysql.connector.connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM client")
        sqldata = cur.fetchall()
        # Send data into dataframe
        df = pd.DataFrame(data=sqldata) 
        cur.close()
        # view dataframe
        print(df)
        #to_excel
        df.to_excel('D:\project_excel/client.xlsx', sheet_name='client')
        messagebox.showinfo("Client","Export successfully!")

    # ---delete client name -----
    def deleteClient(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute('delete from client where client_id=%s', self.del_var.get())
        con.commit()
        self.fetch_allClient()
        con.close()

    #---- Update record -----
    def updateClient(self):
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("update client set client_name=%s, mobile=%s, home_address=%s ,email=%s where client_id=%s",(
                                 self.client_name_var.get(),
                                 self.mobile_var.get(),
                                 self.home_address_var.get(),
                                 self.email_var.get(),  
                                 self.client_id_var.get() 
                                 )
                    )
        con.commit()
        self.fetch_allClient() # display all rows
        self.clearClient()# after added record need to clear all entries
        con.close()

    #---- Search -----
    def searchClient(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from client where " +
        str(self.co_var.get())+" LIKE '%"+str(self.search_var.get())+"%'")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.client_table.delete(*self.client_table.get_children())
            for row in rows:
                self.client_table.insert("", END, values=row)
        con.commit()
        con.close()

    # ---clear entries -----
    def clearClient(self):
        self.client_id_var.set('')
        self.client_name_var.set('')
        self.mobile_var.set('')
        self.home_address_var.set('')
        self.email_var.set('')

    #---- Select row and display data inside each entry
    def get_cursorClient(self, ev):
       cursor_row=self.client_table.focus()
       contents=self.client_table.item(cursor_row)
       row=contents['values']
       self.client_id_var.set(row[0]) 
       self.client_name_var.set(row[1]) 
       self.mobile_var.set(row[2]) 
       self.home_address_var.set(row[3]) 
       self.email_var.set(row[4]) 
    
    def goods(self):
        self.show_top_view()

        Label(self.top_view, text='[Goods Information]', bg=BG_COLOR, 
              font=('monospace', 14), fg='white').pack(fill=X)
        Manage_Frame = Frame(self.top_view, width=WINDOW_WIDTH, bg='white')
        Manage_Frame.place(x=5,y=30,width=175,height=400)

        # --------- Frame For Adding Goods Data-----------
        lbl_goods_id = Label(Manage_Frame, bg='white', text='goods_id')
        lbl_goods_id.pack()
        goods_id_Entry= Entry(Manage_Frame,textvariable=self.goods_id_var, bd='2', justify='center')
        goods_id_Entry.pack()

        lbl_goods_barcode = Label(Manage_Frame, bg='white', text='goods_barcode')
        lbl_goods_barcode.pack()
        goods_barcode_Entry= Entry(Manage_Frame,textvariable=self.goods_barcode_var, bd='2', justify='center')
        goods_barcode_Entry.pack()

        lbl_goods_name = Label(Manage_Frame, bg='white', text='goods_name')
        lbl_goods_name.pack()
        goods_name_Entry= Entry(Manage_Frame,textvariable=self.goods_name_var, bd='2', justify='center')
        goods_name_Entry.pack()

        lbl_Production_place = Label(Manage_Frame, bg='white', text='Production_place')
        lbl_Production_place.pack()
        Production_place_Entry= Entry(Manage_Frame,textvariable=self.Production_place_var, bd='2', justify='center')
        Production_place_Entry.pack()

        lbl_delete = Label(Manage_Frame, bg='white', text='Delete Goods by ID', fg='red')
        lbl_delete.pack()

        delete_Entry= Entry(Manage_Frame,textvariable=self.del_var, bd='2', justify='center')
        delete_Entry.pack()

        #--------- Button Frame------
        btn_Frame= Frame(self.top_view, bg='white')
        btn_Frame.place(x=740,y=25, width=175, height=405)

        title=Label(btn_Frame, text='Controls', font=('Deco', 14), fg='white',bg='#5E95FF')
        title.pack(fill=X)

        add_btn=Button(btn_Frame,text='Add Button', bg='#5E95FF', command=self.add_goods)
        add_btn.place(x=15, y=30, width=150, height=33)

        del_btn=Button(btn_Frame, text='Delete Button', bg='#5E95FF', command=self.deleteGoods) 
        del_btn.place(x=15, y=65, width=150, height=33)

        update_btn=Button(btn_Frame, text='Update Button', bg='#5E95FF', command=self.updateGoods)
        update_btn.place(x=15, y=100, width=150, height=33)

        clear_btn=Button(btn_Frame, text='Clear Button', bg='#5E95FF', command=self.clearGoods)
        clear_btn.place(x=15, y=135, width=150, height=33)

        display_btn=Button(btn_Frame, text='Display Button', bg='#5E95FF', command=self.displayGoods)
        display_btn.place(x=15, y=170, width=150, height=33)

        exit_btn=Button(btn_Frame, text='Exit Button', bg='#5E95FF', command=self.quit)
        exit_btn.place(x=15, y=205, width=150, height=33)

        #--------- Search for Goods Data----
        search_Frame = Frame (self.top_view, bg='#FAE5D3') 
        search_Frame.place (x=10,y=440,width=900, height=75)

        lbl_search=Label (search_Frame, text='Choose to search', bg='#FAE5D3', width=15)
        lbl_search.place (x=170, y=20)

        combo_search = ttk.Combobox (search_Frame, justify='right', textvariable=self.co_var) 
        combo_search['value']=('goods_id','goods_barcode', 'goods_name', 'Production_place')# modify it
        combo_search.place (x=280,y=20)

        search_Entry= Entry(search_Frame,textvariable=self.search_var, justify='right', bd='2')
        search_Entry.place (x=450, y=20)

        search_btn=Button(search_Frame, text='Search', bg='white', command=self.searchGoods)
        search_btn.place(x=600, y=20, width=150, height=20)

        Details_Frame=Frame(self.top_view, bg="gray")
        Details_Frame.place(x=185, y=30, width=550, height=400)

        Scroll_X=Scrollbar(Details_Frame, orient=HORIZONTAL)
        Scroll_Y=Scrollbar(Details_Frame, orient=VERTICAL)

        self.goods_table=ttk.Treeview(Details_Frame,
        columns=('goods_id', 'goods_barcode', 'goods_name', 'Production_place'),
        xscrollcommand=Scroll_X,
        yscrollcommand=Scroll_Y)

        self.goods_table.place(x=10, y=10, width=514, height=365)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.goods_table.xview)
        Scroll_Y.config(command=self.goods_table.yview)

        self.goods_table['show']='headings'
        self.goods_table.heading('goods_id', text='goods_id')
        self.goods_table.heading('goods_barcode', text='goods_barcode')
        self.goods_table.heading('goods_name', text='goods_name')
        self.goods_table.heading('Production_place', text='Production_place')

        self.goods_table.column('goods_id', width=126)
        self.goods_table.column('goods_barcode', width=126)
        self.goods_table.column('goods_name', width=126)
        self.goods_table.column('Production_place', width=126)
        self.goods_table.bind("<ButtonRelease-1>", self.get_cursorGoods)

        self.fetch_allGoods()

    def add_goods(self): #-- pip install PyMySQL -- need to install----
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("insert into goods values(%s,%s,%s,%s) ",(
                                 self.goods_id_var.get(),
                                 self.goods_barcode_var.get(),
                                 self.goods_name_var.get(),
                                 self.Production_place_var.get()
                                 )
                    )
        con.commit()
        self.fetch_allGoods() # display all rows
        self.clearGoods()# after added record need to clear all entries
        con.close()

    def fetch_allGoods(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from goods")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.goods_table.delete(*self.goods_table.get_children())
            for row in rows:
                self.goods_table.insert("", END, values=row)
                con.commit()
            con.close()
    
    def displayGoods(self):
        self.show_top_view()
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur=con.cursor()
        cur.execute("select * from goods")
        rows=cur.fetchall()

        Label(self.top_view, text='Goods', font=('', 60, 'bold'), bg=BG_COLOR).pack()
        info_frame = Frame(self.top_view, width=WINDOW_WIDTH)
        info_frame.pack(pady=(20, 0), expand=True, fill='y')
        Label(info_frame, text='goods_id', font=('', 20)).place(x=10, y=0)
        Label(info_frame, text='goods_barcode', font=('', 20)).place(x=210, y=0)
        Label(info_frame, text='goods_name', font=('', 20)).place(x=440, y=0)
        Label(info_frame, text='Production_place', font=('', 20)).place(x=660, y=0)

        info_all_frame = Frame(info_frame)
        info_all_frame.place(x=0, y=36, width=TOP_WIDTH, height=338)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                fund_info_label = tk.Label(info_frame, text=value)
                fund_info_label.place(x=(j * 220 + 65), y=((i + 3) * 20))
    
        btn_Frame= Frame(self.top_view, bg='#5E95FF')
        btn_Frame.place(x=0,y=450, width=920, height=100)
        export_btn=Button(btn_Frame, text='Export Button', bg='white', command=self.goods_export_to_excel)
        export_btn.place(x=400, y=30, width=150, height=33)

    
    def goods_export_to_excel(self):
        con = mysql.connector.connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM goods")
        sqldata = cur.fetchall()
        # Send data into dataframe
        df = pd.DataFrame(data=sqldata) 
        cur.close()
        # view dataframe
        print(df)
        #to_excel
        df.to_excel('D:\project_excel/goods.xlsx', sheet_name='goods')
        messagebox.showinfo("Goods","Export successfully!")

    
    # ---delete goods name -----
    def deleteGoods(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute('delete from goods where goods_id=%s', self.del_var.get())
        con.commit()
        self.fetch_allGoods()
        con.close()

    #---- Update record -----
    def updateGoods(self):
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("update goods set goods_barcode=%s, goods_name=%s, Production_place=%s where goods_id=%s",(
                                 self.goods_barcode_var.get(),
                                 self.goods_name_var.get(),
                                 self.Production_place_var.get(),
                                 self.goods_id_var.get(),   
                                 )
                    )
        con.commit()
        self.fetch_allGoods() # display all rows
        self.clearGoods()# after added record need to clear all entries
        con.close()

    #---- Search -----
    def searchGoods(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from goods where " +
        str(self.co_var.get())+" LIKE '%"+str(self.search_var.get())+"%'")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.goods_table.delete(*self.goods_table.get_children())
            for row in rows:
                self.goods_table.insert("", END, values=row)
        con.commit()
        con.close()

    # ---clear entries -----
    def clearGoods(self):
        self.goods_id_var.set('')
        self.goods_barcode_var.set('')
        self.goods_name_var.set('')
        self.Production_place_var.set('')

    #---- Select row and display data inside each entry
    def get_cursorGoods(self, ev):
       cursor_row=self.goods_table.focus()
       contents=self.goods_table.item(cursor_row)
       row=contents['values']
       self.goods_id_var.set(row[0]) 
       self.goods_barcode_var.set(row[1]) 
       self.goods_name_var.set(row[2]) 
       self.Production_place_var.set(row[3])
       

    def purchase(self):
        self.show_top_view()

        Label(self.top_view, text='[Purchase Information]', bg=BG_COLOR, 
              font=('monospace', 14), fg='white').pack(fill=X)
        Manage_Frame = Frame(self.top_view, width=WINDOW_WIDTH, bg='white')
        Manage_Frame.place(x=5,y=30,width=175,height=400)

        # --------- Frame For Adding purchase Data-----------
        lbl_purchase_id = Label(Manage_Frame, bg='white', text='purchase_id')
        lbl_purchase_id.pack()
        purchase_id_Entry= Entry(Manage_Frame,textvariable=self.purchase_id_var, bd='2', justify='center')
        purchase_id_Entry.pack()

        lbl_goods_id = Label(Manage_Frame, bg='white', text='goods_id')
        lbl_goods_id.pack()
        goods_id_Entry= Entry(Manage_Frame,textvariable=self.goods_id_var, bd='2', justify='center')
        goods_id_Entry.pack()

        lbl_purchase_price = Label(Manage_Frame, bg='white', text='purchase_price')
        lbl_purchase_price.pack()
        purchase_price_Entry= Entry(Manage_Frame,textvariable=self.purchase_price_var, bd='2', justify='center')
        purchase_price_Entry.pack()

        lbl_purchase_number = Label(Manage_Frame, bg='white', text='purchase_number')
        lbl_purchase_number.pack()
        purchase_number_Entry= Entry(Manage_Frame,textvariable=self.purchase_number_var, bd='2', justify='center')
        purchase_number_Entry.pack()

        lbl_purchase_date = Label(Manage_Frame, bg='white', text='purchase_date')
        lbl_purchase_date.pack()
        purchase_date_Entry= Entry(Manage_Frame,textvariable=self.purchase_date_var, bd='2', justify='center')
        purchase_date_Entry.pack()

        lbl_delete = Label(Manage_Frame, bg='white', text='Delete Purchase by ID', fg='red')
        lbl_delete.pack()
        delete_Entry= Entry(Manage_Frame,textvariable=self.del_var, bd='2', justify='center')
        delete_Entry.pack()

        #--------- Button Frame------
        btn_Frame= Frame(self.top_view, bg='white')
        btn_Frame.place(x=740,y=25, width=175, height=405)

        title=Label(btn_Frame, text='Controls', font=('Deco', 14), fg='white',bg='#5E95FF')
        title.pack(fill=X)

        add_btn=Button(btn_Frame,text='Add Button', bg='#5E95FF', command=self.addPurchase)
        add_btn.place(x=15, y=30, width=150, height=33)

        del_btn=Button(btn_Frame, text='Delete Button', bg='#5E95FF', command=self.deletePurchase) 
        del_btn.place(x=15, y=65, width=150, height=33)

        update_btn=Button(btn_Frame, text='Update Button', bg='#5E95FF', command=self.updatePurchase)
        update_btn.place(x=15, y=100, width=150, height=33)

        clear_btn=Button(btn_Frame, text='Clear Button', bg='#5E95FF', command=self.clearPurchase)
        clear_btn.place(x=15, y=135, width=150, height=33)

        display_btn=Button(btn_Frame, text='Display Button', bg='#5E95FF', command=self.displayPurchase)
        display_btn.place(x=15, y=170, width=150, height=33)

        exit_btn=Button(btn_Frame, text='Exit Button', bg='#5E95FF', command=self.quit)# command=self.about
        exit_btn.place(x=15, y=205, width=150, height=33)

        #--------- Search for purchase Data----
        search_Frame = Frame (self.top_view, bg='#FAE5D3') 
        search_Frame.place (x=10,y=440,width=900, height=75)

        lbl_search=Label (search_Frame, text='Choose to search', bg='#FAE5D3', width=15)
        lbl_search.place (x=170, y=20)

        combo_search = ttk.Combobox (search_Frame, justify='right', textvariable=self.co_var) 
        combo_search['value']=('purchase_id','goods_id', 'purchase_price', 'purchase_number', 'purchase_money', 'purchase_date')# modify it
        combo_search.place (x=280,y=20)

        search_Entry= Entry(search_Frame,textvariable=self.search_var, justify='right', bd='2')
        search_Entry.place (x=450, y=20)

        search_btn=Button(search_Frame, text='Search', bg='white', command=self.searchPurchase)
        search_btn.place(x=600, y=20, width=150, height=20)

        Details_Frame=Frame(self.top_view, bg="gray")
        Details_Frame.place(x=185, y=30, width=550, height=400)

        Scroll_X=Scrollbar(Details_Frame, orient=HORIZONTAL)
        Scroll_Y=Scrollbar(Details_Frame, orient=VERTICAL)

        self.purchase_table=ttk.Treeview(Details_Frame,
        columns=('purchase_id','goods_id', 'purchase_price', 'purchase_number', 'purchase_money', 'purchase_date'),
        xscrollcommand=Scroll_X,
        yscrollcommand=Scroll_Y)

        self.purchase_table.place(x=0, y=0, width=537, height=387)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.purchase_table.xview)
        Scroll_Y.config(command=self.purchase_table.yview)

        self.purchase_table['show']='headings'
        self.purchase_table.heading('purchase_id', text='purchase_id')
        self.purchase_table.heading('goods_id', text='goods_id')
        self.purchase_table.heading('purchase_price', text='purchase_price')
        self.purchase_table.heading('purchase_number', text='purchase_number')
        self.purchase_table.heading('purchase_money', text='purchase_money')
        self.purchase_table.heading('purchase_date', text='purchase_date')

        self.purchase_table.column('purchase_id', width=69)
        self.purchase_table.column('goods_id', width=55)
        self.purchase_table.column('purchase_price', width=90)
        self.purchase_table.column('purchase_number', width=101)
        self.purchase_table.column('purchase_money', width=100)
        self.purchase_table.column('purchase_date', width=89)
        self.purchase_table.bind("<ButtonRelease-1>", self.get_cursorPurchase)

        self.fetch_allPurchase()

    def addPurchase(self): #-- pip install PyMySQL -- need to install----
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("insert into purchase values(%s,%s,%s,%s,DEFAULT,%s) ",(
                                 self.purchase_id_var.get(),
                                 self.goods_id_var.get(),
                                 self.purchase_price_var.get(),
                                 self.purchase_number_var.get(),
                                 self.purchase_date_var.get()
                                 )
                    )
        con.commit()
        self.fetch_allPurchase() # display all rows
        self.clearPurchase()# after added record need to clear all entries
        con.close()

    def fetch_allPurchase(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from purchase")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.purchase_table.delete(*self.purchase_table.get_children())
            for row in rows:
                self.purchase_table.insert("", END, values=row)
                con.commit()
            con.close()

    def displayPurchase(self):
        self.show_top_view()
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur=con.cursor()
        cur.execute("select * from purchase")
        rows=cur.fetchall()


        Label(self.top_view, text='Purchase', font=('', 60, 'bold'), bg=BG_COLOR).pack()
        info_frame = Frame(self.top_view, width=WINDOW_WIDTH)
        info_frame.pack(pady=(20, 0), expand=True, fill='y')
        Label(info_frame, text='purchase_id', font=('', 14)).place(x=10, y=0)
        Label(info_frame, text='goods_id', font=('', 14)).place(x=160, y=0)
        Label(info_frame, text='purchase_price', font=('', 14)).place(x=260, y=0)
        Label(info_frame, text='purchase_number', font=('', 14)).place(x=420, y=0)
        Label(info_frame, text='purchase_money', font=('', 14)).place(x=590, y=0)
        Label(info_frame, text='purchase_date', font=('', 14)).place(x=740, y=0)

        info_all_frame = Frame(info_frame)
        info_all_frame.place(x=0, y=36, width=TOP_WIDTH, height=338)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                fund_info_label = tk.Label(info_frame, text=value)
                fund_info_label.place(x=(j * 140 + 65), y=((i + 3) * 20))
    
        btn_Frame= Frame(self.top_view, bg='#5E95FF')
        btn_Frame.place(x=0,y=450, width=920, height=100)
        export_btn=Button(btn_Frame, text='Export Button', bg='white', command=self.purchase_export_to_excel)
        export_btn.place(x=400, y=30, width=150, height=33)

    
    def purchase_export_to_excel(self):
        con = mysql.connector.connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM purchase")
        sqldata = cur.fetchall()
        # Send data into dataframe
        df = pd.DataFrame(data=sqldata) 
        cur.close()
        # view dataframe
        print(df)
        #to_excel
        df.to_excel('D:\project_excel/purchase.xlsx', sheet_name='purchase')
        messagebox.showinfo("Purchase","Export successfully!")
    
    # ---delete purchase name -----
    def deletePurchase(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute('delete from purchase where purchase_id=%s', self.del_var.get())
        con.commit()
        self.fetch_allPurchase()
        con.close()

    #---- Update record -----
    def updatePurchase(self):
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("update purchase set purchase_price=%s, purchase_number=%s, purchase_money=DEFAULT, purchase_date=%s where purchase_id=%s",(
                                 self.purchase_price_var.get(),
                                 self.purchase_number_var.get(),
                                 self.purchase_date_var.get(),
                                 self.purchase_id_var.get(),   
                                 )
                    )
        con.commit()
        self.fetch_allPurchase() # display all rows
        self.clearPurchase()# after added record need to clear all entries
        con.close()

    #---- Search -----
    def searchPurchase(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from purchase where " +
        str(self.co_var.get())+" LIKE '%"+str(self.search_var.get())+"%'")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.purchase_table.delete(*self.purchase_table.get_children())
            for row in rows:
                self.purchase_table.insert("", END, values=row)
        con.commit()
        con.close()

    # ---clear entries -----
    def clearPurchase(self):
        self.purchase_id_var.set('')
        self.goods_id_var.set('')
        self.purchase_price_var.set('')
        self.purchase_number_var.set('')
        self.purchase_money_var.set('')
        self.purchase_date_var.set('')

    #---- Select row and display data inside each entry
    def get_cursorPurchase(self, ev):
       cursor_row=self.purchase_table.focus()
       contents=self.purchase_table.item(cursor_row)
       row=contents['values']
       self.purchase_id_var.set(row[0]) 
       self.goods_id_var.set(row[1]) 
       self.purchase_price_var.set(row[2]) 
       self.purchase_number_var.set(row[3]) 
       self.purchase_money_var.set(row[4])
       self.purchase_date_var.set(row[5])

    def sale(self):
        self.show_top_view()

        Label(self.top_view, text='[Sale Information]', bg=BG_COLOR, 
              font=('monospace', 14), fg='white').pack(fill=X)
        Manage_Frame = Frame(self.top_view, width=WINDOW_WIDTH, bg='white')
        Manage_Frame.place(x=5,y=30,width=175,height=400)

        # --------- Frame For Adding sale Data-----------
        lbl_sale_id = Label(Manage_Frame, bg='white', text='sale_id')
        lbl_sale_id.pack()
        sale_id_Entry= Entry(Manage_Frame,textvariable=self.sale_id_var, bd='2', justify='center')
        sale_id_Entry.pack()

        lbl_goods_id = Label(Manage_Frame, bg='white', text='goods_id')
        lbl_goods_id.pack()
        goods_id_Entry= Entry(Manage_Frame,textvariable=self.goods_id_var, bd='2', justify='center')
        goods_id_Entry.pack()

        lbl_client_id = Label(Manage_Frame, bg='white', text='client_id')
        lbl_client_id.pack()
        client_id_Entry= Entry(Manage_Frame,textvariable=self.client_id_var, bd='2', justify='center')
        client_id_Entry.pack()

        lbl_sale_price = Label(Manage_Frame, bg='white', text='sale_price')
        lbl_sale_price.pack()
        sale_price_Entry= Entry(Manage_Frame,textvariable=self.sale_price_var, bd='2', justify='center')
        sale_price_Entry.pack()

        lbl_sale_number = Label(Manage_Frame, bg='white', text='sale_number')
        lbl_sale_number.pack()
        sale_number_Entry= Entry(Manage_Frame,textvariable=self.sale_number_var, bd='2', justify='center')
        sale_number_Entry.pack()

        lbl_sale_date = Label(Manage_Frame, bg='white', text='sale_date')
        lbl_sale_date.pack()
        sale_date_Entry= Entry(Manage_Frame,textvariable=self.sale_date_var, bd='2', justify='center')
        sale_date_Entry.pack()

        lbl_delete = Label(Manage_Frame, bg='white', text='Delete Sale by ID', fg='red')
        lbl_delete.pack()
        delete_Entry= Entry(Manage_Frame,textvariable=self.del_var, bd='2', justify='center')
        delete_Entry.pack()

        #--------- Button Frame------
        btn_Frame= Frame(self.top_view, bg='white')
        btn_Frame.place(x=740,y=25, width=175, height=405)

        title=Label(btn_Frame, text='Controls', font=('Deco', 14), fg='white',bg='#5E95FF')
        title.pack(fill=X)

        add_btn=Button(btn_Frame,text='Add Button', bg='#5E95FF', command=self.addSale)
        add_btn.place(x=15, y=30, width=150, height=33)

        del_btn=Button(btn_Frame, text='Delete Button', bg='#5E95FF', command=self.deleteSale) 
        del_btn.place(x=15, y=65, width=150, height=33)

        update_btn=Button(btn_Frame, text='Update Button', bg='#5E95FF', command=self.updateSale)
        update_btn.place(x=15, y=100, width=150, height=33)

        clear_btn=Button(btn_Frame, text='Clear Button', bg='#5E95FF', command=self.clearSale)
        clear_btn.place(x=15, y=135, width=150, height=33)

        display_btn=Button(btn_Frame, text='Display Button', bg='#5E95FF', command=self.displaySale)
        display_btn.place(x=15, y=170, width=150, height=33)

        exit_btn=Button(btn_Frame, text='Exit Button', bg='#5E95FF', command=self.quit)
        exit_btn.place(x=15, y=205, width=150, height=33)

        #--------- Search for sale Data----
        search_Frame = Frame (self.top_view, bg='#FAE5D3') 
        search_Frame.place (x=10,y=440,width=900, height=75)

        lbl_search=Label (search_Frame, text='Choose to search', bg='#FAE5D3', width=15)
        lbl_search.place (x=170, y=20)

        combo_search = ttk.Combobox (search_Frame, justify='right', textvariable=self.co_var) 
        combo_search['value']=('sale_id','goods_id', 'client_id', 'sale_price', 'sale_number', 'sale_sum', 'sale_date')# modify it
        combo_search.place (x=280,y=20)

        search_Entry= Entry(search_Frame,textvariable=self.search_var, justify='right', bd='2')
        search_Entry.place (x=450, y=20)

        search_btn=Button(search_Frame, text='Search', bg='white', command=self.searchSale)
        search_btn.place(x=600, y=20, width=150, height=20)

        Details_Frame=Frame(self.top_view, bg="gray")
        Details_Frame.place(x=185, y=30, width=550, height=400)

        Scroll_X=Scrollbar(Details_Frame, orient=HORIZONTAL)
        Scroll_Y=Scrollbar(Details_Frame, orient=VERTICAL)

        self.sale_table=ttk.Treeview(Details_Frame,
        columns=('sale_id','goods_id','client_id', 'sale_price', 'sale_number', 'sale_sum', 'sale_date'),
        xscrollcommand=Scroll_X,
        yscrollcommand=Scroll_Y)

        self.sale_table.place(x=0, y=0, width=537, height=387)
        Scroll_X.pack(side=BOTTOM, fill=X)
        Scroll_Y.pack(side=RIGHT, fill=Y)
        Scroll_X.config(command=self.sale_table.xview)
        Scroll_Y.config(command=self.sale_table.yview)

        self.sale_table['show']='headings'
        self.sale_table.heading('sale_id', text='sale_id')
        self.sale_table.heading('goods_id', text='goods_id')
        self.sale_table.heading('client_id', text='client_id')
        self.sale_table.heading('sale_price', text='sale_price')
        self.sale_table.heading('sale_number', text='sale_number')
        self.sale_table.heading('sale_sum', text='sale_sum')
        self.sale_table.heading('sale_date', text='sale_date')

        self.sale_table.column('sale_id', width=76)
        self.sale_table.column('goods_id', width=76)
        self.sale_table.column('client_id', width=76)
        self.sale_table.column('sale_price', width=76)
        self.sale_table.column('sale_number', width=76)
        self.sale_table.column('sale_sum', width=76)
        self.sale_table.column('sale_date', width=76)
        self.sale_table.bind("<ButtonRelease-1>", self.get_cursorSale)

        self.fetch_allSale()

    def addSale(self): #-- pip install PyMySQL -- need to install----
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("insert into sale values(%s,%s,%s,%s,%s,DEFAULT,%s) ",(
                                 self.sale_id_var.get(),
                                 self.goods_id_var.get(),
                                 self.client_id_var.get(),
                                 self.sale_price_var.get(),
                                 self.sale_number_var.get(),
                                 self.sale_date_var.get()
                                 )
                    )
        con.commit()
        self.fetch_allSale() # display all rows
        self.clearSale()# after added record need to clear all entries
        con.close()

    def fetch_allSale(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from sale")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.sale_table.delete(*self.sale_table.get_children())
            for row in rows:
                self.sale_table.insert("", END, values=row)
                con.commit()
            con.close()

    def displaySale(self):
        self.show_top_view()
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur=con.cursor()
        cur.execute("select * from sale")
        rows=cur.fetchall()


        Label(self.top_view, text='Sale', font=('', 60, 'bold'), bg=BG_COLOR).pack()
        info_frame = Frame(self.top_view, width=WINDOW_WIDTH)
        info_frame.pack(pady=(20, 0), expand=True, fill='y')
        Label(info_frame, text='sale_id', font=('', 14)).place(x=20, y=0)
        Label(info_frame, text='goods_id', font=('', 14)).place(x=150, y=0)
        Label(info_frame, text='client_id', font=('', 14)).place(x=260, y=0)
        Label(info_frame, text='sale_price', font=('', 14)).place(x=380, y=0)
        Label(info_frame, text='sale_number', font=('', 14)).place(x=510, y=0)
        Label(info_frame, text='sale_sum', font=('', 14)).place(x=640, y=0)
        Label(info_frame, text='sale_date', font=('', 14)).place(x=760, y=0)

        info_all_frame = Frame(info_frame)
        info_all_frame.place(x=0, y=36, width=TOP_WIDTH, height=338)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                fund_info_label = tk.Label(info_frame, text=value)
                fund_info_label.place(x=(j * 120 + 65), y=((i + 3) * 20))
    
        btn_Frame= Frame(self.top_view, bg='#5E95FF')
        btn_Frame.place(x=0,y=450, width=920, height=100)
        export_btn=Button(btn_Frame, text='Export Button', bg='white', command=self.sale_export_to_excel)
        export_btn.place(x=400, y=30, width=150, height=33)

    
    def sale_export_to_excel(self):
        con = mysql.connector.connect(host='localhost', user='root', password='sw06010814', 
                            database='project')
        
        cur = con.cursor()
        cur.execute("SELECT * FROM sale")
        sqldata = cur.fetchall()
        # Send data into dataframe
        df = pd.DataFrame(data=sqldata) 
        cur.close()
        # view dataframe
        print(df)
        #to_excel
        df.to_excel('D:\project_excel/sale.xlsx', sheet_name='sale')
        messagebox.showinfo("Sale","Export successfully!")
    
    # ---delete sale name -----
    def deleteSale(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute('delete from sale where sale_id=%s', self.del_var.get())
        con.commit()
        self.fetch_allSale()
        con.close()

    #---- Update record -----
    def updateSale(self):
        con=pymysql.Connect(host='localhost', user='root', password='sw06010814', 
                                    database='project')
        cur=con.cursor()
        cur.execute("update sale set sale_price=%s, sale_number=%s, sale_sum=DEFAULT, sale_date=%s where sale_id=%s",(
                                 self.sale_price_var.get(),
                                 self.sale_number_var.get(),
                                 self.sale_date_var.get(),
                                 self.sale_id_var.get(),   
                                 )
                    )
        con.commit()
        self.fetch_allSale() # display all rows
        self.clearSale()# after added record need to clear all entries
        con.close()

    #---- Search -----
    def searchSale(self):
        con=pymysql.Connect(host='localhost', database='project', user='root', 
                          password='sw06010814')
        cur=con.cursor()
        cur.execute("select * from sale where " +
        str(self.co_var.get())+" LIKE '%"+str(self.search_var.get())+"%'")
        rows=cur.fetchall()
        if len (rows) !=0:
            self.sale_table.delete(*self.sale_table.get_children())
            for row in rows:
                self.sale_table.insert("", END, values=row)
        con.commit()
        con.close()

    # ---clear entries -----
    def clearSale(self):
        self.sale_id_var.set('')
        self.goods_id_var.set('')
        self.client_id_var.set('')
        self.sale_price_var.set('')
        self.sale_number_var.set('')
        self.sale_sum_var.set('')
        self.sale_date_var.set('')

    #---- Select row and display data inside each entry
    def get_cursorSale(self, ev):
       cursor_row=self.sale_table.focus()
       contents=self.sale_table.item(cursor_row)
       row=contents['values']
       self.sale_id_var.set(row[0]) 
       self.goods_id_var.set(row[1])
       self.client_id_var.set(row[2]) 
       self.sale_price_var.set(row[3]) 
       self.sale_number_var.set(row[4]) 
       self.sale_sum_var.set(row[5])
       self.sale_date_var.set(row[6])
    
    def about(self):
        self.show_top_view()

        Label(self.top_view, text='About me', font=('', 60, 'bold'), bg=BG_COLOR).pack()
        info_frame = Frame(self.top_view, width=WINDOW_WIDTH, bg=BG_COLOR)
        info_frame.pack(pady=(20, 0), expand=True, fill='both')
        Label(info_frame, text='I am Yawen Huang (Claire)\nMy student ID is 1194921\nThis is my final project\nSupermarket management System\nNice to meet you', 
              font=('', 40, 'bold'), bg=BG_COLOR).pack()


    # quit
    def quit(self):
        self.window.destroy()

    # Pop up the sub window
    def show_top_view(self):
        if self.top_view is not None:
            self.top_view.destroy()
            self.top_view = None
        self.top_view = Toplevel(background=BG_COLOR)

        # Get screen height and width
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set the window height and width and center it on the screen
        x = (screen_width - WINDOW_WIDTH) / 2
        y = (screen_height - WINDOW_HEIGHT) / 2
        root_size = '%dx%d+%d+%d' % ( WINDOW_WIDTH, WINDOW_HEIGHT, x, y)
        self.top_view.geometry(root_size)

        # Fixed size
        self.top_view.wm_resizable(False, False)

    # Display main Page
    def show_window(self):
        self.window.mainloop()
    
    
if __name__ == '__main__':
    m = TkinterMain()
    m.show_window()
        