from django.contrib import admin
from wiki.models import Category, Page, SubPage
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PageResource(resources.ModelResource):
    class Meta:
        model = Page
        import_id_fields = ('name',)


class SubPageResource(resources.ModelResource):
    class Meta:
        model = SubPage
        import_id_fields = ('name',)


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        import_id_fields = ('name',)
        fields = ('name', 'label',)


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PageResource
    list_display = ['name', 'category', 'published']


@admin.register(SubPage)
class SubPageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SubPageResource
    list_display = ['name', 'page', 'page_index']
    list_filter = ['page']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource
    list_display = ['name', 'label']
