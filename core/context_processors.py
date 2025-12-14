"""
Context processors for site-wide data
"""
from django.conf import settings


def site_data(request):
    """
    Provides site-wide data to all templates
    """
    return {
        'site': {
            'title': settings.SITE_TITLE,
            'tagline': settings.SITE_TAGLINE,
            'description': settings.SITE_DESCRIPTION,
            'url': settings.SITE_URL,
        },
        'company': {
            'name': 'D-DUMES SHELTER LIMITED',
            'registration': 'RC: 943183',
            'established': 2011,
            'tagline': 'TRANSFORMING DREAMS INTO REALITY',
            'headquarters': 'Abuja, Nigeria',
            'vision': 'To be the leading provider of affordable, sustainable housing solutions in Nigeria, transforming communities and improving the quality of life for millions',
            'mission': 'To deliver high-quality, low-cost housing solutions that cater to the needs of low- and middle-income families. Through innovative design, sustainable construction practices, and strategic partnerships, we aim to bridge Nigeria\'s housing deficit while creating inclusive communities that thrive. We are committed to excellence, integrity, and social responsibility in every project we undertake',
            'core_values': [
                {
                    'name': 'Integrity & Transparency',
                    'description': 'We uphold the highest ethical standards in all our operations. Transparency, honesty, and accountability are the cornerstones of our relationships with clients, partners, and communities.'
                },
                {
                    'name': 'Quality & Affordability',
                    'description': 'Excellence is non-negotiable. From design to construction, we ensure that every home we build meets the highest standards of durability, functionality, and aesthetic appeal, providing lasting value to our residents.'
                },
                {
                    'name': 'Innovation & Sustainability',
                    'description': 'We embrace cutting-edge technologies and creative solutions to deliver affordable, sustainable, and high-quality housing; improving our processes and addressing the evolving client needs.'
                },
                {
                    'name': 'Community Focus',
                    'description': 'At the core of D-Dumes Shelter\'s mission is a steadfast commitment to making homeownership accessible and affordable for all Nigerians, creating vibrant, inclusive communities.'
                }
            ],
            'statistics': {
                'housing_units': 500,
                'communities': 25,
                'years_experience': 14,
                'active_projects': 10,
                'states_covered': 8,
            }
        },
        'contact': {
            'address': 'Suite B11, Dansariri Plaza, Zone 4, Abuja, Nigeria',
            'phone': {
                'primary': '+234 803 314 9954',
                'secondary': '+234 803 420 9387',
            },
            'email': 'ddumesshelterltd@gmail.com',
            'registration': 'RC: 943183',
            'established': 2011,
            'social': {
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'youtube': '#',
                'whatsapp': '#',
            }
        },
        'navigation': {
            'main': [
                {'title': 'Home', 'url': '/'},
                {'title': 'Services', 'url': '/services/'},
                {'title': 'Projects', 'url': '/projects/'},
                {'title': 'Contact', 'url': '/contact/'},
                {'title': 'About', 'url': '/about/'},
            ],
            'footer': [
                {'title': 'About Us', 'url': '/about/'},
                {'title': 'Our Services', 'url': '/services/'},
                {'title': 'Projects', 'url': '/projects/'},
                {'title': 'Contact', 'url': '/contact/'},
            ]
        },
        'navigation_projects': {
            'projects': [
                {
                    'name': 'D-Dumes',
                    'url': '/',
                    'page': 'index.html',
                    'image': 'images/demo/homepage-1.webp',
                    'is_home': True,
                },
                {
                    'name': 'Luxury Service Apartment',
                    'url': '/projects/luxury-service-apartment/',
                    'page': '01_single-property-3.html',
                    'image': 'images/demo/homepage-6.webp',
                },
                {
                    'name': 'Wuse Housing Scheme',
                    'url': '/projects/wuse-housing-scheme/',
                    'page': '02_apartment-homepage-2.html',
                    'image': 'images/demo/homepage-5.webp',
                },
                {
                    'name': 'Maitama Luxury Estate',
                    'url': '/projects/maitama-luxury-estate/',
                    'page': '03_apartment-rent-onepage.html',
                    'image': 'images/demo/homepage-6.webp',
                },
            ]
        },
        'projects': {
            'featured': [
                {
                    'title': 'Kado Project - Affordable Housing Estate',
                    'location': 'Kado District, Abuja, FCT',
                    'type': 'Featured Project',
                    'status': 'Completed',
                    'units': 120,
                    'description': 'A landmark affordable housing project in Kado District, Abuja, providing quality 2-4 bedroom homes for middle-income families. Features modern amenities, 24/7 security, and proximity to schools and markets.',
                    'image': 'images/news/s1.webp',
                    'date': '28',
                    'price_range': '₦8M - ₦15M',
                },
                {
                    'title': 'Asokoro Estate - Luxury Residential Complex',
                    'location': 'Asokoro District, Abuja, FCT',
                    'type': 'Urban Development',
                    'status': 'Completed',
                    'units': 85,
                    'description': 'Premium luxury residential complex in the prestigious Asokoro District. Features 4-5 bedroom duplexes, world-class amenities, and exclusive gated community living.',
                    'image': 'images/news/s2.webp',
                    'date': '26',
                    'price_range': '₦45M - ₦85M',
                },
                {
                    'title': 'Luxury Service Apartment - Garki',
                    'location': 'Garki District, Abuja, FCT',
                    'type': 'Service Apartment',
                    'status': 'Completed',
                    'units': 60,
                    'description': 'Fully serviced luxury apartments in Garki District, ideal for professionals and expatriates. Features include housekeeping, concierge services, and premium facilities.',
                    'image': 'images/news/s3.webp',
                    'date': '24',
                    'price_range': '₦2.5M - ₦4.5M per year',
                },
                {
                    'title': 'Garki Residential Complex - Phase 2',
                    'location': 'Garki District, Abuja, FCT',
                    'type': 'Residential Complex',
                    'status': 'In Progress',
                    'units': 200,
                    'description': 'Modern residential complex in Garki District featuring 3-4 bedroom terraces and semi-detached homes. Phase 2 expansion with enhanced community facilities.',
                    'image': 'images/news/s4.webp',
                    'date': '22',
                    'price_range': '₦12M - ₦25M',
                },
                {
                    'title': 'Wuse Housing Scheme - Affordable Units',
                    'location': 'Wuse Zone 4, Abuja, FCT',
                    'type': 'Housing Scheme',
                    'status': 'Completed',
                    'units': 150,
                    'description': 'Affordable housing scheme in Wuse Zone 4, providing quality 2-3 bedroom homes for low and middle-income families. Strategic location with easy access to city center.',
                    'image': 'images/news/s5.webp',
                    'date': '20',
                    'price_range': '₦6M - ₦12M',
                },
                {
                    'title': 'Maitama Luxury Estate - Premium Living',
                    'location': 'Maitama District, Abuja, FCT',
                    'type': 'Luxury Estate',
                    'status': 'Completed',
                    'units': 45,
                    'description': 'Exclusive luxury estate in Maitama, Abuja\'s most prestigious district. Features 5-6 bedroom mansions, Olympic-sized pool, tennis courts, and 24/7 security.',
                    'image': 'images/news/s6.webp',
                    'date': '18',
                    'price_range': '₦120M - ₦250M',
                },
            ]
        },
        'location': {
            'country': 'Nigeria',
            'city': 'Abuja',
            'address': 'Suite B11, Dansariri Plaza, Zone 4',
            'region': 'Federal Capital Territory',
        }
    }

