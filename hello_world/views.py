import json
import pandas as pd
from django.http import JsonResponse

def getDescription(request):
    df = pd.read_csv("hello_world/Seconds per task (historical).csv", header=1)
    description = df.describe().to_json()
    description = json.loads(description)
    #description = {'hola'};
    return JsonResponse(description)
