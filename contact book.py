from tkinter import*
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    if name and phone:
        contact_list.insert(END, f"{name} - {phone}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        name, phone = selected_contact.split(" - ")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
    except IndexError:
        pass

root = Tk()
root.title("Contact Book")

# Create UI elements
name_label = Label(root, text="Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

phone_label = Label(root, text="Phone:")
phone_label.pack()
phone_entry = Entry(root)
phone_entry.pack()

add_button = Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

clear_button = Button(root, text="Clear Contacts", command=clear_contacts)
clear_button.pack()

contact_list = Listbox(root)
contact_list.pack()

contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()
