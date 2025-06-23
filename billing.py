from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Billing_App:
    def __init__(self, root):
        self.root = root
        self.list1=[]
        self.root.geometry("1530x800")
        self.root.title("Billing Software")
        #variables
        self.customer_name=StringVar()
        self.customer_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.customer_email=StringVar()
        self.product_name=StringVar()
        self.product_price1=IntVar()
        self.subtotal=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.qty=IntVar()
    
        
        #product category list
        self.Categories=["Select Option","Clothing","Lifestyle","Mobiles","Food"]
        self.SubcategoryClothing=["Select Option","Pant","Tshirt","Skirt","Shirts","Tops","Kurti","Kurta set","Night suit","shorts"]
        self.pant=["Levis","Uniqlo","Zara","H&M","gap","Nike","Adidas","Puma"]
        self.price_levis_pant=4000
        self.price_uniqlo_pant=3000
        self.price_zara_pant=2000
        self.price_handm_pant=1500
        self.price_gap_pant=2300
        self.price_nike_pant=5999
        self.price_adidas_pant=7230
        self.price_puma_pant=9830
        self.tshirt=["PeterEngland","Zara","H&M","gap","Nike","Adidas","Puma","American Eagle","Reliance"]
        self.price_peterengland_tshirt=4003
        self.price_zara_tshirt=4820
        self.price_handm_tshirt=6521
        self.price_gap_tshirt=999
        self.price_nike_tshirt=7002
        self.price_adidas_tshirt=7652
        self.price_puma_tshirt=3218        
        self.price_americaneagle_tshirt=4000
        self.price_reliance_tshirt=9832
        self.skirt=["H&M","Zara","Forever 21","Mango","Marks and spencer"]
        self.price_zara_skirt=2300
        self.price_handm_skirt=1544
        self.price_forever21_skirt=983
        self.price_mango_skirt=7653
        self.price_marksandspencer_skirt=8732
        
        self.Shirts=["PeterEngland","Zara","H&M","GAP","Nike","Adidas","Puma","American Eagle","Reliance"]
        self.price_peterengland_shirts=6532
        self.price_zara_shirts=4873
        self.price_handm_shirts=6543
        self.price_gap_shirts=9090
        self.price_nike_shirts=4994
        self.price_adidas_shirts=9812
        self.price_puma_shirts=921      
        self.price_americaneagle_shirts=999
        self.price_reliance_shirts=599
        self.Tops=["Zara","Armani","Gucci","H&M","Max","Reliance","Mango","Uniqlo"]
        self.price_zara_top=4653
        self.price_armani_top=4832
        self.price_gucci_top=6000
        self.price_handm_top=2300
        self.price_max_top=600
        self.price_mango_top=433
        self.price_uniqlo_top=3218        
        self.price_reliance_top=3000
        self.Kurti=["Libas","Biba","Anokhi","Shree","shristi","globus","pantaloons","desi","reliance"]
        self.price_libas_kurti=2450
        self.price_biba_kurti=1999
        self.price_anokhi_kurti=2000
        self.price_shree_kurti=999
        self.price_shrishti_kurti=599
        self.price_globus_kurti=778
        self.price_pantaloons_kurti=3000       
        self.price_desi_kurti=599
        self.price_reliance_kurti=980
        self.kurtaset=["Libas","Biba","Anokhi","Shree","Shrishti","globus","Pantaloons","desi","Reliance"]
        self.price_libas_kurtaset=3450
        self.price_biba_kurtaset=2999
        self.price_anokhi_kurtaset=3000
        self.price_shree_kurtaset=1999
        self.price_shrishti_kurtaset=1599
        self.price_globus_kurtaset=1778
        self.price_pantloons_kurtaset=4000       
        self.price_desi_kurtaset=1599
        self.price_reliance_kurtaset=1980
        self.nightsuit=["zivame","Clovia","Enamor","Pretty Secrets","Life Partners"]
        self.price_zivame=1200
        self.price_clovia=1999
        self.price_enamor=2000
        self.price_prettysecrets=999
        self.price_lifepartners=599
        
        self.shorts=["H&M","Zara","Forever 21","Mango","Marks and spencer"]
        self.price_zara_shorts=2300
        self.price_handm_shorts=1544
        self.price_forever21_shorts=3000
        self.price_mango_shorts=7632
        self.price_marksandspencer_shorts=800

        self.SubcategoryLifestyle=["Bottle","Soap","Pencil","Detergent","Cream","Deoderant","Comb","Bedsheet"]
        self.bottle=["milton","dubblin","nayasa","borosil","cello","tupperware","pigeon"]
        self.price_milton=499
        self.price_dubblin=1200
        self.price_borosil=1000
        self.price_nayasa=299
        self.price_cello=599
        self.price_tupperware=399
        self.price_pigeon=599
        self.soap=["dove","himalaya","patanjali","cinthol","santoor","detol","medimix","margo","pears","khadi"]
        self.price_dove=120
        self.price_santoor=160
        self.price_detol=150
        self.price_himalaya=550
        self.price_cinthol=250
        self.price_detol=100
        self.price_medimix=200
        self.price_margo=300
        self.price_pears=400
        self.price_khadi=500
        self.price_patanjali=300
        self.pencil=["natraj","apsara","doms","camlin","fabercastel"]
        self.price_natraj=60
        self.price_apsara=70
        self.price_doms=100
        self.price_camlin=40
        self.price_fabercastel=50
        self.detergent=["surf excel","tide","ariel","rin","wheel","ezee","gentel"]
        self.price_surfexcel=399
        self.price_tide=400
        self.price_ariel=500
        self.price_rin=250
        self.price_wheel=600
        self.price_ezee=700
        self.price_gentel=300

        self.cream=["dotandkey","wishcare","plum","aqualogica","ponds","nivea","boroplus","vicco turmeric","vaseline"]
        self.price_dotandkey=499
        self.price_wishcare=500
        self.price_boroplus=50
        self.price_ponds=400
        self.price_aqualogica=499
        self.price_vaseline=399
        self.price_nivea=150
        self.price_plum=300
        self.price_viccoturmeric=40

        self.deoderant=["nivea","fogg","park avenue","axe","denever","eve","enagage"]
        self.price_eve=999
        self.price_denver=200
        self.price_axe=350
        self.price_park_avenue=400
        self.price_fogg=300
        self.price_nivea=200
        self.price_enagage=299
        self.price_parkavenue=400
        self.comb=["vega","roots","alan truman","gubb usa","satthwa"]
        self.price_vega=150
        self.price_roots=250
        self.price_alantruman=130
        self.price_gubbusa=111
        self.price_satthwa=300
        self.bedsheets=["bombay dyeing","spaces","swayam","trident","d decor","raymond home","maspar"]
        self.price_bombaydyeing=1200
        self.price_spaces=1000
        self.price_swayam=300
        self.price_trident=499
        self.price_ddecor=699
        self.price_raymondhome=600
        self.price_maspar=500
        self.SubcategoryMobiles=["Iphone","Samsung","One+"]
        self.iphone=["iphone 15 ","iphone15 plus","iphone 15 pro max","iphone se","iphone 16","iphone 16 promax"]
        self.price_iphone15=60000
        self.price_iphone15plus=75000
        self.price_iphone15promax=80000
        self.price_iphonese=150000
        self.price_iphone16=165000
        self.price_iphone16promax=180000
        self.samsung=["samsung m53","samsung f41","samsung s24","galaxy s fold"]
        self.price_samsungm53=20000
        self.price_samsungf41=11000
        self.price_samsungs24=84000
        self.price_galaxysfold=140000
        
        self.oneplus=["one plus 13","one plusnord 4","one plus ace 5 pro"]
        self.price_oneplus13=25000
        self.price_oneplusnord4=20000
        self.price_oneplusace5pro=30000

        self.SubcategoryFood=["Dal","Rice","Vegetables","Chips","Namkeens","Biscuit"]
        self.dal=["urad","malka","toor","moong","chana dal","rajma","lobia"]
        self.price_urad=120
        self.price_malka=80
        self.price_toor=70
        self.price_moong=70
        self.price_chanadal=140
        self.price_rajma=90
        self.price_lobia=40
        
        self.rice=["basmati","ponni","sonna","idli","black rice"]
        self.price_basmati=399
        self.price_ponni=2100
        self.price_sonna=3009
        self.price_idli=250
        self.price_blackrice=240
      
        self.vegetables=["aloo","bindi","karela","onion","garlic","lauki","capsicum"]
        self.price_aloo=10
        self.price_bindi=50
        self.price_karela=40
        self.price_onion=60
        self.price_garlic=30
        self.price_lauki=20
        self.price_capsicum=30

        self.chips=["lays", "bingo", "UncleChips", "Crax", "Pringles", "kurkure"]
        self.price_lays=25
        self.price_bingo=35
        self.price_UncleChips=30
        self.price_Crax=20
        self.price_Pringles=80
        self.price_kurkure=45

       
        self.namkeens=["navratan","halirams","bikaji","bikaner","kalev","kipps"]
        self.price_navratan=55
        self.price_haldiram=200
        self.price_bikaji=40
        self.price_bikaner=250
        self.price_kalev=200
        self.price_kipps=79
        self.biscuits=["parle g","hide and seek","oreo","bourbon","jim jam","milk bikis","malkist"]
        self.price_parleg=20
        self.price_hideandseek=35
        self.price_oreo=30
        self.price_bourbon=25
        self.price_jimjam=20
        self.price_milkbikis=50
        self.price_malkist=300
        

        # ========== HEADER IMAGES ==========
        # Image 1 (Left)
        img = Image.open(r"Food-Grocery-Vegetables-1140771380.jpg")
        img = img.resize((400, 100))  # Resize first
        self.photoimg = ImageTk.PhotoImage(img)

        labelimg = Label(self.root, image=self.photoimg)
        labelimg.place(x=0, y=0, width=400, height=100)

        # Image 2 (Center)
        img1 = Image.open(r"OIP (4).jpg")
        img1 = img1.resize((400, 100))  # Resize first
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimg2 = Label(self.root, image=self.photoimg1)
        labelimg2.place(x=360, y=0, width=400, height=100)  # Adjust position

        # Image 3 (Right)
        img2 = Image.open(r"OIP (5).jpg")
        img2 = img2.resize((300, 100))  # Resize first
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimg3 = Label(self.root, image=self.photoimg2)
        labelimg3.place(x=750, y=0, width=300, height=100)  # Adjust position

        # Image 4 (Right)
        img3 = Image.open(r"OIP (6).jpg")
        img3 = img3.resize((600, 100))  # Resize first
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelimg4 = Label(self.root, image=self.photoimg3)
        labelimg4.place(x=1040, y=0, width=400, height=100)  # Adjust position

        # ========== TITLE ==========
        lbl_title = Label(self.root, text="BILLING SOFTWARE", font=("times new roman", 25, "bold"),
                          bg="#B76E79", fg="pink")
        lbl_title.place(x=0, y=100, width=1530, height=45)

        def time():
          string1=strftime("%H:%M:%S %p")
          lbl.config(text=string1)
          lbl.after(1000,time)
        lbl=Label(lbl_title,font=('times new roman',16,"bold"),background="white",foreground="#B76E79")
        lbl.place(x=0,y=(-1),width=120,height=50)
        time()

        # ========== MAIN FRAME ==========
        main_frame = Frame(self.root, bd=5, relief="groove", bg="white")
        main_frame.place(x=0, y=140, width=1525, height=555)

        # ========== CUSTOMER FRAME ==========
        customer_label = LabelFrame(main_frame, text="Customer", font=("times new roman", 12, "bold"),
                                    bg="#B76E79", fg="pink")
        customer_label.place(x=10, y=5, width=350, height=140)

        Label(customer_label, text="Mobile Number", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=0, column=0, sticky=W, padx=5, pady=2)
        Entry(customer_label,textvariable=self.customer_phone, font=("times new roman", 12, "bold"), width=24).grid(row=0, column=1)

        Label(customer_label, text="Name", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=1, column=0, sticky=W, padx=5, pady=2)
        Entry(customer_label,textvariable=self.customer_name, font=("times new roman", 12, "bold"), width=24).grid(row=1, column=1)

        Label(customer_label, text="Email", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=2, column=0, sticky=W, padx=5, pady=2)
        Entry(customer_label,textvariable=self.customer_email, font=("times new roman", 12, "bold"), width=24).grid(row=2, column=1)

        # ========== PRODUCT FRAME ==========
        product_label = LabelFrame(main_frame, text="Product", font=("times new roman", 12, "bold"),
                                   bg="#B76E79", fg="pink")
        product_label.place(x=365, y=5, width=500, height=140)
        #category
        Label(product_label, text="Select Category", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.combocategory = ttk.Combobox(product_label,textvariable=self.product_name, font=("arial", 9, "bold"),
                                          width=13, state="readonly",
                                          values=self.Categories)
        self.combocategory.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.combocategory.current(0)
        self.combocategory.bind("<<ComboboxSelected>>",self.update_subcategories)
        #subcategory
        Label(product_label, text="Select Subcategory", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.combosubcategory = ttk.Combobox(product_label, font=("arial", 9, "bold"),
                                          width=13, state="readonly",
                                          )
        self.combosubcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        
        self.combosubcategory.bind("<<ComboboxSelected>>",self.update_productname)

        #productname
        Label(product_label, text="Product Name" ,font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.comboproduct_name = ttk.Combobox(product_label, font=("arial", 9, "bold"),
                                          width=13, state="readonly"
                                           )
        self.comboproduct_name.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.comboproduct_name.bind("<<ComboboxSelected>>",self.product_price)
        #productprice
        Label(product_label, text="Price", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.comboproduct_price = ttk.Combobox(product_label, font=("arial", 9, "bold"),
                                          width=13, state="readonly",
                                          )
        self.comboproduct_price.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        #self.combocategory.bind("<<ComboboxSelected>>",self.update_productprice)

        Entry(product_label,textvariable=self.qty, font=("times new roman", 12, "bold"), width=14).grid(row=1, column=3)

        Label(product_label, text="Quantity", font=("times new roman", 12, "bold"),
              bg="#B76E79", fg="black").grid(row=1, column=2, sticky=W, padx=5, pady=2)
        
      #=================== MIDDLE FRAME ===============================
        middle_frame = Frame(main_frame, bd=5, relief="groove", bg="white")
        middle_frame.place(x=10, y=150, width=850, height=215)

        # Image 1 (Left)
        shopping = Image.open(r"OIP (7).jpg")
        shopping = shopping.resize((400, 215))
        self.shopingimg = ImageTk.PhotoImage(shopping)

        lbl_shopping = Label(middle_frame, image=self.shopingimg, bd=2)
        lbl_shopping.place(x=0, y=0, width=400, height=215)

      # Image 2 (Right)
        shopping1 = Image.open(r"Food-Grocery-Vegetables-1140771380.jpg")
        shopping1 = shopping1.resize((450, 215))
        self.shopingimg1 = ImageTk.PhotoImage(shopping1)

        lbl_shopping1 = Label(middle_frame, image=self.shopingimg1, bd=2)
        lbl_shopping1.place(x=400, y=0, width=450, height=215)


        #search
        bill_frame=Frame(main_frame,bd=2,bg="white")
        bill_frame.place(x=870,y=5,width=1000,height=600 )

        self.lblbill=Label(bill_frame,font=('arial',10,'bold'),fg="black",width=24,text="Bill Number",background="pink")
        self.lblbill.grid(row=0,column=0,sticky=W,padx=0,pady=0)


        self.text_entry_search=ttk.Entry(bill_frame,font=('arial',12,'bold'),width=16)
        self.text_entry_search.grid(row=0,column=1,sticky=W,padx=2,pady=2)

        self.btnsearch=Button(bill_frame,text="Search",command=self.search,font=('arial',10,"bold"),width=14,bg="pink",fg="black")
        self.btnsearch.grid(row=0,column=5)
        #Right Frame 
        rightlabelframe= LabelFrame(main_frame, text="Bill Area", font=("times new roman", 12, "bold"),
                                    bg="#B76E79", fg="pink")
        rightlabelframe.place(x=870, y=40, width=480, height=356)

        scroll_y=Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea=Text(rightlabelframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",
                           font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        
        #bottom frame
        bottom_frame=LabelFrame(main_frame,text="Bill Counter",font=("times new roman",12,"bold",),bg="#B76E79",fg="pink")
        bottom_frame.place(x=0,y=385,width=1350,height=160)
        self.labelsubtotal=Label(bottom_frame,font=("arial",12,"bold"),bg="#B76E79",fg="pink",text="Subtotal",bd=4)
        self.labelsubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Entry=ttk.Entry(bottom_frame,textvariable=self.subtotal,font=("arial",12,"bold"),width=10)
        self.Entry.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.labeltax=Label(bottom_frame,font=("arial",12,"bold"),bg="#B76E79",fg="black",text="Tax",bd=4)
        self.labeltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.Entry=ttk.Entry(bottom_frame,textvariable=self.tax_input,font=("arial",12,"bold"),width=10)
        self.Entry.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.labelamounttotal=Label(bottom_frame,font=("arial",12,"bold"),bg="#B76E79",fg="black",text="Amount total",bd=4)
        self.labelamounttotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Entry=ttk.Entry(bottom_frame, textvariable=self.total,font=("arial",12,"bold"),width=10)
        self.Entry.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #button frame
        button_frame=Frame(bottom_frame,bd=2,bg="white")
        button_frame.place(x=245,y=0)

        self.btnaddtocart=Button(button_frame,text="Add to Cart",command=self.additem,font=("times new roman",15,"bold"),bg="pink",fg="black",width=12,cursor="hand2")
        self.btnaddtocart.grid(row=0,column=0)

        self.btngenerate=Button(button_frame,text="Generate Bill",command=self.generatebill,font=("times new roman",15,"bold"),bg="pink",fg="black",width=12 ,cursor="hand2")
        self.btngenerate.grid(row=0,column=1)

        self.btnclear=Button(button_frame,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="pink",fg="black",width=12,cursor="hand2")
        self.btnclear.grid(row=0,column=2)

        self.btnsave=Button(button_frame,text="Save Bill",command=self.save_bill,font=("times new roman",15,"bold"),bg="pink",fg="black",width=12,cursor="hand2")
        self.btnsave.grid(row=0,column=3)

        self.btnexit=Button(button_frame,text="Exit",font=("times new roman",15,"bold"),bg="pink",fg="black",width=12,cursor="hand2")
        self.btnexit.grid(row=0,column=4)

        self.btnprint=Button(button_frame,text="print",command=self.print1,font=("times new roman",15,"bold"),bg="pink",fg="black",width=12,cursor="hand2")
        self.btnprint.grid(row=0,column=5)
        
        self.welcome()
    
         
    def search(self):
          found = False
          bill_no = self.text_entry_search.get()

          for i in os.listdir("bills/"):
               if i.split(".")[0] == bill_no:
                    with open(f"bills/{i}", 'r') as f1:
                         self.textarea.delete(1.0, END)
                         for j in f1:
                              self.textarea.insert(END, j)
                    found = True
                    break  # Bill found, no need to keep checking

          if not found:
               messagebox.showerror("Error", "No such bill found")
    def clear(self):
         self.textarea.delete(1.0,END)
         self.customer_name.set("")
         self.customer_email.set("")
         self.customer_phone.set("")
         x=random.randint(1000,99999)
         self.bill_no.set(str(x))
         self.text_entry_search.set("")
         self.comboproduct_price.set(0)
         self.qty.set(0)
         self.list1=[0]
         self.total.set("")
         self.subtotal.set("")
         self.tax_input.set("")
         self.welcome()



         

          
        

    def additem(self):
          Tax = 1

          if self.product_name.get() == "Select Option":
               messagebox.showerror("Error", "Please select a valid product")
               return

          try:
               self.n = float(self.comboproduct_price.get())
               self.m = int(self.qty.get()) * self.n
          except:
               messagebox.showerror("Error", "Invalid quantity or price")
               return

          # ✅ Store (product name, quantity, price)
          product = self.comboproduct_name.get()
          quantity = int(self.qty.get())
          price = self.m

          self.list1.append((product, quantity, price))

          self.textarea.insert(END, f"\n {product}\t\t\t{quantity}\t{price}")
          
          subtotal = sum(item[2] for item in self.list1)  # sum of prices
          self.subtotal.set(f'Rs.{subtotal:.2f}')
          tax_amount = ((subtotal - self.n) * Tax) / 100
          self.tax_input.set(f'Rs.{tax_amount:.2f}')
          self.total.set(f'Rs.{subtotal + tax_amount:.2f}')


          


 

    def generatebill(self):
          if self.product_name.get() == "Select":
               messagebox.showerror("Error", "Please select a valid product")
               return

          else:
               
               text=self.textarea.get(10.0,(10.0+ float(len(self.list1))))

               self.welcome() # Starts a fresh bill
               for item in self.list1:
            # Assuming each item in self.list is a tuple like: (product_name, quantity, price)
                    product, qty, price = item
                    self.textarea.insert(END, f"\n{product:<20}{qty:<10}{price:<10}\n")

               

               self.textarea.insert(END, "\n==================================================")
               self.textarea.insert(END, f"\n Sub amount:\t\t\t{self.subtotal.get()}")
               self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
               self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")
               self.textarea.insert(END, "\n==================================================")
    def print1(self):
         q=self.textarea.get(1.0,"end-1c")
         filename=tempfile.mktemp('.txt')
         open(filename,'w').write(q)
         os.startfile(filename,"print")
          

    def save_bill(self):
         op=messagebox.askyesno("SAVE BILL","Do you want to save the bill")
         if op>0:
              self.bill_data=self.textarea.get(1.0,END)
              f1=open('bills/'+str(self.bill_no.get())+ ".txt",'w')
              f1.write(self.bill_data)
              f1.close()


                
    def welcome(self):
         
         self.textarea.delete(1.0, END)
         self.textarea.insert(END, "\t\tWelcome to City Center Mall")
         self.textarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
         self.textarea.insert(END, f"\n Customer Name: {self.customer_name.get()}")
         self.textarea.insert(END, f"\n Customer Email: {self.customer_email.get()}")
         self.textarea.insert(END, f"\n Phone Number: {self.customer_phone.get()}")

         self.textarea.insert(END, "\n" + "="*50)
         self.textarea.insert(END, f"\n{'Product':<20}{'Quantity':<10}{'Price':<10}")
         self.textarea.insert(END, "\n" + "="*50)
               
    def update_subcategories(self, event=None):
        category = self.combocategory.get()
        if category == "Clothing":
            self.combosubcategory['values'] = self.SubcategoryClothing
        elif category == "Lifestyle":
            self.combosubcategory['values'] = self.SubcategoryLifestyle
        elif category == "Mobiles":
            self.combosubcategory['values'] = self.SubcategoryMobiles
        elif category == "Food":
            self.combosubcategory['values'] = self.SubcategoryFood
        else:
            self.combosubcategory['values'] = []

        self.combosubcategory.current(0)
        #self.combosubcategory.bind("<<ComboboxSelected>>", self.update_productname)

    def update_productname(self, event=None):
      subcategory = self.combosubcategory.get()
      product_list = []

      # Clothing
      if subcategory == "Pant":
            product_list = self.pant
      elif subcategory == "Tshirt":
            product_list = self.tshirt
      elif subcategory == "Skirt":
            product_list = self.skirt
      elif subcategory == "Shirts":
            product_list = self.Shirts
      elif subcategory == "Tops":
            product_list = self.Tops
      elif subcategory == "Kurti":
            product_list = self.Kurti
      elif subcategory == "Kurta set":
            product_list = self.kurtaset
      elif subcategory == "Night suit":
            product_list = self.nightsuit
      elif subcategory == "shorts":
        product_list = self.shorts

      # Lifestyle
      elif subcategory == "Bottle":
            product_list = self.bottle
      elif subcategory == "Soap":
            product_list = self.soap
      elif subcategory == "Pencil":
            product_list = self.pencil
      elif subcategory == "Detergent":
            product_list = self.detergent
      elif subcategory == "Cream":
            product_list = self.cream
      elif subcategory == "Deoderant":
            product_list = self.deoderant
      elif subcategory == "Comb":
            product_list = self.comb
      elif subcategory == "Bedsheet":
            product_list = self.bedsheets

      # Mobiles
      elif subcategory == "Iphone":
            product_list = self.iphone
      elif subcategory == "Samsung":
            product_list = self.samsung
      elif subcategory == "One+":
            product_list = self.oneplus

      # Food
      elif subcategory == "Dal":
            product_list = self.dal
      elif subcategory == "Rice":
            product_list = self.rice
      elif subcategory == "Vegetables":
            product_list = self.vegetables
      elif subcategory == "Chips":
            product_list = self.chips
           
            
            
      elif subcategory == "Namkeens":
            product_list = self.namkeens
      elif subcategory == "Biscuit":
            product_list = self.biscuits

      self.comboproduct_name['values'] = product_list
      if product_list:
        self.comboproduct_name.current(0)
    def product_price(self,event=""):
         #pant
         #["Levis","Uniqlo","Zara","H&M","Gap","Nike","Adidas","Puma"]
         if  self.comboproduct_name.get()=="Levis":
              self.comboproduct_price.config(value=self.price_levis_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Uniqlo":
              self.comboproduct_price.config(value=self.price_uniqlo_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Gap":
              self.comboproduct_price.config(value=self.price_gap_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Nike":
              self.comboproduct_price.config(value=self.price_nike_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Adidas":
              self.comboproduct_price.config(value=self.price_adidas_pant)
              self.qty.set(1)
         elif  self.comboproduct_name.get()=="Puma":
              self.comboproduct_price.config(value=self.price_puma_pant)
              self.qty.set(1)
        #tshirt
         elif self.comboproduct_name.get()=="PeterEngland":
              self.comboproduct_price.config(value=self.price_peterengland_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="gap":
              self.comboproduct_price.config(value=self.price_gap_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Nike":
              self.comboproduct_price.config(value=self.price_nike_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Adidas":
              self.comboproduct_price.config(value=self.price_adidas_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Puma":
              self.comboproduct_price.config(value=self.price_puma_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="American Eagle":
              self.comboproduct_price.config(value=self.price_americaneagle_tshirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Reliance":
              self.comboproduct_price.config(value=self.price_reliance_tshirt)
              self.qty.set(1)
         #skirt

         elif self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_skirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_skirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Forever 21":
              self.comboproduct_price.config(value=self.price_forever21_skirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Mango":
              self.comboproduct_price.config(value=self.price_mango_skirt)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Marks and spencer":
              self.comboproduct_price.config(value=self.price_marksandspencer_skirt)
              self.qty.set(1)
         #shirt

         elif self.comboproduct_name.get()=="PeterEngland":
              self.comboproduct_price.config(value=self.price_peterengland_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="gap":
              self.comboproduct_price.config(value=self.price_gap_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Nike":
              self.comboproduct_price.config(value=self.price_nike_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Adidas":
              self.comboproduct_price.config(value=self.price_adidas_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Puma":
              self.comboproduct_price.config(value=self.price_puma_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="American Eagle":
              self.comboproduct_price.config(value=self.price_americaneagle_shirts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Reliance":
              self.comboproduct_price.config(value=self.price_reliance_shirts)
              self.qty.set(1)

         #tops
         elif self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Armani":
              self.comboproduct_price.config(value=self.price_zara_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Gucci":
              self.comboproduct_price.config(value=self.price_gucci_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Max":
              self.comboproduct_price.config(value=self.price_max_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Mango":
              self.comboproduct_price.config(value=self.price_mango_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Unqilo":
              self.comboproduct_price.config(value=self.price_uniqlo_top)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Reliance":
              self.comboproduct_price.config(value=self.price_reliance_top)
              self.qty.set(1)
         #kurti
         elif self.comboproduct_name.get()=="Libas":
              self.comboproduct_price.config(value=self.price_libas_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Biba":
              self.comboproduct_price.config(value=self.price_biba_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Anokhi":
              self.comboproduct_price.config(value=self.price_anokhi_kurti)
              self.qty.set(1)

         elif self.comboproduct_name.get()=="Shree":
              self.comboproduct_price.config(value=self.price_shree_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Shrishti":
              self.comboproduct_price.config(value=self.price_shrishti_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="globus":
              self.comboproduct_price.config(value=self.price_globus_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Pantaloons":
              self.comboproduct_price.config(value=self.price_pantaloons_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="desi":
              self.comboproduct_price.config(value=self.price_desi_kurti)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Reliance":
              self.comboproduct_price.config(value=self.price_reliance_kurti)   
              self.qty.set(1)
         #kurtaset  
         #         self.kurtaset=["Libas","Biba","Anokhi","Shree","shristi","globus","pantaloons","desi","reliance"]
   
         elif self.comboproduct_name.get()=="Libas":
              self.comboproduct_price.config(value=self.price_libas_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Biba":
              self.comboproduct_price.config(value=self.price_biba_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Anokhi":
              self.comboproduct_price.config(value=self.price_anokhi_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Shree":
              self.comboproduct_price.config(value=self.price_shree_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Shrishti":
              self.comboproduct_price.config(value=self.price_shrishti_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="globus":
              self.comboproduct_price.config(value=self.price_globus_kurtaset)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Pantaloons":
              self.comboproduct_price.config(value=self.price_pantaloon_kurtaset)
         elif self.comboproduct_name.get()=="desi":
              self.qty.set(1)
              self.comboproduct_price.config(value=self.price_desi_kurtaset)
         elif self.comboproduct_name.get()=="Reliance":
              self.comboproduct_price.config(value=self.price_reliance_kurtaset)
              self.qty.set(1)
         #nightsuit
         
         elif self.comboproduct_name.get()=="zivame":
              self.comboproduct_price.config(value=self.price_zivame)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Clovia":
              self.comboproduct_price.config(value=self.price_clovia)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Enamor":
              self.comboproduct_price.config(value=self.price_enamor)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Pretty Secrets":
              self.comboproduct_price.config(value=self.price_prettysecrets)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Life Partners":
              self.comboproduct_price.config(value=self.price_lifepartners)
              self.qty.set(1)
         #shorts
         elif self.comboproduct_name.get()=="H&M":
              self.comboproduct_price.config(value=self.price_handm_shorts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Zara":
              self.comboproduct_price.config(value=self.price_zara_shorts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Forever21":
              self.comboproduct_price.config(value=self.price_forever21_shorts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Mango":
              self.comboproduct_price.config(value=self.price_mango_shorts)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="Marks and spencer":
              self.comboproduct_price.config(value=self.price_marksandspencer_shorts)
              self.qty.set(1)
         #bottles
         #x=["milton","dubblin","nayasa","borosil","cello","tupperware","pigeon"]
         elif self.comboproduct_name.get()=="milton":
              self.comboproduct_price.config(value=self.price_milton)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="dubblin":
              self.comboproduct_price.config(value=self.price_dubblin)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="nayasa":
              self.comboproduct_price.config(value=self.price_nayasa)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="borosil":
              self.comboproduct_price.config(value=self.price_borosil)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="cello":
              self.comboproduct_price.config(value=self.price_cello)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="tupperware":
              self.comboproduct_price.config(value=self.price_tupperware)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="pigeon":
              self.comboproduct_price.config(value=self.price_pigeon)
              self.qty.set(1)
         #soap
         #["dove","himalaya","patanjali","cinthol","santoor","detol","medimix","margo","pears","khadi"]
         elif self.comboproduct_name.get()=="dove":
              self.comboproduct_price.config(value=self.price_dove)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="himalaya":
              self.comboproduct_price.config(value=self.price_himalaya)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="patanjali":
              self.comboproduct_price.config(value=self.price_patanjali)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="cinthol":
              self.comboproduct_price.config(value=self.price_cinthol)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="santoor":
              self.comboproduct_price.config(value=self.price_santoor)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="detol":
              self.comboproduct_price.config(value=self.price_detol)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="medimix":
              self.comboproduct_price.config(value=self.price_medimix)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="margo":
              self.comboproduct_price.config(value=self.price_margo)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="pears":
              self.comboproduct_price.config(value=self.price_pears)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="khadi":
              self.comboproduct_price.config(value=self.price_khadi)
              self.qty.set(1)
         #pencil
         #["natraj","apsara","doms","camlin","faber castel"]
         elif self.comboproduct_name.get()=="natraj":
              self.comboproduct_price.config(value=self.price_natraj)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="apsara":
              self.comboproduct_price.config(value=self.price_apsara)
              self.comboproduct_price.current(0)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="camlin":
              self.comboproduct_price.config(value=self.price_camlin)
              self.comboproduct_price.current(0)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="fabercastel":
              self.comboproduct_price.config(value=self.price_fabercastel)
              self.comboproduct_price.current(0)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="doms":
              self.comboproduct_price.config(value=self.price_doms)
              self.comboproduct_price.current(0)

         #["surf excel","tide","ariel","rin","wheel","ezee","gentel"]
         elif self.comboproduct_name.get()=="surf excel":
              self.comboproduct_price.config(value=self.price_surfexcel)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="tide":
              self.comboproduct_price.config(value=self.price_tide)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="ariel":
              self.comboproduct_price.config(value=self.price_ariel)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="rin":
              self.comboproduct_price.config(value=self.price_rin)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="wheel":
              self.comboproduct_price.config(value=self.price_wheel)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="ezee":
              self.comboproduct_price.config(value=self.price_ezee)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="gentel":
              self.comboproduct_price.config(value=self.price_gentel)
              self.qty.set(1)
         #["dotandkey","wishcare","plum","aqualogica","ponds","nivea","boroplus","vicco turmeric","vaseline"]
         elif self.comboproduct_name.get()=="dotandkey":
              self.comboproduct_price.config(value=self.price_dotandkey)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="wishcare":
              self.comboproduct_price.config(value=self.price_wishcare)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="plum":
              self.comboproduct_price.config(value=self.price_plum)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="aqualogica":
              self.comboproduct_price.config(value=self.price_aqualogica)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="ponds":
              self.comboproduct_price.config(value=self.price_ponds)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="nivea":
              self.comboproduct_price.config(value=self.price_nivea)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="boroplus":
              self.comboproduct_price.config(value=self.price_boroplus)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="vicco turmeric":
              self.comboproduct_price.config(value=self.price_viccoturmeric)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="vaseline":
              self.comboproduct_price.config(value=self.price_vaseline)
              self.qty.set(1)
         #deoderant
         #["nivea","fogg","park avenue","axe","denever","eve","enagage"]
         elif self.comboproduct_name.get()=="nivea":
              self.comboproduct_price.config(value=self.price_nivea)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="fogg":
              self.comboproduct_price.config(value=self.price_fogg)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="park avenue":
              self.comboproduct_price.config(value=self.price_park_avenue)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="axe":
              self.comboproduct_price.config(value=self.price_axe)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="denever":
              self.comboproduct_price.config(value=self.price_denver)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="eve":
              self.comboproduct_price.config(value=self.price_eve)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="engage":
              self.comboproduct_price.config(value=self.price_enagage)
              self.qty.set(1)
         #comb
         #["vega","roots","alan truman","gubb usa","satthwa"]
         elif self.comboproduct_name.get()=="vega":
              self.comboproduct_price.config(value=self.price_vega)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="roots":
              self.comboproduct_price.config(value=self.price_roots)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="alan truman":
              self.comboproduct_price.config(value=self.price_alantruman)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="gubb usa":
              self.comboproduct_price.config(value=self.price_gubbusa)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="satthwa":
              self.comboproduct_price.config(value=self.price_satthwa)
              self.qty.set(1)
         #bedsheets
         #["bombay dyeing","spaces","swayam","trident","d decor","raymond home","maspar"]
         elif self.comboproduct_name.get()=="bombay dyeing":
              self.comboproduct_price.config(value=self.price_bombaydyeing)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="spaces":
              self.comboproduct_price.config(value=self.price_spaces)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="swayam":
              self.comboproduct_price.config(value=self.price_swayam)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="trident":
              self.comboproduct_price.config(value=self.price_trident)
              self.qty.set(1)
         elif self.comboproduct_name.get()=="d decor":
              self.comboproduct_price.config(value=self.price_ddecor)
              self.qty.set(1)
              
              
         elif self.comboproduct_name.get()=="raymond home":
              self.comboproduct_price.config(value=self.price_raymondhome)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="maspar":
              self.comboproduct_price.config(value=self.price_maspar)
              self.qty.set(1) 
         #iphone
         #["iphone 15 ","iphone15 plus","iphone 15 pro max","iphone se","iphone 16","iphone 16 promax"]
         elif self.comboproduct_name.get()=="iphone 15":
              self.comboproduct_price.config(value=self.price_iphone15 )
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="iphone 15 pro max":
              self.comboproduct_price.config(value=self.price_iphone15promax)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="iphone se":
              self.comboproduct_price.config(value=self.price_iphonese)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="iphone 16":
              self.comboproduct_price.config(value=self.price_iphone16)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="iphone 16 promax":
              self.comboproduct_price.config(value=self.price_iphone16promax)
              self.qty.set(1) 
         #samsung
         #["samsung m53","samsung f41","samsung s24","galaxy s fold"]
         elif self.comboproduct_name.get()=="samsung m53":
              self.comboproduct_price.config(value=self.price_samsungm53)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="samsungf41":
              self.comboproduct_price.config(value=self.price_samsungf41)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="samsung s24":
              self.comboproduct_price.config(value=self.price_samsungs24)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="samsung galaxy s fold":
              self.comboproduct_price.config(value=self.price_galaxysfold)
              self.qty.set(1) 
         #oneplus
         #["one plus 13","one plusnord 4","one plus ace 5 pro"]
         elif self.comboproduct_name.get()=="one plus 13":
              self.comboproduct_price.config(value=self.price_oneplus13)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="one plusnord 4":
              self.comboproduct_price.config(value=self.price_oneplusnord4)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="one plus ace 5 pro":
              self.comboproduct_price.config(value=self.price_oneplusace5pro)
              self.qty.set(1) 
         #dal
         #["urad","malka","toor","moong","chana dal","rajma","lobia"]
         elif self.comboproduct_name.get()=="urad":
              self.comboproduct_price.config(value=self.price_urad)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="malka":
              self.comboproduct_price.config(value=self.price_malka)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="toor":
              self.comboproduct_price.config(value=self.price_toor)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="moong":
              self.comboproduct_price.config(value=self.price_moong)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="chana dal":
              self.comboproduct_price.config(value=self.price_chanadal)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="rajma":
              self.comboproduct_price.config(value=self.price_rajma)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="lobia":
              self.comboproduct_price.config(value=self.price_lobia)
              self.qty.set(1) 
         #rice
         #["basmati","ponni","sonna","idli","black rice"]
         elif self.comboproduct_name.get()=="basmati":
              self.comboproduct_price.config(value=self.price_basmati)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="ponni":
              self.comboproduct_price.config(value=self.price_ponni)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="sonna":
              self.comboproduct_price.config(value=self.price_sonna)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="idli":
              self.comboproduct_price.config(value=self.price_idli)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="blackrice":
              self.comboproduct_price.config(value=self.price_blackrice)
              self.qty.set(1) 
         #vegetables
         
         elif self.comboproduct_name.get()=="aloo":
              self.comboproduct_price.config(value=self.price_aloo)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="bindi":
              self.comboproduct_price.config(value=self.price_bindi)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="karela":
              self.comboproduct_price.config(value=self.price_karela)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="onion":
              self.comboproduct_price.config(value=self.price_onion)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="garlic":
              self.comboproduct_price.config(value=self.price_garlic)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="lauki":
              self.comboproduct_price.config(value=self.price_lauki)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="capsicum":
              self.comboproduct_price.config(value=self.price_capsicum)
              self.qty.set(1)
          #chips
          
       
         elif self.comboproduct_name.get()=="lays":
              self.comboproduct_price.config(value=self.price_lays)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="bingo":
              self.comboproduct_price.config(value=self.price_bingo)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="UncleChips":
              self.comboproduct_price.config(value=self.price_UncleChips)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="Crax":
              self.comboproduct_price.config(value=self.price_Crax)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="Pringles":
              self.comboproduct_price.config(value=self.price_Pringles)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="kurkure":
              self.comboproduct_price.config(value=self.price_kurkure)
              self.qty.set(1) 
       


         #namkeens
       
         elif self.comboproduct_name.get()=="navratan":
              self.comboproduct_price.config(value=self.price_navratan)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="haldirams":
              self.comboproduct_price.config(value=self.price_haldirams)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="bikaji":
              self.comboproduct_price.config(value=self.price_bikaji)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="bikaner":
              self.comboproduct_price.config(value=self.price_bikaner)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="kalev":
              self.comboproduct_price.config(value=self.price_kalev)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="kipps":
              self.comboproduct_price.config(value=self.price_kipps)
              self.qty.set(1) 
         #biscuits
        
         elif self.comboproduct_name.get()=="parle g":
              self.comboproduct_price.config(value=self.price_parleg)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="haldirams":
              self.comboproduct_price.config(value=self.price_hideandseek)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="oreo":
              self.comboproduct_price.config(value=self.price_oreo)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="bourbon":
              self.comboproduct_price.config(value=self.price_bourbon)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="jimjam":
              self.comboproduct_price.config(value=self.price_jimjam)
              self.qty.set(1) 
         elif self.comboproduct_name.get()=="milk bikis":
              self.qty.set(1)
              self.comboproduct_price.config(value=self.price_milkbikis)
         elif self.comboproduct_name.get()=="malkist":
              self.comboproduct_price.config(value=self.price_malkist) 
              
              self.qty.set(1) 
         self.comboproduct_price.current(0)   

         
           
        


if __name__ == '__main__':
    root = Tk()
    obj = Billing_App(root)
    root.mainloop()
