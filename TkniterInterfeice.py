from tkinter import *

window = Tk()
window.title(" Добро пожаловать в калькулятор конверсий сотрудников!")


lbl = Label(window, text="Добрый день, пользователь", font=("Arial Bold", 25)) #font шрифт и размер текста
lbl.grid(column=0, row=0)
window.geometry('1000x500')

# Добавим событие нажатия кнопки
def clicked():
    lbl.configure(text='Я же просил тебя не нажимать гребаную кнопку')

#Добавляем кнопку
#Затем мы подключим ее с помощью кнопки, указав следующую функцию:
btn = Button(window, text='Dont push', bg='red', fg='black', command=clicked)#bg фон кнопки, fg цвет текста
btn.grid(column=1, row=0)

btn1 = Button(window, text='Целевая конверсия', bg='green', fg='black') # Кнопка целевой конверсии
btn1.grid(column=0, row=1)
btn2 = Button(window, text='Отработанные выставленные', bg='blue', fg='black')
btn2.grid(column=0, row=2)
btn3 = Button(window, text='Дожим', bg='gold', fg='black')
btn3.grid(column=0, row=3)

window.mainloop() # функция отоборажения для пользователя
