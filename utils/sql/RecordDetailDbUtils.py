import logging

from utils.sql.SqlUtils import SqlUtils


class RecordDetailDbUtils(SqlUtils):
    def add_record_by_car_detail(self,
                                 date,
                                 person_name,
                                 car_id,
                                 coal_name,
                                 coal_sell_price,
                                 coal_sell_compute_way,
                                 coal_fund,
                                 weight_value,
                                 ticket_name,
                                 ticket_sell_price,
                                 ticket_sell_compute_way,
                                 ticket_sell_fund,
                                 should_take_count,
                                 profit):
        conn = self.get_connection()
        cursor = conn.cursor()
        record_by_car = (date, person_name, car_id,
                         coal_name, coal_sell_price, coal_sell_compute_way,
                         coal_fund, weight_value, ticket_name,
                         ticket_sell_price, ticket_sell_compute_way, ticket_sell_fund,
                         should_take_count, profit)
        logging.info("record info is " + str(record_by_car))
        sql = 'INSERT INTO %s VALUES(?,?,?,?,?' \
              ',?,?,?,?,?' \
              ',?,?,?,?)' % self.record_by_car_table_name
        logging.info("execute sql:\n" + sql)
        print("execute sql:\n" + sql)
        cursor.execute(sql, record_by_car)
        conn.commit()
        conn.close()

    def query_total_tons_coalfunds_profit(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT SUM(WEIGHT_VALUE),SUM(COAL_FUND),SUM(PROFIT) FROM %s' % self.record_by_car_table_name
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results

    def query_all_records(self, begin_date, end_date):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM %(table_name)s where DATE >= "%(begin_date)s" and DATE <= "%(end_date)s" order by DATE asc' % {
            'table_name': self.record_by_car_table_name, 'begin_date': begin_date, 'end_date': end_date}
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results

    def query_coal_info_group_by_coal_name(self, begin_date, end_date):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT date,coal_name,sum(weight_value),sum(coal_fund) FROM %(table_name)s  ' \
              'where DATE >= "%(begin_date)s" and DATE <= "%(end_date)s" group by date,coal_name order by DATE asc' % {
            'table_name': self.record_by_car_table_name, 'begin_date': begin_date, 'end_date': end_date}
        print("execute sql:\n" + sql)
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        conn.close()
        return results


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


if __name__ == '__main__':
    # results = RecordDetailDbUtils().query_all_records()
    results = RecordDetailDbUtils().query_total_tons_coalfunds_profit()
    print(results)
