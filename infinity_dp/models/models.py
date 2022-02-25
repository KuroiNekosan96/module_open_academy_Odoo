##PONER EN DIFERENTES ARCHIVOS - 

# -*- coding: utf-8 -*-

#from typing_extensions import Required
from datetime import timedelta #Para funcion calendario
from odoo import models, fields, api, exceptions, _


#Defino mis clases segun la base de datos

#Tabla 1
class prueba1(models.Model):
    _name = 'infinity_dp.prueba1' #nombremodulo.nombredelaclase
    _description= "Permite definir caracteristicas de la prueba1"

    name=fields.Char(string="Title", Required=True) #definir a identificar con un objeto cuando está relacionado con otras tablas
    
    description=fields.Text()#
    #relacion Many2One
    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    #one2Many
    session_ids=fields.One2many('infinity_dp.session','course_id',string="Sessions")
    
    
   
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)
        default['name'] = new_name
        return super(prueba1, self).copy(default)
    
    
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

#Tabla 2
