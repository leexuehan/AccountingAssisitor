from utils.SqlUtils import SqlUtils


class AccountingUtils(object):
    # 吨位合计（按照煤种统计出来）
    # 煤款合计（主要是售价煤款）
    # 利润

    def compute_by_condition(self, person, tickets, coals, start_date, end_date):
        dbUtils = SqlUtils()
        sql = ''
        dbUtils.query_coal_sell_price_by_name()
        dbUtils.execute_sql_without_close_connection()

    def compute_total_tons_by_coal(self, person, coal):
        sql_1 = 'SELECT * FROM record_by_car_detail where person_name is ' + person
        sql_2 = ''

    # 以元/吨计价的煤款进价总数
    def all_coals_cost_compute_by_tons_purchase_price(self, db_utils, cursor, name):
        sql = 'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,' \
              't2.purchase_price purchase_price,t1.weight_value*t2.purchase_price cost ' \
              'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, ' \
              '(select coal_name, purchase_price from coals where purchase_compute_way == "元/吨") t2 ' \
              'where t1.coal_name == t2.coal_name) where name is "%s" ' % name
        print("execute sql:" + sql)
        result = db_utils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/车计价的煤款进价总数
    def all_coals_cost_compute_by_cars_purchase_price(self, db_utils, cursor, name):
        sql = 'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,' \
              't2.purchase_price purchase_price,1*t2.purchase_price cost ' \
              'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, ' \
              '(select coal_name, purchase_price from coals where purchase_compute_way == "元/车") t2 ' \
              'where t1.coal_name == t2.coal_name) where name is "%s"' % name
        print("execute sql:" + sql)
        result = db_utils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/车计价的煤款售价总数
    def all_coals_cost_compute_by_tons_sell_price(self, dbUtils, cursor, name):
        sql = 'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,' \
              't2.sell_price sell_price,1*t2.sell_price cost ' \
              'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, ' \
              '(select coal_name, sell_price from coals where purchase_compute_way == "元/车") t2 ' \
              'where t1.coal_name == t2.coal_name) where name is "%s"' % name
        print("execute sql:" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 以元/吨计价的煤款售价总数
    def all_coals_cost_compute_by_cars_sell_price(self, dbUtils, cursor, name):
        sql = 'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,' \
              't2.sell_price sell_price,t1.weight_value*t2.sell_price cost ' \
              'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, ' \
              '(select coal_name, sell_price from coals where purchase_compute_way == "元/吨") t2 ' \
              'where t1.coal_name == t2.coal_name) where name is "%s"' % name
        print("execute sql:" + sql)
        result = dbUtils.execute_sql_without_close_connection(sql, cursor)
        return result

    # 按客户分类所有煤款进价
    def all_coals_purchase_cost_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.all_coals_cost_compute_by_tons_purchase_price(dbUtils, cursor, name)
        result_by_cars = self.all_coals_cost_compute_by_cars_purchase_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if len(result_by_tons) > 0:
            price_by_tons = result_by_tons[0][1]
        if len(result_by_cars) > 0:
            price_by_cars = result_by_cars[0][1]
        return price_by_tons + price_by_cars

    # 按客户分类所有煤款售价
    def all_coals_sell_perice_by_person(self, name):
        dbUtils = SqlUtils()
        conn = dbUtils.get_connection()
        cursor = conn.cursor()
        result_by_tons = self.all_coals_cost_compute_by_tons_sell_price(dbUtils, cursor, name)
        result_by_cars = self.all_coals_cost_compute_by_cars_sell_price(dbUtils, cursor, name)
        conn.close()
        price_by_tons = 0.0
        price_by_cars = 0.0
        if len(result_by_tons) > 0:
            price_by_tons = result_by_tons[0][1]
        if len(result_by_cars) > 0:
            price_by_cars = result_by_cars[0][1]
        return price_by_tons + price_by_cars


if __name__ == '__main__':
    result1 = AccountingUtils().all_coals_purchase_cost_by_person('李雪寒')
    print(result1)
    result2 = AccountingUtils().all_coals_sell_perice_by_person('李雪寒')
    print(result2)