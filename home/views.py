from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from PIL import Image
import pytesseract
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def front(request):
    if request.method == "POST":
        userlogin = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request,username=userlogin,password=password)
            messages.success(request,"Vous êtes Connecté !!!")
            login(request,user)
            return redirect('home')
            
        except:
            messages.success(request,"Identifiants erroné !!!")
            
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    messages.success(request,"Vous êtes Déconnecté !!!")
    return redirect('front')



def home(request):
	historique = fileUpload.objects.filter(user=request.user).order_by("-id")
	context = {
	"historique" : historique,
	}
	if request.method == 'POST':
		fileupload = request.FILES.get("image")
		newfile = fileUpload.objects.create(name=fileupload.name,file=fileupload,user=request.user)
		print(newfile.file.name)
		try:
			newfile.text = pytesseract.image_to_string('media/'+newfile.file.name)
		except:
			newfile.text = pytesseract.image_to_string('media/'+newfile.file.name)
		newfile.save()
		context['result'] = newfile
	

	return render(request,"index.html",context)