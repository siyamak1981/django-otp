from django.contrib import admin
from .models import Province, User, City, SendSmsRequest
from django.utils.translation import gettext as _
from khayyam import JalaliDate as jd
from painless.models.actions import PostableMixin,ExportMixin, make_active, make_deactive
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'General Profile'
    fk_name = 'user'
    
    
    fieldsets = [
        ('I. Personal Information', {
            'fields': ['address', 'city'],
            'classes': ['collapse']
        }),
        ('II. Personal Information', {
            'fields':[ 'gender', 'varification_type', 'job'],
            'classes': ['collapse']
        }),
        ('III. Personal Information', {
            'fields': ['avatar', 'birth_date', 'level'],
            'classes': ['collapse']
        })
    ]   



@admin.register(User)
class UserAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
  
    fieldsets = (
       

        ('main', { 
            'fields': ( 
                    ('mobile_number',), 
                    ('email', 'password', ),
                    ('first_name', 'last_name',),
                    ('is_staff', 'is_active', 'is_superuser'),
                
                ),
            }
        ),

        (
            _("Permissions"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

  
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2"),
            },
        ),
    )
    list_display_links = ("mobile_number","email")
    list_display = ('mobile_number','email', "first_name", "last_name", "is_staff",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ( "first_name", "last_name", "email")
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    inlines = (
            ProfileInline,
        )
        
    actions = [make_active, make_deactive]
    ordering = ('email',)


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['title',  'published']
    list_filter = ['published_at']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title',), 
                    'published_at'
                     
                ),
            }
        ),

    ]

    def published(self, obj):
        return jd(obj.published_at)


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []




@admin.register(City)
class CityAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['title', 'province', 'published']
    list_filter = ['published_at']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title',), 
                    ('province',), 
                    'published_at'
                     
                ),
            }
        ),

    ]

    def published(self, obj):
        return jd(obj.published_at)


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []



@admin.register(SendSmsRequest)
class OTPRequestAdmin(admin.ModelAdmin, PostableMixin, ExportMixin):
    list_display = ['channel', 'receiver', 'code', 'created']
    actions = ['make_published', 'make_draft', 'export_as_json', 'export_as_csv']
  
    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('channel',), 
                    ('receiver',), 
                    'code',
                ),
            }
        ),

    ]

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)







admin.site.site_header = "Bernet Adminstration"
admin.site.site_title = "Bernet site admin"
admin.site.index_title = "Welcome to Bernet dashboard"

