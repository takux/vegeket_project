from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Item, Category, Tag


class TagInline(admin.TabularInline):
    model = Item.tags.through


class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ('tags',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)  # 元からあるグループを使わないので非表示に
