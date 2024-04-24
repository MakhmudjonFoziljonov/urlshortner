from django.db import models
import string
import random


class Url(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.original_url} |  {self.created_at}'

    def get_generate_short_code(self):
        symbols = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(symbols) for i in range(6))
        return short_code

    def save(self, *args, **kwargs):
        self.short_code = self.get_generate_short_code()
        return super().save(*args, **kwargs)
