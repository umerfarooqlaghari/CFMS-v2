# models.py
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import pgtrigger
from django.contrib.auth.models import User as AuthUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    active_status = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='user_set_project_app')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_set_permission')
    
    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    cell_phone = models.CharField(max_length=15, default='Null')
    address = models.TextField(default='Null')

class Port(models.Model):
    name = models.CharField(max_length=255)
    availability = models.BooleanField()
    
    def __str__(self):
        return self.name

class CargoType(models.Model):
    cargo_CHOICES = [
        ('Shipper', 'SHIPPER'),
        ('Warehousing', 'WAREHOUSING'),
        ('Accessorial', 'ACCESSORIAL'),
        ('Blind shipment', 'BLIND SHIPMENT'),
        ('Embargo', 'EMBARGO'),
    ]
    cargo_type_name = models.CharField(
        max_length=20,
        choices=cargo_CHOICES,
        default='none told',
    )
    
    def __str__(self):
        return self.cargo_type_name

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    booking_date = models.DateField()
    pick_up_location = models.ForeignKey(Port, related_name='pick_up_port', on_delete=models.CASCADE, default=None)
    destination = models.ForeignKey(Port, related_name='delivery_port', on_delete=models.CASCADE, default=None)
    cargo_type_name = models.ForeignKey(CargoType, on_delete=models.CASCADE)
    weight = models.FloatField()
    booking_email_id = models.EmailField()
    booking_phone = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Booking"
    
    def calculate_booking_cost(self):
        weight = self.weight
        tax = 17
        base_shipment_cost = 2000

        doubled_weight = weight * 5
        doubled_tax = tax / 10
        cost1 = doubled_weight + base_shipment_cost
        cost = (cost1 * doubled_tax) + cost1
        return cost    
    
    def save(self, *args, **kwargs):
        # Calculate and set the cost before saving the booking
        self.cost = self.calculate_booking_cost()
        super().save(*args, **kwargs)

class FAQ(models.Model):
    query_Date = models.DateField(auto_now_add=True)
    query = models.TextField()
    user_name = models.CharField(blank=True, null=True, max_length=255)
    user_email = models.EmailField(blank=True, null=True)

class Order(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('IN_TRANSIT', 'In transit'),
        ('DELIVERED', 'Delivered'),
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='IN_TRANSIT',
    )
    expected_arrival_date = models.DateTimeField(default=timezone.now() + timedelta(days=40))

@pgtrigger.register(pgtrigger.Protect(name='user_log_insert_trigger', operation=pgtrigger.Insert))
@pgtrigger.register(pgtrigger.Protect(name='user_log_update_trigger', operation=pgtrigger.Update))
@pgtrigger.register(pgtrigger.Protect(name='user_log_delete_trigger', operation=pgtrigger.Delete))
class UserLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_user_log(sender, instance, created, **kwargs):
    if created:
        UserLog.objects.create(user=instance)

@receiver(pre_delete, sender=User)
def delete_user_log(sender, instance, **kwargs):
    UserLog.objects.filter(user=instance).delete()

@pgtrigger.register(pgtrigger.Protect(name='booking_log_insert_trigger', operation=pgtrigger.Insert))
@pgtrigger.register(pgtrigger.Protect(name='booking_log_update_trigger', operation=pgtrigger.Update))
@pgtrigger.register(pgtrigger.Protect(name='booking_log_delete_trigger', operation=pgtrigger.Delete))
class BookingLog(models.Model):
    booking_order_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Booking)
def create_booking_log(sender, instance, created, **kwargs):
    if created:
        BookingLog.objects.create(booking_order_id=instance)

@receiver(pre_delete, sender=Booking)
def delete_booking_log(sender, instance, **kwargs):
    BookingLog.objects.filter(booking_order_id=instance).delete()




class PortLog(models.Model):
    Port_id = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    operation_type = models.CharField(default=None ,max_length=10)  # Add a field to store the operation type

# Define triggers to log changes to the Port model
@pgtrigger.register(
    pgtrigger.Protect(name='Port_log_insert_trigger', operation=pgtrigger.Insert),
    pgtrigger.Protect(name='Port_log_update_trigger', operation=pgtrigger.Update),
    pgtrigger.Protect(name='Port_log_delete_trigger', operation=pgtrigger.Delete),
)
class PortLog(models.Model):
    Port_id = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    operation_type = models.CharField(default=None,max_length=10)  # Add a field to store the operation type

# Signal to create PortLog entry when a Port is saved
@receiver(post_save, sender=Port)
def create_Portlog(sender, instance, created, **kwargs):
    if created:
        PortLog.objects.create(Port_id=instance, operation_type='CREATE')
    else:
        PortLog.objects.create(Port_id=instance, operation_type='UPDATE')

# Signal to delete PortLog entry when a Port is deleted
def delete_Portlog(sender, instance, **kwargs):

    port_log_entry = PortLog.objects.get(Port_id=instance)
    port_log_entry.operation_type = 'DELETE'
    port_log_entry.save()


