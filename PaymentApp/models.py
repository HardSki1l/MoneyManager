
from django.db import models
from UserApp.models import UsersInfoModel
from CardApp.models import CardModel

class HistoryModel(models.Model):
    card_related = models.ForeignKey(CardModel, on_delete=models.CASCADE)
    who_payed = models.ForeignKey(UsersInfoModel, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(default=0)
    when_date = models.DateTimeField(auto_now_add=True)
    CHOICES = (
        ('Taksi', 'Taksi'),
        ('Oziq-ovqat', 'Oziq-ovqat'),
        ('Texnika', 'Texnika'),
        ('O`tkazmalar', 'O`tkazmalar'),
        ('Kiyim', 'Kiyim'),
        ('Transport', 'Transport'),
        ('Komunal-To`lovlar', 'Komunal-To`lovlar'),
        ('Internet-Xizmatlari', 'Internet-Xizmatlari'),
        ('Telefoniya', 'Telefoniya'),
        ('Ta`lim', 'Ta`lim'),
        ('Jarimalar', 'Jarimalar'),
        ('Madaniy-Hordiq', 'Madaniy-Hordiq'),
        ('Xayriya-Fondlari', 'Xayriya-Fondlari'),
        ('Dorixona', 'Dorixona'),
        ('Boshqalar', 'Boshqalar'),
        ('Soliqlar', 'Soliqlar'),
        ('Notarius', 'Notarius'),
        ('Kredit', 'Kredit')
    )
    where = models.CharField(choices=CHOICES, max_length=40)

    def save(self, *args, **kwargs):
        if not self.who_payed and self.card_related:
            self.who_payed = self.card_related.card_holder
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.who_payed)
