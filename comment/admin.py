from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display=("block","article","owner","content","status","create_timestamp","last_update_timestamp")
    search_fields=["owner","content",]
    list_filter=("article",)
admin.site.register(Comment,CommentAdmin)

