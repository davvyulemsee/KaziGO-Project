from . import views
from django.urls import include, path

app_name = 'gigs'

urlpatterns = [
    path('', views.all_gigs, name='all_gigs'),
    path('create_gig/', views.create_gig, name='create_gig'),
    path('submit-task/<str:category_code>/<int:seller_id>/', views.submit_task, name='submit_task'),
    path('category/<slug:code>/', views.gigs_by_category, name='gigs_by_category'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('<slug:slug>/', views.gig_detail, name='gig_detail'),
]