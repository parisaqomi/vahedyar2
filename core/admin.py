from django.contrib import admin

# Register your models here.
from .models import University , Faculty ,Chart, Study , Course ,Scores
# Register your models here.
admin.site.register(University)

admin.site.register(Faculty)

admin.site.register(Chart)

admin.site.register(Study)

admin.site.register(Scores)

admin.site.register(Course)

admin.site.site_header = ' سامانه واحدیار - پنل مدیریت '
admin.site.site_title = ' پرتال مدیریت - واحدیار'
admin.site.index_title = ' صفحه مدیریت سایت'