from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='anres/%Y/%m')
    role = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('staff', 'Staff'), ('customer', 'Customer')))


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class HomePage(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WeddingService(BaseModel):
    name = models.CharField(max_length=100)
    description = RichTextField()
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WeddingMenu(BaseModel):
    name = models.CharField(max_length=255)
    wedding_service = models.ForeignKey(WeddingService, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class WeddingHall(BaseModel):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price_morning = models.CharField(max_length=50, null=True)
    price_afternoon = models.CharField(max_length=50, null=True)
    price_evening = models.CharField(max_length=50, null=True)
    price_weekend = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='anres/%Y/%m')
    service = models.ForeignKey(WeddingService, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WeddingBooking(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    hall = models.ForeignKey(WeddingHall, on_delete=models.CASCADE)
    menu = models.ForeignKey(WeddingMenu, on_delete=models.CASCADE)
    service = models.ManyToManyField(WeddingService)
    date = models.DateField()
    start_time = models.TimeField()
    total_price = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.customer} - {self.hall.name} on {self.date}'


class BanquetRoom(BaseModel):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField(null=True)
    image = models.ImageField(upload_to='anres/%Y/%m')
    wedding_hall = models.ForeignKey(WeddingHall, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FoodItem(BaseModel):
    name = models.CharField(max_length=255, null=True, unique=True)
    description = RichTextField(null=True)
    service = models.ForeignKey(WeddingService, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FoodMenu(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='anres/%Y/%m')
    wedding_menu = models.ForeignKey(WeddingMenu, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wedding_service = models.ManyToManyField(WeddingService)

    class Meta:
        abstract = True


class FeedBack(Interaction):
    content = RichTextField()