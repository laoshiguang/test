from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from api import models
from api.serializers.account import UserModelSerializer
import uuid


class Login(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        pwd = request.data.get("password")
        user = models.User.objects.filter(phone=phone, pwd=pwd).first()
        ret = {"code": 1000}
        if not user:
            ret["code"] = 1001
            ret["error"] = "用户名或密码错误"
        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user, defaults={"token": uuid})
            ret["token"] = uid
            ret["name"] = user.name
        return Response(ret)


class Account(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserModelSerializer

    def create(self, request, *args, **kwargs):
        us = UserModelSerializer(data=request.data)
        ret = {"code": 1000}
        if us.is_valid():
            us.save()  # create方法
        else:
            ret["code"] = 1001
            ret["error"] = us.errors
        return Response(ret)

    def list(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        ret = {"code": 1000}
        try:
            user_list = models.User.objects.filter(parent_user__phone=phone)
            us = UserModelSerializer(user_list, many=True, context={'request': request})
            ret["data"] = us.data
        except:
            ret["code"] = 1001
            ret["error"] = "发生错误"
        return Response(ret)


def account_examine(request):
    if request.method == "PUT":
        pass
