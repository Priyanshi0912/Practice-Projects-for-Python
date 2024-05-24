import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('500x600')
window.title('UNIT CONVERTER')
window.configure(bg='pink')

# Creating the fonts
font1 = font.Font(family='helvetica', size='30')
font2 = font.Font(family='helvetica', size='10')
font3 = font.Font(family='helvetica', size='20')

number_from = StringVar()
number_to = StringVar()

# All the functions
# Selected function
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('Cubic meter', 'Cubic foot', 'Litres', 'Gallon', 'Cubic Centimeters')
        todd['values'] = ('Cubic meter', 'Cubic foot', 'Litres', 'Gallon', 'Cubic Centimeters')
    elif unit == 'Length':
        fromdd['values'] = ('Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Kilometers')
        todd['values'] = ('Millimeters', 'Centimeters', 'Decimeters', 'Meters', 'Kilometers')
    elif unit == 'Mass':
        fromdd['values'] = ('Milligrams', 'Centigrams', 'Grams', 'Kilograms')
        todd['values'] = ('Milligrams', 'Centigrams', 'Grams', 'Kilograms')

# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()

# Answer function
def answer(n1):
    num1 = n1.get()

    try:
        number1 = float(num1)
    except ValueError:
        messagebox.showerror('ERROR', 'TERMS NOT RECOGNIZED')
        return

    # Conversion logic for volume (example)
    if result_from == 'Cubic meter' and result_to == 'Cubic meter':
        calculate = number1
    elif result_from == 'Cubic meter' and result_to == 'Cubic foot':
        calculate = number1 * 35.3147
    elif result_from == 'Cubic meter' and result_to == 'Litres':
        calculate = number1 * 1000
    elif result_from == 'Cubic meter' and result_to == 'Gallon':
        calculate = number1 * 264.172
    elif result_from == 'Cubic meter' and result_to == 'Cubic Centimeters':
        calculate = number1 * 1000000
    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
    elif result_from == 'Cubic foot' and result_to == 'Litres':
        calculate = number1 * 28.3168
    elif result_from == 'Cubic foot' and result_to == 'Gallon':
        calculate = number1 * 7.48052
    elif result_from == 'Cubic foot' and result_to == 'Cubic Centimeters':
        calculate = number1 * 28316.8
    elif result_from == 'Litres' and result_to == 'Cubic Centimeters':
        calculate = number1 * 1000
    else:
        messagebox.showerror('ERROR', 'CONVERSION NOT RECOGNIZED')
        return

    result.configure(text=f"{calculate:.2f} {result_to}")

# Creating unit converter
main = tk.Label(window, text='UNIT CONVERTER', bg='pink', fg='Black')
main['font'] = font1
main.place(relx='0.48', rely='0.1', anchor='center')

# Creating the unit label
unit = tk.Label(window, text='Unit:', bg='pink')
unit['font'] = font2
unit.place(relx='0.25', rely='0.28')

# Creating the main combobox
n = StringVar()
unitdd = ttk.Combobox(window, width='35', textvariable=n)
unitdd['values'] = ('Volume', 'Length', 'Mass')
unitdd.place(relx='0.57', rely='0.3', anchor='center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>', selected)

# Creating the from label
label_from = tk.Label(window, text='From:', bg='pink')
label_from['font'] = font2
label_from.place(relx='0.238', rely='0.37')

# Creating the fromdd
f = StringVar()
fromdd = ttk.Combobox(window, width='35', textvariable=f)
fromdd.place(relx='0.57', rely='0.39', anchor='center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>', fromfunc)

# Creating the num_from entry
num_from = tk.Entry(window, width=10, textvariable=number_from)
num_from.place(relx='0.82', rely='0.37')

answer_partial = partial(answer, num_from)

# Creating the to label
to = tk.Label(window, text='To:', bg='pink')
to['font'] = font2
to.place(relx='0.268', rely='0.45')

# Creating the dropdown
t = StringVar()
todd = ttk.Combobox(window, width=35, textvariable=t)
todd.place(relx='0.57', rely='0.47', anchor='center')
todd.current()
todd.bind('<<ComboboxSelected>>', tofunc)

# Creating the result label
result = tk.Label(window, text=' ', bg='white', width=20)
result['font'] = font3
result.place(relx='0.57', rely='0.6', anchor='center')

# Creating the get answer button
get_answer = tk.Button(window, text='Get Answer', bg='cyan', command=answer_partial)
get_answer['font'] = font3
get_answer.place(relx='0.57', rely='0.7', anchor='center')

# Mainloop
window.mainloop()
