# Warehouse Ops

Warehouse Ops is a Django-based internal tool for tracking shipments using photos as the primary source of truth.

A shipment is created when the first photo is taken. Additional shipment details such as order number, carrier, and tracking number can be added later.

## Features

- Create shipment records automatically from uploaded photos
- Store multiple photos per shipment
- Optional tracking information (carrier, tracking number)
- Audit fields for creation and modification
- Clean separation of apps and media files

## Tech Stack

- Python 3
- Django
- SQLite (development)
- Git & GitHub

## Project Structure

warehouse_ops/
│
├── shipment_tracker/ # Shipment tracking app
├── warehouse_ops/ # Project configuration
├── media/ # Uploaded media files (ignored by git)
├── manage.py
└── README.md

## Development Setup

1. Create and activate virtual environment
2. Install dependencies
3. Configure environment variables
4. Run migrations
5. Start development server

## Status

🚧 Work in progress – early development stage.
