import tkinter as tk

root = tk.Tk()
name = "Lloyd"
section = "BSIT-2A"
root.title(f"Task Management")
root.geometry("400x300")
root.configure(bg="gray")


pangalan = tk.Entry(root)
pangalan.grid(row=0, column=1, padx=140, pady=20)

counter = 1
def display_text():
    global counter
    print(f"{counter}. {pangalan.get()}")
    counter += 1

button = tk.Button(root, text="Submit", command=display_text)
button.grid(row=1, column=1, padx=20, pady=20)

root.mainloop()
