from odoo import http

class FormController(http.Controller):

    # CREATE  || Ruta para crear nuevos usuarios
    @http.route('/usuarios', type="http", auth='public', methods=['POST'], csrf=False)
    def create_new_user(self, **post):
        # Capturar los datos enviados desde el formulario
        new_user = {
            'name': post.get('name'),
            'last_name': post.get('last_name'),
            'birth_date': post.get('birth_date')
        }
        http.request.env['web.data'].create([new_user])

        # Redireccionar a la página principal después de guardar
        return http.request.redirect('/usuarios')
    
    @http.route('/usuarios/new', auth='public', type='http', website=True)
    def display_create_user_form(self, **kw):
        return http.request.render('modulo_web_data.create_user_form_template')
    
    @http.route('/usuarios/delete', auth='public', type='http', website=True)
    def display_delete_user_form(self, **kw):
        return http.request.render('modulo_web_data.delete_user_form_template')


    # READ  || Ruta para leer lista de usuarios
    @http.route('/usuarios', auth='public', type='http', website=True, methods=['GET'])
    def display_users_list(self, **kw):

        # Retorna la lista de usuarios
        users = http.request.env['web.data'].search([])
        users_data = []

        # Comprueba que haya almenos un usuario en mi recordset
        if len(users) == 0:
            return http.request.render('modulo_web_data.user_list_template')
        else:
            # Itera sobre el recordset y lo agrega la lista
            for user in users:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'birth_date': user.birth_date,
                    'last_name' : user.last_name,
                }
                users_data.append(data)
            # Retorna una respuesta renderizando la template , con la data dentro del diccionario
            return http.request.render('modulo_web_data.user_list_template', {
            'users': users_data,
            })

            

    
    # DELETE || Ruta para eliminar usuarios por el ID
    @http.route('/usuarios/delete', type="http", auth='public', methods=['POST'], csrf=False)
    def delete_new_user(self, **post):
        # Capturar los datos enviados desde el formulario
        id = post.get('id')
        print(id)
        # Busca el usuario con el id y luego lo elimina utilizando el unlink
        http.request.env['web.data'].search([
            ('id', '=', id)
        ]).unlink()

        # Redireccionar a la página principal después de guardar
        return http.request.redirect('/usuarios')
    



    

        