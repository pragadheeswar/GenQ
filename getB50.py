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

def selectquestion(u,n,l):
	if (n==0):
		return []
	connection=sqlite3.connect("questions.db")
	cursor = connection.cursor()
	unit = str(u)
	level = str(l)
	cursor.execute("Select Q_id,Importance from Twelve_marks where Unit = ? and Level= ?",(unit,level))
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
		cursor.execute("Select Question from Twelve_marks where Q_id = ?",(a,))
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

			cursor.execute("Select Question from Twelve_marks where Q_id = ?",(a,))
			row = cursor.fetchone()
			# print(row[0])
			l.append(row[0])
		cursor.close()
		connection.close()
		return l


def getB50_1(l):
	question=[]
	question += selectquestion(l[0],2,1)
	question += selectquestion(l[0],2,0)
	return question

def getB50_2(l):
	r = [0,1]
	c = random.randint(0,1)
	if(c==0):
		r = [1,0]

	question =[]
	question += selectquestion(l[0],1,r[0])
	question += selectquestion(l[1],1,r[1])
	c = random.randint(0,1)
	if(c==0):
		r = [0,1]
	question += selectquestion(l[1],1,r[0])
	question += selectquestion(l[0],1,r[1])
	return question

def getB50_3(l):
	level = [1,1,0,0]
	random.shuffle(level)
	question = []
	question += selectquestion(l[0],1,level[0])
	question += selectquestion(l[1],1,level[1])
	question += selectquestion(l[2],1,level[2])
	c = random.randint(0,2)
	question += selectquestion(l[c],1,level[3])
	return question

def getB50_4(l):
	level = [1,1,0,0]
	random.shuffle(level)
	question = []
	question += selectquestion(l[0],1,level[0])
	question += selectquestion(l[1],1,level[1])
	question += selectquestion(l[2],1,level[2])
	question += selectquestion(l[3],1,level[3])
	return question

def getB50_5(l):
	level = [1,1,0,0]
	random.shuffle(level)
	c = random.randint(0,4)
	l.pop(c)
	question = []
	question += selectquestion(l[0],1,level[0])
	question += selectquestion(l[1],1,level[1])
	question += selectquestion(l[2],1,level[2])
	question += selectquestion(l[3],1,level[3])
	return question


def getB50(l):
	if(len(l)==1):
		return getB50_1(l)
	if(len(l)==2):
		return getB50_2(l)
	if(len(l)==3):
		return getB50_3(l)
	if(len(l)==4):
		return getB50_4(l)
	if(len(l)==5):
		return getB50_5(l)


print(getB50([3,1,2,5,4]))

# print(getB50_5([4,5,2,1,3]))