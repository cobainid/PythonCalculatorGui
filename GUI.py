from Tkinter import * #import all modules from Tkinter

import tkMessageBox # used to show message box

operation = "" # created variable to safe math

# create class GUI
class GUI():
	# Created function click
	# adding num/op to var operationn
	def click(self,n):
		global operation # make var operation work in func click

		operation = operation + str(n)

		self.textEntry.set(operation)
		if operation=="*" or operation=="/":
			tkMessageBox.showerror("Error","operator tidak dapat diletakkan didepan")
			self.textEntry.set("")
			operation = ""
			pass

	def actionEquals(self):
		global operation # make var operation work in func actionEquals
		try:
			if "+" not in operation and "-" not in operation and "/" not in operation and "*" not in operation :
				tkMessageBox.showerror("Error","Operator tidak ada")
			else:
				operation = str(eval(operation))
				self.textEntry.set(str(operation))
		except Exception as e:
			tkMessageBox.showerror("Error","Ada masalah saat melakukan operasi")

	def Clear(self):
		global operation
		operation=""
		self.textEntry.set(operation)

	def actionD(self):
		global operation
		lengthOP = len(operation)
		operation = operation[0:lengthOP-1]
		self.textEntry.set(operation)

	def actionChange(self):
		global operation
		lengthOP = len(operation)
		if lengthOP != 0:
			if operation[0] == "-" :
				operation = operation[1:lengthOP]
			else:
				operation = "-"+operation
			self.textEntry.set(operation)
		else:
			tkMessageBox.showerror("Error","Operasi error gan")


	def actionDot(self):
		global operation
		lengthOP = len(operation)
		if operation[lengthOP-1] == ".":
			tkMessageBox.showerror("Error","Tidak dapat menambahkan koma")
		else:
			operation = operation+"."
			if operation == ".":
				tkMessageBox.showerror("Error","Tidak dapat menambahkan koma")
				operation=""
			else:
				self.textEntry.set(operation)














	def main(self):
		global Entry

		gui = Tk()

		gui.configure(background="dark blue")

		gui.title("Simple Calc") # set application title

		gui.geometry("360x480") # set width and height application

		self.textEntry = StringVar()

		self.textEntry.set("Selamat menggunakan") #set text variable self.textEntry
		
		Entry = Entry(gui,
			textvariable=self.textEntry,
			state='disable',
			bd=0,
			disabledbackground='dark blue',
			disabledforeground='white',
			highlightthickness=1
		)

		Entry.grid(row=0,
			columnspan=4,
			ipady=25,
			padx=4,
			pady=4,
			ipadx=94,
		)






		# Row 1
		# btn clear - btn delete - btn change plus minus - btn plus


		actClear = Button(gui,
			text="C",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.Clear()
		)

		actClear.grid(row=1,
			column=0
		)

		actD = Button(gui,
			text="D",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.actionD()
		)

		actD.grid(row=1,
			column=1
		)

		actChange = Button(gui,
			text="+/-",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.actionChange()
		)

		actChange.grid(row=1,
			column=2
		)

		actAv = Button(gui,
			text="/",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click("/")
		)

		actAv.grid(row=4,
			column=3
		)












		btn7 = Button(gui,
			text="7",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(7)
		)

		btn7.grid(row=2,
			column=0
		)

		btn8 = Button(gui,
			text="8",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(8)
		)

		btn8.grid(row=2,
			column=1
		)

		btn9 = Button(gui,
			text="9",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(9)
		)

		btn9.grid(row=2,
			column=2
		)

		actPlus = Button(gui,
			text="+",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click("+")
		)

		actPlus.grid(row=1,
			column=3
		)














		# baris ke 3
		btn4 = Button(gui,
			text="4",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(4)
		)

		btn4.grid(row=3,
			column=0
		)

		btn5 = Button(gui,
			text="5",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(5)
		)

		btn5.grid(row=3,
			column=1
		)

		btn6 = Button(gui,
			text="6",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(6)
		)

		btn6.grid(row=3,
			column=2
		)

		actMin = Button(gui,
			text="-",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click("-")
		)

		actMin.grid(row=2,
			column=3
		)





















		# Button 1
		btn1 = Button(gui,
			text="1",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(1)
		)

		btn1.grid(row=4,
			column=0
		)

		btn2 = Button(gui,
			text="2",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(2)
		)

		btn2.grid(row=4,
			column=1
		)

		btn3 = Button(gui,
			text="3",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(3)
		)

		btn3.grid(row=4,
			column=2
		)

		actMulti = Button(gui,
			text="*",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click("*")
		)

		actMulti.grid(row=3,
			column=3
		)















		actDots = Button(gui,
			text=".",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.actionDot()
		)

		actDots.grid(row=5,
			column=0
		)

		btn0 = Button(gui,
			text="0",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=8,
			command=lambda:self.click(0)
		)

		btn0.grid(row=5,
			column=1
		)

		actEquals = Button(gui,
			text="=",
			bd=0,
			highlightthickness=1,
			bg="brown",
			fg="white",
			height=4,
			width=19,
			command=lambda:self.actionEquals()
		)

		actEquals.grid(row=5,
			column=2,
			columnspan=2,
		)
		tkMessageBox.showinfo("Creator","Defri Indra Mahardika\nSmkn 1 Jenangan\nXI RPL A")
		gui.mainloop()
