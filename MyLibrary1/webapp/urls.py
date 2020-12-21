from django.urls import include, path
from .views import BookViewSet, BorrowerViewSet, available_book_list, borrow_book, return_book
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='language')
router.register('borrower', BorrowerViewSet, basename='paradigm')


urlpatterns = [
    # path('book/', book_list),
    # path('borrower/', borrower_list),
    path('', include(router.urls)),
    path('available-book-list/', available_book_list),
    path('borrow-book/', borrow_book),
    path('return-book/', return_book),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
