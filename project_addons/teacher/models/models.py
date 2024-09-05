# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'teacher.teacher'
    _rec_name = "first_name"
    
    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    phone_number = fields.Char("Phone number")
