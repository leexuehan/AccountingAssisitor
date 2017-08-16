## 所有计算策略的父类
class BaseAccountingStrategy(object):
    # 按客户分类所有煤款进价
    def all_coals_purchase_cost_by_person(self, name):
        pass

    # 按客户分类所有煤款售价
    def all_coals_sell_perice_by_person(self, name):
        pass

    # 按客户分类所有票款售价
    def all_ticket_sell_price_by_person(self, name):
        pass

    # 按客户分类所有票款进价
    def all_ticket_purchase_price_by_person(self, name):
        pass
