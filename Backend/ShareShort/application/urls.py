from django.urls import path , include
from .views import ProfileLinksView, ExtraLinksGetPostView , ExtraLinksPutDeleteView , StoreLinksGetPostView , StorePutDeleteView 
urlpatterns = [
   path('profile/' , ProfileLinksView.as_view()),
   path('links/' , ExtraLinksGetPostView.as_view()),
   path('link/<int:extralinkid>' , ExtraLinksPutDeleteView.as_view()),
   path('stores/' , StoreLinksGetPostView.as_view()),
   path('store/<int:storeid>' , StorePutDeleteView.as_view()),
]