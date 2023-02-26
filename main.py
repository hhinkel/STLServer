import tkinter as tk
import tkinter.ttk as ttk


def start_timer():
    pass


def stop_timer():
    pass


def reset_timer():
    pass


window = tk.Tk()
window.title("Storytelling Timer Light")
window.resizable(width=False, height=False)
window.geometry("800x600")

topLabel = ttk.Label(window, text="Time Left: 1:15:00", )

buttonFrame = ttk.Frame(master=window, relief=tk.RAISED)
startButton = tk.Button(buttonFrame, text="Start", background="green", width=10, command=start_timer)
stopButton = tk.Button(buttonFrame, text="Stop", background="red", width=10, command=stop_timer)
resetButton = tk.Button(buttonFrame, text="Reset", background="orange", width=10, command=reset_timer)

startButton.grid(row=0, column=0, sticky="e", padx=5, pady=5)
stopButton.grid(row=1, column=0, sticky="e", padx=5, pady=5)
resetButton.grid(row=2, column=0, sticky="e", padx=5, pady=5)

topLabel.place(relx=0.5, rely=0.0, anchor="n")
buttonFrame.place(relx=0.12, rely=0.5, anchor="e")

window.mainloop()
