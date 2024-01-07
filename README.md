# Django Project: Restaurant Management System

## Overview

This Django project is a restaurant management system designed to handle table bookings and menu management through APIs. It consists of various views, including API endpoints for handling menu items and table bookings.

## URLs Configuration

### `project urls.py`

- URL configuration for the `littlelemon` project.
- `urlpatterns` list routes URLs to views, including:
  - Admin URLs (`/admin/`)
  - Restaurant app URLs (`/restaurant/`)
  - Authentication URLs (`/auth/`)

### `app urls.py`

- URL configuration for the `restaurant` app, including:
  - Index and home views (`/`, `/home/`)
  - API endpoints for menu items (`/menu/items/`, `/menu/items/<int:pk>/`)
  - API authentication endpoint (`/api-token-auth/`)

## Views and Endpoints

### `views.py`

- `index(request)`: Renders the index.html template.
- `home(request)`: Renders the index.html template.
- `MenuItemsView`: API endpoint for listing and creating menu items.
- `SingleMenuItemView`: API endpoint for retrieving, updating, and deleting individual menu items.
- `BookingViewSet`: API endpoint for handling table bookings with CRUD functionality.

### Permissions

- `IsAuthenticated`: Permission class used to secure the `BookingViewSet`.

## Files Structure

- `views.py`: Contains view functions and API endpoints.
- `project urls.py`: Configuration for project-level URLs.
- `app urls.py`: Configuration for app-specific URLs.
- Templates: HTML templates (e.g., `index.html`).

## Usage
- Access various endpoints and views:
   - Admin: `/admin/`
   - Restaurant app: `/restaurant/`
   - API endpoints: `/restaurant/booking/`, `/restaurant/menu/`
   - Authentication: `/auth/`
