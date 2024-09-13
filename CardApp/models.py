import datetime
from django.db import models
from UserApp.models import UsersInfoModel

current_date = datetime.datetime.now()
expiration_date = current_date.replace(year=current_date.year + 4)


class CardModel(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    expiration_date = models.DateField(default=expiration_date)  # default ozi qoshib ketadi
    created_date = models.DateField(auto_now_add=True)  # default ozi qoshib ketdi
    card_holder = models.ForeignKey(UsersInfoModel, on_delete=models.CASCADE)
    money = models.FloatField(default=0)

    def __str__(self):
        return self.card_number










