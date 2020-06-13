from django.contrib import admin

from .models import Freet, FreetLike

class FreetLikeAdmin(admin.TabularInline):
    model = FreetLike

class FreetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner']
    search_fields = ['content', 'owner__username', 'user__email']
    class Meta:
        model = Freet

admin.site.register(Freet, FreetAdmin)