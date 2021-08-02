import tkinter


window = tkinter.Tk()
window.minsize(500, 400)
window.maxsize(500, 400)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label_empty = tkinter.Label()
label_empty.grid(column=0, row=0, padx=10, pady=10)

label = tkinter.Label(text="is equal to", font=("Arial", 20, "normal"))
label.grid(column=0, row=1, padx=0, pady=10)

km_label = tkinter.Label(text=0, font=("Arial", 20, "normal"))
km_label.grid(column=1, row=1, padx=30, pady=10)

miles_label = tkinter.Entry(text=0, font=("Arial", 20, "normal"), width=10)
miles_label.grid(column=1, row=0, padx=30, pady=10)

button = tkinter.Button(text="Calculate", font=("Arial", 20, "normal"), width=10)
button.grid(column=1, row=2, padx=30, pady=10)

text_miles_label = tkinter.Label(text="Miles", font=("Arial", 20, "normal"))
text_miles_label.grid(column=2, row=0, padx=30, pady=10)

text_km_label = tkinter.Label(text="Km", font=("Arial", 20, "normal"))
text_km_label.grid(column=2, row=1, padx=30, pady=10)

window.mainloop()