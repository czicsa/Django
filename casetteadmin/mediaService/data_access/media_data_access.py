from mediaService.models import Media
import time

def get_all_media():
    return Media.objects.filter(is_deleted = False)

def get_all_rented_media():
    return Media.objects.filter(is_deleted = False).exclude(customer = None )

def get_media_by_id(media_id):
    return Media.objects.get(id = media_id)

def insert_media(media):
    media.save()

def update_media(media):
    media.save()

def delete_media(media):
    media.is_deleted = True
    media.save()