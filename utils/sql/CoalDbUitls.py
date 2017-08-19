import logging

from utils.sql.SqlUtils import SqlUtils


class CoalDbUtils(SqlUtils):
    def query_coal_latest_sell_price_by_name(self, coal_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT MAX(DATE),SELL_PRICE,SELL_COMPUTE_WAY FROM %s WHERE COAL_NAME IS "%s"' % (
            self.coal_table_name, coal_name)
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results

    def add_coal_record(self, add_date, coal_name, purchase_price, purchase_compute_way,
                        sell_price, sell_compute_way):
        conn = self.get_connection()
        cursor = conn.cursor()
        record = (add_date, coal_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'INSERT INTO %s VALUES(?,?,?,?,?,?)' % self.coal_table_name
        logging.info("execute sql:" + str(sql))
        cursor.execute(sql, record)
        conn.commit()
        conn.close()

    def query_all_coal_names(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT DISTINCT COAL_NAME FROM %s' % self.coal_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results

    def query_coal_purchase_price_by_name(self, coal_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT PURCHASE_PRICE,PURCHASE_COMPUTE_WAY FROM %s WHERE COAL_NAME IS "%s"' % (
            self.coal_table_name, coal_name)
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results
