import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Simple Calculator")
    window.geometry("300x400")
    window.mainloop()

if __name__ == "__main__":
    create_window()