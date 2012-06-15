# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sermon.pubdate'
        db.delete_column('grabber_sermon', 'pubdate')

        # Adding field 'Sermon.date'
        db.add_column('grabber_sermon', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Sermon.pubdate'
        db.add_column('grabber_sermon', 'pubdate',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 6, 15, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Sermon.date'
        db.delete_column('grabber_sermon', 'date')


    models = {
        'grabber.grabber': {
            'Meta': {'object_name': 'Grabber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'grabber.sermon': {
            'Meta': {'object_name': 'Sermon'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'scripture': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['grabber']