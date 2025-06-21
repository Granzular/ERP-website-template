from .models import Organization, Staff, CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

@receiver(post_save,sender=CustomUser)
def post_save_create_org_or_staff(sender,instance,created,**kwargs):
    if created:
        if instance.user_type=='org':
            public_key = str(uuid.uuid4())[:9]
            Organization.objects.create(user=instance,public_key=public_key)
            
