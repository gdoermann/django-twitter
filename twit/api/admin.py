from django.contrib import admin
from twit.api.models import *

def get_friends(modeladmin, request, queryset):
    account = request.user.get_profile().account
    account.get_friends(request.api)
get_friends.short_description = "Load Friends"

def get_followers(modeladmin, request, queryset):
    account = request.user.get_profile().account
    account.get_followers(request.api)
get_followers.short_description = "Load Followers"


class UserAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'name', 'followers_count', 'friends_count', 'location')
    fieldsets = (
            (None, {
                'fields': (
                    ('name', 'screen_name'),
                    ('description',),
                    ('created', 'modified',),
                )
                }),
            ('Extras', {
                'classes': ['collapse'],
                'fields': (
                    ('location', 'url',),
                    ('tz', 'utc_offset')
                )
                }),
            )
    actions = [get_friends]
    readonly_fields = ('created', 'modified')
admin.site.register(User, UserAdmin)

class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'member_count', 'subscriber_count')
    fieldsets = (
            (None, {
                'fields': (
                    ('name', 'slug'),
                    ('description', 'full_name',),
                    ('created', 'modified',),
                )
                }),
            ('Extras', {
                'classes': ['collapse'],
                'fields': (
                    ('uri', 'mode'),
                )
                }),
            )
    readonly_fields = ('created', 'modified')
admin.site.register(List, ListAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'location', 'created_at')
    fieldsets = (
            (None, {
                'fields': (
                    ('user',),
                    ('text',),
                    ('created_at',),
                    ('created', 'modified',),
                )
                }),
            ('Extras', {
                'classes': ['collapse'],
                'fields': (
                    ('favorited', 'truncated'),
                    ('source', 'location'),
                )
                }),
            )
    readonly_fields = ('created', 'modified')
admin.site.register(Status, StatusAdmin)
