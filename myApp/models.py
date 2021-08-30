from django.db import models

# Create your models here.
class Comment(models.Model):
  name = models.CharField(max_length=80)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return 'Comment {} by {}'.format(self.body, self.name)

class Project(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='media/images')

  def __str__(self):
    return self.name

class Photo(models.Model):
  image = models.ImageField(upload_to='media/images')
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
  def __str__(self):
    return str(self.project)