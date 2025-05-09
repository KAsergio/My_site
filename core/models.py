from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CarouselImage(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Titre de l'image",
        verbose_name="Titre"
    )
    image = models.ImageField(
        upload_to='carousel/',
        help_text="Image du carrousel",
        verbose_name="Image",
        validators=[
            # Tu peux ajouter des validateurs d'image ici si nécessaire
        ]
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Ordre d'affichage",
        verbose_name="Ordre",
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Afficher cette image dans le carrousel",
        verbose_name="Actif"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Image du carrousel"
        verbose_name_plural = "Images du carrousel"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Si c'est une nouvelle image et qu'aucun ordre n'est spécifié
        if not self.pk and self.order == 0:
            # Récupérer le dernier ordre utilisé
            last_order = CarouselImage.objects.aggregate(models.Max('order'))['order__max'] or 0
            self.order = last_order + 1
        super().save(*args, **kwargs)
