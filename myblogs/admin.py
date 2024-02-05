from django.contrib import admin
from .models import Blog_Category
from .models import contact_info
from .models import Subscription
from .models import blog_post ,Comment


# Register your models here.
admin.site.register(Blog_Category)
admin.site.register(contact_info)
admin.site.register(Subscription)
admin.site.register(blog_post)
admin.site.register(Comment)
