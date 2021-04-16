from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    content = HTMLField()
    article_link = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class TeacherProfile(models.Model):

    name = models.CharField(max_length=100)
    my_picture = CloudinaryField('image')
    about = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    my_posts = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)

    def create_profile(sender, instance, created, **kwargs):
        if created:
            TeacherProfile.objects.create(user= instance)

        post_save.connect(create_profile, sender = User)

    def save_profile(self):

        self.save()

    def __str__(self):
        return self.name

