from django.db import models
import uuid
from django.conf import settings
User = settings.AUTH_USER_MODEL
from account.models import UserData

class Category(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "categories"

class Template(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="templates", on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=10, decimal_places=8)
    price = models.DecimalField(max_digits=10, decimal_places=8)
    source_code = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "templates"

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    template = models.OneToOneField(Template, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "wishlist"
    
STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

class Event(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(UserData, on_delete=models.CASCADE, default=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    market_status = models.CharField(max_length=255)
    description = models.TextField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    is_custom_template = models.BooleanField(default=True)
    guests = models.IntegerField(default=True)
    tbd = models.BooleanField(default=True)
    start_date = models.DateField(default=True)
    end_date = models.DateField(default=True)
    start_time = models.TimeField(default=True)
    end_time = models.TimeField(default=True)
    timezone = models.CharField(max_length=30, default=True)
    address = models.CharField(max_length=255, default=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, default=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, default=True)
    status = models.CharField(max_length=255, choices= STATUS_CHOICES, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "events"
    
class EventAttachment(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = "attachments"

class CustomTemplate(models.Model):
    forkey = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    forkey = models.ForeignKey(Template, on_delete=models.CASCADE, default=None)
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    headline_font_size = models.CharField(max_length=255)
    sub_headline = models.CharField(max_length=255)
    sub_headline_font_size = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    venue_name = models.CharField(max_length=255)
    text_under_barcode = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'custom_templates'

class EventInvitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=255)
    ticket_no = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255)
    checkin = models.DateTimeField(null=True, blank=True)
    checkout = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=255)
    actioned_datetime = models.DateTimeField(null=True, blank=True)
    coupon_id = models.IntegerField(null=True, blank=True)  # Assuming this is an integer
    coupon_discount = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invitations"

ZONES_CHOICES = (
    ("Checkin", "Checkin"),
    ("Checkout", "Checkout"),
    ("Both", "Both")
)

class EventZones(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    type = models.CharField(max_length=50, choices=ZONES_CHOICES)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'zones'


TICKETS_CHOICES = (
    ("Gold", "Gold"),
    ("Silver", "Silver"),
    ("Maroon", "Maroon"),
    ("VIP", "VIP")
)

import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
TICKETS_ENTERIES = (
    ('Single','Single'),
    ('Multiple', 'Multiple'),
    ('Open', 'Open')
)
class EventTickets(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description  = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=8)
    discount = models.DecimalField(max_digits=10, decimal_places=8)
    quantity = models.IntegerField()
    type = models.CharField(max_length=255, choices=TICKETS_CHOICES)
    date = models.DateField()
    timezone = models.CharField(max_length=255, choices=TIMEZONES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    no_of_enteries = models.CharField(max_length=255, choices=TICKETS_ENTERIES)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tickets'

class TicketZones(models.Model):
    ticket = models.ForeignKey(EventTickets, on_delete=models.CASCADE)
    zone = models.ForeignKey(EventZones, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ticket_zones'

DISCOUNT_TYPES = (
    ('Fixed', 'Fixed'),
    ('Percentage', 'Percentage')
)

class EventCoupons(models.Model):
        event = models.ForeignKey(Event, on_delete=models.CASCADE)
        name = models.CharField(max_length=25)
        code = models.CharField(max_length=255)
        discount_type = models.CharField(max_length=255, choices=DISCOUNT_TYPES)
        discount = models.DecimalField(max_digits=10, decimal_places=8)
        no_of_usage = models.IntegerField() 
        ticket_type = models.CharField(max_length=255, choices=TICKETS_CHOICES)
        start_date = models.DateField()
        end_date = models.DateField()
        timezone = models.CharField(max_length=255, choices=TIMEZONES)
        start_time = models.TimeField()
        end_time = models.TimeField()
        until_sold_out = models.BooleanField(default=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        class Meta:
            db_table = 'event_coupouns'


class CouponZones(models.Model):
    coupon = models.ForeignKey(EventCoupons, on_delete=models.CASCADE)
    zone = models.ForeignKey(EventZones, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'coupon_zones'