from django.db import models


class House(models.Model):
    addr = models.CharField(max_length=32)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"House: {self.addr}"
