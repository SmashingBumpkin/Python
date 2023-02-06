from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet

admin.site.unregister(User)
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.register(User, UserAdmin)
admin.site.register(Dweet)