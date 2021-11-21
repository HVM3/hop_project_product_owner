from odoo import fields, models, api


class ProjectTasks(models.Model):
	_inherit = "project.task"
	

	product_id = fields.Many2one("product.template", string="Product")

	@api.onchange('user_id','product_id')
	def onchange_set_product_owner(self):
		if self.user_id and self.product_id:
			self.product_id.product_variant_id.user_id = self.user_id
			self.product_id.user_id = self.user_id