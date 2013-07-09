# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Catelog'
        db.create_table(u'groups_catelog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cate_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('south_test', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'groups', ['Catelog'])

        # Adding model 'Group'
        db.create_table(u'groups_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('catelog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catelog_groups', to=orm['groups.Catelog'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_groups', to=orm['User.MyUser'])),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('member_join', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_topic_add', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 14, 0, 0))),
        ))
        db.send_create_signal(u'groups', ['Group'])

        # Adding M2M table for field member on 'Group'
        db.create_table(u'groups_group_member', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'groups.group'], null=False)),
            ('myuser', models.ForeignKey(orm[u'User.myuser'], null=False))
        ))
        db.create_unique(u'groups_group_member', ['group_id', 'myuser_id'])

        # Adding model 'Group_topic_amount'
        db.create_table(u'groups_group_topic_amount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_topic_amounts', unique=True, to=orm['groups.Group'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'groups', ['Group_topic_amount'])

        # Adding model 'Topic'
        db.create_table(u'groups_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_topics', to=orm['groups.Group'])),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_topics', to=orm['User.MyUser'])),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_reply_add', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 14, 0, 0))),
        ))
        db.send_create_signal(u'groups', ['Topic'])

        # Adding model 'Topic_reply_amount'
        db.create_table(u'groups_topic_reply_amount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_reply_amounts', unique=True, to=orm['groups.Topic'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'groups', ['Topic_reply_amount'])

        # Adding model 'Reply'
        db.create_table(u'groups_reply', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_replies', to=orm['User.MyUser'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topic_replies', to=orm['groups.Topic'])),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'groups', ['Reply'])

        # Adding model 'Group_memeber'
        db.create_table(u'groups_group_memeber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='group_gms', to=orm['groups.Group'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='member_gms', to=orm['User.MyUser'])),
            ('member_role', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'groups', ['Group_memeber'])

        # Adding unique constraint on 'Group_memeber', fields ['group', 'member']
        db.create_unique(u'groups_group_memeber', ['group_id', 'member_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Group_memeber', fields ['group', 'member']
        db.delete_unique(u'groups_group_memeber', ['group_id', 'member_id'])

        # Deleting model 'Catelog'
        db.delete_table(u'groups_catelog')

        # Deleting model 'Group'
        db.delete_table(u'groups_group')

        # Removing M2M table for field member on 'Group'
        db.delete_table('groups_group_member')

        # Deleting model 'Group_topic_amount'
        db.delete_table(u'groups_group_topic_amount')

        # Deleting model 'Topic'
        db.delete_table(u'groups_topic')

        # Deleting model 'Topic_reply_amount'
        db.delete_table(u'groups_topic_reply_amount')

        # Deleting model 'Reply'
        db.delete_table(u'groups_reply')

        # Deleting model 'Group_memeber'
        db.delete_table(u'groups_group_memeber')


    models = {
        u'User.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ipaddr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'iplocation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['groups.Catelog']", 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nickname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_groups': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'groups.catelog': {
            'Meta': {'object_name': 'Catelog'},
            'cate_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'south_test': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'groups.group': {
            'Meta': {'object_name': 'Group'},
            'catelog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catelog_groups'", 'to': u"orm['groups.Catelog']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_groups'", 'to': u"orm['User.MyUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_topic_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 0, 0)'}),
            'member': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['User.MyUser']", 'symmetrical': 'False'}),
            'member_join': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'groups.group_memeber': {
            'Meta': {'unique_together': "(('group', 'member'),)", 'object_name': 'Group_memeber'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_gms'", 'to': u"orm['groups.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'member_gms'", 'to': u"orm['User.MyUser']"}),
            'member_role': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'groups.group_topic_amount': {
            'Meta': {'object_name': 'Group_topic_amount'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_topic_amounts'", 'unique': 'True', 'to': u"orm['groups.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'groups.reply': {
            'Meta': {'object_name': 'Reply'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_replies'", 'to': u"orm['User.MyUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_replies'", 'to': u"orm['groups.Topic']"})
        },
        u'groups.topic': {
            'Meta': {'object_name': 'Topic'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_topics'", 'to': u"orm['User.MyUser']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_topics'", 'to': u"orm['groups.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_reply_add': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 14, 0, 0)'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'groups.topic_reply_amount': {
            'Meta': {'object_name': 'Topic_reply_amount'},
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topic_reply_amounts'", 'unique': 'True', 'to': u"orm['groups.Topic']"})
        }
    }

    complete_apps = ['groups']