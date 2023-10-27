# -*- coding: utf-8 -*-

from odoo import models, fields

class Tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'Tareas'

    name = fields.Char(string='Nombre', required=True, help='Introducir nombre')
    descripcion = fields.Text(string='Descripción')
    horas = fields.Float(string='Horas')
    fecha_creacion = fields.Date(string='Fecha de Creación')
    fecha_inicio = fields.Datetime(string='Fecha de Comienzo')
    fecha_fin = fields.Datetime(string='Fecha de Fin')
    pausada = fields.Boolean(string='Pausada')

    # Relaciones
    sprint_id = fields.Many2one('tareas.sprint', string='Sprint')
    tecnologias_ids = fields.Many2many('tareas.tecnologias', string='Tecnologías')

class Sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'Sprint'

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    fecha_creacion = fields.Datetime(string='Fecha de Creación')
    fecha_fin = fields.Datetime(string='Fecha de Fin')

    # Relaciones
    tarea_ids = fields.One2many('tareas.tareas', 'sprint_id', string='Tareas')

class Tecnologias(models.Model):
    _name = 'tareas.tecnologias'
    _description = 'Tecnologías'

    name = fields.Char(string='Nombre')
    foto = fields.Binary(string='Foto', attachment=True, help='Añade una imagen con max. anchura de 200 y max. altura de 200')

    # Relaciones
    tareas_ids = fields.Many2many('tareas.tareas', string='Tareas')

