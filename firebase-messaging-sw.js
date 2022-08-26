importScripts('https://www.gstatic.com/firebasejs/7.14.5/firebase-app.js');
// eslint-disable-next-line no-undef
importScripts('https://www.gstatic.com/firebasejs/7.14.5/firebase-messaging.js');

// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyC5550kgB5r8Ixz8lq2TRwpkA-fuqHFhK8",
    authDomain: "webscrap-b57b5.firebaseapp.com",
    databaseURL: "https://webscrap-b57b5-default-rtdb.firebaseio.com",
    projectId: "webscrap-b57b5",
    storageBucket: "webscrap-b57b5.appspot.com",
    messagingSenderId: "485507184772",
    appId: "1:485507184772:web:b7d3ebf7c3703a127dead1",
    measurementId: "G-GVN5CF6X4S",
};
// Initialize Firebase
// eslint-disable-next-line no-undef
firebase.initializeApp(firebaseConfig);

// eslint-disable-next-line no-undef
const messaging = firebase.messaging();
messaging.setBackgroundMessageHandler(payload => {
    const options = {
        body: payload.data.body,
        icon: payload.data.icon,
        data: payload.data.click_action, //the url which we gonna use later
        sound: '/sound.mp3',
        silent: false,
    };
    // eslint-disable-next-line no-restricted-globals
    return self.registration.showNotification(payload.data.title, options);
});

self.addEventListener('notificationclick', event => {
    const url = event.notification.data;
    const urlToOpen = new URL(url, self.location.origin);

    const promiseChain = clients.matchAll({
        type: 'window',
        includeUncontrolled: true,
    }).then((windowClients) => {
        let matchingClient = null;
        for (let i = 0; i < windowClients.length; i++) {
            const windowClient = windowClients[i];
            const parsedClientUrl = new URL(windowClient.url, self.location.href);
            if (parsedClientUrl.host === urlToOpen.host) {
                // Check current organization
                const parsedClient = parsedClientUrl.pathname.split('/')
                const parsedUrl = urlToOpen.pathname.split('/')
                if (parsedClient[1] === parsedUrl[1]) matchingClient = windowClient;
                break;
            }
        }

        if (matchingClient) {
            matchingClient.postMessage({url, type: 'BG'});
            return matchingClient.focus();
        } else {
            return clients.openWindow(url);
        }
    });

    event.waitUntil(promiseChain);
});

// importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js");
// importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-messaging.js");
// importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-auth.js");
// importScripts("https://www.gstatic.com/firebasejs/9.9.3/firebase-firestore.js");

//          var firebaseConfig = initializeApp({
//                 apiKey: "AIzaSyC5550kgB5r8Ixz8lq2TRwpkA-fuqHFhK8",
//                 authDomain: "webscrap-b57b5.firebaseapp.com",
//                 databaseURL: "https://webscrap-b57b5-default-rtdb.firebaseio.com",
//                 projectId: "webscrap-b57b5",
//                 storageBucket: "webscrap-b57b5.appspot.com",
//                 messagingSenderId: "485507184772",
//                 appId: "1:485507184772:web:b7d3ebf7c3703a127dead1",
//                 measurementId: "G-GVN5CF6X4S",
//             });
//             const messaging = getMessaging(firebaseApp);
//         //  const messaging=getMessaging(app);
//          messaging.setBackgroundMessageHandler(function (payload) {
//              console.log(payload);
//              const notification=JSON.parse(payload);
//              const notificationOption={
//                  body:notification.body,
//                  icon:notification.icon
//              };
//              return self.registration.showNotification(payload.notification.title,notificationOption);
//          });