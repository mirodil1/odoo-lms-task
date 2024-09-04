# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Group(models.Model):
    _name = 'group.group'
    _description = 'group.group'

    name = fields.Char("Name")
    course_id = fields.Many2one('course.course', string='Course')
    student_ids = fields.Many2many('student.student', string='Students')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
