import sqlite3

def addQ(subject,question,unit,level,mark,importance):
	connection=sqlite3.connect("questions.db")

	cursor = connection.cursor()
	unit = str(unit)
	level=str(level)
	importance = str(importance)

	if(mark=="2"):
		cursor.execute("insert into Two_marks (Question,Unit,Level,Importance) values(?,?,?,?)",(question,unit,level,importance))
	if(mark=="12"):
		cursor.execute("insert into Twelve_marks (Question,Unit,Level,Importance) values(?,?,?,?)",(question,unit,level,importance))

	# for row in cursor.execute("select * from Two_marks"):
	# 	print(row)
	cursor.close()
	connection.commit()
	connection.close()


# addQ("network","hellow 12 23  ",12,1,12,5)