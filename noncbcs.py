#!/usr/bin/python
import urllib
import urllib.request
from bs4 import BeautifulSoup
from tkinter import *





area_code = str(input("Enter area code: "))
college_code = str(input("Enter college code: "))
semester = str(input("Enter semester: "))
branch = str(input("Enter branch: "))
limit = int(input("Enter extraction limit: "))
divisor = 0

if semester == "6":
	year = 14
	divisor = 900
else:
	year = 13
	divisor = 750

import csv
download_dir = area_code + college_code.upper() + str(year) + branch.upper() + "_results.csv"
csv = open(download_dir, "a")

tot_sum = 0
sgpa = 0

for usn in range(1, limit+1):

	try:
		if usn < 10:
			usn = '00' + str(usn)
		elif usn < 99:
			usn = '0' + str(usn)
		else:
			usn = str(usn)

		results_page = 'http://results.vtu.ac.in/results17/result_page.php?usn=' + str(area_code) + college_code + str(year) + branch + usn
		page = urllib.request.urlopen(results_page)

		soup = BeautifulSoup(page, 'html.parser')

		data = []

		table = soup.find('table',attrs={"class":"table table-bordered"})
		table_body = table.find_all('tbody')

		for i in table_body:
			items = i.find_all('tbody')
			rows = i.find_all('tr')
			for row in rows:
				cols = row.find_all('td')
				cols = [ele.text.strip() for ele in cols]
				data.append([ele for ele in cols if ele])

		student_name = soup.find('td', attrs={'style':'padding-left:15px'})
		student_name = student_name.text.strip()

		print("Extracting results for: " + str(area_code) + str(college_code).upper() + str(year) + branch.upper() + usn)
		usn = "University Seat Number: " + "," + str(area_code) + str(college_code).upper() + str(year) + branch.upper() + usn + "\n"
		student = "Student name: " + "," + student_name[2:] + "\n"
		csv.write(usn)
		csv.write(student)


		thead = table.find('thead')
		trow = thead.find('tr')
		h = thead.find_all('th', attrs = {'style':'text-align:center;'})
		hvar = []
		for i in h:
			i = i.text.strip()
			hvar.append(i)

		hh = hvar[0] + "," + hvar[1] + "," + hvar[2] + "," + hvar[3] + "," + hvar[4] + "," + hvar[5] + "\n"
		csv.write(hh)


		for i in data:
			var1 = i[0]
			var2 = i[1]
			var3 = i[2]
			var4 = i[3]
			var5 = i[4]
			var6 = i[5]
			
			tot_sum += int(var5)
			j = str(var1) + "," + str(var2) + "," + str(var3) + "," + str(var4) + "," + str(var5) + "," + str(var6) + "\n"
			csv.write(j)

		
		a = " " + "," + " " + "," + " " + "," + " " + "," + "Aggregate: " + "," + str(tot_sum) + "/" + str(divisor) + "\n"
		csv.write(a)
		tot_sum = 0
		
		new_line = "\n\n\n\n\n\n\n\n\n\n"
		csv.write(new_line)

	except:
		print("Not Found")
		continue

print("DONE")
csv.close()


#	area_code = str(ar.get())
#	college_code = str(col.get())
#	semester = str(sem.get())
#	branch = str(br.get())
#	limit = int(lim.get())



'''
master = Tk()
Label(master, text="Enter area code").grid(row=0)
Label(master, text="Enter college code").grid(row=1)
Label(master, text="Enter semester").grid(row=2)
Label(master, text="Enter branch").grid(row=3)
Label(master, text="Enter extraction limit").grid(row=4)

ar = Entry(master)
col = Entry(master)
sem = Entry(master)
br = Entry(master)
lim = Entry(master)

ar.grid(row = 0, column = 1)
col.grid(row = 1, column = 1)
sem.grid(row = 2, column = 1)
br.grid(row = 3, column = 1)
lim.grid(row = 4, column = 1)

Button(master, text='Extract', command=show_entry_fields).grid(row=5, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=5, column=2, sticky=W, pady=4)

mainloop( )
'''
