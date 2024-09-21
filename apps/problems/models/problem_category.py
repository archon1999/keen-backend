from django.db import models

from . import Category
from . import Problem


class ProblemCategory(models.Model):
    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
