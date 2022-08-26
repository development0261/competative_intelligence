


importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-messaging.js");
importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-auth.js");
importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-firestore.js");

         var firebaseConfig = initializeApp({
                apiKey: "AIzaSyC5550kgB5r8Ixz8lq2TRwpkA-fuqHFhK8",
                authDomain: "webscrap-b57b5.firebaseapp.com",
                databaseURL: "https://webscrap-b57b5-default-rtdb.firebaseio.com",
                projectId: "webscrap-b57b5",
                storageBucket: "webscrap-b57b5.appspot.com",
                messagingSenderId: "485507184772",
                appId: "1:485507184772:web:b7d3ebf7c3703a127dead1",
                measurementId: "G-GVN5CF6X4S",
            });
            const messaging = getMessaging(firebaseApp);
        //  const messaging=getMessaging(app);
         messaging.setBackgroundMessageHandler(function (payload) {
             console.log(payload);
             const notification=JSON.parse(payload);
             const notificationOption={
                 body:notification.body,
                 icon:notification.icon
             };
             return self.registration.showNotification(payload.notification.title,notificationOption);
         });