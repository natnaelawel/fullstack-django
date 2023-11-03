from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField("name", max_length=100) 
    description = models.TextField("description", blank=True, null=True)

    def __str__(self):
        return self.name
    

class Server(models.Model):
    name = models.CharField("name", max_length=100) 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="server_owner", on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, verbose_name=("server_category"), on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField("description", max_length=250, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=("server_member"), on_delete=models.CASCADE, related_name="server_member")
    

    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.models.CharField("Channel", max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("channel_user"), on_delete=models.CASCADE)
    topic = models.CharField("topic", max_length=100)
    server = models.ForeignKey(Server, verbose_name=("channel_server"), related_name=("channel_server"), on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

