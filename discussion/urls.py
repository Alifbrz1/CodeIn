from django.urls import path
from . import views

urlpatterns = [
    path('discussion/<int:code>', views.discussion, name='discussion'),
    path('send/<int:code>/<int:std_id>', views.send, name='send'),
    path('message/<int:code>/<int:fac_id>', views.send_fac, name='send_fac'),
    path('delete/<int:code>/<int:discussion_id>', views.delete_discussion, name='delete_discussion'),
    # path('discussion/<code>/reply/<int:discussion_id>/', views.reply, name='reply'),



]