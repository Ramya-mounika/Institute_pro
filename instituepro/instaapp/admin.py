from django.contrib import admin
from .models import Courses

class AdminCourses(admin.ModelAdmin):
    class Meta:
        model=Courses
        fields=['__all__']

admin.site.register(Courses,AdminCourses)

# Register your models here.

#username:mounika password:123456
#username:ramya password:996633
#username:mani password:manI@123
#username:narayana password:narayana
#username:seetha password:Seetha@12
#username:apple password:Apple@123456
#username:banana password:Bana@123
