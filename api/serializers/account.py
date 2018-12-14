from api import models

from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """

    class Meta:
        model = models.User
        fields = "__all__"
