from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json
from .models import Token
from fcm_django.models import FCMDevice


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# # Create your views here.

def webscrap_indexpg(request):
    # showFirebaseJS(request)
    if request.method=="POST":
        # print(request.POST)
        search_key= request.POST['search_box']
        reg_token=Token.objects.all().values('token')
        rec_list=[]
        for content in reg_token:
            rec_list.append(content['token'])

        message_desc="hello"
        print("======= reg frm database",rec_list)
        
        
        
        send_notification(rec_list, search_key , message_desc)
        return render(request,'indexpg.html', {'res':rec_list})

    return render(request, 'indexpg.html')

def send_notification(registration_ids , message_title , message_desc):
    
    fcm_api ="AAAAcQp7uIQ:APA91bE8gDEQ3bEARYGEwNjM_ohze5wbFu2laP_MzF47F71gmKAfkrskO3121xC5x2GIjbH6r91PcWOz1dJLQm2_4Jmb6sDccCJoVX1RCe7annXYcuD41o_IZn7dNW0lf7ugwEnxFh1N"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            # "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            # "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())
    return HttpResponse("sent")





# def index(request):
#     return render(request , 'index.html')

# def send(request,reg_token,):
#     resgistration  = [reg_token]
#     send_notification(resgistration , ' New ads added' , 'New ads alert')
#     return HttpResponse("sent")



def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/7.14.5/firebase-app.js");'\
         'importScripts("https://www.gstatic.com/firebasejs/7.14.5/firebase-messaging.js");'\
         'var firebaseConfig = {'\
                'apiKey: "AIzaSyC5550kgB5r8Ixz8lq2TRwpkA-fuqHFhK8",'\
                'authDomain: "webscrap-b57b5.firebaseapp.com",'\
                'databaseURL: "https://webscrap-b57b5-default-rtdb.firebaseio.com",'\
                'projectId: "webscrap-b57b5",'\
                'storageBucket: "webscrap-b57b5.appspot.com",'\
                'messagingSenderId: "485507184772",'\
                'appId: "1:485507184772:web:b7d3ebf7c3703a127dead1",'\
                'measurementId: "G-GVN5CF6X4S"'\
            '};' \
         'app=firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging(app);' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="application/javascript")

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def token(request):
    # print("inside===>", request.POST)
    a=request.POST['token']
    print(a)
    if Token.objects.filter(token=a).exists():
        print("inside if +++++++++++")
        pass
    else:
        print("inside else --------------")
        tkn=Token(token=a)
        tkn.save()