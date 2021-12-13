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
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)
    district = fields.Many2one(string='District', related='partner_id.district_id', store=True)

class PurchaseOrder(models.Model):
    _inherit="purchase.order"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)
    district = fields.Many2one(string='District', related='partner_id.district_id', store=True)

class AccountMove(models.Model):
    _inherit="account.move"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)

class AccountPayment(models.Model):
    _inherit="account.payment"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)                                                                      

class SaleOrder(models.Model):
    _inherit="sale.order"
    
    partner_category = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)
    district = fields.Many2one(string='District', related='partner_id.district_id', store=True)

class SaleReport(models.Model):
    _inherit="sale.report"
    
    customer_location = fields.Many2one(string='Customer Location', related='partner_id.property_stock_customer', store=True)
    vendor_location = fields.Many2one(string='Vendor Location', related='partner_id.property_stock_supplier', store=True)
    customer_company = fields.Many2one(string='Customer Company', related='partner_id.company_id', store=True)
    district = fields.Many2one(string='District', related='partner_id.district_id', store=True)

    def _query(self, with_clause="", fields=None, groupby="", from_clause=""):
        if fields is None:
            fields = {}
        select_str = """,
            s.vendor_location as vendor_location, 
            s.customer_location as customer_location, 
            s.customer_company as customer_company,
            s.district as district
		"""
        
        fields.update({"vendor_location, customer_location, customer_company, district_id": select_str})
        return super()._query(
            with_clause=with_clause,
            fields=fields,
            groupby=groupby,
            from_clause=from_clause,
        )



 