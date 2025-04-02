from odoo import fields, models 

class WebData(models.Model):
    _name = 'web.data'

    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento")
    