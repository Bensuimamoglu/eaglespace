from django.contrib import admin
from .models import Post, UserProfile, Comment, Notification

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'location', 'birth_date')
    search_fields = ('user__username', 'name', 'location')
    list_filter = ('location',)
    date_hierarchy = 'birth_date'
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'bio', 'birth_date', 'location', 'picture', 'cover_photo', 'followers')
        }),
    )

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)