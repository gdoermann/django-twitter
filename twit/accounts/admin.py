from django.contrib import admin
from twit.accounts import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'screen_name', )
    fieldsets = (
            (None, {
                'fields': (
                    ('user', 'screen_name',),
                    ('created', 'modified',),
                )
                }),
            ('oAuth', {
                'classes': ['collapse'],
                'fields': ('access_key', 'access_secret',)
                }),
            )
    readonly_fields = ('created', 'modified')
admin.site.register(models.UserProfile, UserProfileAdmin)
