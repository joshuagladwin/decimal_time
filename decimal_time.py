from datetime import datetime
from tkinter import *

debug = False


def decimal_time(debug=False):
    if debug:
        current_datetime = datetime.strptime("2023-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    else:
        current_datetime = datetime.now()

    year_len = datetime(year=current_datetime.year, month=12, day=31).timetuple().tm_yday

    dt = ((current_datetime.hour * 3600) + (current_datetime.minute * 60) + current_datetime.second +
          (current_datetime.microsecond / 1e6)) / 86400

    dt_str = f"{dt:.5f}"

    dt_hours = dt_str[2]
    dt_minutes = dt_str[3:5].zfill(2)
    dt_seconds = dt_str[5:7].zfill(2)

    dd_year = current_datetime.strftime("%y")
    dd_day = current_datetime.timetuple().tm_yday - 1
    dd_month = f"{(dd_day + dt) / year_len}"[2:5].zfill(3)

    ddt_string = f"{dd_year}{dd_month}.{dt_hours}{dt_minutes}{dt_seconds}"

    lbl.config(text=ddt_string)

    if not debug:
        lbl.after(100, decimal_time)


root = Tk()
root.title("Decimal Clock")
root.attributes('-topmost', True)
root.overrideredirect(True)
root.resizable(False, False)
w = 205
h = 40
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = ws - w - 300
y = hs - (2 * h)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

lbl = Label(root,
            font=('helvetica', 26, 'bold'),
            background='purple',
            foreground='white')

lbl.pack(anchor='center')

decimal_time(debug)

root.mainloop()
