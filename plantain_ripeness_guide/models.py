from django.db import models


class RipenessGuide(models.Model):
    RIPENESS_CHOICES = [
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('brown', 'Brown'),
        ('overripe', 'Overripe'),
    ]

    stage = models.CharField(max_length=20, choices=RIPENESS_CHOICES, unique=True)
    description = models.TextField()
    best_uses = models.TextField()
    cooking_tips = models.TextField()
    image = models.ImageField(upload_to='ripeness_guide/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_stage_display()

    class Meta:
        ordering = ['order']