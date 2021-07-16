from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Item, Category, Tag


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.unregister(Group)  # 元からあるグループを使わないので非表示に
