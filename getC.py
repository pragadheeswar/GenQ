import random
from random import uniform
import sqlite3



def select(w):
	total = sum(w)
	n = [i/total for i in w]
	normal = [n[0]]
	for i in range(1,len(n)):
		a = normal[i-1]+n[i]
		normal.append(a)
	c = uniform(0,1)
	for index , value in enumerate(normal):
		if c <= value:
			return index

def select2(w):
	temp = w.copy()
	i = select(w)
	temp.pop(i)
	j = select(temp)
	if(j>=i):
		j+=1
	return [i,j]

def getC():


	connection=sqlite3.connect("questions.db")

	cursor = connection.cursor()
	cursor.execute("Select Q_id,Importance from Twelve_marks where Level= 2")
	q=[]
	w=[]
	for row in cursor:
		q.append(row[0])
		w.append(row[1])
		# print(q)
		# print(w)

	x= select2(w)
	l=[]
	for i in x:
		a = str(q[i])
			# print(a)

		cursor.execute("Select Question from Twelve_marks where Q_id = ?",(a,))
		row = cursor.fetchone()
		# print(row[0])
		l.append(row[0])
	cursor.close()
	connection.close()
	return l 
 

# print(getC())