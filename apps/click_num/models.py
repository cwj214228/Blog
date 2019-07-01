from django.db import models


class Click_Num(models.Model):
    data = models.DateField(auto_now_add=True, null=True)
    num = models.IntegerField(default=0)
    user_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'clicknumber'