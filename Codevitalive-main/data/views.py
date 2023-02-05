from re import L
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from pyrebase import pyrebase
import smtplib
from email.mime.text import MIMEText

#pass -- aymfhqapevpdooue

def index(request):
    return render(request,'index.html')

def creds(request):
    form= UserForm(request.POST or None)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("gowshickh09102021@gmail.com","aymfhqapevpdooue")

    if form.is_valid():
        firstname= str(form.cleaned_data.get("first_name"))
        last_name=str(form.cleaned_data.get("last_name"))
        date=str(form.cleaned_data.get("date"))
        gender=form.cleaned_data.get("gender")
        mail=str(form.cleaned_data.get("mail"))
        in_name=str(form.cleaned_data.get("in_name"))
        qualification=str(form.cleaned_data.get("qualification"))
        linkedin=str(form.cleaned_data.get("linkedin"))
        github=str(form.cleaned_data.get("github"))
        department=str(form.cleaned_data.get("department"))
        #print(type(firstname))
        
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

        data={
            "firstname":firstname,
            "lastname":last_name,
            "date":date,
            "mail":mail,
            "in_name":in_name,
            "qualification":qualification,
            "linkedin":linkedin,
            "github":github,
            "gender":gender,
            "department":department

        }
        if(department=="Web Development"):
            msg=MIMEText(u'https://forms.gle/ML8biKeVUt4r2k9J9')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="Data Science"):
            msg=MIMEText(u'https://forms.gle/fFML7vvYcWhWFi797')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="Computer Vision"):
            msg=MIMEText(u'https://forms.gle/PSW7VXhdPPEpVCC97 ')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="Campus Ambassador"):
            msg=MIMEText(u'https://forms.gle/QkC2ASh9pcvsBhwg8 ')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="Blockchain(Requires Assesment)"):
            msg=MIMEText(u'https://forms.gle/s1e1fP2nG7Ewa1Mo8')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="Product Management/Entrepreuner In Residence"):
            msg=MIMEText(u'https://forms.gle/DF28eCiQMevVUYqeA')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()
        elif(department=="App Development"):
            msg=MIMEText(u'https://forms.gle/ivtD3Thd7bphCx1k6 ')
            server.sendmail("gowshickh09102021@gmail.com",mail,msg.as_string())
            server.quit()

            
        db.push(data)
        
        
     
        return HttpResponse("hey")
    else:
        return HttpResponse("no")
    
        
