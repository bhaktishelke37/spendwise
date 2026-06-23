import tkinter as tk
from tkinter import messagebox

FILE_NAME = "expenses.txt"


# ---------- FUNCTIONS ----------

def save_expense():

    amount = amount_entry.get()
    category = category_entry.get()
    description = desc_entry.get()

    if amount == "" or category == "" or description == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    data = amount + "," + category + "," + description + "\n"

    file = open(FILE_NAME, "a")
    file.write(data)
    file.close()

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

    load_expenses()
    update_total()


def load_expenses():

    history_box.delete(0, tk.END)

    try:
        file = open(FILE_NAME, "r")
        expenses = file.readlines()
        file.close()

        for expense in expenses:

            data = expense.strip().split(",")

            display = "₹" + data[0] + " | " + data[1] + " | " + data[2]

            history_box.insert(tk.END, display)

    except:
        pass


def delete_expense():

    selected = history_box.curselection()

    if not selected:
        messagebox.showwarning("Error", "Select an expense")
        return

    index = selected[0]

    file = open(FILE_NAME, "r")
    expenses = file.readlines()
    file.close()

    expenses.pop(index)

    file = open(FILE_NAME, "w")

    for expense in expenses:
        file.write(expense)

    file.close()

    load_expenses()
    update_total()


def update_total():

    total = 0

    try:
        file = open(FILE_NAME, "r")
        expenses = file.readlines()
        file.close()

        for expense in expenses:

            data = expense.strip().split(",")

            total += int(data[0])

    except:
        pass

    total_label.config(text="Total Spending: ₹" + str(total))


def show_summary():

    categories = {}

    try:
        file = open(FILE_NAME, "r")
        expenses = file.readlines()
        file.close()

        for expense in expenses:

            data = expense.strip().split(",")

            amount = int(data[0])
            category = data[1]

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        text = ""

        for cat in categories:
            text += cat + " → ₹" + str(categories[cat]) + "\n"

        messagebox.showinfo("Category Summary", text)

    except:
        messagebox.showinfo("Summary", "No expenses found")


# ---------- WINDOW ----------

window = tk.Tk()
window.title("SpendWise")
window.geometry("520x700")
window.configure(bg="#1e1e2f")


# ---------- TITLE ----------

title = tk.Label(
    window,
    text="SpendWise 💸",
    font=("Arial", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)


# ---------- INPUTS ----------

amount_label = tk.Label(
    window,
    text="Amount",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 11)
)
amount_label.pack()

amount_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 11)
)
amount_entry.pack(pady=5)


category_label = tk.Label(
    window,
    text="Category",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 11)
)
category_label.pack()

category_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 11)
)
category_entry.pack(pady=5)


desc_label = tk.Label(
    window,
    text="Description",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 11)
)
desc_label.pack()

desc_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 11)
)
desc_entry.pack(pady=5)


# ---------- BUTTONS ----------

add_button = tk.Button(
    window,
    text="Add Expense",
    command=save_expense,
    bg="#7c4dff",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2",
    font=("Arial", 11, "bold")
)
add_button.pack(pady=15)


delete_button = tk.Button(
    window,
    text="Delete Selected",
    command=delete_expense,
    bg="#ff4d6d",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2",
    font=("Arial", 11, "bold")
)
delete_button.pack(pady=5)


summary_button = tk.Button(
    window,
    text="Show Summary",
    command=show_summary,
    bg="#00b894",
    fg="white",
    width=20,
    relief="flat",
    cursor="hand2",
    font=("Arial", 11, "bold")
)
summary_button.pack(pady=5)


# ---------- HISTORY ----------

history_title = tk.Label(
    window,
    text="Expense History",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 14, "bold")
)
history_title.pack(pady=15)


history_box = tk.Listbox(
    window,
    width=55,
    height=12,
    bg="#2b2b40",
    fg="white",
    border=0,
    font=("Arial", 10)
)
history_box.pack()


# ---------- TOTAL ----------

total_label = tk.Label(
    window,
    text="Total Spending: ₹0",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 14, "bold")
)
total_label.pack(pady=20)


# ---------- LOAD DATA ----------

load_expenses()
update_total()

window.mainloop()