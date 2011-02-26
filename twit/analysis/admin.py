from django.contrib import admin
from twit.analysis.models import *

class UserOrListAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'object', 'member_count')
    fieldsets = (
            (None, {
                'fields': (
                    ('name', 'slug', 'obj_type'),
                    ('created', 'modified',),
                )
                }),
            ('Object', {
                'classes': ['collapse'],
                'fields': ('user', 'lst',)
                }),
            )
    readonly_fields = ('created', 'modified')

admin.site.register(Location, UserOrListAdmin)
admin.site.register(Interest, UserOrListAdmin)
