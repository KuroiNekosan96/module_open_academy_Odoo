#from email.policy import default
from odoo import models, fields, api,_

class Wizard(models.TransientModel):
    _name = 'infinity_dp.wizard'
    
    def _default_session(self):
        return self.env['infinity_dp.session'].browse(self._context.get('active_id'))


    session_ids = fields.Many2one('infinity_dp.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        #self.session_id.attendee_ids |= self.attendee_ids
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}