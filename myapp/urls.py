from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from qlsv import views,process
from . import settings

admin.site.site_header="ADD STUDENT INFORMATIONS"
admin.site.index_title="WELCOME"
urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.form),
    path('add_student_save',process.add_student_save),
    path('display',process.display),
    # path('delete',process.delete),
    path('setting',process.setting),
    path('displaydb',process.displaydb),
    path('edit',process.edit),
    path('edit_save',process.edit_save),
    path('delete',process.delete),
]
