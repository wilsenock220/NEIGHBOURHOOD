from django.db import models
from django.contrib.auth.models import User


class Neighbour(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=220)
    occupationCount = models.IntegerField()
    police = models.CharField(max_length=50, blank=True)
    hospital = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        neigbor = Neighbour.objects.all().delete()
        return neigbor

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        neigbor = cls.objects.filter(id=neigborhood_id)
        return neigbor


class Profile(models.Model):
    fullname = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile/", blank=True)
    neigbor = models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    secondaryEmail = models.EmailField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    class Meta:
        pass
