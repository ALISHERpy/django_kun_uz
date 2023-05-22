from django.contrib import admin
from kun_uz_app.models import Post,Hashtag,Language,Category,Viloyatlar

# Register your models here.

# class Post_Admin(admin.ModelAdmin):
#     fieldsets = (
#         ("Postning mavzusi quyidagicha", {
#             "fields": ( ['title'] 
#             ),
#         }),
#     )
    


# admin.site.register(Post,Post_Admin)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Viloyatlar)
admin.site.register(Hashtag)
admin.site.register(Language)
