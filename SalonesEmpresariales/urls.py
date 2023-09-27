from django.urls import path,include
from SalonesEmpresariales import views
from rest_framework import routers

routerClient = routers.DefaultRouter()
routerClient.register(r'cliente',views.ClientView,'cliente')

routerEvent = routers.DefaultRouter()
routerEvent.register(r'evento',views.EventView,'evento')


urlpatterns = [
    path('',include(routerClient.urls)),
    path('',include(routerEvent.urls)),
    path('eventfilter/',views.EventFilter)
]
