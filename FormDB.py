from tkinter import *
import sqlite3

root = Tk()
root.title("Database app")
root.geometry("400x400")


# submit function
def submit():
	# create db
	conn = sqlite3.connect('students.db')
	# create cursor
	c = conn.cursor()

	# create table
	c.execute("""CREATE TABLE if not exists student(
	name text,
	grade integer,
	section integer,
	code integer
	)""")

	# insert into Table
	c.execute("INSERT INTO student VALUES (:name, :grade, :section, :code)",
		{
		'name': name.get(),
		'grade': grade.get(),
		'section': section.get(),
		'code': code.get(),
		})

	# commit change
	conn.commit()
	# close connection
	conn.close()

	# clear text box
	name.delete(0, END)
	grade.delete(0, END)
	section.delete(0, END)
	code.delete(0, END)

# create query fun
def query():
	# create db
	conn = sqlite3.connect('students.db')
	# create cursor
	c = conn.cursor()

	# query the database
	c.execute("SELECT *,oid FROM student")
	records = c.fetchall()
	#print(records)

	# Loop thry Results
	print_records = ''
	for record in records:
		print_records += 'Name : ' + str(record[0]) + ', Grade : ' + str(record[1]) + ', Section : ' + str(record[2]) + ', Code : ' + str(record[3]) + '\n'
	query_label = Label(root, text=print_records)
	query_label.grid(row=6, column=0, columnspan=2)


	# commit change
	conn.commit()
	# close connection
	conn.close()


# create text boxes
name = Entry(root, width=30)
name.grid(row=0, column=1, padx=20)
grade = Entry(root, width=30)
grade.grid(row=1, column=1, padx=20)
section = Entry(root, width=30)
section.grid(row=2, column=1, padx=20)
code = Entry(root, width=30)
code.grid(row=3, column=1, padx=20)

# create label
name_label = Label(root, text='Name')
name_label.grid(row=0, column=0)

grade_label = Label(root, text='Grade')
grade_label.grid(row=1, column=0)

section_label = Label(root, text='Section')
section_label.grid(row=2, column=0)

code_label = Label(root, text='Code')
code_label.grid(row=3, column=0)


# create submit button
submit_btn = Button(root, text='Add to Database', command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, padx=10, ipadx=100)

# create a query button
query_btn = Button(root,text='Show Records', command=query)
query_btn.grid(row=5, column=0,columnspan=2,pady=10, padx=10, ipadx=100)

root.mainloop()