# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError
from odoo.tools.enlettres import convlettres



class LapoRequest(models.Model):
    _name = "lapo.request"
    _description = "Request"

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('lapo.request') or _('New')
        vals['name'] = sequence
        result = super(LapoRequest, self).create(vals)
        return result

    def send(self):
        t=0
    def to_draft(self):
        t=0
    def cancel(self):
        t=0

    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    name = fields.Char(string="Reference" , readonly=True)
    title = fields.Char(string="Title")
    item = fields.Char(string="Item requested" , readonly=True)
    description = fields.Text(string="Description")
    amount = fields.Float(string="Estimated amount")
    
    state = fields.Selection(
        [
            ('draft','Draft'),
            ('progess','In Progess'),
            ('validated','Validated'),
            ('canceled','Canceled'),
            ('rejected','Rejected'),
        ], string='State', readonly=True, default='draft')

    