import logging

from utils.sql.SqlUtils import SqlUtils


class RecordDetailDbUtils(SqlUtils):
    def add_record_by_car_detail(self, date, person_name, car_id, coal_name, weight_value, ticket_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        record_by_car = (date, person_name, car_id, coal_name, weight_value, ticket_name)
        logging.info("record info is " + str(record_by_car))
        sql = 'INSERT INTO %s VALUES(?,?,?,?,?,?)' % self.record_by_car_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql, record_by_car)
        conn.commit()
        conn.close()

    def query_all_person_names(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT DISTINCT PERSON_NAME FROM %s' % self.record_by_car_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results
