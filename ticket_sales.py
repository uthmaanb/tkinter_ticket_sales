from tkinter import *


root = Tk()

# code to add widgets and style window will go here
root.geometry("500x650")
root.title("Ticket Sales (Uthmaan Breda)")


class Cell:
    price1 = StringVar()
    amt_tick_ent = StringVar()
    reserve_ent = StringVar()

    def __init__(self, master):
        self.lab1 = Label(master, text="Enter Cell Number: ")
        self.lab1.place(x=5, y=200)
        self.entry1 = Entry(master)
        self.entry1.place(x=150, y=200)
        self.lab2 = Label(master, text="Ticket Category: ")
        self.lab2.place(x=5, y=250)

        self.option = ["Soccer", "Movie", "Theatre"]  # set values for option list
        self.values = StringVar(root)  # set variable to keep track of option value selected
        self.values.set("Select an option")  # set default value on display (value from list can be put sayin option[0])
        self.opt = OptionMenu(master, self.values, *self.option)
        self.opt.config(width=15)
        self.opt.place(x=150, y=250)

        self.lab3 = Label(master, text="Number of Tickets: ")
        self.lab3.place(x=5, y=300)
        self.spin_box = Spinbox(
            root,
            from_=0,
            to=10000,
            increment=1
            )
        self.spin_box.place(x=150, y=300)

        self.lab4 = Label(master, text="Amount Payable: ").place(x=5, y=450)
        self.amount = Label(master, text="", width="20", textvariable=self.price1).place(x=150, y=450)
        self.lab5 = Label(master, text="Reservation for: ").place(x=5, y=475)
        self.amount = Label(master, text="", width="20", textvariable=self.amt_tick_ent).place(x=150, y=475)
        self.lab5 = Label(master, text="Was done by: ").place(x=5, y=500)
        self.amount = Label(master, text="", width="20", textvariable=self.reserve_ent).place(x=150, y=500)

        self.mybutton = Button(root, text="choice", command=self.price)
        self.mybutton.place(x=150, y=400)

    def amt_tick(self):
        amt = self.spin_box.get()
        self.amt_tick_ent.set(amt)

    def reserve(self):
        res = self.entry1.get()
        self.reserve_ent.set(res)

    def price(self):

        self.amt_tick()
        self.reserve()

        if self.values.get() == "Soccer":
            pay_me = float(self.spin_box.get()) * 40 + 0.14 * (float(self.spin_box.get()) * 40)
            self.price1.set(pay_me)

        elif self.values.get() == "Movie":
            pay_me = float(self.spin_box.get()) * 75 + 0.14 * (float(self.spin_box.get()) * 75)
            self.price1.set(pay_me)

        elif self.values.get() == "Theatre":
            pay_me = float(self.spin_box.get()) * 100 + 0.14 * (float(self.spin_box.get()) * 100)
            self.price1.set(pay_me)


y = Cell(root)

root.mainloop()  # continuously runs program in window
