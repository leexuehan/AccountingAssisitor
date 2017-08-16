SQL_dict = {
    'create_table_sqls': {
        'CREATE_COALS_TABLE_SQL': 'CREATE TABLE IF NOT EXISTS coals('
                                  'DATE TEXT NOT NULL,'
                                  'COAL_NAME TEXT PRIMARY KEY,'
                                  'PURCHASE_PRICE REAL,'
                                  'PURCHASE_COMPUTE_WAY TEXT,'
                                  'SELL_PRICE REAL,'
                                  'SELL_COMPUTE_WAY TEXT)',
        'CREATE_TICKET_TABLE_SQL': 'CREATE TABLE IF NOT EXISTS tickets('
                                   'DATE TEXT NOT NULL,'
                                   'TICKET_NAME TEXT PRIMARY KEY,'
                                   'PURCHASE_PRICE REAL,'
                                   'PURCHASE_COMPUTE_WAY TEXT,'
                                   'SELL_PRICE REAL,'
                                   'SELL_COMPUTE_WAY TEXT)',
        'CREATE_RECORD_BY_CAR_TABLE_SQL': 'CREATE TABLE IF NOT EXISTS record_by_car_detail('
                                          'DATE TEXT NOT NULL,'
                                          'PERSON_NAME TEXT NOT NULL,'
                                          'CAR_ID TEXT,'
                                          'COAL_NAME TEXT,'
                                          'WEIGHT_VALUE REAL,'
                                          'TICKET_NAME TEXT)'
    },
    ### 精确出账
    'accounting_sqls_accurate': {
        ###煤的进价
        'coal_total_purchase_price_by_tons':
            'select name, sum(cost) from ('
            'select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.purchase_price purchase_price,t1.weight_value*t2.purchase_price cost from('
            'select person_name,coal_name,weight_value from record_by_car_detail) t1, ('
            'select coal_name,purchase_price from coals where purchase_compute_way == "元/吨") t2'
            ' where t1.coal_name == t2.coal_name) where name is "%s";',
        'coal_total_purchase_price_by_cars':
            'select name, sum(cost) from ('
            'select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.purchase_price purchase_price,1*t2.purchase_price cost from('
            'select person_name,coal_name,weight_value from record_by_car_detail) t1, ('
            'select coal_name,purchase_price from coals where purchase_compute_way == "元/车") t2'
            ' where t1.coal_name == t2.coal_name) where name is "%s";',
        ###煤的售价
        'coal_total_sell_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,t1.weight_value*t2.sell_price cost '
            'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, '
            '(select coal_name, sell_price from coals where purchase_compute_way == "元/吨") t2 '
            'where t1.coal_name == t2.coal_name) where name is "%s"',
        'coal_total_sell_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,1*t2.sell_price cost '
            'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, '
            '(select coal_name, sell_price from coals where purchase_compute_way == "元/车") t2 '
            'where t1.coal_name == t2.coal_name) where name is "%s"',
        ###票的进价
        'ticket_total_purchase_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,t1.weight_value*t2.sell_price cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/吨") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        'ticket_total_purchase_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,1*t2.sell_price cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/车") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        ###票的售价
        'ticket_total_sell_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name,'
            't2.purchase_price purchase_price,t1.weight_value*t2.purchase_price cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, purchase_price from tickets where purchase_compute_way == "元/吨") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        'ticket_total_sell_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name,'
            't2.sell_price sell_price,1*t2.sell_price cost '
            'from (select person_name, ticket_name from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/车") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"'
    },
    ###### 按照免除个位数零头出账
    'accounting_sqls_rough': {
        ###煤的进价
        'coal_total_purchase_price_by_tons':
            'select name, sum(cost) from ('
            'select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.purchase_price purchase_price, (t1.weight_value*t2.purchase_price - t1.weight_value*t2.purchase_price%%10) cost from('
            'select person_name,coal_name,weight_value from record_by_car_detail) t1, ('
            'select coal_name,purchase_price from coals where purchase_compute_way == "元/吨") t2'
            ' where t1.coal_name == t2.coal_name) where name is "%s"',
        'coal_total_purchase_price_by_cars':
            'select name, sum(cost) from ('
            'select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.purchase_price purchase_price,(1*t2.purchase_price - 1*t2.purchase_price%10) cost from('
            'select person_name,coal_name,weight_value from record_by_car_detail) t1, ('
            'select coal_name,purchase_price from coals where purchase_compute_way == "元/车") t2'
            ' where t1.coal_name == t2.coal_name) where name is "%s"',
        ###煤的售价
        'coal_total_sell_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,(t1.weight_value*t2.sell_price - t1.weight_value*t2.sell_price%%10) cost '
            'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, '
            '(select coal_name, sell_price from coals where purchase_compute_way == "元/吨") t2 '
            'where t1.coal_name == t2.coal_name) where name is "%s"',
        'coal_total_sell_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,(1*t2.sell_price - 1*t2.sell_price%10) cost '
            'from (select person_name, coal_name, weight_value from record_by_car_detail) t1, '
            '(select coal_name, sell_price from coals where purchase_compute_way == "元/车") t2 '
            'where t1.coal_name == t2.coal_name) where name is "%s"',
        ###票的进价
        'ticket_total_purchase_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,(t1.weight_value*t2.sell_price - t1.weight_value*t2.sell_price%10) cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/吨") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        'ticket_total_purchase_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name, t1.weight_value weight_value,'
            't2.sell_price sell_price,(1*t2.sell_price - 1*t2.sell_price%10) cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/车") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        ###票的售价
        'ticket_total_sell_price_by_tons':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name,'
            't2.purchase_price purchase_price,(t1.weight_value*t2.purchase_price - t1.weight_value*t2.purchase_price%%10) cost '
            'from (select person_name, ticket_name, weight_value from record_by_car_detail) t1, '
            '(select ticket_name, purchase_price from tickets where purchase_compute_way == "元/吨") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"',
        'ticket_total_sell_price_by_cars':
            'select name, sum(cost) from (select t1.person_name name, t1.ticket_name ticket_name,'
            't2.sell_price sell_price,(1*t2.sell_price - 1*t2.sell_price%%10)cost '
            'from (select person_name, ticket_name from record_by_car_detail) t1, '
            '(select ticket_name, sell_price from tickets where sell_compute_way == "元/车") t2 '
            'where t1.ticket_name == t2.ticket_name) where name is "%s"'
    }
}
