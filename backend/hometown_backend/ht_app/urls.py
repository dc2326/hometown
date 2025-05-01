from django.urls import path
from ht_app.views import CommListAPIView, CommDetailAPIView

urlpatterns = [
    path('community/', CommListAPIView.as_view()),
    path('community/<int:pk>', CommDetailAPIView.as_view())
]