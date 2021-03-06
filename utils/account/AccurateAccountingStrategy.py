from utils.account.BaseAccountingStrategy import BaseAccountingStrategy
from utils.account.RoughAccountingStrategy import RoughAccountingStrategy
from utils.sql.SQL_dict import SQL_dict
from utils.sql.SqlUtils import SqlUtils


## 精确计算策略，精确到小数点后两位
class AccurateAccountingStrategy(BaseAccountingStrategy):
    # 吨位合计（按照煤种统计出来）
    # 煤款合计（主要是售价煤款）
    # 利润
    # 按客户分类所有煤款进价
    def all_coals_purchase_cost_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.__all_coals_cost_compute_by_tons_purchase_price(dbUtils, cursor, name)
        result_by_cars = self.__all_coals_cost_compute_by_cars_purchase_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if result_by_tons[0][0] is not None:
            price_by_tons = result_by_tons[0][1]
        if result_by_cars[0][0] is not None:
            price_by_cars = result_by_cars[0][1]
        return price_by_tons + price_by_cars

    # 按客户分类所有煤款售价
    def all_coals_sell_perice_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.__all_coals_cost_compute_by_tons_sell_price(dbUtils, cursor, name)
        result_by_cars = self.__all_coals_cost_compute_by_cars_sell_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if result_by_tons[0][0] is not None:
            price_by_tons = result_by_tons[0][1]
        if result_by_cars[0][0] is not None:
            price_by_cars = result_by_cars[0][1]
        return price_by_tons + price_by_cars

    # 按客户分类所有票款售价
    def all_ticket_sell_price_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.all_tickets_cost_compute_by_tons_sell_price(dbUtils, cursor, name)
        result_by_cars = self.all_tickets_cost_compute_by_cars_sell_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if result_by_tons[0][0] is not None:
            price_by_tons = result_by_tons[0][1]
        if result_by_cars[0][0] is not None:
            price_by_cars = result_by_cars[0][1]
        return price_by_tons + price_by_cars

    # 按客户分类所有票款进价
    def all_ticket_purchase_price_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.__all_tickets_cost_compute_by_tons_purchase_price(dbUtils, cursor, name)
        result_by_cars = self.__all_tickets_cost_compute_by_cars_purchase_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if result_by_tons[0][0] is not None:
            price_by_tons = result_by_tons[0][1]
        if result_by_cars[0][0] is not None:
            price_by_cars = result_by_cars[0][1]
        print('price by car:' + str(price_by_cars) + ',price by tons' + str(price_by_tons))
        return price_by_tons + price_by_cars

    # 以元/吨计价的煤款进价总数
    def __all_coals_cost_compute_by_tons_purchase_price(self, db_utils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['coal_total_purchase_price_by_tons'] % name
        print("execute sql:" + sql)
        result = db_utils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/车计价的煤款进价总数
    def __all_coals_cost_compute_by_cars_purchase_price(self, db_utils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['coal_total_purchase_price_by_cars'] % name
        print("execute sql:" + sql)
        result = db_utils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/车计价的煤款售价总数
    def __all_coals_cost_compute_by_tons_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['coal_total_sell_price_by_cars'] % name
        print("execute sql:" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/吨计价的煤款售价总数
    def __all_coals_cost_compute_by_cars_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['coal_total_sell_price_by_tons'] % name
        print("execute sql:" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def all_tickets_cost_compute_by_tons_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['ticket_total_sell_price_by_tons'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def all_tickets_cost_compute_by_cars_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['ticket_total_sell_price_by_cars'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_tickets_cost_compute_by_tons_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['ticket_total_purchase_price_by_tons'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_tickets_cost_compute_by_cars_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_accurate']['ticket_total_purchase_price_by_cars'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result


if __name__ == '__main__':
    result1 = AccurateAccountingStrategy().all_coals_purchase_cost_by_person('刘帅')
    print(result1)
    result2 = AccurateAccountingStrategy().all_coals_sell_perice_by_person('刘帅')
    print(result2)
    result = RoughAccountingStrategy().all_coals_sell_perice_by_person('李雪寒')
    print(result)
