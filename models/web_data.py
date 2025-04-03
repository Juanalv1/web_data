from odoo import fields, models, api 
import logging
_logger = logging.getLogger(__name__)

class WebData(models.Model):
    _inherit = ['mail.activity.mixin', 'mail.thread']
    _name = 'web.data'

    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellido")
    birth_date = fields.Date(string="Fecha de nacimiento")
    
    @api.model
    def create(self, vals):
        # Llamar al super para crear el registro
        record = super().create(vals)

        # Usamos el metodo message_post para postear un nuevo mensaje
        record.message_post(
            body=f"Nuevo usuario creado por: {self.env.user.name}",
            subject="Usuario Creado",
            message_type="notification",
            subtype_xmlid="mail.mt_note"  # Notificación en el chatter
        )

        return record
    
    @api.model
    def clear_board(self):
        """ Método para eliminar todos los registros del tablón periódicamente.
        """
        self.env['mail.message'].search([('model', '=', 'web.data')]).unlink()  # Borra mensajes relacionados con el modelo web.data
