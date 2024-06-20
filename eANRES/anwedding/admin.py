from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import (HomePage, WeddingService, WeddingHall, WeddingBooking, WeddingMenu,
                     FoodMenu, FeedBack, BanquetRoom, FoodItem)
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class MyWeddingServiceAdminSite(admin.AdminSite):
    site_header = 'AN_WEDDING_RESTAURANT'

    # def get_urls(self):
    #     return [path('anwedding-stats/', self.stats_view)] + super().get_urls()
    #
    # def stats_view(self, request):
    #     Count
    #
    #     return TemplateResponse(request, 'admin/stats.html', {
    #         "service_stats": "STATISTIC"
    #     })


admin_site = MyWeddingServiceAdminSite(name='ANNA')


class WeddingServiceForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = WeddingService
        fields = '__all__'


class MyHomePageAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date', 'updated_date', 'active']
    list_filter = ['created_date', 'name']


class MyWeddingServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_date', 'name']
    form = WeddingServiceForm


class MyWeddingHallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name', 'location', 'price_morning',
                     'price_afternoon', 'price_evening', 'price_weekend']
    list_filter = ['created_date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, hall):
        if hall.image:
            return mark_safe(f"<img src='/static/{hall.image.name}' />")


class MyWeddingBookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'date', 'start_time', 'total_price']
    list_filter = ['created_date', 'updated_date']


class MyWeddingMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name', 'price']
    list_filter = ['created_date', 'updated_date', 'name']


class MyBanquetRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name', 'area', 'kind_of_table',
                     'table', 'stage', 'room_shape']
    list_filter = ['created_date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, room):
        if room.image:
            return mark_safe(f"<img src='/static/{room.image.name}' />")


class FoodItemForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = FoodItem
        fields = '__all__'


class MyFoodItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_date', 'name']
    form = FoodItemForm


class MyFoodMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    search_fields = ['id', 'name']
    list_filter = ['created_date', 'updated_date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, food_menu):
        if food_menu.image:
            return mark_safe(f"<img src='/static/{food_menu.image.name}' />")


class FeedBackForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = FeedBack
        fields = '__all__'


class MyFeedBackAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_date', 'updated_date', 'active']
    list_filter = ['created_date', 'updated_date', 'content']
    form = FeedBackForm


admin_site.register(HomePage, MyHomePageAdmin)
admin_site.register(WeddingService, MyWeddingServiceAdmin)
admin_site.register(WeddingHall, MyWeddingHallAdmin)
admin_site.register(WeddingBooking, MyWeddingBookingAdmin)
admin_site.register(WeddingMenu, MyWeddingMenuAdmin)
admin_site.register(BanquetRoom, MyBanquetRoomAdmin)
admin_site.register(FoodItem, MyFoodItemAdmin)
admin_site.register(FoodMenu, MyFoodMenuAdmin)
admin_site.register(FeedBack, MyFeedBackAdmin)
