from odoo import fields, models


class ProductProductInherits(models.Model):
	_inherit = "product.product"
	
	
	user_id = fields.Many2one("res.users", string="Product Owner")