# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:57:13 2022

@author: Dane Mettam (デイン　メッタム) 
"""

from tkinter import * 
from PIL import ImageTk,Image 
import sqlite3 

fPath='C:/Users/danea/Documents/Python Scripts/Tkinter Tutorial/images/' 

root = Tk()
root.title("Databases")
root.iconbitmap(fPath + 'tumblr_pbrevojubz_X7Y_icon.ico')
root.geometry("400x500")  


# Create a DB or connect to one 
conn = sqlite3.connect('address_book.db')

# Curser is what you send off to do commands. 
# Create cursor 
c = conn.cursor() 


''' 
# Create Table - data types == text, integers, real, null, blob
c.execute("""CREATE TABLE addresses ( 
    first_name text,
    last_name text,
    address text, 
    city text, 
    state text,
    zipcode integer
    )""") 
'''

# Create submit function for database
def submit():
    conn = sqlite3.connect('address_book.db') # Connect to DB 
    c = conn.cursor() # Create cursor
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(), 
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get() 
                  }) 
    conn.commit() # Commit changes 
    conn.close() # Close connection 
    # Clear the textboxes
    f_name.delete(0, END) 
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create function to delete record 
def delete():
    conn = sqlite3.connect('address_book.db') # Connect to DB 
    c = conn.cursor() # Create cursor 
    # Delete a record 
    c.execute("DELETE from addresses WHERE oid= " + edit_box.get()) 
    conn.commit() # Commit changes 
    conn.close() # Close connection 

# Create a query function
def query():
    conn = sqlite3.connect('address_book.db') # Connect to DB 
    c = conn.cursor() # Create cursor 
    # Query the database 
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() #c.fetchmany()  #c.fetchone() 
    #print(records) 
    #Loop through results
    print_records = ''
    conn.commit() # Commit changes 
    conn.close() # Close connection 
    for record in records: #[0]
        print_records += str(record[6]) + "\t" + str(record[0]) + " " + str(record[1]) + "\n" 
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2) 

# Create a save function
def update():
    conn = sqlite3.connect('address_book.db') # Connect to DB 
    c = conn.cursor() # Create cursor 
    record_id = edit_box.get()   
    c.execute("""UPDATE addresses SET
              first_name = :first, 
              last_name = :last,
              address = :address, 
              city = :city,
              state = :state,
              zipcode = :zipcode           
              WHERE oid = :oid""",
              {
              'first': f_name_editor.get(),
              'last': l_name_editor.get(),
              'address': address_editor.get(),
              'city': city_editor.get(),
              'state': state_editor.get(),
              'zipcode': zipcode_editor.get(),
              'oid': record_id 
              })

    conn.commit() # Commit changes 
    conn.close() # Close connection 
    editor.destroy() 
    


# Create edit function to update a record    
def edit():
    global editor 
    editor = Tk()
    editor.title("Record Updator")
    editor.iconbitmap(fPath + 'tumblr_pbrevojubz_X7Y_icon.ico')
    editor.geometry("280x300") 
    
    conn = sqlite3.connect('address_book.db') # Connect to DB 
    c = conn.cursor() # Create cursor 
    record_id = edit_box.get()     
    # Query the database 
    c.execute("SELECT * FROM addresses WHERE oid =" + record_id)
    records = c.fetchall() 
    
    # Create global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    # Create text boxes 
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20 ,pady=(10,0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    
    # Create text box labels 
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column =0, pady=(10,0)) 
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column =0) 
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column =0) 
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column =0) 
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column =0) 
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column =0) 
    
    # Creat an save button an edited record
    save_btn = Button(editor, text="Save Record", command=update) 
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=90)
    
    # Loop through results
    for record in records: 
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    

 

# Create text boxes 
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20 ,pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

edit_box = Entry(root, width=30) 
edit_box.grid(row=10, column=1, pady=5) 

# Create text box labels 
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column =0, pady=(10,0)) 
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column =0) 
address_label = Label(root, text="Address")
address_label.grid(row=2, column =0) 
city_label = Label(root, text="City")
city_label.grid(row=3, column =0) 
state_label = Label(root, text="State")
state_label.grid(row=4, column =0) 
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column =0) 

select_box_label = Label(root, text="Selected ID")
select_box_label.grid(row=10, column=0, pady=5) 

# Create submit button(s) 
submit_btn = Button(root, text="Add record to database.", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100) 

# Create a query button 
query_btn = Button(root, text="Show Records", command=query) 
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a delete button 
delete_btn = Button(root, text="Delete Records", command=delete) 
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Creat an update button 
edit_btn = Button(root, text="Edit Records", command=edit) 
edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=131)

# Commit Changes 
conn.commit() 

# Close Connection 
conn.close() 


root.mainloop() 