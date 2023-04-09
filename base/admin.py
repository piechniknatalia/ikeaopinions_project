from django.contrib import admin

# Register your models here.
from .models import Opinion, Comment, Product

admin.site.register(Opinion) 
admin.site.register(Comment)
admin.site.register(Product)

