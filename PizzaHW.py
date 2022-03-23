import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")

        self.main_window.configure(bg='yellow')

        self.top_frame = tkinter.Frame(self.main_window)
        self.tm_frame = tkinter.Frame(self.main_window)
        self.bm_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter your name:")
        self.prompt_label.configure(bg='red')

        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.name_entry.pack(side="left")
        self.top_frame.pack(side="top")
        self.tm_frame.pack(side="top")
        self.bm_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.orderbutton = tkinter.Button(
            self.main_window, text="Place Order", command=self.calculate
        )

        self.quit_button = tkinter.Button(
            self.main_window, text="Quit!", command=self.main_window.destroy
        )

        self.orderbutton.pack(side="left")
        self.quit_button.pack(side="right")

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(0)

        self.rb1 = tkinter.Radiobutton(
            self.tm_frame, text="Thin Crust", variable=self.radio_var, value=8
        )
        self.rb1.configure(bg='green')


        self.rb2 = tkinter.Radiobutton(
            self.tm_frame, text="Original Crust", variable=self.radio_var, value=10
        )
        self.rb2.configure(bg='green')

        self.rb3 = tkinter.Radiobutton(
            self.tm_frame, text="Stuffed Crust", variable=self.radio_var, value=15
        )
        self.rb3.configure(bg='green')

        self.rb2.select()

        self.rb1.pack(side="left")
        self.rb2.pack(side="left")
        self.rb3.pack(side="left")

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.bm_frame, text="Pepperoni", variable=self.cb_var1
        )
        self.cb1.configure(bg='magenta')

        self.cb2 = tkinter.Checkbutton(
            self.bm_frame, text="Sausage", variable=self.cb_var2
        )
        self.cb2.configure(bg='magenta')

        self.cb3 = tkinter.Checkbutton(
            self.bm_frame, text="Banana Peppers", variable=self.cb_var3
        )
        self.cb3.configure(bg='magenta')

        self.cb4 = tkinter.Checkbutton(
            self.bm_frame, text="Olives", variable=self.cb_var4
        )
        self.cb4.configure(bg='magenta')

        self.cb5 = tkinter.Checkbutton(
            self.bm_frame, text="Pineapple", variable=self.cb_var5
        )
        self.cb5.configure(bg='magenta')

        self.cb1.pack(side="left")
        self.cb2.pack(side="left")
        self.cb3.pack(side="left")
        self.cb4.pack(side="left")
        self.cb5.pack(side="left")

        tkinter.mainloop()

    def calculate(self):
        total = float(self.radio_var.get())

        if self.cb_var1.get() == 1:
            total += 1
        if self.cb_var2.get() == 1:
            total += 1.5
        if self.cb_var3.get() == 1:
            total += 3
        if self.cb_var4.get() == 1:
            total += 3.5
        if self.cb_var5.get() == 1:
            total += 4

        money = "${:,.2f}".format(total)
        customer = self.name_entry.get()

        tkinter.messagebox.showinfo(
            "Checkout",str(customer) + "'s pizza will cost " + str(money)
        )


my_gui = MyGUI()
