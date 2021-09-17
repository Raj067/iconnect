from django.contrib import admin
from .models import *
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'timestamp')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'timestamp')


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.site_header = 'Iconnect Company'
admin.site.register(Post, PostAdmin)
