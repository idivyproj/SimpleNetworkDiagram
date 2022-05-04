#import tkinter to be able to draw elements
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image

root = Tk()
root.geometry ("350x600")
root.title("Simple Network Diagram")


def show_selected_ISP():
    showinfo(
        title='Result',
        message=selected_ISP.get()
    )

selected_ISP = StringVar()
ISPs = (('ATT', 'ATT'),
         ('Verizon', Image.open(r"C:\Users\inder\Documents\Code\Project\verizon.png")),
         ('XIBER', 'X'),
         ('Other', 'Other'))

# label
label = ttk.Label(text="Who is your ISP?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for ISP in ISPs:
    r = ttk.Radiobutton(
        root,
        text=ISP[0],
        value=ISP[1],
        variable=selected_ISP
    )
    r.pack(fill='x', padx=5, pady=5)

button = ttk.Button(
    root,
    text="Show ISP Device",
    command=show_selected_ISP)

button.pack(fill='x', padx=5, pady=5)
















def show_selected_Firewall():
    showinfo(
        title='Result',
        message=selected_FW.get()
    )

selected_FW = StringVar()
Firewalls = (('Sonicwall', 'S'),
         ('Meraki', 'M'),
         ('No', 'N'))

# label
label = ttk.Label(text="Do you have a firewall?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for FW in Firewalls:
    r = ttk.Radiobutton(
        root,
        text=FW[0],
        value=FW[1],
        variable=selected_FW
    )
    r.pack(fill='x', padx=5, pady=5)


root.mainloop()