from django.urls import path

from .views import Home, StoresListView, StoresDetailView, StoresCreateView, StoresUpdateView, StoresDeleteView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('store/', StoresListView.as_view(), name="Store_list"),
    path('<int:pk>/', StoresDetailView.as_view(), name='Store_detail'),
    path('create/', StoresCreateView.as_view(), name='Store_create'),
    path("<int:pk>/update/", StoresUpdateView.as_view(), name='Store_update'),
    path('<int:pk>/delete/', StoresDeleteView.as_view(), name="Store_delete")
]