# -*- coding: utf-8 -*-

from odoo import models, fields, api

'''
class Course(models.Model): #modelo
    _name='openacademy.course' #nombre de modelo
    #Campos
    name=fields.Char(string="Titulo", required=True)
    description=fields.Text()
'''

class Dietfacts_product_template(models.Model):
    #datos del modelo
    _name='product_template'
    _inherit ='product_template'

    #campos
    calories=fields.Integer("Calories")
    