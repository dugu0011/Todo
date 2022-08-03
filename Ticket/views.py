from imghdr import what
from re import T
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


# Create your views here.

users = UserProfile.objects.filter(is_admin = True)




@login_required(login_url='/login/')
def raiseTicket(request):
    user = request.user
    userid = user
    msg = ""
    qw=request.user.mobile
    print(qw)
    myTicket = RaiseTicket.objects.filter(user=request.user, is_active=True)
    is_raise_ticket='YES'
    
    if request.method == "POST":
        ticket = RaiseTicketForm(request.POST, request.FILES)
        

        if ticket.is_valid():
            instance = ticket.save(commit=False)
            instance.user = request.user
            instance.raised_by=request.user
            txnid = tkt_id(is_raise_ticket,request.user)
            instance.ticket_id=txnid
            instance.save()
            
            
            # msg_html = loader.render_to_string("ticket_raise_mail.html",{'user': user, 'msg': msg, 'ticketid': txnid})
            # send_mail(
                

            #     'Ticket Raised Sucessfully',
            #     "Dear " + request.user.name,
            #     'no-reply@tech58.in',
            #     [UserProfile.objects.get(email=request.user.email)],
            #     html_message=msg_html,
            #     fail_silently=False

        
            # )
            # ticketid=txnid
            
            # smss(qw,ticketid)
            # messages.success(request, 'Contact request submitted successfully.')
            # messages.info(request, 'Your has been changed successfully!')
            # msg = "Thank you for raising a ticket"
            # return HttpResponseRedirect('/')


            
    else:
        ticket = RaiseTicketForm()
    return render(request, 'web/jinja2/ticket_raise/ticket_raise.html.j2', {'user': user, 'msg': msg, 'ticket': ticket, 'myTicket': myTicket,})




@login_required(login_url='/login/')
def status1(request):
    status_type = request.GET.get('status_type')
    assign_to = request.GET.get('assign_to')
    print(assign_to,"dugu222")
    
    s_id = request.GET.get('s_id')
    if status_type:
        st=RaiseTicket.objects.get(id=int(s_id))#.update(status=status_type)
        # namm=st.user.name
        # mailss=st.raised_by
        # cl_id=st.ticket_id
        # msg_html = loader.render_to_string("st_mail.html",{'cl_id':cl_id,'namm':namm })
        st.status = status_type
        st.save()

    return HttpResponseRedirect('/') 

        # if status_type == 'Closed':

        #     send_mail('Ticket status','Dear ststtss','no-reply@tech58.in',[mailss],fail_silently=False)

            
               
    


    # return HttpResponseRedirect('/Ticket/viewraiseticket/'+ str(ticket_id))
    


@login_required(login_url='/login/')
def test(request):
    ticket_id=request.GET.get('ticket')
    message=request.GET.get('message')
    cmt_obj = Comment(message=message, user=request.user, ticket=RaiseTicket.objects.get(id=int(ticket_id)))
    cmt_obj.save()
    return HttpResponseRedirect('/Ticket/viewraiseticket/'+ str(ticket_id))
    



@login_required(login_url='/login/')
def viewall(request):
    if request.user.is_admin == True:
        myTicket = RaiseTicket.objects.filter(is_active=True).order_by('created')[::-1]
    else:
        myTicket = RaiseTicket.objects.filter(
            user=request.user, is_active=True).order_by('-subject')
    ticket = RaiseTicketForm()

    return render(request, 'web/jinja2/ticket_raise/viewTicket.html.j2', {'ticket': ticket, 'myTicket': myTicket })


@login_required(login_url='/login/')
def assignme(request):
    

    if request.user.is_admin == True:
        myTicket = RaiseTicket.objects.filter(is_active=True)
    else:
        myTicket = RaiseTicket.objects.filter(
            assign_to=request.user, is_active=True)
    ticket = RaiseTicketForm()

    return render(request, 'web/jinja2/ticket_raise/viewTicket.html.j2', {'ticket': ticket, 'myTicket': myTicket})







@login_required(login_url='/login/')
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






















# pratice code    


def practice(request):
    return render(request,'web/jinja2/ticket_raise/practice.html')
    
