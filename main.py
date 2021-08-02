import tkinter


FONT = ("Arial", 20, "normal")


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_output.config(text=km)


window = tkinter.Tk()
window.minsize(500, 400)
window.maxsize(500, 400)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


label = tkinter.Label(text="is equal to", font=FONT)
label.grid(column=0, row=1, padx=0, pady=10)

km_output = tkinter.Label(text=0, font=FONT)
km_output.grid(column=1, row=1, padx=30, pady=10)

miles_input = tkinter.Entry(text=0, font=FONT, width=10)
miles_input.grid(column=1, row=0, padx=30, pady=10)

button = tkinter.Button(text="Calculate", font=FONT, width=10, command=calculate)
button.grid(column=1, row=2, padx=30, pady=10)

text_miles_label = tkinter.Label(text="Miles", font=FONT)
text_miles_label.grid(column=2, row=0, padx=30, pady=10)

text_km_label = tkinter.Label(text="Km", font=FONT)
text_km_label.grid(column=2, row=1, padx=30, pady=10)

window.mainloop()
