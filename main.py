import tkinter as tk
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import Scrollbar

root = tk.Tk()

#root.geometry("1000*500")
#Not working because of an issue over multiply sign

#Alternative way for the dimensions of GUI
root.minsize(width=1000, height=450)
root.maxsize(width=2000, height=10000)

#Heading
root.title("Personal Budget Tracker")
root.configure(background="#2F2F2F")

item_list = []

def add_item():
    item = item_label_text.get()
    quantity = quantity_label_text.get()
    cost = cost_label_text.get()
    total = int(quantity) * int(cost)
    # print(item, quantity, cost, total)
    single_item_label = tk.Label(frame2, text = f"{item}\t\t{quantity}\t\t{cost}\t\t{total}", bg ="#2F2F2F", fg = "white", font = "Arial 15")
    single_item= {"Item": item, "Quantity":quantity, "Cost":cost, "Total Amount":total}
    item_list.append(single_item)
    single_item_label.pack(pady=5)

def clear_item():
    item_label_text.delete(0, "end")
    quantity_label_text.delete(0, "end")
    cost_label_text.delete(0, "end") 

def analyze():
    df = pd.DataFrame(item_list)
    items = df['Item']
    total = df['Total Amount']
    fig = plt.figure(figsize=(10, 5))
    plt.bar(items, total, color = 'green', width = 0.4) 
    plt.ylabel("Cost of items")
    plt.xlabel("Items purchased")
    plt.title("Personal Budget Tracker Analysis")
    plt.show()


#Heading #2
title_label = tk.Label(root, text = "Personal Budget Tracker", bg = "#2F2F2F", fg = "white", font = "Arial 20 ")
title_label.pack(pady=30)

#Item heading
item_label = tk.Label(root, text = "Item", bg = "#2F2F2F", fg = "white", font = "Arial 15")
item_label.pack(pady=30)
item_label_text = tk.Entry(root, font = "Arial 15")
item_label_text.pack()

#Quantity heading
quantity_label = tk.Label(root, text ="Quantity", bg = "#2F2F2F", fg = "white", font = "Arial 15")
quantity_label.pack(padx=(30, 5))
quantity_label_text = tk.Entry(root, font = "Arial 15")
quantity_label_text.pack()

#Cost Heading
cost_label = tk.Label(root, text = "Cost Per Unit", bg ="#2F2F2F", fg = "white", font = "Arial 15" )
cost_label.pack(pady=(10, 5))
cost_label_text = tk.Entry(root, font = "Arial 15" )
cost_label_text.pack()

#Frame
frame1 = tk.Frame(root, bg = "#2F2F2F")

#Add Item Button
Add_button = tk.Button(frame1, text = "Add Item", bg ="#2F2F2F", fg = "white", font = ("Arial 15"),command=add_item)
Add_button.pack(pady=20, side=tk.LEFT, anchor=tk.CENTER)

#Clear Button 
Clear_Button = tk.Button(frame1, text = "Clear", bg ="#2F2F2F", fg = "white", font = ("Arial 15"),command=clear_item)
Clear_Button.pack(pady=20, side=tk.LEFT, anchor=tk.CENTER)

frame1.pack()

#Expanse Button
Expanses_label = tk.Label(root, text = "Expenses", bg ="#2F2F2F", fg = "white", font = "Arial 15" )
Expanses_label.pack()

#Frame
frame2 = tk.Frame(root, bg = "#2F2F2F")

#Headings Button
headings_label = tk.Label(frame2, text ="Item\t\tQuantity\t\tUnit Cost\t\tTotal", bg ="#2F2F2F", fg = "white", font = "Arial 15" )
headings_label.pack(pady=5)

frame2.pack()

#Analyze Button
Analyze_label = tk.Button(root, text = "Analyze", bg ="#2F2F2F", fg = "white", font = ("Arial 15"),command=analyze)
Analyze_label.pack(pady=30)

root.mainloop()