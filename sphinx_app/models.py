# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Products(models.Model):
    #id = models.IntegerField()
    design_no = models.CharField(max_length=32)
    album_id = models.IntegerField()
    catalogno = models.TextField()
    brand = models.TextField()
    product = models.TextField()
    fabric = models.TextField()
    stock = models.TextField()
    total_products = models.CharField(max_length=32)
    #image = models.TextField(db_column='Image')  # Field name made lowercase.
    subcategory = models.CharField(max_length=50)
    category_id = models.CharField(max_length=32)
    wholesale_price = models.CharField(max_length=100)
    weight = models.CharField(max_length=10)
    fcolor = models.TextField()
    fwork = models.TextField()
    ffabric = models.TextField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.product
