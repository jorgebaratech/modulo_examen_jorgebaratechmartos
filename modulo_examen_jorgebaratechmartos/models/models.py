# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Cliente(models.Model):
    _name = 'mi_modulo.cliente'
    _description = 'Modelo de datos para clientes'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    estado = fields.Char(string='Estado')
    codigo_postal = fields.Char(string='Código Postal')
    pais = fields.Char(string='País')


class Factura(models.Model):
    _name = 'mi_modulo.factura'
    _description = 'Modelo de datos para facturas'

    numero_factura = fields.Char(string='Número de factura', required=True)
    fecha_emision = fields.Date(string='Fecha de emisión', default=fields.Date.today())
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    monto_total = fields.Float(string='Monto total')
    cliente_id = fields.Many2one('mi_modulo.cliente', string='Cliente')


    
class Producto(models.Model):
    _name = 'mi_modulo.producto'
    _description = 'Modelo de datos para productos'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    cantidad = fields.Integer(string='Cantidad de productos', default=0)


    @api.multi
    def write(self, vals):
        if 'cantidad' in vals and vals['cantidad'] == 0:
            vals['precio'] = 0
        return super(Producto, self).write(vals)
    