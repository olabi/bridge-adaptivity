from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _


@admin.register(LtiProvider)
class LtiProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(LtiConsumer)
class LtiConsumerAdmin(admin.ModelAdmin):
    pass


@admin.register(LtiUser)
class LtiUserAdmin(admin.ModelAdmin):
    pass


@admin.register(LtiSource)
class LtiSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(BridgeUser)
class BridgeUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'roles', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'roles', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'roles', 'first_name', 'last_name', 'is_staff')
