from re import search
from django.contrib import admin
from .models import Post
#from post.models import Post

# Register your models here.

#admin classı olması için admin kütüphanesinden
#ModelAdmin sınıfını çağırarak genişlettik
class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    list_editable = ['title']

    #meta classında Post modelini referans alarak
    #bu admin modelinin hangi uygulamaya ait olduğunu belirttik
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)