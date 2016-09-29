import Tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
		self.createWidgets()
	def createWidgets(self):
		top=self.winfo_toplevel()
		top.rowconfigure(0, weight=1)
		top.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		self.quitButton = tk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
		self.Label1 = tk.Label(self, bg='white', text='Time UTC = ')
		self.Label1.grid()
		self.Text1 = tk.Text(self, bg='white', state=tk.NORMAL)
		self.Text1.grid()
		Text2 = tk.Canvas(self)
		id = Text2.create_text(10,20,text='112:3443')
		self.Text2.grid()
		
app = Application()
app.master.title('Astro GUI by Lauro Fortuna')
app.mainloop()