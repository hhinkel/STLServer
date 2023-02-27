import time

import tkinter as tk
import tkinter.ttk as ttk

# Make a time class with this data and time elapsed data
TIME_ALLOWED_STRING = "01:15:00"
TIME_ALLOWED_SECONDS = 0


def convert_to_seconds(timeString):
    timeList = list(int(item) for item in timeString.split(":"))
    return timeList[0] * 3600 + (timeList[1] * 60) + timeList[2]


def convert_to_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def timer(function, timeInSeconds):
    if function and function != "Stop" and function != "Reset":
        timeLeft = timeInSeconds
        while timeLeft > 0 and (function != "Stop" or function != "Reset"):
            print(convert_to_time(timeLeft))
            time.sleep(1)
            timeLeft -= 1


def start_timer():
    timeSeconds = convert_to_seconds(TIME_ALLOWED_STRING)
    timer("Start", timeSeconds)
    print("Start button pressed")


def stop_timer():
    print("Stop button pressed")


def reset_timer():
    print("Reset button pressed")


window = tk.Tk()
window.title("Storytelling Timer Light")
window.resizable(width=False, height=False)
window.geometry("800x600")

topLabel = ttk.Label(window, text="Time Allowed: 1:15:00", )

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
