import firebase_admin
from firebase_admin import credentials, firestore\


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('cosmatic')

# def async getMarker(): {
#     const snapshot = await firebase.firestore().collection('cosmatic').get()
#     return snapshot.docs.map(doc => doc.data());
# }

# Note: Use of CollectionRef stream() is prefered to get()
docs = db.collection(u'cosmatic').stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')

# doc = collection.document()
# res = doc.get().to_dict()
# print(res)

# import threading
# # Create an Event for notifying main thread.
# callback_done = threading.Event()

# # Create a callback on_snapshot function to capture changes
# def on_snapshot(doc_snapshot, changes, read_time):
#     for doc in doc_snapshot:
#         print(f'Received document snapshot: {doc.id}')
#     callback_done.set()

# doc_ref = db.collection(u'cosmatic')

# # Watch the document
# doc_watch = doc_ref.on_snapshot(on_snapshot)
# print(doc_watch)