from django.conf.urls import url
from  dairy import views as dairyView

urlpatterns = [
    url(r'^dairy(.html)?$', dairyView.IndexView.as_view(), name='dairy'),
]
