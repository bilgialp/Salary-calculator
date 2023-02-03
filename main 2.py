import tkinter as tk

def calculation():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    result = a/12 + b*22.37 + c*(a/2080)
    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")

label_a = tk.Label(root, text="a")
label_a.grid(row=0, column=0)

entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="b")
label_b.grid(row=1, column=0)

entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

label_c = tk.Label(root, text="c")
label_c.grid(row=2, column=0)

entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculation)
button_calculate.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2)

root.mainloop()