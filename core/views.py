from django.shortcuts import render
from .models import Category, CarouselImage
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def get_carousel_images():
    images = CarouselImage.objects.filter(is_active=True).order_by('order')
    logger.info(f"Nombre d'images du carrousel trouvées : {images.count()}")
    for image in images:
        logger.info(f"Image : {image.title} - {image.image.url}")
    return images
