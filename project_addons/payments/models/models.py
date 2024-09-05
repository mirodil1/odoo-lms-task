# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentPayment(models.Model):
    _name = 'student.payment'
    _description = 'Student Payment'

    name = fields.Char(string='Payment Reference', required=True, readonly=True, default=lambda self: 'New')
    student_id = fields.Many2one('student.student', string='Student', required=True)
    group_id = fields.Many2one('group.group', string='Group', required=True)
    amount = fields.Float(string='Amount', required=True)
    comment = fields.Text(string='Comment')


class TeacherPayment(models.Model):
    _name = 'teacher.payment'
    _description = 'Teacher Payment'

    name = fields.Char(string='Payment Reference', required=True, readonly=True, default=lambda self: 'New')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Amount', required=True)
    comment = fields.Text(string='Comment')
