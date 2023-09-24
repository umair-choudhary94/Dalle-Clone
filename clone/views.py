from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"dallefrontend.html")
def profile(request):
    return render(request,"profile.html")

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")


@csrf_exempt
def generate_response(request):
    if request.method == "POST":
        data = request.POST
        description = data.get("description")

        # Process the description and generate response
        # You'll need to implement your own logic here

        response = {"text": "Generated response based on the description"}

        return JsonResponse(response)







