from django.shortcuts import render
from .models import Event
import mysql.connector as mc
# Create your views here.
from django import template

register = template.Library()
def new(request):
    return render(request,'addevent.html')
@register.filter
def get_at_index(list, index):
    return list[index]
def home(request):
    return render(request,'home.html')
def check(request):
    
    con=mc.connect(host="localhost",user="root",password="",database="sample")
    cur=con.cursor()
    cur.execute("select * from admin")
    v=[]
    v=cur.fetchall()
    em= request.POST["email"]
    pwd=request.POST["pwd"]
    for i in v:
        if i[0]==em and i[1]==pwd :
            cur.execute("select * from events")
            l=[]
            l=cur.fetchall()
            l2=[]
            for i in l:
                ev = Event()
                ev.url = i[0]
                ev.event=i[1]
                ev.venue=i[2]
                ev.artist=i[3]
                ev.city=i[4]
                ev.date=i[5]
                ev.time = i[6]
                ev.created=i[7]
                ev.status=i[8]
                l2.append(ev)
            return render(request,'logged.html',{'lists':l2})
    return render(request,'home.html')