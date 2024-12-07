from odoo import models,fields

class ToDo(models.Model):
    _name= 'todo.task'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Task Name", required=True,tracking=True)
    assign_to_id = fields.Many2one(comodel_name='res.users',string="Assign To",tracking=True)
    description = fields.Text(string = "Description",tracking=True)
    due_date = fields.Datetime(string="Due Date",tracking=True)
    state = fields.Selection([
        ('new','New'),
        ('in_progress','In Progress'),
        ('completed','Completed')
    ], default='new',tracking=True)

