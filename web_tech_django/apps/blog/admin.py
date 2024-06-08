from django.contrib import admin
from .models import Tour, Hotel, OrderHotel, Checkoutenquiry, Payment ,Hotelcheckout
from .models import OrderTour, Customer, VendorRequest

# Register your models here.
admin.site.register(Tour)
admin.site.register(OrderTour)
admin.site.register(Hotel)
admin.site.register(OrderHotel)
admin.site.register(Hotelcheckout)
admin.site.register(Checkoutenquiry)
admin.site.register(VendorRequest)
admin.site.register(Payment)
