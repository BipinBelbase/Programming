import tkinter as tk
#.................................................

#making object for window
root = tk.Tk()
root.title("This Is Sample")
root.geometry('400x300')
root.resizable(0,0)
root.config(bg="red")

#making new object for input 
text_result=tk.Entry(root,width=9,bg ="red",fg="white",font=('verdana',40,'bold'),highlightthickness=0,borderwidth=0)
#only object making doesn't work so we have to tell what tipe of input ,  in this case we are using grid 
text_result.grid(row=0,column=0,pady=(20,20))

### First Row Button
btn_ac = tk.Button(root,text='AC',bg="yellow",fg='grey',width=3, height=3)
btn_ac.grid(row=1,column=0,paddy=(1,1))

### Second Row Button
btn_negative= tk.Button(root,text='NEG',bg="yellow",fg='grey',height=3,width=3)
btn_negative.grid(row=1,column=1,paddy=(1,1))

### Third Row Button
btn_possitive= tk.Button(root,text='NEG',bg="yellow",fg='grey',height=3,width=3)
btn_possitive.grid(row=1,column=1,paddy=(0,1))

### Forth Row Button
btn_equalto= tk.Button(root,text='NEG',bg="yellow",fg='grey',height=3,width=3)
btn_equalto.grid(row=1,column=1)




# last line of this GUI After this last like whatever you write doesnot affect the GUI interface
root.mainloop()