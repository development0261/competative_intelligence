from django.urls import path
from .import views
from django.contrib import admin

urlpatterns=[
    path('', views.webscrap_indexpg, name= 'webscrap_indexpg'),
    path('token/' ,views.token, name= 'token'),
    # path('send/' ,views.webscrap_indexpg, name= 'webscrap_indexpg'),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    # path('retrieve_data/' ,views.retrieve_data, name='retrieve_data'),
    # path('firebase-messaging-sw.js', views.showFirebaseJS, name="show_firebase_js"),
    
]
