from django.db import models


class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('orders', 'Orders'),
        ('delivery', 'Delivery'),
        ('products', 'Products'),
        ('returns', 'Returns'),
        ('general', 'General'),
    ]

    question = models.CharField(max_length=500)
    answer = models.TextField()
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, default='general')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question
