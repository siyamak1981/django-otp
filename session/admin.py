from django.contrib import admin
from painless.models.actions import ExportMixin, PostableMixin
from session.models import Session





@admin.register(Session)
class SessionAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['client_ip',  'user', 'server_version', 'is_blooked']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
 
