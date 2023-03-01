import tkinter as tk
import tkinter.ttk as ttk


class Interface:
    def __init__(self):
        self.top_label: tk.Label
        self.button_frame: ttk.Frame
        self.start_button: tk.Button
        self.stop_button: tk.Button
        self.reset_button: tk.Button
        self.clock: tk.Label

class TimeObject:
    def __init__(self):
        self.interface = Interface()
        self.time_allowed_string = "01:15:30"
        self.time_in_seconds = self.convertToSeconds(self.time_allowed_string)
        self.clock = None
        self.running = False
        self.time_left = self.time_allowed_string

    def convertToSeconds(self, time_string):
        time_list = list(int(item) for item in time_string.split(":"))
        return time_list[0] * 3600 + (time_list[1] * 60) + time_list[2]

    def convertToTime(self):
        seconds = self.time_in_seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)

    def startTimer(self):
        self.time_in_seconds = self.convertToSeconds(self.time_allowed_string)
        self.running = True
        timer(self)
        print("Start button pressed")

    def stopTimer(self):
        self.running = False
        print("Stop button pressed")

    def reset_timer(self):
        print("Reset button pressed")
        if self.running is True:
            self.running = False


def interfaceButtons(window, time_object):
    time_object.interface.button_frame = ttk.Frame(master=window, relief=tk.RAISED)
    time_object.interface.start_button = tk.Button(time_object.interface.button_frame, text="Start", background="green",
                                                   width=10, command=time_object.startTimer)
    time_object.interface.stop_button = tk.Button(time_object.interface.button_frame, text="Stop", background="red",
                                                  width=10, command=time_object.stopTimer)
    time_object.interface.reset_button = tk.Button(time_object.interface.button_frame, text="Reset", background="orange",
                                                   width=10, command=time_object.reset_timer)

    time_object.interface.start_button.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    time_object.interface.stop_button.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    time_object.interface.reset_button.grid(row=2, column=0, sticky="e", padx=5, pady=5)

    time_object.interface.button_frame.place(relx=0.12, rely=0.5, anchor="e")


def interfaceClockDisplay(window, time_object):
    time_object.interface.clock = tk.Label(window, text=time_object.time_allowed_string, font=("Courier", 20),
                                           width = 10, foreground="green")
    time_object.interface.clock.place(relx=0.5, rely=0.5, anchor="center")


def interface(window, time_object):
    time_object.interface.top_label = ttk.Label(window, text="Time Allowed: " + time_object.time_allowed_string)
    interfaceButtons(window, time_object)
    interfaceClockDisplay(window, time_object)
    time_object.interface.top_label.place(relx=0.5, rely=0.0, anchor="n")


def timer(time_object):
    if time_object.running:
        if time_object.time_in_seconds <= 0:
            time_object.interface.clock.configure(text="00:00:00", foreground="red")
        else:
            time_object.interface.clock.configure(text=time_object.convertToTime(), foreground="green")
            time_object.time_in_seconds -= 1
            after(1000, timer(time_object))


def main():
    time_object = TimeObject()
    window = tk.Tk()
    window.title("Timing Light")
    window.resizable(width=False, height=False)
    window.geometry("800x600")
    interface(window, time_object)
    window.mainloop()


if __name__ == "__main__":
    main()
