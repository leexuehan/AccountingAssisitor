from unittest import TestCase

from utils.SqlUtils import SqlUtils


class TestSqlUtils(TestCase):
    def test_create_ticket_table(self):
        sqlUtils = SqlUtils()
        sqlUtils.create_ticket_table_if_necessary()

    def test_add_ticket_record(self):
        sqlUtils = SqlUtils()
        sqlUtils.add_ticket_record('2016/03/15','bytons','example1','1.2','2.0')
