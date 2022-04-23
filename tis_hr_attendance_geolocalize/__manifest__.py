# -- coding: utf-8 --
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

{
    'name': 'HR Attendance Geolocalize',
    'version': '15.0.0.0',
    'category': 'Human Resources/Attendances',
    'sequence': 1,
    'summary': 'Track employee attendance',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'price': 20,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'description': "This module aims to manage employee's attendances and track location",
    'depends': ['hr_attendance', 'base_geolocalize'],
    'data': [
        'views/hr_attendance_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tis_hr_attendance_geolocalize/static/js/geo_location_finder.js',
            'tis_hr_attendance_geolocalize/static/js/kiosk_mode_geo_location.js',
        ],
    },
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
