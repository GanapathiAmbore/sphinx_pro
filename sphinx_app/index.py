from django_sphinx_db.backend.models import SphinxModel, SphinxField
from django.db import models
class MyIndex(SphinxModel):
    class Meta:
        # This next bit is important, you don't want Django to manage
        db_table='products'
        managed = False

    name = SphinxField()
    content = SphinxField()
    date = models.DateTimeField()
    size = models.IntegerField()