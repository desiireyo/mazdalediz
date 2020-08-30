from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import *
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models.functions import Lower
from django.db.models import Count
from django.db import connection
# from django.views.decorators.csrf import csrf_exempt

import datetime

# Create your views here.

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT A.TYPE,A.MODEL,B.MODELDES,A.COLOR,C.COLORDES,COUNT(A.MODEL) QTY FROM INVTRAN A,SETMODEL B,SETCOLOR C WHERE A.MODEL=B.MODELCOD AND A.COLOR=C.COLORCOD AND FLAG='D' AND (A.CONTNO IS NULL OR A.CONTNO='') AND (A.SDATE IS NULL) AND (A.STAT IN ('N','H')) AND (A.CURMATCH = 'N') AND upper(A.TYPE)||upper(A.MODEL)||upper(B.MODELDES)||upper(A.COLOR)||upper(C.COLORDES)||lower(A.TYPE)||lower(A.MODEL)||lower(B.MODELDES)||lower(A.COLOR)||lower(C.COLORDES) LIKE '%"+self+"%' GROUP BY A.TYPE,A.MODEL,B.MODELDES,A.COLOR,C.COLORDES ORDER BY A.TYPE,A.MODEL,A.COLOR ")
        row = cursor.fetchall()
        # print(self)

    return row

def index_searchstock(request):
    
    if request.method == "POST":
        chk1 = request.POST.get('nmType')
    else:
        chk1 = ''
    # print('chk1 ===== ',chk1)
    datasearch = my_custom_sql(chk1)
    
    context = {              
        'datasearch': datasearch
    }
    return render(request, 'searchstock.html', context)


def index_new(request):
    
    query_office = OFFICER.objects.all()
    query_setmodel = SETMODEL.objects.all()
    query_resource = Prospect_resource.objects.all()
    query_resourcemore = Prospect_resourcemore.objects.all()
    query_requirement = Prospect_requirement.objects.all()
    query_trace = Prospect_trace.objects.all()
    query_media = Prospect_media.objects.all()
    query_custmast = CUSTMAST.objects.all()
    query_color = SETCOLOR.objects.all()
    query_condition = Prospect_condition.objects.all()

    # print(query_resourcemore)
    
    
    context = {        
        'query_office': query_office,
        'query_setmodel': query_setmodel,
        'query_resource': query_resource,
        'query_resourcemore': query_resourcemore,
        'query_requirement': query_requirement,
        'query_trace': query_trace,
        'query_media': query_media,
        'query_custmast': query_custmast,
        'query_color': query_color,
        'query_condition': query_condition,
        
    }

    return render(request,'index2.html',context)

def save_prospect(request):
    if request.method == "POST":
        chk1 = request.POST.get('status_prospect')
        # print('chk1 ===== ',chk1)

        receivedt = request.POST.get('receivedt')
        if receivedt == '':
            data_receivedt = None
        else:
            data_receivedt = receivedt

        matchdt = request.POST.get('matchdt')
        if matchdt == '':
            data_matchdt = None
        else:
            data_matchdt = matchdt
        deliverydt = request.POST.get('deliverydt')
        if deliverydt == '':
            data_deliverydt = None
        else:
            data_deliverydt = deliverydt
        birthday = request.POST.get('birthday')
        if birthday == '':
            data_birthday = None
        else:
            data_birthday = birthday

        prospect_data = Prospect_test(
            PROSPECTDT = request.POST.get('prospectdt'),
            RESOURCE_id = request.POST.get('resource'),
            RESOURCEMORE_id = request.POST.get('resourcemore'),
            SALES_CONSULTANT_id = request.POST.get('sales_consultant'),
            CUST_NAME = request.POST.get('firstnm'),
            CUST_LNAME = request.POST.get('lastnm'),
            CUST_TEL1 = request.POST.get('telphone1'),
            CUST_TEL2 = request.POST.get('telphone2'),
            CUST_TEL3 = request.POST.get('telphone3'),
            CUST_NOCARD = request.POST.get('custnocard'),
            CUST_BIRTHDT = data_birthday,
            CUST_EMAIL = request.POST.get('custemail'),
            REQUIREMENT_id = request.POST.get('requirement'),
            ADVISER_id = request.POST.get('adviser'),
            MODEL_id = request.POST.get('model'),
            SALES_PRICE = request.POST.get('saleprc'),
            STATUS_PROSPECT = request.POST.get('status_prospect'),
            TRACE_id = request.POST.get('trace'),
            MEDIA_id = request.POST.get('media'),
            COLOR_id = request.POST.get('color'),
            MEMO = request.POST.get('memo'),
            STATUS_CRE = request.POST.get('customer_cre'),
            TERM_CONDITION_id = request.POST.get('condition'),
            RECEIVEDT = data_receivedt,
            MATCHDT = data_matchdt,
            DELIVERYDT = data_deliverydt,
        )
        prospect_data.save()

    return redirect('/index_view')

class ResourceListView(ListView):
    model = Prospect_resource
    context_object_name = 'resource'
    template_name = 'resource_list.html'


def load_resourcemore(request):
    resource = request.GET.get('resource')
    # print('resource :', resource)

    cities = Prospect_resourcemore.objects.filter(RESOURCE=resource)
    # print('cities : ', cities)
    context = {
        'cities': cities,
    }
    return render(request, 'include/_resource.html', context)

def index_view(request):
    
    query_prospect = Prospect_test.objects.order_by(Lower('CREATED_AT').desc())
    
    context = {        
        'query_prospect': query_prospect,        
    }

    return render(request,'vwtable.html',context)

def prospect_delete(request, id):
    data = Prospect_test.objects.get(id=id)
    data.delete()
    return redirect('/index_view')

def prospect_edit(request, id):
    query_office = OFFICER.objects.all()
    query_setmodel = SETMODEL.objects.all()
    query_resource = Prospect_resource.objects.all()
    query_resourcemore = Prospect_resourcemore.objects.all()
    query_requirement = Prospect_requirement.objects.all()
    query_trace = Prospect_trace.objects.all()
    query_media = Prospect_media.objects.all()
    query_custmast = CUSTMAST.objects.all()
    query_color = SETCOLOR.objects.all()
    query_condition = Prospect_condition.objects.all()
    
    chkupd = 'Y'
    updprospect = Prospect_test.objects.get(id=id)
    # print(updprospect.RESOURCE)

    context = {
        'updprospect' : updprospect,
        'chkupd': chkupd,        
        'query_office': query_office,
        'query_setmodel': query_setmodel,
        'query_resource': query_resource,
        'query_resourcemore': query_resourcemore,
        'query_requirement': query_requirement,
        'query_trace': query_trace,
        'query_media': query_media,
        'query_custmast': query_custmast,
        'query_color': query_color,
        'query_condition': query_condition,
        
    }

    return render(request,'index2.html',context)

def prospect_update(request, id):
    if request.method == "POST":
        chk1 = request.POST.get('status_prospect')
        # print('chk1 ===== ',chk1)

        receivedt = request.POST.get('receivedt')
        if receivedt == '':
            data_receivedt = None
        else:
            data_receivedt = receivedt

        matchdt = request.POST.get('matchdt')
        if matchdt == '':
            data_matchdt = None
        else:
            data_matchdt = matchdt
        deliverydt = request.POST.get('deliverydt')
        if deliverydt == '':
            data_deliverydt = None
        else:
            data_deliverydt = deliverydt
        birthday = request.POST.get('birthday')
        if birthday == '':
            data_birthday = None
        else:
            data_birthday = birthday
        
        prospect_data = Prospect_test.objects.get(id=id)
        
        prospect_data.PROSPECTDT = request.POST.get('prospectdt')
        prospect_data.RESOURCE_id = request.POST.get('resource')
        prospect_data.RESOURCEMORE_id = request.POST.get('resourcemore')
        prospect_data.SALES_CONSULTANT_id = request.POST.get('sales_consultant')
        prospect_data.CUST_NAME = request.POST.get('firstnm')
        prospect_data.CUST_LNAME = request.POST.get('lastnm')
        prospect_data.CUST_TEL1 = request.POST.get('telphone1')
        prospect_data.CUST_TEL2 = request.POST.get('telphone2')
        prospect_data.CUST_TEL3 = request.POST.get('telphone3')
        prospect_data.CUST_NOCARD = request.POST.get('custnocard')
        prospect_data.CUST_BIRTHDT = data_birthday
        prospect_data.CUST_EMAIL = request.POST.get('custemail')
        prospect_data.REQUIREMENT_id = request.POST.get('requirement')
        prospect_data.ADVISER_id = request.POST.get('adviser')
        prospect_data.MODEL_id = request.POST.get('model')
        prospect_data.SALES_PRICE = request.POST.get('saleprc')
        prospect_data.STATUS_PROSPECT = request.POST.get('status_prospect')
        prospect_data.TRACE_id = request.POST.get('trace')
        prospect_data.MEDIA_id = request.POST.get('media')
        prospect_data.COLOR_id = request.POST.get('color')
        prospect_data.MEMO = request.POST.get('memo')
        prospect_data.STATUS_CRE = request.POST.get('customer_cre')
        prospect_data.TERM_CONDITION_id = request.POST.get('condition')
        prospect_data.RECEIVEDT = data_receivedt
        prospect_data.MATCHDT = data_matchdt
        prospect_data.DELIVERYDT = data_deliverydt
        
        prospect_data.save()

    return redirect('/index_view')

# def endcode_pass(userid, passwrd):
#     L = len(userid)
#     P = range(len(passwrd))
#     K = range(len(userid))
#     for J in K:
#         L = L+(ord(userid[J])*(J+1))+len(userid)

#     endcode = ''
#     for I in P:
#         endcode = endcode + chr(1) + str(ord(passwrd[I]) + L + (I+1))
#     endcode = endcode + chr(1)
#     return endcode

def endcode_pass(userid, passwrd):
    userid_strip = userid.strip()
    passwrd_strip = passwrd.strip()
    L = len(userid_strip)
    P = range(len(passwrd_strip))
    K = range(len(userid_strip))
    for J in K:
        L = L+(ord(userid_strip[J])*(J+1))+len(userid_strip)

    endcode = ''
    for I in P:
        endcode = endcode + chr(26) + str(ord(passwrd_strip[I]) + L + (I+1))
    endcode = endcode + chr(26)
    return endcode

# def decode_pass(userid, endcode):
#     L = len(userid)
#     K = range(len(userid))
#     P = range(len(endcode))
#     pass_str = ''
#     decode = ''
#     C = 1
#     for J in K:
#         L = L+(ord(userid[J])*(J+1))+len(userid)
#     for I in P:
#         if not endcode[I] == chr(127):
#             pass_str = pass_str + endcode[I]
#         if (endcode[I] == chr(127)) and (pass_str != ''):
#             decode = decode + chr(int(pass_str) - (L + C))
#             C = C + 1
#             pass_str = ''
#     return decode

def prospect_login(request):
    if request.method == "POST":
        secret_user = request.POST.get('username')
        secret_pass = request.POST.get('password')
        print('secret_user:',secret_user)
        print('secret_pass:',secret_pass)

        endcode = endcode_pass(secret_user, secret_pass)
        print('endcode:',endcode)
        print('type:',type(endcode))

        chks = SECRET.objects.get(USERID=secret_user)
        print('field endcode :', chks.ENDCODE)
        print('type:', type(chks.ENDCODE))
        
        print('==============')
        if (endcode == chks.ENDCODE.strip()):
            print('true')
        else:
            print('false')

        print('127:',chr(127))
        print('1:',chr(1))
        
        
        

    context = {}
    return render(request, 'loginsecret.html', context)