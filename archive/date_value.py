# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from ...registry import check
from ...error import Error
import datetime


# Module API

@check('date_value', type='custom', context='body')
class DateValue(object):

    # Public
    def __init__(self, date_format, **options):
        self.__date_string = "date"
        self.__date_format = date_format
        self.__date_column = []

    def check_row(self, cells):

        # Check if date header is present or not
        for cell in cells:
            if self.__date_string in cell['header']:
                value = cell.get('value')
                try:
                    datetime.datetime.strptime(value, self.__date_format)
                except ValueError:
                    message = ('Value "{value}" in column {column_number} on row {row_number}'
                               ' should be of format {date_format}')
                    message_substitutions = {
                        'value': value,
                        'date_format': self.__date_format,
                    }
                    error = Error(
                            'date_value',
                            cell,
                            message=message,
                            message_substitutions=message_substitutions
                        )
                    return [error]
