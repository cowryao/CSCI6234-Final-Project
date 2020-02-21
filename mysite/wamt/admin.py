from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.auth.models import User,Group
from .models import Movie, Event, NewUserManager, NewGroupManager, MMTest

# Register your models here.
admin.site.register(Movie)


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Vote", {"fields": ["event_start_vote_time", "event_end_vote_time"]}),
        ("Event", {"fields": ["event_name", "event_location", "event_time"]}),
    ]


admin.site.register(Event, EventAdmin)


class NewGroupManagerInline(admin.StackedInline):
    model = NewGroupManager
    filter_horizontal = ('group_events','group_user')


class CustomGroupAdmin(GroupAdmin):
    #filter_horizontal = ('user_permissions', 'groups', 'ope')
    save_on_top = True
    list_display = ['name', 'pk']
    inlines = [NewGroupManagerInline]


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)


class NewUserManagerInline(admin.StackedInline):
    model = NewUserManager
    filter_horizontal = ('group_owned',)


class CustomUserAdmin(UserAdmin):
    #filter_horizontal = ('user_permissions', 'groups', 'ope')
    save_on_top = True
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login')
    inlines = [NewUserManagerInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(MMTest)