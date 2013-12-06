# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Live'
        db.create_table(u'courses_live', (
            (u'lesson_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['courses.Lesson'], unique=True, primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('enable_chat', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'courses', ['Live'])


    def backwards(self, orm):
        # Deleting model 'Live'
        db.delete_table(u'courses_live')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'Your description'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        },
        u'courses.lesson': {
            'Meta': {'object_name': 'Lesson'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '244', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lessons'", 'to': u"orm['courses.Section']"}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'user_completed_lessons': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'courses.live': {
            'Meta': {'object_name': 'Live', '_ormbases': [u'courses.Lesson']},
            'enable_chat': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'lesson_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courses.Lesson']", 'unique': 'True', 'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'courses.section': {
            'Meta': {'object_name': 'Section'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['courses.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'})
        }
    }

    complete_apps = ['courses']