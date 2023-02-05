from pyrebase import pyrebase
# Create your models here.
firebaseconfig={
    'apiKey': "AIzaSyCWB19HVPFG4KDd9yUqzdVmLtk2gu47u_M",
  'authDomain': "hackathon-c95d2.firebaseapp.com",
  'databaseURL': "https://hackathon-c95d2-default-rtdb.firebaseio.com",
  'projectId': "hackathon-c95d2",
  'storageBucket': "hackathon-c95d2.appspot.com",
  'messagingSenderId': "721890335371",
  'appId': "1:721890335371:web:b895936bdc70c4841d928e",
  'measurementId': "G-040YPQPJ6R",
  

}
fire=pyrebase.initialize_app(firebaseconfig)
db=fire.database()

data={"name":"ajay"}
db.push(data)
print("hi")