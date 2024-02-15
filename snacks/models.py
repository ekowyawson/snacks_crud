from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    title = models.CharField(max_length=256)
    purchaser = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    purchase_date = models.DateTimeField("date purchased")

    def __str__(self):
        return self.title
