from odoo import fields, models


class ProductTemplateInherits(models.Model):
	_inherit = "product.template"


	user_id = fields.Many2one("res.users", string="Product Owner")
	