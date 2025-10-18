from django.http import JsonResponse
from django.shortcuts import render
import json
import requests
#import datetime 
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# implement basic logging for debugging
# consider rate limiting for the endpoint
# handle cors


# GET METHOD ONLY

@csrf_exempt
def home(request):
    if request.method == 'GET':
        print(request.method)
        api_response = requests.get("https://catfact.ninja/fact", timeout=5)

        if api_response.status_code == 200:
            json_object = {
                "status": "success",
                "user": {
                    "email": "mikelonu15@gmail.com",
                    "name": "Michael Onuekwusi",
                    "stack": "Django",
                },
                "timestamp": f"{timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')}",
                #"timestamp": datetime.datetime.now(timezone.utc).time().isoformat(),
                "fact": api_response.json().get("fact")
            }
            response = JsonResponse(json_object, status=200)
        else:
            json_object = {
                "status": "error",
                "message": "Failed to fetch cat fact"
            }
            response = JsonResponse(json_object, status=500)
    else:
        json_object = {
            "status": "error",
            "message": "Invalid request method"
        }
        json_object = JsonResponse(json_object, status=405)
        
    response["Content-Type"] = "application/json"
    return response
