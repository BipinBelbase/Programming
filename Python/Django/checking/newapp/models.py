from djongo import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_langth = 100)
    email = models.EmailField()
    aga = models.IntegerField()

    def __str__(self):
        return self.name