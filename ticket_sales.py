from tkinter import *


root = Tk()

# code to add widgets and style window will go here
root.geometry("500x650")
root.title("Ticket Sales (Uthmaan Breda)")
root.config(bg="black")

ticket = PhotoImage(file="ticket.png")
img = Label(root, image=ticket, bg="black", fg="white")
img.place(x=120, y=5)


# create class
class Cell:
    price1 = StringVar()
    amt_tick_ent = StringVar()
    reserve_ent = StringVar()

    def __init__(self, master):
        # define labels
        self.lab1 = Label(master, text="Enter Cell Number: ", bg="black", fg="white")
        self.lab1.place(x=5, y=200)
        self.entry1 = Entry(master, bg="black", fg="white")
        self.entry1.place(x=150, y=200)
        self.entry1.focus()
        self.lab2 = Label(master, text="Ticket Category: ", bg="black", fg="white")
        self.lab2.place(x=5, y=250)

        # define option menu
        self.option = ["Soccer", "Movie", "Theatre"]  # set values for option list
        self.values = StringVar(root)  # set variable to keep track of option value selected
        self.values.set("Select an option")  # set default value on display (value from list can be put sayin option[0])
        self.opt = OptionMenu(master, self.values, *self.option)
        self.opt.config(width=15, bg="black", fg="white")
        self.opt.place(x=150, y=250)

        # spinbox
        self.lab3 = Label(master, text="Number of Tickets: ", bg="black", fg="white")
        self.lab3.place(x=5, y=300)
        self.spin_box = Spinbox(
            master,
            from_=0,
            to=10000,
            increment=1,
            bg="black",
            fg="white"
            )
        self.spin_box.place(x=150, y=300)

        # using Labels to display results
        self.lab4 = Label(master, text="Amount Payable: ", bg="black", fg="white").place(x=5, y=450)
        self.amount1 = Label(master, text="", width="20", textvariable=self.price1, bg="black", fg="white")
        self.amount1.place(x=150, y=450)
        self.lab5 = Label(master, text="Reservation for: ", bg="black", fg="white").place(x=5, y=475)
        self.amount2 = Label(master, text="", width="20", textvariable=self.amt_tick_ent, bg="black", fg="white")
        self.amount2.place(x=150, y=475)
        self.lab5 = Label(master, text="Was done by: ", bg="black", fg="white").place(x=5, y=500)
        self.amount3 = Label(master, text="", width="20", textvariable=self.reserve_ent, bg="black", fg="white")
        self.amount3.place(x=150, y=500)

        # create buttons
        self.mybutton = Button(master, text="calculate price", command=self.price, bg="black", fg="white")
        self.mybutton.place(x=150, y=390)
        self.mybutton2 = Button(master, text="Clear", command=self.clear, bg="black", fg="white")
        self.mybutton2.place(x=150, y=550)

    # define functions for equations, clear and exit
    def reserve(self):
        res = self.entry1.get()
        self.reserve_ent.set(res)

    def price(self):

        self.amt_tick_ent.set(self.spin_box.get())
        self.reserve()

        if self.values.get() == "Soccer":
            pay_me = float(self.spin_box.get()) * 40 + 0.14 * (float(self.spin_box.get()) * 40)
            self.price1.set("R" + str(pay_me))

        elif self.values.get() == "Movie":
            pay_me = float(self.spin_box.get()) * 75 + 0.14 * (float(self.spin_box.get()) * 75)
            self.price1.set("R" + str(pay_me))

        elif self.values.get() == "Theatre":
            pay_me = float(self.spin_box.get()) * 100 + 0.14 * (float(self.spin_box.get()) * 100)
            self.price1.set("R" + str(pay_me))

    def clear(self):
        self.entry1.delete(0, END)
        self.spin_box.delete(0, END)
        self.values.set("Select an option")
        self.price1.set("")
        self.amt_tick_ent.set("")
        self.reserve_ent.set("")
        self.entry1.focus()


y = Cell(root)  # call class to root frame

root.mainloop()  # continuously runs program in window
