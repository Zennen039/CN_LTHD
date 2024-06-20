from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.decorators import action
from .models import WeddingService, WeddingHall, BanquetRoom, User, WeddingMenu, WeddingBooking, FoodMenu, FeedBack, \
    FoodItem, HomePage, Staff
from anwedding import serializers, paginators, permission
from rest_framework.response import Response


class HomePageViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = HomePage.objects.all()
    serializer_class = serializers.HomePageSerializer


class WeddingServiceViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingService.objects.all()
    serializer_class = serializers.WeddingServiceSerializer

    def get_permissions(self):
        if self.action in ['add_feedback']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='feedbacks', detail=True)
    def get_feedbacks(self, request, fb):
        feedbacks = self.get_object().feedback_set.select_related('user').order_by('-id')

        paginator = paginators.FeedBackPaginator()
        page = paginator.paginate_queryset(feedbacks)
        if page is not None:
            serializer = serializers.FeedBackSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        return Response(serializers.FeedBackSerializer(feedbacks, many=True).data)

    @action(methods=['post'], url_path='feedbacks', detail=True)
    def add_feedback(self, request, fb):
        a = self.get_object().feedback_set.create(content=request.data.get('content'), user=request.user)

        return Response(serializers.FeedBackSerializer(a).data, status=status.HTTP_201_CREATED)


class WeddingHallViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingHall.objects.all()
    serializer_class = serializers.WeddingHallSerializer
    pagination_class = paginators.WeddingHallPaginator

    def get_queryset(self):
        queryset = self.queryset

        q = self.request.query_params.get('q')

        if q:
            queryset = queryset.filter(name__icontains=q)

        hall_id = self.request.query_params.get('wedding_hall_id')

        if hall_id:
            queryset = queryset.filter(wedding_hall_id=hall_id)

        return queryset

    @action(methods=['get'], url_path='banquet_rooms', detail=True)
    def get_banquet_rooms(self, request, bq):
        banquet_rooms = self.get_object().banquet_room_set.filter(active=True)
        return Response(serializers.BanquetRoomSerializer(banquet_rooms, many=True).data,
                        status=status.HTTP_200_OK)


class WeddingMenuViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingMenu.objects.all()
    serializer_class = serializers.WeddingMenuSerializer
    pagination_class = paginators.WeddingMenuPaginator


class WeddingBookingViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = WeddingBooking.objects.all()
    serializer_class = serializers.WeddingBookingSerializer


class BanquetRoomViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = BanquetRoom.objects.all()
    serializer_class = serializers.BanquetRoomSerializer
    pagination_class = paginators.BanquetRoomPaginator


class FoodItemViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = serializers.FoodItemSerializer
    pagination_class = paginators.FoodItemPaginator


class FoodMenuViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = FoodMenu.objects.all()
    serializer_class = serializers.FoodMenuSerializer
    pagination_class = paginators.FoodMenuPaginator


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action in ['get_current_user']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get', 'patch'], url_path='current-user', detail=False)
    def get_current_user(self, request):
        user = request.user

        if request.method.__eq__('PATCH'):
            for k, v in request.data.items():
                setattr(user, k, v)
            user.save()
        return Response(serializers.UserSerializer(user).data)


class StaffViewet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer


class FeedBackViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = serializers.FeedBackSerializer
    permission_classes = permission.FeedBackOwner