from demoapp.models import Widget

from celery import shared_task
from urllib import request
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from pyrsistent import T
from .service import tkt_id
from accounts.models import UserProfile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timezone,timedelta
import time
from time import gmtime, strftime
import datetime
from django.db.models import Q
from django.template import loader
from django.shortcuts import redirect
User = settings.AUTH_USER_MODEL
# import msg91_sms as msgsms
from .sms import *

from django.core.mail import send_mail
from datetime import datetime, time





@shared_task
def masterui(request):
    user = request.user

    auto_scheduled_week_month = Automation.objects.filter(is_active=True)
    print(auto_scheduled_week_month,89898989898)
    auto_scheduled_weekly = Automation.objects.filter(is_active=True,time_period='Weekly')
    auto_scheduled_monthly = Automation.objects.filter(is_active=True,time_period='Monthly')
    print(auto_scheduled_monthly,7878)
    week = datetime.today().isoweekday() ==3 
    month_day = datetime.today().day == 11

    if week==True and month_day==False:

        for asw in auto_scheduled_weekly:
            sub=asw.subject
            message=asw.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=asw.assign_to.email)],
                fail_silently=False,
                


        
    )

            
            auto_assigned = RaiseTicket.objects.create(Type=asw.Type,category=asw.category,subcategory=asw.subcategory,subject=asw.subject, img=asw.img,priority=asw.priority,msg=asw.msg, assign_to=UserProfile.objects.get(id=int(asw.assign_to.id)),
                                                    time_period=asw.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")
    elif month_day==True and week==False:
        for asm in auto_scheduled_monthly:
            sub=asm.subject
            message=asm.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=asm.assign_to.email)],
                fail_silently=False

        
    )
            auto_assigned = RaiseTicket.objects.create(Type=asm.Type,category=asm.category,subcategory=asm.subcategory,subject=asm.subject,img=asm.img,priority=asm.priority, msg=asm.msg, assign_to=UserProfile.objects.get(id=int(asm.assign_to.id)),
                                                    time_period=asm.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")
            
    elif (month_day and week)==True:
        for aswm in auto_scheduled_week_month:
            sub=aswm.subject
            message=aswm.msg
            send_mail(
                
                sub,
                message,
                "please check you have assign a ticket"
                'no-reply@tech58.in',
                [UserProfile.objects.get(email=aswm.assign_to.email)],
                fail_silently=False

        
    )
            auto_assigned = RaiseTicket.objects.create(Type=aswm.Type,category=aswm.category,subcategory=aswm.subcategory,subject=aswm.subject,img=aswm.img,priority=aswm.priority, msg=aswm.msg, assign_to=UserProfile.objects.get(id=int(aswm.assign_to.id)),
                                                    time_period=aswm.time_period, user=request.user)
            print(auto_assigned)
            print("Running")
            Automation.objects.filter(is_active=True).update(is_active=False)
            print("Success")


    

    request.session["_message"] = {
        'type': messages.SUCCESS, 'text': 'Yeah! Tasks has been assigned successfully.'}

    return HttpResponseRedirect('/')