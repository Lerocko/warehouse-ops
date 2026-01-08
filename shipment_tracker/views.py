from django.views import View
from django.shortcuts import redirect
from django.urls import reverse

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
        return redirect(reverse("shipment-new"))
