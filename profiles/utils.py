from .models import Organization

def get_org(public_key):
    """ this function takes a special key and decrypt it, and returns organization name whose key matches"""

    organization = Organization.objects.get(public_key=public_key)
    return organization
