from asyncio import current_task
from http.client import HTTPResponse
from sqlite3 import Cursor
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import mysql.connector as sql

fn=''
ln=''
em=''
pwd=''

# Create your views here.

def home(request):
    # return HttpResponse("hello i am rohit")
    return render(request, "authentication/index.html")

def signup(request):

    global fn, ln, em, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="zTN9MNDq@1",database='shodhSignup')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="email":
                em=value
            if key=="pass1":
                pwd=value
            
        c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,"authentication/signup.html")

def signin(request):

    global em, pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="zTN9MNDq@1",database='shodhSignup')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="pass1":
                pwd=value
            
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'authentication/error.html')
        else:
            return render(request,'authentication/welcome.html')

    return render(request,'authentication/signin.html')

def signout(request):
    return render(request,'authentication/signout.html')



# for meassage

# def welcome(request):
    
    