from django.contrib import admin

from reader_app.models import Category, Channel, Content


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_build_date')
    list_filter = ('category', )
    search_fields = ('name', )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('channel', 'title', 'publication_date')
    list_filter = ('channel', )
    search_fields = ('title', )
    date_hierarchy = 'publication_date'
