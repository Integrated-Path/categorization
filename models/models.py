# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockValuationLayer(models.Model):
    _inherit='stock.valuation.layer'

    product_category = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)

class Stock_Move(models.Model):
    _inherit="stock.move"

    product_category = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)

