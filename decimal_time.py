from datetime import datetime, date
from tkinter import *


def decimal_time():
    current_datetime = datetime.now()
    year_len = (date(current_datetime.year, 12, 31) - date(current_datetime.year - 1, 12, 31)).days

    dt = ((current_datetime.hour * 3600) + (current_datetime.minute * 60) + current_datetime.second +
          (current_datetime.microsecond / 1e6)) / 86400

    dt_hours = str(dt)[2]
    dt_minutes = str(dt)[3:5]
    dt_seconds = str(dt)[5:7]

    dd_year = current_datetime.strftime("%y")
    dd_day = (current_datetime.date() - date(current_datetime.year - 1, 12, 31)).days
    dd_month = str((dd_day + dt) / year_len)[2:5]

    ddt_string = f"{dd_year}{dd_month}.{dt_hours}{dt_minutes.zfill(2)}{dt_seconds.zfill(2)}"

    lbl.config(text=ddt_string)
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

decimal_time()

root.mainloop()
