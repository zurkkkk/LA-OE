import tkinter as tk

your_name = "Lloyd_DelaCruz"
your_section = "BSIT-2ABC"
anime_title = "demonslayer"

root = tk.Tk()
root.title(f"OOP LA28 {your_name}")
root.geometry("400x300")
root.configure(bg="gray")

counter = 0
def display_text():
    global counter
    print(f"{counter} my favorite anime is {anime_title}")
    counter += 1

button = tk.Button(root, text ="Run", command=display_text)
button.grid(row=10, column=10, padx=20, pady=20)



root.mainloop()
