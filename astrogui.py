import Tkinter as tk
import datetime
from astroapi import posizione


def counter_label(label,label1,label2):
  def count():
	global data
	data = datetime.datetime.utcnow()
	label.config(text="Tempo UTC "+ str(data))
	res = posizione(14.261,19.172,12.452,41.922,1)
	TSL = res["TSL"]
	Azi = res["Az"]
	Alt = res["h"]
	h=int(TSL)
	m=int((TSL - h) *60)
	s=60 * ((TSL-h)*60-m)
	label1.config(text=str("Tempo Siderale Apparente" + str(h) +"h "+ str(m) +"m " + str(s) +"s"))
	label2.config(text=str("Az/H " + str(Azi) +" "+ str(Alt) +" "))
	label.after(1000, count)
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="black")
label.pack()
label1 = tk.Label(root, fg="red")
label1.pack()
label2 = tk.Label(root, fg="blue")
label2.pack()
counter_label(label,label1,label2)

button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()