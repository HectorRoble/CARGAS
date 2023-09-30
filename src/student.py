from tkinter import Tk, Canvas,Frame,Label, Entry, Button, W,E, Listbox,END
import psycopg2

root = Tk()
root.title("Python y PostgreSqL")

def save_new_chofer(nombre, apellido, legajo, fecha_ingreso,observaciones):
    # necesitamos para la conexxion con posgres la: nombre de bd, usuasrio y contraseña, host y puerto.
    conn=psycopg2.connect(dbname="cargas_blt",
                          user="postgres",
                          password="balut1994...",
                          host="localhost",
                          port="5432")
    cursor=conn.cursor()
    query=''' INSERT INTO chofer(nombre, apellido, legajo, fecha_ingreso,observaciones) VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(query, (nombre, apellido, legajo, fecha_ingreso,observaciones))
    print("Data Saved")
    conn.commit()
    conn.close()
    # REFRESH NEW STUDENT
    display_chofer()

def display_chofer():
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM chofer'''
    cursor.execute(query)
    row1=cursor.fetchall()
    listbox=Listbox(frame, width=30, height=10)
    listbox.grid(row1=10,columnspan=4,sticky=W+E)

    for x in row1:
        listbox.insert(END,x)
    conn.commit()
    conn.close()

# # Canvas es un contenedor 
canvas = Canvas(root, height=850, width=1550
                )
# para que se muestre dentro de nuestra ventana usamos packk
canvas.pack()
# colocar especies de espaciados, colocar o posicionar los elementosa partir de una grilla
frame= Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label= Label(frame, text="  añadir chofer")
label.grid(row=0, column=1)
# PEDIR NOMBRE
label= Label(frame, text="nombre")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
# PEDIR APELLIDO
label= Label(frame, text="apellido")
label.grid(row=2, column=0)

entry_apellido = Entry(frame)
entry_apellido.grid(row=2, column=1)

# PEDIR NOMBRE
label= Label(frame, text="Legajo")
label.grid(row=3, column=0)

entry_legajo = Entry(frame)
entry_legajo.grid(row=3, column=1)


label= Label(frame, text="Fecha ingreso")
label.grid(row=4, column=0)

entry_ingreso = Entry(frame)
entry_ingreso.grid(row=4, column=1)

label= Label(frame, text="Observaciones")
label.grid(row=5, column=0)

entry_obervaciones = Entry(frame)
entry_obervaciones.grid(row=5, column=1)

button= Button(frame,text="Add", command=lambda:save_new_chofer(
    entry_name.get(),
    entry_apellido.get(),
    entry_legajo.get(),
    entry_ingreso.get(),
    entry_obervaciones.get()
    ))

button.grid(row=6, column=1, sticky=W+E)

# copia aqui lo otro
# SEARCH
label= Label(frame,text="Search Data")
label.grid(row=8,column=0)

label= Label(frame,text="Search by id")
label.grid(row=7,column=0)

id_search = Entry(frame)
id_search.grid(row=7, column=1)

def search(id):
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM chofer WHERE id= %s'''
    cursor.execute(query,(id))
    row=cursor.fetchone()
    display_data_serach(row)
    conn.commit()
    conn.close()

button= Button(frame,text="Search1", command=lambda:search(id_search.get()))
button.grid(row=7, column=2)

def display_data_serach(row):
    listbox=Listbox(frame, width=20,height=5)
    listbox.grid(row=9,columnspan=4, sticky=E+W)
    listbox.insert(END,row)

# ----------------------------------------------------------------------------------------------------
def save_new_interno(dominio, num_interno, marca,obervaciones_i):
    # necesitamos para la conexxion con posgres la: nombre de bd, usuasrio y contraseña, host y puerto.
    conn=psycopg2.connect(dbname="cargas_blt",
                          user="postgres",
                          password="balut1994...",
                          host="localhost",
                          port="5432")
    cursor=conn.cursor()
    query=''' INSERT INTO interno (dominio, num_interno, marca,obervaciones_i) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, (dominio, num_interno, marca,obervaciones_i))
    print("Data Saved")
    conn.commit()
    conn.close()
    # REFRESH NEW STUDENT
    display_interno()

def display_interno():
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM interno'''
    cursor.execute(query)
    row=cursor.fetchall()
    listbox=Listbox(frame, width=30, height=10)
    listbox.grid(row=10,columnspan=4,sticky=W+E)

    for x in row:
        listbox.insert(END,x)
    conn.commit()
    conn.close()


label= Label(frame, text="Añadir interno")
label.grid(row=0, column=5)
# PEDIR NOMBRE
label= Label(frame, text="dominio")
label.grid(row=1, column=4)

entry_dominio = Entry(frame)
entry_dominio.grid(row=1, column=5)
# PEDIR APELLIDO
label= Label(frame, text="Nro. Interno")
label.grid(row=2, column=4)

entry_interno= Entry(frame)
entry_interno.grid(row=2, column=5)

# PEDIR NOMBRE
label= Label(frame, text="Marca")
label.grid(row=3, column=4)

entry_marca = Entry(frame)
entry_marca.grid(row=3, column=5)
0

label= Label(frame, text="Observaciones")
label.grid(row=4, column=4)

entry_observaciones_i = Entry(frame)
entry_observaciones_i.grid(row=4, column=5)

button= Button(frame,text="Add Interno", command=lambda:save_new_interno(
    entry_dominio.get(),
    entry_interno.get(),
    entry_marca.get(),
    entry_observaciones_i.get()
    ))

button.grid(row=5, column=5, sticky=W+E)


# SEARCH
label= Label(frame,text="Data Interno")
label.grid(row=8,column=4)


label= Label(frame,text="Search by id")
label.grid(row=7,column=4)

id_search = Entry(frame)
id_search.grid(row=7, column=5)
def search(id):
    conn=psycopg2.connect(dbname="cargas_blt",user="postgres",password="balut1994...", host="localhost",port="5432")
    cursor=conn.cursor()
    query=''' SELECT * FROM interno WHERE id= %s'''
    cursor.execute(query,(id))
    row=cursor.fetchone()
    display_data_serach(row)
    conn.commit()
    conn.close()

button= Button(frame,text="Search2", command=lambda:search(id_search.get()))
button.grid(row=7, column=6)

def display_data_serach(row):
    listbox=Listbox(frame, width=20,height=5)
    listbox.grid(row=9,columnspan=4, sticky=E+W)
    listbox.insert(END,row)

listbox_choferes = Listbox(frame, width=30, height=10)
listbox_choferes.grid(row=10, column=0, sticky=W+E)

listbox_internos = Listbox(frame, width=30, height=10)
listbox_internos.grid(row=10, column=1, sticky=W+E)

# Función para mostrar choferes
def display_chofer():
    conn = psycopg2.connect(dbname="cargas_blt", user="postgres", password="balut1994...", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM chofer'''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox_choferes.delete(0, END)  # Borra los datos anteriores
    for x in row:
        listbox_choferes.insert(END, x)
    conn.close()

# Función para mostrar internos
def display_interno():
    conn = psycopg2.connect(dbname="cargas_blt", user="postgres", password="balut1994...", host="localhost", port="5432")
    cursor = conn.cursor()
    query = '''SELECT * FROM interno'''
    cursor.execute(query)
    row = cursor.fetchall()
    listbox_internos.delete(0, END)  # Borra los datos anteriores
    for x in row:
        listbox_internos.insert(END, x)
    conn.close()

# Botones para cambiar entre choferes e internos
button_choferes = Button(frame, text="Mostrar Choferes", command=display_chofer)
button_choferes.grid(row=11, column=0)

button_internos = Button(frame, text="Mostrar Internos", command=display_interno)
button_internos.grid(row=11, column=3)

display_chofer()
display_interno()
root.mainloop()

