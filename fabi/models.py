from django.db import models

# Create your models here.


class Fabonacci(models.Model):
    numstr = models.CharField(max_length=20)
    terms = models.CharField(max_length=500)

    def __str__(self):
        return "The first " + str(self.numstr) + " terms in fibonacci series : " + self.terms
