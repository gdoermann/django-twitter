# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('analysis_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('obj_type', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_location_set', null=True, to=orm['api.User'])),
            ('lst', self.gf('django.db.models.fields.related.ForeignKey')(related_name='list_location_set', null=True, to=orm['api.List'])),
        ))
        db.send_create_signal('analysis', ['Location'])

        # Adding M2M table for field members on 'Location'
        db.create_table('analysis_location_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm['analysis.location'], null=False)),
            ('user', models.ForeignKey(orm['api.user'], null=False))
        ))
        db.create_unique('analysis_location_members', ['location_id', 'user_id'])

        # Adding model 'Interest'
        db.create_table('analysis_interest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, db_index=True)),
            ('obj_type', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_interest_set', null=True, to=orm['api.User'])),
            ('lst', self.gf('django.db.models.fields.related.ForeignKey')(related_name='list_interest_set', null=True, to=orm['api.List'])),
        ))
        db.send_create_signal('analysis', ['Interest'])

        # Adding M2M table for field members on 'Interest'
        db.create_table('analysis_interest_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('interest', models.ForeignKey(orm['analysis.interest'], null=False)),
            ('user', models.ForeignKey(orm['api.user'], null=False))
        ))
        db.create_unique('analysis_interest_members', ['interest_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('analysis_location')

        # Removing M2M table for field members on 'Location'
        db.delete_table('analysis_location_members')

        # Deleting model 'Interest'
        db.delete_table('analysis_interest')

        # Removing M2M table for field members on 'Interest'
        db.delete_table('analysis_interest_members')


    models = {
        'analysis.interest': {
            'Meta': {'object_name': 'Interest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lst': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'list_interest_set'", 'null': 'True', 'to': "orm['api.List']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'list_location_member_set'", 'symmetrical': 'False', 'to': "orm['api.User']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'obj_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_interest_set'", 'null': 'True', 'to': "orm['api.User']"})
        },
        'analysis.location': {
            'Meta': {'object_name': 'Location'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lst': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'list_location_set'", 'null': 'True', 'to': "orm['api.List']"}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_location_member_set'", 'symmetrical': 'False', 'to': "orm['api.User']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'obj_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_location_set'", 'null': 'True', 'to': "orm['api.User']"})
        },
        'api.list': {
            'Meta': {'object_name': 'List'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'following': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'member_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.User']", 'symmetrical': 'False'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'subscriber_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'uri': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'api.user': {
            'Meta': {'object_name': 'User'},
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'background_img': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'followers_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.User']", 'symmetrical': 'False'}),
            'friends_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'screen_name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'tz': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'utc_offset': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['analysis']
