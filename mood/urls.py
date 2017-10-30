from django.conf.urls import url
from  mood import views as moodView

urlpatterns = [
    url(r'^mood(.html)?$', moodView.IndexView.as_view(), name='mood'),
]
