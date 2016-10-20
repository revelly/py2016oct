import tkinter as tk

counter = 0
stopCounter=False

def counter_label(label):
  def count():
    global counter, stopCounter
    

    if not stopCounter:
        label.config(text=str(counter))
        counter += 1
    label.after(1000, count)
        
  count()
 
def stopcounter():
    global stopCounter
    stopCounter=True

def startcounter():
    global stopCounter
    stopCounter=False
    
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()

button = tk.Button(root, text='Stop', width=25, command=stopcounter)
button.pack()

button2 = tk.Button(root, text='Start', width=25, command=startcounter)
button2.pack()

counter_label(label)

root.mainloop()
