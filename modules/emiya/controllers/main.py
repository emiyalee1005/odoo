from odoo import http
import json
import werkzeug


class Todo(http.Controller):

    @http.route('/library/todo', auth='user')
    def list(self, **kwargs):
        Todos = http.request.env['library.todos']

        # Todos.create({
        #     'name': 'Odoo Development Essentials123',
        #     'description': '879-1-78439-279-6',
        #     'status': 1})
        # todos = Todos.search([])
        todos = Todos.search([('status', '=', 0)])
        finish = Todos.search([('status', '=', 1)])
        return http.request.render(
            'emiya.book_list_template', {'todos': todos, 'finish': finish})

    @http.route('/library/todo/detail', auth='user')
    def detail(self, **kwargs):
        # for v, k in vars(http.request.httprequest).items():
        #     print('{v}:{k}'.format(v=v, k=k))
        Todos = http.request.env['library.todos']

        # print(http.request.httprequest.args['id'])

        # Todos.create({
        #     'name': 'Odoo Development Essentials123',
        #     'description': '879-1-78439-279-6',
        #     'status': 1})
        # todos = Todos.search([])
        if 'id' in http.request.httprequest.args.keys():
            data = Todos.search([('id', '=', http.request.httprequest.args['id'])])[0]
        else:
            data = None

        return http.request.render(
            'emiya.book_detail_template', {'data': data})

    @http.route('/library/todo/submit', auth='user', methods=['POST'], csrf=False)
    def submit(self, **kwargs):
        Todos = http.request.env['library.todos']

        # Todos.create({
        #     'name': 'Odoo Development Essentials123',
        #     'description': '879-1-78439-279-6',
        #     'status': 1})
        # todos = Todos.search([])

        if 'id' in kwargs.keys():
            data = Todos.browse([kwargs.get('id')])

            r = data.write(kwargs)
            return http.Response(json.dumps({"status": r}), headers={"Content-Type": "application/json"})

        else:
            print(kwargs)
            r = Todos.create(kwargs)
            return http.Response(json.dumps({"status": True}), headers={"Content-Type": "application/json"})

        # return http.request.make_response(jsonify({"status": 123}))

    @http.route('/library/todo/delete', auth='user', methods=['DELETE'], csrf=False)
    def delete(self, **kwargs):
        Todos = http.request.env['library.todos']

        # Todos.create({
        #     'name': 'Odoo Development Essentials123',
        #     'description': '879-1-78439-279-6',
        #     'status': 1})
        # todos = Todos.search([])

        data = Todos.browse([kwargs.get('id')])

        r = data.unlink()

        # return http.request.make_response(jsonify({"status": 123}))

        return http.Response(json.dumps({"status": r}), headers={"Content-Type": "application/json"})
