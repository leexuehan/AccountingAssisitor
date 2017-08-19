import logging

from utils.sql.SqlUtils import SqlUtils


class TicketDbUtils(SqlUtils):
    def add_ticket_record(self, add_date, ticket_name, purchase_price, purchase_compute_way,
                          sell_price, sell_compute_way):
        conn = self.get_connection()
        cursor = conn.cursor()
        record = (add_date, ticket_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.ticket_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql, record)
        conn.commit()
        conn.close()
        # 原子性???

    def query_all_tickets_name(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT TICKET_NAME FROM %s' % self.ticket_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql)
        fetch_result = cursor.fetchall()
        logging.info(fetch_result)
        conn.close()
        return fetch_result

    def query_latest_ticket_sell_price_by_name(self, ticket_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT MAX(DATE),SELL_PRICE,SELL_COMPUTE_WAY FROM %s WHERE TICKET_NAME IS "%s"' % (
            self.ticket_table_name, ticket_name)
        logging.info("execute sql:\n" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results
