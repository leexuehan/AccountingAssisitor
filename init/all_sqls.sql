select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,
t2.purchase_price purchase_price,t1.weight_value*t2.purchase_price cost from
(select person_name,coal_name,weight_value from record_by_car_detail) t1, (select coal_name,purchase_price from coals where purchase_compute_way == '元/车') t2
where t1.coal_name == t2.coal_name) group by name;



select name, sum(cost) from (select t1.person_name name, t1.coal_name coal_name, t1.weight_value weight_value,
t2.purchase_price purchase_price,t1.weight_value*t2.purchase_price cost from
(select person_name,coal_name,weight_value from record_by_car_detail) t1, (select coal_name,purchase_price from coals where purchase_compute_way == '元/吨') t2
where t1.coal_name == t2.coal_name) group by name;


