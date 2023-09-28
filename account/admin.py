from django.contrib import admin

from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','first_name', 'last_name','country',)
    search_fields = ('first_name','email','last_name') 
 
    actions = ['verify','unverify','activate' ,'deactivate' ]
    
    def verify(self, queryset):
        queryset.update(is_verified=True)
        
    def unverify(self, queryset):
        queryset.update(is_verified=False)
        
    def activate(self, queryset):
        queryset.update(is_active=True)
        
    def deactivate(self, queryset):
        queryset.update(is_active=False)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','l_updated', )
    search_fields = ('title', ) 
  
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author','l_updated')
    search_fields = ('title', 'body' ) 
 
@admin.register(Review)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','body')
    search_fields = ('name', 'email','body') 
  
 