from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import sqlite3

app=Flask(__name__)
CORS(app)


#cgpa calculating function
def gpa(a):
	lis=[]
	for l in a:
		if(l[2]=="O" or l[2]=="10"):
			l[2]=10
			lis.append(l[2])
		elif(l[2]=="E" or l[2]=="9"):
			l[2]=9
			lis.append(l[2])
		elif(l[2]=="A" or l[2]=="8"):
			l[2]=8
			lis.append(l[2])
		elif(l[2]=="B" or l[2]=="7"):
			l[2]=7
			lis.append(l[2])
		elif(l[2]=="C" or l[2]=="6"):
			l[2]=6
			lis.append(l[2])
		elif(l[2]=="D" or l[2]=="5"):
			l[2]=5
			lis.append(l[2])
		elif(l[2]=="S" or l[2]=="0"):
			l[2]=0
			lis.append(l[2])
		elif(l[2]=="M" or l[2]=="0"):
			l[2]=0
			lis.append(l[2])
		elif(l[2]=="F" or l[2]=="0"):
			l[2]=0
			lis.append(l[2])
		else:
			lis.append(float(l[2]))

	sum=0
	for i in lis:
		sum=sum+i
	cgpa=sum/len(lis)
	return cgpa



#list to dict
def converter(a):
	final=[]
	m=0
	for i in a:
		record={}
		c=0
		for k in i:
			if(c==0):
				record["subcode"]=k
			elif(c==1):
				record["subjectname"]=k
			else:
				record["grade"]=k
			c=c+1
		final.append(record)
		m=m+1

	return final




#convert to list
def convert(a):
	lis=[]
	for l in a:
		k=[]
		for l1 in l:
			k.append(l1)
		lis.append(k)
	return lis


#index.html
@app.route("/")
def h():
	return render_template("index.html")







#APi Link For result
@app.route("/result",methods=["GET","POST"])
def index():
	if(request.method=="POST" or request.method=="GET" ):
		try:
			registration_no=str(request.args['regno'])
		except:
			return jsonify({"error":'Please Provide Registration no:'})
		connection=sqlite3.connect('a.db')
		c=connection.cursor()
		statement='SELECT "SUB.CODE","SUBJECTNAME","Grade" FROM "sheet1" WHERE "REGD.NO"='+registration_no
		c.execute(statement)
		result=c.fetchall()
		if len(result) > 0:
			res=c.fetchall()
			res2=convert(result)
			#print(res2)
			diction=converter(res2)
			cgpa=gpa(res2)
			c.close()
		else:
			return jsonify({"error":'Registration no not found !'})
		return jsonify(diction)    
	return "failed"


if __name__=="__main__":
    app.run(debug=True)