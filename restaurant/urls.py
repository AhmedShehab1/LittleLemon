from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tables', views.BookingViewSet, basename='bookingsView')

urlpatterns = [
    path('', views.home, name="index"),
    path('menu', views.MenuItemsView.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name="menu"),
    path('', include(router.urls)),
]