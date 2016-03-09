from django.contrib import admin

# Register your models here.
from models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display=("title","block","owner","create_timestamp","last_update_timestamp")
    search_fields=["title","content",]
    list_filter=("block",)
admin.site.register(Article,ArticleAdmin)

