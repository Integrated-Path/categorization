# -*- coding: utf-8 -*-

from odoo import models, fields

class StockValuationLayer(models.Model):
    _inherit='stock.valuation.layer'

    product_category = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)
    partner_category = fields.Many2one(string='Partner Category', related='stock_move_id.partner_id.client_category_id', store=True)
    
class Stock_Move(models.Model):
    _inherit="stock.move"

    product_category = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)

class StockPicking(models.Model):
    _inherit="stock.picking"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)

class SaleOrder(models.Model):
    _inherit="sale.order"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)

class PurchaseOrder(models.Model):
    _inherit="purchase.order"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)

class AccountMove(models.Model):
    _inherit="account.move"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)





 