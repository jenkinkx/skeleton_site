from django.urls import include

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
