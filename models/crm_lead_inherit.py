from odoo import models, fields, api
from datetime import date

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_lead_category = fields.Selection([
        ('residencial', 'Residencial'),
        ('empresarial', 'Empresarial'),
        ('gubernamental', 'Gubernamental')
    ], string='Categoría de Lead')
    
    x_delivery_deadline = fields.Date(string='Fecha Límite de Entrega')
    x_approved_by = fields.Many2one('res.users', string='Aprobado por', readonly=True)
    x_approved_date = fields.Date(string='Fecha de Aprobación', readonly=True)
    
    x_duration_since_approved = fields.Integer(
        string='Días desde aprobación', 
        compute='_compute_duration_since_approved', 
        readonly=True
    )
    
    x_installation_required = fields.Boolean(string='Requiere Instalación Técnica')
    x_installation_date = fields.Date(string='Fecha de Instalación')
    x_contract_reference = fields.Char(string='Referencia de Contrato')
    x_support_required = fields.Boolean(string='Requiere Soporte Técnico Postventa')

    @api.depends('x_approved_date')
    def _compute_duration_since_approved(self):
        for record in self:
            if record.x_approved_date:
                delta = date.today() - record.x_approved_date
                record.x_duration_since_approved = delta.days
            else:
                record.x_duration_since_approved = 0

    def action_approve_lead(self):
        for record in self:
            record.x_approved_by = self.env.user.id
            record.x_delivery_deadline = fields.Date.context_today(self)
            record.x_approved_date = fields.Date.context_today(self)