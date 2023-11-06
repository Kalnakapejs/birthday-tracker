import tkinter as tk

w = tk.Tk()
w.title("C -> F")
w.geometry("300x200")

def convert():
    celsius = float(c_input.get())
    result.configure(text=(celsius*(9/5)+32))
tk.Label(w,text="C temp.").\
    grid(row = 0, column = 0, padx = 5, pady = 5)
c_input =tk.Entry(w, width = 20)
c_input.grid(row = 0, column = 1, padx = 5, pady = 5)

tk.Button(w,text = "Pārveidot!", command = lambda: convert).\
    grid(row=0,column = 2, padx = 5, pady = 5)

w.mainloop()