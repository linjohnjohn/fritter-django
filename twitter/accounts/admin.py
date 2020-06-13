from django.contrib import admin

# Register your models here.

from .models import Profile

class ProfileAdmin(admin.TabularInline):
    model = Profile

# class FreetAdmin(admin.ModelAdmin):
#     list_display = ['__str__', 'owner']
#     search_fields = ['content', 'owner__username', 'user__email']
#     class Meta:
#         model = Freet

admin.site.register(Profile)
