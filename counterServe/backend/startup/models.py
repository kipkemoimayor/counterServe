from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    pub_date = models.DateField(
        'date published', default=datetime.today().strftime('%Y-%m-%d'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
