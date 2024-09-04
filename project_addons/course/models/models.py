# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'course.course'
    _description = 'course'

    name = fields.Char("Name")
    