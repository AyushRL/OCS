from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
from .models import myuser

def validate(request : HttpRequest ):
    if(request.method != "POST"):
        return HttpResponse("Please go thourh submitting the form")
    id = request.POST.get("username")
    hash = request.POST.get("password")
    test_user = myuser.objects.filter(id = id , hash = hash) 
    if len(test_user) != 0:
        test_user = test_user[0]
        isadmin = test_user.is_admin
        if not isadmin:
            data = {
                "id" : id,
                "hash" : hash,
            }
            return JsonResponse(data)
        else:
            data = {
                "data" : [],
            }
            test_users : list[myuser] = myuser.objects.filter()
            for test_user in test_users:
                temp = {"id" : test_user.id, "hash" : test_user.hash}
                if test_user.is_admin:
                    temp["role"] = "admin" 
                else:
                    temp["role"] = "basic"
                data["data"].append(temp)
            return JsonResponse(data)
    else:
        return HttpResponse(f"Invalid Id password  id  = {id} and password = {hash}")
            
def home(request):
    return render(request, "home.html")