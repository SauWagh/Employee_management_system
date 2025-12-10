from django.urls import path
from emp_app.views import*
from uuid import UUID

from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('',home, name='home'),
    path('add/',add_emp_data),
    path('emp_table/',emp_table),
    path('emp_list/',emp_list),
    path('emp_detail/<uuid:employe_id>/', emp_detail, name='emp_detail'),
    path('delete/<uuid:employe_id>/',delete , name='delete'),
    path('update/<uuid:employe_id>/',emp_update, name='update')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'emp_app/static'))