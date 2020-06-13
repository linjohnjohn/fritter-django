from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class FreetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Freet", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Freet(models.Model):
    source_freet = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=FreetLike)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def is_refreet(self):
        return self.source_freet != None