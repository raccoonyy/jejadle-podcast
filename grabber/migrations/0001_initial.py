# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grabber'
        db.create_table('grabber_grabber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('grabber', ['Grabber'])

        # Adding model 'Sermon'
        db.create_table('grabber_sermon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('scripture', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('pubdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('grabber', ['Sermon'])


    def backwards(self, orm):
        # Deleting model 'Grabber'
        db.delete_table('grabber_grabber')

        # Deleting model 'Sermon'
        db.delete_table('grabber_sermon')


    models = {
        'grabber.grabber': {
            'Meta': {'object_name': 'Grabber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'grabber.sermon': {
            'Meta': {'object_name': 'Sermon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'pubdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'scripture': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['grabber']