from rest_framework import pagination


class WeddingHallPaginator(pagination.PageNumberPagination):
    page_size = 20


class BanquetRoomPaginator(pagination.PageNumberPagination):
    page_size = 20


class FoodItemPaginator(pagination.PageNumberPagination):
    page_size = 5


class FoodMenuPaginator(pagination.PageNumberPagination):
    page_size = 20


class FeedBackPaginator(pagination.PageNumberPagination):
    page_size = 20


class WeddingMenuPaginator(pagination.PageNumberPagination):
    page_size = 20