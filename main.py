import tkinter as tk

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


root.mainloop()