# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'student'
    _rec_name = 'first_name'

    first_name = fields.Char("First Name")
    last_name = fields.Char("Last Name")
    phone_number = fields.Char("Phone number")
    #payment_ids = fields.One2many('student.payment', 'student_id', string='Payments')