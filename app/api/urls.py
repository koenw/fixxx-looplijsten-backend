from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


from api.itinerary.views import ItineraryViewSet, ItineraryItemViewSet
from api.users.views import TeamsViewset
from api.health.views import health

router = DefaultRouter()
router.register(r'itineraries', ItineraryViewSet)
router.register(r'teams', TeamsViewset, basename='teams')
router.register(r'cases', ItineraryItemViewSet, basename='case')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health', health),
    path('api/v1/', include(router.urls)),

    # authentication endpoints
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    # the 'api-root' from django rest-frameworks default router
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
