#Program #4 - Creating a program which you will enter the amoun of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title ("Maihannn's Apple Store")
root.geometry ( '1110x780')
bg_color="#EEF0F1"

#Variable
apple_cost=(20.00)
current_money_input=IntVar()
maximum_apple=IntVar()
maximum_apple=StringVar()
total_price=IntVar()
total_price=StringVar()
remaining_money_total=IntVar()
remaining_money_total=StringVar()

#Functions

def Total():
    if current_money_input.get()==0:
        messagebox.showerror("Error", "PLease your current money")
    else:
        cm=current_money_input.get()

        quantity=(cm//apple_cost)
        maximum_apple.set(str(round(quantity)))

        total=(quantity*apple_cost)
        total_price.set("₱" + str(round(total, 2)))

        change=(cm%apple_cost)
        remaining_money_total.set("₱" + str(change))

def Receipt():
    textarea.delete(1.0, END)
    textarea.insert (END, "\t Maihannn's Apple Store\n")
    textarea.insert (END, "\nItem\t          Quantity\t                Price\n")
    textarea.insert (END, f"\n Apple \t\t {maximum_apple.get()}\t        ₱{apple_cost}\n")
    textarea.insert (END, "\n===================================\n")
    textarea.insert (END, f"\t\t Cash: ₱{current_money_input.get()}\n")
    textarea.insert (END, f"\t\t Total: {total_price.get()}\n")
    textarea.insert (END, f"\t\t Change:{remaining_money_total.get()}")
    
   
def Reset():
    textarea.delete(1.0, END)
    current_money_input.set(0)
    maximum_apple.set(0)
    total_price.set(0)
    remaining_money_total.set(0)
       
def Exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

#Title
title=Label(root, text = "Maihannn's Apple Store", bg="#E2F4E0", fg="#1A9423", font=("STIX", 35, "bold"), relief=GROOVE, bd=10)
title.pack(fill=X)

#Product_details
product_details_label=LabelFrame(root, text = "Product Details", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
product_details_label.place(x=25, y=90, width=580, height=200)

#headings
item=Label(product_details_label, text="Items", font=("Garuda", 25, "bold", "underline"), fg="#262224", bg="#EED3E1")
item.grid(row=0, column=0, padx=20, pady=15)

price=Label(product_details_label, text="Price", font=("Garuda", 25, "bold", "underline"), fg="#262224", bg="#EED3E1")
price.grid(row=0, column=1, padx=20, pady=15)

#Product
apple=Label(product_details_label, text="Apple", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
apple.grid(row=1, column=0, padx=20, pady=15)
apple_price=Label(product_details_label, text="₱20", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
apple_price.grid (row=1, column=1, padx=20, pady=15)

#Payment 
payment_label=LabelFrame(root, text = "Payment", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
payment_label.place(x=25, y=290, width=580, height=100)

current_money=Label(payment_label, text="Enter your Money", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
current_money.grid(row=1, column=0, padx=20, pady=15)
current_money=Entry (payment_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=current_money_input)
current_money.grid (row=1, column=1, padx=20, pady=15)

#Total 
total_label=LabelFrame(root, text = "Total", font=("STIX", 20, "bold"), fg="#F63392", bg="#EED3E1", relief=GROOVE, bd=7)
total_label.place(x=25, y=390, width=580, height=350)

max_apple=Label(total_label, text=" Apple (Quantity):", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
max_apple.grid(row=1, column=0, padx=20, pady=15)
max_apple=Entry (total_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=maximum_apple)
max_apple.grid (row=1, column=1, padx=20, pady=15)
total_cost=Label(total_label, text="Total:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
total_cost.grid(row=2, column=0, padx=20, pady=15)
total_cost=Entry (total_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=total_price)
total_cost.grid (row=2, column=1, padx=20, pady=15)
remaining_money=Label(total_label, text="Change:", font=("Courier 10 Pitch", 18, "bold"), fg="#262224", bg="#EED3E1")
remaining_money.grid(row=3, column=0, padx=20, pady=15)
remaining_money=Entry (total_label, font=("Courier 10 Pitch", 18), bg="#F7F1F4", relief=SUNKEN, bd=7, justify=CENTER, textvariable=remaining_money_total)
remaining_money.grid (row=3, column=1, padx=20, pady=15)

#Receipt
receipt=Frame(root, relief=GROOVE, bd=7)
receipt.place(x=610, y=90,width=500, height = 560)
receipt_title=Label(receipt, text="Receipt", font=("Courier 10 Pitch", 20, "bold"), fg="#F63392", relief=GROOVE, bd=7).pack(fill=X)
scroll=Scrollbar(receipt, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)
textarea=Text(receipt, font=("Courier 10 Pitch", 17, "bold"), yscrollcommand=scroll.set)
textarea.pack(fill=BOTH)
scroll.config(command=textarea.yview)

#Buttons
button=Frame(root, relief=GROOVE, bd=10)
button.place(x=25, y=650, width=1085, height=120)

total_button=Button (button, text="Total", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Total)
total_button.grid(row=0, column=0, padx=20, pady=10)

receipt_button=Button (button, text="Receipt", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Receipt)
receipt_button.grid(row=0, column=1, padx=20, pady=10)

reset_button=Button (button, text="Reset", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Reset)
reset_button.grid(row=0, column=3, padx=20, pady=10)

exit_button=Button (button, text="Exit", font=("Ubuntu", 20, "bold"), bg="#E2F4E0",  fg="#1A9423", padx=5, pady=5, width=10, command=Exit)
exit_button.grid(row=0, column=4, padx=20, pady=10)

root.mainloop()
