import time

import tkinter as tk
import tkinter.ttk as ttk

# Make a time class with this data and time elapsed data
TIME_ALLOWED_STRING = "01:15:00"
TIME_ALLOWED_SECONDS = 0


def convertToSeconds(timeString):
    time_list = list(int(item) for item in timeString.split(":"))
    return time_list[0] * 3600 + (time_list[1] * 60) + time_list[2]


def convertToTime(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def timer(function, time_in_seconds):
    if function and function != "Stop" and function != "Reset":
        time_left = time_in_seconds
        while time_left > 0 and (function != "Stop" or function != "Reset"):
            print(convertToTime(time_left))
            time.sleep(1)
            time_left -= 1


def startTimer():
    time_seconds = convertToSeconds(TIME_ALLOWED_STRING)
    timer("Start", time_seconds)
    print("Start button pressed")


def stopTimer():
    print("Stop button pressed")


def reset_timer():
    print("Reset button pressed")


def interfaceButtons(window):
    button_frame = ttk.Frame(master=window, relief=tk.RAISED)
    start_button = tk.Button(button_frame, text="Start", background="green", width=10, command=startTimer)
    stop_button = tk.Button(button_frame, text="Stop", background="red", width=10, command=stopTimer)
    reset_button = tk.Button(button_frame, text="Reset", background="orange", width=10, command=reset_timer)

    start_button.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    stop_button.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    reset_button.grid(row=2, column=0, sticky="e", padx=5, pady=5)

    button_frame.place(relx=0.12, rely=0.5, anchor="e")


def interfaceClockDisplay(window):
    clock = tk.Label(window, text=TIME_ALLOWED_STRING, font=("Courier", 20), width = 10)
    clock.place(relx=0.5, rely=0.5, anchor="center")


def interface(window):
    top_label = ttk.Label(window, text="Time Allowed: 1:15:00", )
    interfaceButtons(window)
    interfaceClockDisplay(window)
    top_label.place(relx=0.5, rely=0.0, anchor="n")


def main():
    window = tk.Tk()
    window.title("Timing Light")
    window.resizable(width=False, height=False)
    window.geometry("800x600")
    interface(window)
    window.mainloop()


if __name__ == "__main__":
    main()
