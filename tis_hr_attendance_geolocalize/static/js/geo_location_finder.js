odoo.define('tis_hr_attendance_geolocalize.geo_location_finder', function (require) {
    "use strict";

    const attendance = require('hr_attendance.my_attendances');
    attendance.include({
        update_attendance(){
            var self = this;
            var options = {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            };
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(self.attendance_fetch.bind(self), self._getPositionError, options);
            }
        },
        attendance_fetch(position){
            var self = this;
            var emp_latitude = position.coords.latitude;
            var emp_longitude = position.coords.longitude;
            this._rpc({
                model: 'hr.employee',
                method: 'attendance_fetch',
                args: [[self.employee.id], 'hr_attendance.hr_attendance_action_my_attendances', null, [emp_latitude, emp_longitude]],
            })
            .then(function(result) {
                if (result.action) {
                    self.do_action(result.action);
                } else if (result.warning) {
                    self.do_warn(result.warning);
                }
            });
        },
        _getPositionError(err) {
            alert("Can't fetch location...Try again!!!")
        },
    });

});
