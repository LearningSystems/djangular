from django.conf.urls import patterns, include, url
from rest_framework_nested import routers

from authentication.views import AccountViewSet, LogoutView
from djangular.views import IndexView
from authentication.views import LoginView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns('',
                       # ... URLs
                       url(r'^api/v1/auth/login/$', LoginView.as_view(),
                           name='login'),
                       url(r'^api/v1/auth/logout/$', LogoutView.as_view(),
                           name='logout'),
                       url('^.*$', IndexView.as_view(), name='index'),
)