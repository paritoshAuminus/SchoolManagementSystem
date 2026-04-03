from django.contrib import admin
from .models import Standard, Section

# Register your models here.
@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('title', 'school')
    list_display_links = ('school',)
    search_fields = ('title', 'school')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'standard')
    list_display_links = ('title', 'standard')
    search_fields = ('title', 'standard')
