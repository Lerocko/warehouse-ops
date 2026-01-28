from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Shipment
import uuid

# ===============================================================
# shipment_traker/views.py
# Author: Leopoldo Mendoza
# Alias: Lerocko
# Last modified: 8th January 2026
# Version: 1.0
# Refactoring date: --/--/----
# Description: 
#   View layer for the Shipment Tracker application.
#   This module contains class-based views responsible for
#   handling user navigation and request flow.
# ===============================================================


# ================================================================
# NewShipment view
# ================================================================
class NewShipment(View):
    """
    Entry-point view for creating a new shipment.

    This view does not create database records directly.
    Its sole responsibility is to handle the initial GET request
    triggered by the "New Shipment" action and redirect the user
    to the shipment photo upload flow.

    HTTP Methods:
        GET:
            Redirects the user to the shipment photo upload view.
    """
    
    def get(self, request):
        """
        Handle GET requests.

        Redirects the user to the shipment photo upload view,
        where the shipment creation process begins.

        Args:
            request (HttpRequest): Incoming HTTP request.

        Returns:
            HttpResponseRedirect: Redirect response to the photo upload URL.
        """
        # return redirect(reverse("shipment-new"))
        return render(request, "shipment_tracker/new_shipment.html")
    
    def post(self, request):
        """
        Handle POST requests.

        Redirects the user to the shipment photo upload view,
        where the shipment creation process begins.

        Args:
            request (HttpRequest): Incoming HTTP request.

        Returns:
            HttpResponseRedirect: Redirect response to the photo upload URL.
        """
        shipment = Shipment.objects.create(order_number=str(uuid.uuid4()))
        return redirect(reverse("shipment-photo-upload", args=[shipment.id]))
    
# ================================================================
# ShipmentPhotoUpload view
# ================================================================
class ShipmentPhotoUpload(View):
    """
    View for handling shipment photo uploads.

    This view manages the upload of photos associated with a shipment.
    It handles both displaying the upload form and processing the uploaded files.

    HTTP Methods:
        GET:
            Renders the photo upload form.
        POST:
            Processes the uploaded photos and associates them with the shipment.
    """

    def get(self, request, shipment_id):
        """
        Handle GET requests.

        Renders the photo upload form for the specified shipment.

        Args:
            request (HttpRequest): Incoming HTTP request.
            shipment_id (int): ID of the shipment to which photos will be uploaded.

        Returns:
            HttpResponse: Rendered photo upload form.
        """
        shipment = Shipment.objects.get(id=shipment_id)
        return render(request, "shipment_tracker/photo_upload.html", {"shipment": shipment})
    
    def post(self, request, shipment_id):
        """
        Handle POST requests.

        Processes the uploaded photos and associates them with the specified shipment.

        Args:
            request (HttpRequest): Incoming HTTP request.
            shipment_id (int): ID of the shipment to which photos will be uploaded.

        Returns:
            HttpResponseRedirect: Redirect response to the shipment detail view after successful upload.
        """
        return redirect(reverse("shipment-new"))
