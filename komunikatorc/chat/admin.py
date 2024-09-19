from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import User, Friend, Group, Message, Reaction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar')
    search_fields = ('username',)
    list_filter = ('username',)

    # Override the save_model method to hash the password
    def save_model(self, request, obj, form, change):
        if form.cleaned_data['password']:
            obj.password = make_password(obj.password)  # Hash the password
        super().save_model(request, obj, form, change)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend')
    search_fields = ('user__username', 'friend__username')
    list_filter = ('user', 'friend')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'author', 'text', 'created_at')
    search_fields = ('text', 'author__username', 'group__name')
    list_filter = ('group', 'author', 'created_at')


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'reaction')
    search_fields = ('user__username', 'message__text', 'reaction')
    list_filter = ('reaction',)
