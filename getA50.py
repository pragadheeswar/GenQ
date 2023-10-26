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


def selectp(pair):
		w= [i[1] for i in pair]
		total = sum(w)
		n = [i/total for i in w]
		normal = [n[0]]
		for i in range(1,len(n)):
			a = normal[i-1]+n[i]
			normal.append(a)
		c = uniform(0,1)
		for index , value in enumerate(normal):
			if c <= value:
				return pair[index]


def selectn(pair,n):
	temp=pair.copy()
	l=[]
	for i in range(n):
		a = selectp(temp)
		l.append(a[0])
		temp.remove(a)
	return l

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
		return [row[0]]
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



def getA50_1(l):
	question = []
	connection=sqlite3.connect("questions.db")
	cursor = connection.cursor()
	unit = str(l[0])
	# print(unit)
	cursor.execute("Select Q_id,Importance from Two_marks where Unit = ? and Level= ?",(unit,1))
	q=[]
	w=[]
	pair=[]
	# pair=[[1,1],[2,5],[3,4],[4,1],[5,3]]
	for row in cursor:
		pair.append([row[0],row[1]])
	a1 = selectn(pair,4)
	for a in a1:
		a = str(a)
		# print(a)

		cursor.execute("Select Question from Two_marks where Q_id = ?",(a,))
		row = cursor.fetchone()
		print(row[0])
		question.append(row[0])
	cursor.execute("Select Q_id,Importance from Two_marks where Unit = ? and Level= ?",(unit,0))
	q=[]
	w=[]
	pair=[]
	# pair=[[1,1],[2,5],[3,4],[4,1],[5,3]]
	for row in cursor:
		pair.append([row[0],row[1]])
	a1 = selectn(pair,3)
	for a in a1:
		a = str(a)
		# print(a)

		cursor.execute("Select Question from Two_marks where Q_id = ?",(a,))
		row = cursor.fetchone()
		print(row[0])
		question.append(row[0])
	cursor.close()
	connection.close()
	return question

def getA50_2(l):
	question=[]
	question += selectquestion(l[0],2,0)
	question += selectquestion(l[0],2,1)
	question += selectquestion(l[1],2,1)
	question += selectquestion(l[1],1,0)
	return question

def getA50_2(l):
	question=[]
	question += selectquestion(l[0],2,0)
	question += selectquestion(l[0],2,1)
	question += selectquestion(l[1],2,1)
	question += selectquestion(l[1],1,0)
	return question

def  getA50_3(l):
	question=[]
	question += selectquestion(l[0],1,0)
	question += selectquestion(l[0],1,1)
	question += selectquestion(l[1],1,0)
	question += selectquestion(l[1],1,1)
	question += selectquestion(l[2],1,0)
	question += selectquestion(l[2],1,1)
	question += selectquestion(l[2],1,0)
	return question

def  getA50_4(l):
	question=[]
	question += selectquestion(l[0],1,0)
	question += selectquestion(l[0],1,1)
	question += selectquestion(l[1],1,0)
	question += selectquestion(l[1],1,1)
	question += selectquestion(l[2],1,0)
	question += selectquestion(l[3],1,1)
	question += selectquestion(l[3],1,0)
	return question

def  getA50_5(l):
	question=[]
	question += selectquestion(l[0],1,0)
	question += selectquestion(l[1],1,1)
	question += selectquestion(l[2],1,0)
	question += selectquestion(l[3],1,1)
	question += selectquestion(l[4],1,0)
	question += selectquestion(l[0],1,1)
	question += selectquestion(l[4],1,0)
	return question

def getA50(l):
	if(len(l)==1):
		return getA50_1(l)
	if(len(l)==2):
		return getA50_2(l)
	if(len(l)==3):
		return getA50_3(l)
	if(len(l)==4):
		return getA50_4(l)
	if(len(l)==5):
		return getA50_5(l)


# getA50( list of units ) return 7 questions as list

# print(getA50([1]))
# print(getA50([1,4]))

