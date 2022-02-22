import base64
from multiprocessing import context
from unittest import result
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import json

from datetime import datetime
import mysql.connector
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
config = {

    # 'username':'lbce$lbce',
    'user': 'lbce',
    'password': 'password007',
    'host': 'lbce.mysql.pythonanywhere-services.com',
    # 'database': 'lbce'
}

def profileview(request,name):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # query = ("SELECT fullname, phone,branch,batch,rollno,classname,email,username from tblprofile")

    query = ("SELECT * from `lbce$lbce`.`facultyinfo` where name='"+name+"'")
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    for id in cursor:
        idd.append(id)
        print(idd)
        print(type(idd))
    print(idd)
    cursor.close()
    return render(request,'facultyview.html', {
        'profile': id
        }
    )

    
