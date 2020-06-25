import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 # 追加
from jsonres_only.models import jsonres_model

def index(request):
    if request.method == 'GET':
        model_data = jsonres_model.objects.all()
        model_bekku = get_object_or_404(jsonres_model,jsonres_nama="bekku")
        user_info = {"login_name": model_bekku.jsonres_nama,
                     "age" : model_bekku.age,
                     "coment" : model_bekku.coment}
        json_item = json.dumps(user_info)
        return HttpResponse(json_item)
