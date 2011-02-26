# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'User'
        db.create_table('api_user', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_index=True)),
            ('screen_name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('followers_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('friends_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('background_img', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('protected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, blank=True)),
            ('tz', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('utc_offset', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('api', ['User'])

        # Adding M2M table for field friends on 'User'
        db.create_table('api_user_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm['api.user'], null=False)),
            ('to_user', models.ForeignKey(orm['api.user'], null=False))
        ))
        db.create_unique('api_user_friends', ['from_user_id', 'to_user_id'])

        # Adding model 'List'
        db.create_table('api_list', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_index=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30, db_index=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=30, db_index=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('uri', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('member_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('subscriber_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('following', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('api', ['List'])

        # Adding M2M table for field members on 'List'
        db.create_table('api_list_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('list', models.ForeignKey(orm['api.list'], null=False)),
            ('user', models.ForeignKey(orm['api.user'], null=False))
        ))
        db.create_unique('api_list_members', ['list_id', 'user_id'])

        # Adding model 'Url'
        db.create_table('api_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('expanded_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
        ))
        db.send_create_signal('api', ['Url'])

        # Adding model 'Status'
        db.create_table('api_status', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_status_set', to=orm['api.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('favorited', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_reply_to_screen_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('in_reply_to_user_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('in_reply_to_status_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('truncated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['Status'])

        # Adding M2M table for field urls on 'Status'
        db.create_table('api_status_urls', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('status', models.ForeignKey(orm['api.status'], null=False)),
            ('url', models.ForeignKey(orm['api.url'], null=False))
        ))
        db.create_unique('api_status_urls', ['status_id', 'url_id'])

        # Adding M2M table for field contributors on 'Status'
        db.create_table('api_status_contributors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('status', models.ForeignKey(orm['api.status'], null=False)),
            ('user', models.ForeignKey(orm['api.user'], null=False))
        ))
        db.create_unique('api_status_contributors', ['status_id', 'user_id'])


    def backwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('api_user')

        # Removing M2M table for field friends on 'User'
        db.delete_table('api_user_friends')

        # Deleting model 'List'
        db.delete_table('api_list')

        # Removing M2M table for field members on 'List'
        db.delete_table('api_list_members')

        # Deleting model 'Url'
        db.delete_table('api_url')

        # Deleting model 'Status'
        db.delete_table('api_status')

        # Removing M2M table for field urls on 'Status'
        db.delete_table('api_status_urls')

        # Removing M2M table for field contributors on 'Status'
        db.delete_table('api_status_contributors')


    models = {
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
        'api.status': {
            'Meta': {'object_name': 'Status'},
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_contributors_set'", 'symmetrical': 'False', 'to': "orm['api.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'favorited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_index': 'True'}),
            'in_reply_to_screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'in_reply_to_status_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'in_reply_to_user_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'truncated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['api.Url']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_status_set'", 'to': "orm['api.User']"})
        },
        'api.url': {
            'Meta': {'object_name': 'Url'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'expanded_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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

    complete_apps = ['api']
