"""
shipment_tracker/urls.py

URL routing for the shipment_tracker application.
"""
from django.urls import path
from .views import NewShipment

# ===============================================================
# shipment_tracker/urls.py
# Author: Leopoldo Mendoza
# Alias: Lerocko
# Last modified: 9th January 2026
# Version: 1.0
# Refactoring date: --/--/----
# Description: 
#   URL routing for the shipment_tracker application.
# ===============================================================


urlpatterns = [
    path("new/", NewShipment.as_view(), name="shipment-new"),
]
