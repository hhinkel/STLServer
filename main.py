import tkinter as tk
import tkinter.ttk as ttk


def startTimer():
    pass


def stopTimer():
    pass


def resetTimer():
    pass


window = tk.Tk()
window.title("Storytelling Timer Light")
window.resizable(width=False, height=False)
window.geometry("800x600")

top_label = ttk.Label(window, text="Time Left: 1:15:00",)

button_frame = ttk.Frame(master=window, relief=tk.RAISED)
start_button = tk.Button(button_frame, text="Start", background="green", width=10, command=startTimer)
stop_button = tk.Button(button_frame, text="Stop", background="red", width=10, command=stopTimer)
reset_button = tk.Button(button_frame, text="Reset", background="orange", width=10, command= resetTimer)

start_button.grid(row=0, column=0, sticky="e", padx=5, pady=5)
stop_button.grid(row=1, column=0, sticky="e", padx=5, pady=5)
reset_button.grid(row=2, column=0, sticky="e", padx=5, pady=5)

top_label.place(relx=0.5, rely=0.0, anchor="n")
button_frame.place(relx=0.12, rely=0.5, anchor="e")

window.mainloop()
