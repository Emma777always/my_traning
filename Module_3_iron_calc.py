import tkinter as tk



def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    num3 = int(number3_entry.get())
    return num1, num2, num3


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def math():
    num1, num2, num3 = get_values()
    res = int(num1 * (num2 - num3) * 0.24 + 500) # по формуле Гудзони
    insert_values(res)



window = tk.Tk()
window.title('Калькулятор дефицита железа')
window.geometry("350x350")
window.resizable(False, False)
window.config(bg='lightgray')
button_add = tk.Button(window, text="Рассчитать дефицит железа", width=23, height=2, command=math)
button_add.place(x=100, y=210)

number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=55)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=110)
number3_entry = tk.Entry(window, width=28)
number3_entry.place(x=100, y=180)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)

number1 = tk.Label(window, text="Mасса тела, кг")
number1.place(x=100, y=30)
number2 = tk.Label(window, text="Целевой Hb, г/л")
number2.place(x=100, y=85)
number3 = tk.Label(window, text="Hb пациентa, г/л") # Hb - гемоглобин
number3.place(x=100, y=155)
answer = tk.Label(window, text="Общий дефицит железа, мг")
answer.place(x=100, y=275)


window.mainloop()

