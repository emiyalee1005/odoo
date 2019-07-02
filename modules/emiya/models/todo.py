from odoo import fields, models, api
from odoo.exceptions import Warning


class Todos(models.Model):
    _name = 'library.abc'
    _description = 'Todos'
    name = fields.Char('name', required=True)
    description = fields.Char('description')
    status = fields.Integer(default=0)


class TodoTask(models.Model):
    _name = 'library.todos'
    _description = 'Todos'
    name = fields.Char('name', required=True)
    description = fields.Char('description')
    status = fields.Integer(default=0)
