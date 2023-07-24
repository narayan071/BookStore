from django.urls import path
from book.views import *

urlpatterns = [
    path("", all_books, name="all_books"),
    path("add_to_cart", add_to_cart, name="add_to_cart"),
    path("cart/", cart, name="cart"),
    path("remove_from_cart/<int:id>/", remove_from_cart, name="remove_from_cart"),
    path("<int:id>/", book_details, name='book_details'),
    path("category/<int:cid>/", category_books, name="book_category"),
    path("check_out/", check_out, name="check_out"),
    path("place_order/", place_order, name="place_order"),
    path("orders/", orders, name="orders"),
    path("add_feedback/", add_feedback, name="add_feedback"),

]