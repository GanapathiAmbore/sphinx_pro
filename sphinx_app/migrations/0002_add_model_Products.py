# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Products'
        db.create_table(u'products', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('design_no', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('album_id', self.gf('django.db.models.fields.IntegerField')()),
            ('catalogno', self.gf('django.db.models.fields.TextField')()),
            ('brand', self.gf('django.db.models.fields.TextField')()),
            ('product', self.gf('django.db.models.fields.TextField')()),
            ('fabric', self.gf('django.db.models.fields.TextField')()),
            ('stock', self.gf('django.db.models.fields.TextField')()),
            ('total_products', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('wholesale_price', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fcolor', self.gf('django.db.models.fields.TextField')()),
            ('fwork', self.gf('django.db.models.fields.TextField')()),
            ('ffabric', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'sphinx_app', ['Products'])


    def backwards(self, orm):
        # Deleting model 'Products'
        db.delete_table(u'products')


    models = {
        u'sphinx_app.products': {
            'Meta': {'object_name': 'Products', 'db_table': "u'products'", 'managed': 'False'},
            'album_id': ('django.db.models.fields.IntegerField', [], {}),
            'brand': ('django.db.models.fields.TextField', [], {}),
            'catalogno': ('django.db.models.fields.TextField', [], {}),
            'category_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'design_no': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'fabric': ('django.db.models.fields.TextField', [], {}),
            'fcolor': ('django.db.models.fields.TextField', [], {}),
            'ffabric': ('django.db.models.fields.TextField', [], {}),
            'fwork': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.TextField', [], {}),
            'stock': ('django.db.models.fields.TextField', [], {}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_products': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'wholesale_price': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sphinx_app']