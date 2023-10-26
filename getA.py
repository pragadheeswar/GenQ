import random
from random import uniform
import sqlite3

def ran(l):
		s=0
		for i in range(5):
			if l[i]!=0:
				s=s+1
		n = random.randint(1,s)
		a=0
		for i in range(5):
			if(l[i]!=0):
				a+=1
			if(n==a):
				return i

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

def selectquestion(u,n,l):
	if (n==0):
		return []
	connection=sqlite3.connect("questions.db")
	cursor = connection.cursor()
	unit = str(u)
	level = str(l)
	cursor.execute("Select Q_id,Importance from Two_marks where Unit = ? and Level= ?",(unit,level))
	q=[]
	w=[]
	for row in cursor:
		q.append(row[0])
		w.append(row[1])
		# print(q)
		# print(w)
	if(n==1):
		x = select(w)
		a = str(q[x])
			# print(a)
		cursor.execute("Select Question from Two_marks where Q_id = ?",(a,))
		row = cursor.fetchone()
		cursor.close()
		connection.close()
			# print(row[0])
		return row[0]
	else:
		x= select2(w)
		l=[]
		for i in x:
			a = str(q[i])
			# print(a)

			cursor.execute("Select Question from Two_marks where Q_id = ?",(a,))
			row = cursor.fetchone()
			# print(row[0])
			l.append(row[0])
		cursor.close()
		connection.close()
		return l

def getA():


	q=[1,1,1,1,1]
	c = random.randint(0,1)
	if(c==0):
		q = [2,2,2,2,2]

	understand={1:0,2:0,3:0,4:0,5:0}

	for i in range(5):
		x = ran(q)
		q[x]-=1
		understand[x+1]+=1



		

	# print(understand)
	quetions = {1:[],2:[],3:[],4:[],5:[]}
	for key in understand:
		x = selectquestion(key,understand[key],0)
		if(understand[key]==2):
			quetions[key]=x 
		elif(understand[key]==1):
			quetions[key].append(x)

	# print(quetions)
	# selectquestion(3,1)

	for key in understand:
		a = 2-understand[key]
		x = selectquestion(key,a,1)
		if(a==2):
			quetions[key]=x 
		elif(a==1):
			quetions[key].append(x)
	return quetions

# print(getA())
		