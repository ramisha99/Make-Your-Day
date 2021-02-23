from django.db import models

# Create your models here.

class Todolist(models.Model):
      title=models.CharField(max_length= 200)
      complete=models.BooleanField(default= False)
      created=models.DateTimeField(auto_now_add= True)# auto create date when each item is made

      def __str__(self):
          return self.title

