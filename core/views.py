"""
Views for core app
"""
from django.shortcuts import render


def index(request):
    """Home page view"""
    context = {
        'page_title': 'D-DUMES SHELTER LIMITED - Affordable Housing Solutions',
        'page_description': 'D-DUMES SHELTER LIMITED - Transforming Dreams into Reality. Leading Nigerian affordable housing development company. RC: 943183',
        'project_name': 'D-Dumes',
        'scripts': [
            'js/validation-booking.js',
            'js/swiper.js',
            'js/custom-swiper-2.js',
        ],
        'gallery_images': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
    }
    return render(request, 'index.html', context)


def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us - D-DUMES SHELTER LIMITED',
        'page_description': 'About D-DUMES SHELTER LIMITED - Leading Nigerian affordable housing development company. Established 2011. RC: 943183',
    }
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    context = {
        'page_title': 'Services - D-DUMES SHELTER LIMITED',
        'page_description': 'D-DUMES SHELTER LIMITED Services - Real Estate Development, Affordable Housing Solutions, Project Management',
    }
    return render(request, 'services.html', context)


def projects(request):
    """Projects page view"""
    context = {
        'page_title': 'Projects - D-DUMES SHELTER LIMITED',
        'page_description': 'D-DUMES SHELTER LIMITED Projects - Featured Housing Developments, Community Initiatives, Recent Completions',
    }
    return render(request, 'projects.html', context)


def contact(request):
    """Contact page view"""
    context = {
        'page_title': 'Contact Us - D-DUMES SHELTER LIMITED',
        'page_description': 'Contact D-DUMES SHELTER LIMITED - Suite B11, Dansariri Plaza, Zone 4, Abuja. Phone: +234 803 314 9954',
        'scripts': [
            'js/validation-booking.js',
        ]
    }
    return render(request, 'contact.html', context)


def amenities(request):
    """Amenities page view (Maitama Luxury Estate)"""
    context = {
        'page_title': 'Maitama Luxury Estate - Premium Amenities',
        'page_description': 'Maitama Luxury Estate - Premium Amenities & World-Class Facilities',
    }
    return render(request, 'amenities.html', context)


def housing_types(request):
    """Housing types page view"""
    context = {
        'page_title': 'Housing Types - D-DUMES SHELTER LIMITED',
        'page_description': 'Explore Our Diverse Property Categories - Duplex, Terraces, Semi-Detached, Detached Bungalows',
    }
    return render(request, 'housing_types.html', context)


def housing_types_3_cols(request):
    """Housing types 3 columns page view"""
    context = {
        'page_title': 'Housing Types - D-DUMES SHELTER LIMITED',
        'page_description': 'Explore Our Diverse Property Categories',
    }
    return render(request, 'housing_types_3_cols.html', context)


# Project detail pages
def luxury_service_apartment(request):
    """Luxury Service Apartment project page"""
    context = {
        'page_title': 'Luxury Service Apartment - D-DUMES SHELTER LIMITED',
        'page_description': 'Luxury Service Apartment - Fully Serviced Apartments in Garki, Abuja',
        'project_name': 'Luxury Service Apartment',
    }
    return render(request, 'projects/luxury_service_apartment.html', context)


def wuse_housing_scheme(request):
    """Wuse Housing Scheme project page"""
    context = {
        'page_title': 'Wuse Housing Scheme - D-DUMES SHELTER LIMITED',
        'page_description': 'Wuse Housing Scheme - Affordable Housing in Wuse Zone 4, Abuja',
        'project_name': 'Wuse Housing Scheme',
    }
    return render(request, 'projects/wuse_housing_scheme.html', context)


def maitama_luxury_estate(request):
    """Maitama Luxury Estate project page"""
    context = {
        'page_title': 'Maitama Luxury Estate - D-DUMES SHELTER LIMITED',
        'page_description': 'Maitama Luxury Estate - Premium Living in Maitama, Abuja',
        'project_name': 'Maitama Luxury Estate',
        'scripts': [
            'js/validation-booking.js',
            'js/swiper.js',
            'js/custom-swiper-2.js',
        ],
    }
    return render(request, 'projects/maitama_luxury_estate.html', context)

