import tkinter as tk
def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    else:
        entry.insert(tk.END, value)
        
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.pack(pady=20, padx=20, fill='x')

buttons_frame = tk.Frame(root)
buttons_frame.pack(expand=True, fill='both', padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", '.', '=', "+"
]
for index, text in enumerate(buttons):
    row = index // 4
    col = index % 4
    button = tk.Button(buttons_frame, text=text, font=("Arial", 14), command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)
for i in range(4):
    buttons_frame.rowconfigure(i, weight=1)


root.mainloop()
