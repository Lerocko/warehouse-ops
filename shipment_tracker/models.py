from django.db import models

# ===============================================================
# shipment_traker/models.py
# Author: Leopoldo Mendoza
# Alias: Lerocko
# Last modified: 3rd January 2026
# Version: 1.0
# Refactoring date: --/--/----
# Description: 
#   Data models for shipment tracking.
#   A shipment is created when the first photo is taken.
#   Each shipment can have one or more associated photos.
# ================================================================

CARRIER_CHOICES = [
    ("NZC", "New Zealand Couriers"),
    ("P.Haste", "Post Haste"),
    ("FWM", "Mainfreight"),
    ("DHL", "DHL"),
]

# ================================================================
# Shipment model
# ================================================================
class Shipment(models.Model):
    """
    Represents a shipment order.

    A Shipment record is created at the moment the first photo is taken.
    Tracking details may be added later.

    Fields:
        id (AutoField):
            Primary key.

        order_number (CharField):
            Unique order identifier.

        tracking_number (CharField):
            Carrier tracking number. Optional at creation time.

        carrier (CharField):
            Shipping carrier company. Optional at creation time.
        
        notes (TextField):
            Optional free-text notes.

        created_at (DateTimeField):
            Timestamp when the shipment was created.

        last_modified_at (DateTimeField):
            Timestamp of the last modification.

        created_by (CharField):
            User who created the shipment record.

        modified_by (CharField):
            User who last modified the shipment.
    """
    order_number = models.CharField(max_length=10, unique=True)
    tracking_number = models.CharField(max_length=25, blank=True, null=True)
    carrier = models.CharField(max_length=25, choices=CARRIER_CHOICES, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=25)
    modified_by = models.CharField(max_length=25)

    def __str__(self):
        return f"Shipment {self.order_number}"
    
# ================================================================
# ShipmentPhotos model
# ================================================================
class ShipmentPhoto(models.Model):
    """
    Stores photos associated with a shipment.

    Relationship:
        One Shipment -> Many ShipmentPhoto records.

    Fields:
        id (AutoField):
            Primary key.

        shipment (ForeignKey):
            Related shipment order.

        photo (ImageField):
            Uploaded shipment image.

        uploaded_at (DateTimeField):
            Timestamp when the photo was uploaded.

        uploaded_by (CharField):
            User who uploaded the photo.
    """
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="shipment_photos")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=25)

    def __str__(self):
        return f"Photo for order {self.shipment.order_number}"