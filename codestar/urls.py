from django.conf.urls import url
from codestar import views

urlpatterns = [
	url(r'^home/$',views.greetings),
    url(r'^home/run$',views.runcode),
    url(r'^home/run2$',views.runcode2),
    url(r'^home/run3$',views.runcode3),
]
