# -- coding: utf-8 --
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.
import requests

from odoo import models, fields, api, exceptions, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def attendance_fetch(self, next_action, entered_pin=False, location=False):
        res = super(HrEmployee, self.with_context(attendance_location=location)).attendance_manual(next_action,
                                                                                                   entered_pin)
        return res

    def _attendance_action_change(self):
        res = super()._attendance_action_change()
        location = self.env.context.get('attendance_location', False)
        if location:
            if self.attendance_state == 'checked_in':
                addr = requests.get(
                    "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=" + str(
                        location[0]) + "&longitude=" + str(location[1])).json()
                check_in_city = addr.get('city')
                check_in_region = addr.get('principalSubdivision')
                check_in_country = addr.get('countryName')
                check_in_location = check_in_city, check_in_region, check_in_country

                res.update({
                    "check_in_latitude": location[0],
                    "check_in_longitude": location[1],
                    "check_in_location": check_in_location
                })
            else:
                addr = requests.get(
                    "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=" + str(
                        location[0]) + "&longitude=" + str(location[1])).json()
                check_out_city = addr.get('city')
                check_out_region = addr.get('principalSubdivision')
                check_out_country = addr.get('countryName')
                check_out_location = check_out_city, check_out_region, check_out_country
                res.update({
                    "check_out_latitude": location[0],
                    "check_out_longitude": location[1],
                    "check_out_location": check_out_location
                })
        return res
