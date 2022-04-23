# -- coding: utf-8 --
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import models, fields, api, exceptions, _
#import httpagentparser
from odoo.http import request


try:
    import httpagentparser
except ImportError:
    raise ImportError(
        'This module needs httpagentparser. Please install httpagentparser on your system. (sudo pip3 install httpagentparser)')

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    check_in_latitude = fields.Char(string='Check in Latitude')
    check_in_longitude = fields.Char(string='Check in Longitude')
    check_out_latitude = fields.Char(string='Check out Latitude')
    check_out_longitude = fields.Char(string='Check out Longitude')
    check_in_source = fields.Char(string='Check in Source')
    check_out_source = fields.Char(string='Check out Source')
    check_in_location = fields.Char(string='Check in Location')
    check_out_location = fields.Char(string='Check out Location')

    @api.constrains('check_in', 'check_out', 'employee_id')
    def _check_validity(self):
        hr_attendance = super(HrAttendance, self)._check_validity()
        for attendance in self:
            if not attendance.check_out:
                agent = request.httprequest.environ.get('HTTP_USER_AGENT', '')
                browser = httpagentparser.detect(agent)
                if not browser:
                    browser = agent.split('/')[0]
                else:
                    browser_name = browser['browser']['name']
                    browser_version = browser['browser']['version']
                    platform = browser['platform']['name']

                    self.check_in_source = browser_name, str(browser_version), platform

            else:
                agent = request.httprequest.environ.get('HTTP_USER_AGENT', '')
                browser = httpagentparser.detect(agent)
                if not browser:
                    browser = agent.split('/')[0]
                else:
                    browser_name = browser['browser']['name']
                    browser_version = browser['browser']['version']
                    platform = browser['platform']['name']

                    self.check_out_source = browser_name, str(browser_version), platform
                return browser
        return hr_attendance

    def check_in_map_button(self):
        url = "http://maps.google.com/maps/@" + str(self.check_in_latitude) + ',' + str(self.check_in_longitude)

        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url
        }

    def check_out_map_button(self):
        url = "http://maps.google.com/maps/@" + str(self.check_out_latitude) + ',' + str(self.check_out_longitude)

        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url
        }
