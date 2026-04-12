from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Doctor_Information
from hospital.models import User

@receiver(post_save, sender=Doctor_Information)
def updateUser(sender, instance, created, **kwargs):
    doctor = instance
    user = doctor.user

    if created == False:
        user.first_name = doctor.name
        user.username = doctor.username
        user.email = doctor.email
        user.save()
