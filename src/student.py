from tkinter import Tk, Canvas,Frame,Label, Entry, Button, W,E, Listbox,END
import psycopg2

root = Tk()
root.title("Python y PostgreSqL")

def save_new_student(name, age, adress):
    # necesitamos para la conexxion con posgres la: nombre de bd, usuasrio y contraseña, host y puerto.
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' INSERT INTO student(name, age, adress) VALUES (%s, %s, %s)'''
    cursor.execute(query, (name, age, adress))
    print("Data Saved")
    conn.commit()
    conn.close()
    # REFRESH NEW STUDENT
    display_student()

def display_student():
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM student'''
    cursor.execute(query)
    row=cursor.fetchall()
    listbox=Listbox(frame, width=30, height=10)
    listbox.grid(row=10,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END,x)
    conn.commit()
    conn.close()

# # Canvas es un contenedor 
canvas = Canvas(root, height=850, width=1550
                )
# para que se muestre dentro de nuestra ventana usamos pack
canvas.pack()
# colocar especies de espaciados, colocar o posicionar los elementosa partir de una grilla
frame= Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label= Label(frame, text="  añadir estudiante")
label.grid(row=0, column=1)
# PEDIR NOMBRE
label= Label(frame, text="nombre")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
# PEDIR EDAD
label= Label(frame, text="edad")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)
# PEDIR NOMBRE
label= Label(frame, text="Adress")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button= Button(frame,text="Add", command=lambda:save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
    ))
button.grid(row=4, column=1, sticky=W+E)

# SEARCH
label= Label(frame,text="Search Data")
label.grid(row=5,column=0)

label= Label(frame,text="Search by id")
label.grid(row=6,column=0)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

def search(id):
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM student WHERE id= %s'''
    cursor.execute(query,(id))
    row=cursor.fetchone()
    display_data_serach(row)
    conn.commit()
    conn.close()

button= Button(frame,text="Search", command=lambda:search(id_search.get()))
button.grid(row=6, column=2)

def display_data_serach(row):
    listbox=Listbox(frame, width=20,height=5)
    listbox.grid(row=9,columnspan=4, sticky=E+W)
    listbox.insert(END,row)


display_student()
root.mainloop()

