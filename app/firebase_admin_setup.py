import firebase_admin
from firebase_admin import credentials, storage

# Path to your downloaded JSON key
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'refined-x-reassured.appspot.com'
})
