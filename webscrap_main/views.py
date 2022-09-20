from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore
import requests
import json
from .models import Token
from fcm_django.models import FCMDevice
from .scrap import *



# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# # Create your views here.

def webscrap_indexpg(request):
    # showFirebaseJS(request)
    if request.method=="POST":
        # print(request.POST)
        country="India"
        search_key= request.POST['search_box']
        reg_token=Token.objects.all().values('token')
        rec_list=[]
        for contents in reg_token:
            rec_list.append(contents['token'])
        scrap_content= scrape(country,search_key)
        print(scrap_content)
        required_data=data_fetch(scrap_content)
        print(required_data)
        data_insert(search_key,required_data,rec_list)
        data_for_print=[]
        try:
            doc = db.collection(search_key).get()
            for elements in doc:
                data_for_print_temp=elements.to_dict()
                data_for_print.append(data_for_print_temp)
        except:
            doc=""
            data_for_print.append(doc)
        print(data_for_print)
        return render(request,'indexpg.html', {'res':rec_list, 'req_data':data_for_print})

    return render(request, 'indexpg.html')

# def send_notification(registration_ids , message_title , message_desc):
    
#     fcm_api ="AAAAcQp7uIQ:APA91bE8gDEQ3bEARYGEwNjM_ohze5wbFu2laP_MzF47F71gmKAfkrskO3121xC5x2GIjbH6r91PcWOz1dJLQm2_4Jmb6sDccCJoVX1RCe7annXYcuD41o_IZn7dNW0lf7ugwEnxFh1N"
#     url = "https://fcm.googleapis.com/fcm/send"
    
#     headers = {
#     "Content-Type":"application/json",
#     "Authorization": 'key='+fcm_api}

#     payload = {
#         "registration_ids" :registration_ids,
#         "priority" : "high",
#         "notification" : {
#             "body" : message_desc,
#             "title" : message_title,
#             # "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
#             # "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
#         }
#     }

    # result = requests.post(url,  data=json.dumps(payload), headers=headers )
    # print(result.json())
    # return HttpResponse("sent")





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
                'apiKey: "AIzaSyBSPe5tQax3sjneTtqDrKNdqTgHidN822M",'\
                'authDomain: "competitive-intelligence-4a07d.firebaseapp.com",'\
                'projectId: "competitive-intelligence-4a07d",'\
                'storageBucket: "competitive-intelligence-4a07d.appspot.com",'\
                'messagingSenderId: "937746016632",'\
                'appId: "1:937746016632:web:a0e471e384651de7ce808d",'\
                'measurementId: "G-SG2JFK5C72"'\
            '};' \
         'app=firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging(app);' \
         'console.log("this is inside view");'\
         'messaging.setBackgroundMessageHandler(function (payload) {' \
            ' console.log("this is inside onMessageBackground");'\
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
    return HttpResponse("Done")