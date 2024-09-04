
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, EmbargoDateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('embargo/<str:start_date>/<str:embargo_date>/', EmbargoDateView.as_view(), name='embargo-date'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]