from datetime import timedelta #Para funcion calendario
from odoo import models, fields, api, exceptions, _


class Session(models.Model):
    _name = 'infinity_dp.session'
    _description="Tabla sesion"

    name = fields.Char(required=True)
    #start_date = fields.Date()
    start_date=fields.Date(default=fields.Date.today)#Me muestra el dia de hoy
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active=fields.Boolean(default=True) #Campos por defecto
    color=fields.Integer()

    #relacion Many2one
    instructor_id = fields.Many2one('res.partner', string="Instructor", 
    #domain=[('instructor','=',True)]) #consulta solo los que son instructores
    domain=['|',('instructor','=',True), ('category_id.name','ilike',"Teacher")])
    course_id = fields.Many2one('infinity_dp.prueba1',
        ondelete='cascade', string="Curso", required=True)
    #Many2Many
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    #Campo Calculado
    taken_seats = fields.Float(string="Asientos tomados", compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=True,
        compute='_get_end_date', inverse='_set_end_date')

    #vista grafica
    attendees_count = fields.Integer(
        string="Attendees count", compute='_get_attendees_count', store=True)
    

    @api.depends('seats','attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
    
    
    @api.onchange('seats','attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                },
            }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but:
            #  Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be an attendee"))