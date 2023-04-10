from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import get_user_model
from sesame.utils import get_token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import SendMsg
from datetime import datetime

def index(request):
    return render(request, "index.html")


# new 05-04-2023
@api_view(['GET'])
def GET_TOKEN(request):
    User = get_user_model()
    user = User.objects.get(username="admin")
    return JsonResponse({"token": get_token(user)}, safe=False, status=HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def send(request):
    data = request.data
    _save_ = SendMsg(message=data["message"], date=datetime.now(), chat_id=data["chat_id"])
    _save_.save()
    return JsonResponse({"mesage": data["message"]}, safe=False, status=HTTP_200_OK)


@api_view(['GET'])
def recover(request):
    db = SendMsg.objects.all()
    DICTS = []
    for data in db:
        DICTS.append({"message": data.message, "date": data.date, "chat_id": data.chat_id})
    return JsonResponse(DICTS, safe=False, status=HTTP_200_OK)