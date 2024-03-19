# -*- coding: utf-8 -*-

from odoo import models, fields

class StockValuationLayer(models.Model):
    _inherit='stock.valuation.layer'

    product_category_id = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)
    partner_category_id = fields.Many2one(string='Partner Category', related='stock_move_id.partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='stock_move_id.partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='stock_move_id.partner_id.company_id', store=True)

class StockMove(models.Model):
    _inherit="stock.move"

    product_category_id = fields.Many2one('product.category', string='Product Category', related='product_id.categ_id', store=True)
    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class StockPicking(models.Model):
    _inherit="stock.picking"
    
    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class PurchaseOrder(models.Model):
    _inherit="purchase.order"

    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class AccountMove(models.Model):
    _inherit="account.move"

    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class AccountPayment(models.Model):
    _inherit="account.payment"

    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class SaleOrder(models.Model):
    _inherit="sale.order"

    partner_category_id = fields.Many2one(string='Partner Category', related='partner_id.client_category_id', store=True)
    partner_district_id = fields.Many2one(string='Partner District', related='partner_id.district_id', store=True)
    partner_city_id = fields.Many2one(string='Partner City', related='partner_district_id.city_id', store=True)
    partner_company_id = fields.Many2one(string='Partner Company', related='partner_id.company_id', store=True)

class SaleReport(models.Model):
    _inherit="sale.report"


    partner_category_id = fields.Many2one('res.category', string='Partner Category')
    partner_district_id = fields.Many2one('res.city.district', string='Partner District')
    partner_city_id = fields.Many2one('res.city', string='Partner City')
    partner_company_id = fields.Many2one('res.company', string='Partner Company')


    def _select_sale(self):
        select_ = super(SaleReport, self)._select_sale()

        select_ += """,
            s.partner_category_id AS partner_category_id,
            s.partner_district_id AS partner_district_id,
            s.partner_city_id AS partner_city_id,
            s.partner_company_id AS partner_company_id"""
        return select_

    def _group_by_sale(self):
        group_by = super(SaleReport, self)._group_by_sale()

        group_by += """,
            s.partner_category_id,
            s.partner_district_id,
            s.partner_city_id,
            s.partner_company_id"""
        return group_by



 