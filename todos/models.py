from django.db import models
from accounts.models import User


class Todo(models.Model):
    """ Model definition for todos"""
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Title for specific todo', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Returns a string representation of title of todo """
        return self.title
