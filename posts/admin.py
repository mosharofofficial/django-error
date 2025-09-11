from django.contrib import admin
from posts.models import modelList
# Register your models here.

for model in modelList:
    admin.site.register(model)
