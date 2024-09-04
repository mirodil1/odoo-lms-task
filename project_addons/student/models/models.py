# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'student.student'

    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    phone_number = fields.Char("Phone number")
