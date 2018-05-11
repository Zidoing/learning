from django.contrib import admin

# Register your models here.
from .models import Publisher, Author, Book
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')  # 进入模块展示行
    list_filter = ('publication_date',)  # 过滤，在右方
    date_hierarchy = 'publication_date'  # 日期的层级效果 在上方
    ordering = ('-publication_date',)
    fields = ('title', 'author', 'publisher', 'publication_date')
    filter_horizontal = ('author',)  # 对于多对多选择的时候 ，可以使用此方法将其 分成2列
    raw_id_fields = ['publisher']  # 当查询外键的对象太多的时候 ，使用此方法，将跳出一个新的提示框，然后进行选择


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

#
# class AuthorInline(admin.StackedInline):
#     model = Author
#     can_delete = False
#     verbose_name_plural = 'author'
#
#
# class UserAdmin(UserAdmin):
#     inlines = (AuthorInline,)

#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
