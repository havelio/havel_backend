from django.urls import path, include


urlpatterns = [
    path('galeries/', include(('havel_backend.api.galeries.urls', 'galeries'), namespace='galeries')),
    path('biographies/', include(('havel_backend.api.biographies.urls', 'biographies'), namespace='biographies'))
]
