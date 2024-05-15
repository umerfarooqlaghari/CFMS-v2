from django.contrib import admin
from .models import User, UserProfile, Booking, Order, Port, CargoType, FAQ
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')


class CustomUserAdmin(AuthUserAdmin):  
    list_display = ['username', 'active_status']
    list_filter = [ 'active_status']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('active_status',)}),
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_date', 'booking_id', 'pick_up_location', 'destination', 'cargo_type_name', 'weight', 'booking_email_id', 'booking_phone')
    list_filter = ('booking_date', 'pick_up_location', 'destination', 'cargo_type_name')
    search_fields = ('booking_id', 'user__email', 'booking_email_id__email')

    def save_model(self, request, obj, form, change):
        obj.cost = obj.calculate_booking_cost()
        super().save_model(request, obj, form, change)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('cargo_type', 'start_port', 'end_port', 'distance', 'departure_date', 'cost', 'arrival_date', 'status')
    list_filter = ('cargo_type', 'start_port', 'end_port', 'status')
    search_fields = ('start_port__name', 'end_port__name')


class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo_type_name')


class PortAdmin(admin.ModelAdmin):
    list_display = ('id', 'port_name', 'availability')
    list_filter = ('availability',)
    search_fields = ('port_name',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'query_date_display')
    search_fields = ('question', 'answer')

    def query_date_display(self, obj):
        return obj.query_date

    query_date_display.short_description = 'Query Date'


class CostCalculationAdmin(admin.ModelAdmin):
    list_display = ('weight', 'shipment_cost', 'tax', 'cargo_type')
    list_filter = ('cargo_type',)
    search_fields = ('weight', 'cargo_type__name')


admin.site.register(User, CustomUserAdmin)  # Register the modified admin class
admin.site.register(UserProfile)
admin.site.register(CargoType)
admin.site.register(Order)  # Assuming TrackAdmin is meant for Order
admin.site.register(Port)
admin.site.register(FAQ)
admin.site.register(Booking)
