from tkinter import *
from playsound import playsound
import time

def Timer1():
	times = int(mins.get()) * 60 + int(sec.get()) 
	while times > -1:
		minute, second = (times//60, times%60)

		hour = 0
		if minute > 60:
			hour, minute = (minute//60, minute%60)
		sec.set(second)
		mins.set(minute)

		root.update()
		time.sleep(1)

		if (times == 0):
			playsound("boom.wav")
			sec.set('00')
			mins.set('00')

		times -= 1

root = Tk()
root.title("Timers")
root.geometry("1080x700")
root.config(bg='#000')


#timer1
mins = StringVar()
Entry(root, textvariable=mins, width=2, font='arial 50', bg='#000', fg='#fff', bd=0).place(relx=0.4,rely=0)
mins.set('00')

sec = StringVar()
Entry(root, textvariable=sec, width=2, font='arial 50', bg='#000', fg='#fff', bd=0).place(relx=0.5,rely=0)
sec.set('00')

Label(root, text='min', font='arial 12', bg='#000', fg='#fff').place(relx=0.47, rely=0.06)
Label(root, text='sec', font='arial 12', bg='#000', fg='#fff').place(relx=0.57, rely=0.06)

button = Button(root, text='Start', font='arial 10 bold', bg='#ea3548', fg='#fff', bd=0, width=20, height=2, command=Timer1)
button.place(relx=0.64, rely=0.018)

root.mainloop()
