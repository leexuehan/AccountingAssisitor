from utils.SQL_dict import SQL_dict
from utils.SqlUtils import SqlUtils
from utils.account.BaseAccountingStrategy import BaseAccountingStrategy


## 粗略计算策略，精确到十位数
class RoughAccountingStrategy(BaseAccountingStrategy):
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

    def __all_coals_cost_compute_by_tons_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['coal_total_purchase_price_by_tons'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_coals_cost_compute_by_cars_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['coal_total_purchase_price_by_cars'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_coals_cost_compute_by_tons_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['coal_total_sell_price_by_cars'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_coals_cost_compute_by_cars_sell_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['coal_total_sell_price_by_tons'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def all_tickets_cost_compute_by_tons_sell_price(self, dbUtils, cursor, name):
        tons_ = SQL_dict['accounting_sqls_rough']['ticket_total_sell_price_by_tons']
        sql = tons_ % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def all_tickets_cost_compute_by_cars_sell_price(self, dbUtils, cursor, name):
        cars_ = SQL_dict['accounting_sqls_rough']['ticket_total_sell_price_by_cars']
        print(cars_), type(cars_)
        sql = cars_ % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_tickets_cost_compute_by_tons_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['ticket_total_purchase_price_by_tons'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    def __all_tickets_cost_compute_by_cars_purchase_price(self, dbUtils, cursor, name):
        sql = SQL_dict['accounting_sqls_rough']['ticket_total_purchase_price_by_cars'] % name
        print("execute sql:\n" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result


if __name__ == '__main__':
    # RoughAccountingStrategy().all_ticket_sell_price_by_person('李雪寒')
    RoughAccountingStrategy().all_ticket_sell_price_by_person('li')
