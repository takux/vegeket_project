from django.contrib import admin
from django.contrib.auth.models import Group

from base.models import Item, Tag, Category, User, Profile
from django.contrib.auth.admin import UserAdmin
from base.forms import UserCreationForm


class TagInline(admin.TabularInline):
    model = Item.tags.through


class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)})
    )

    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
    )
    # --- adminでuser作成用に追加 ---

    add_form = UserCreationForm
    inlines = (ProfileInline,)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
