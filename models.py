from django.db import models

# Create your models here.
class Todo(models.Model):
  todo_name = models.CharField(max_length=100)
  todo_content = models.TextField(max_length=1000)
  todo_good_count = models.IntegerField(default=0)

 