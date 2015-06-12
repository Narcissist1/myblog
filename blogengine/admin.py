from django.contrib import admin
import models
from django.contrib.auth.models import User
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryToPostInline(admin.TabularInline):
    model = models.CategoryToPost
    extra = 1

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	exclude=('author',)
	# readonly_fields=('text',)
	inlines = [CategoryToPostInline]

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()

admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Category,CategoryAdmin)