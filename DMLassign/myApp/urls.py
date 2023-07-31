from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from . import api

app_name = 'myApp'

router = DefaultRouter()
router.register(r'invoice', api.GetInvoiceModelViewSet, basename='api-invoice')
router.register(r'detail', api.GetInvoiceDetailModelViewSet, basename='api-detail')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/', include(router.urls)),

]
