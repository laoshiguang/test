from django.db import models


# Create your models here.
class UserRole(models.Model):
    title = models.CharField(max_length=16)


class User(models.Model):
    phone = models.CharField(max_length=16, unique=True)
    pwd = models.CharField(max_length=16)
    name = models.CharField(max_length=8)
    gender_choice = (
        (1, "男"),
        (2, "女")
    )
    gender = models.IntegerField(choices=gender_choice)
    id_card = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    parent_user = models.ForeignKey("self", to_field="invitation_code")
    invitation_code = models.CharField(max_length=16, unique=True, null=True)
    status = models.ForeignKey("UserRole", default=1)


class UserToken(models.Model):
    user = models.ForeignKey(to="User")
    token = models.CharField(max_length=32)
