from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


class TeacherProfile(models.Model):

    name = models.CharField(max_length=100)
    my_picture = CloudinaryField('image')
    about = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_profile(sender, instance, created, **kwargs):
        if created:
            TeacherProfile.objects.create(user= instance)

        post_save.connect(create_profile, sender = User)

    def save_profile(self):

        self.save()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=10)
    image = CloudinaryField('image')
    content = models.TextField()
    posted_by = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title