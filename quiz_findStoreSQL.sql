# Write your MySQL query statement below

select s.store_id,
       s.store_name,
       s.location,
       t.most_exp_product,
       t.cheapest_product,
       t.imbalance_ratio 
from stores s
join (
    select t1.store_id,
           t2.product_name as most_exp_product,
           t1.product_name as cheapest_product,
           round(t1.quantity / t2.quantity, 2) as imbalance_ratio 
    from (
        select i2.inventory_id,
               i2.store_id,
               i2.product_name,
               i2.quantity,
               i2.price  
        from inventory i2
        join (
            select store_id, min(price) as mn 
            from inventory
            group by store_id
            having count(inventory_id) >= 3
        ) i3
        on i2.store_id = i3.store_id 
        and i2.price = i3.mn
    ) t1 
    join (
        select i4.inventory_id,
               i4.store_id,
               i4.product_name,
               i4.quantity,
               i4.price  
        from inventory i4
        join (
            select store_id, max(price) as mx 
            from inventory
            group by store_id
            having count(inventory_id) >= 3
        ) i5
        on i4.store_id = i5.store_id 
        and i4.price = i5.mx
    ) t2
    on t1.store_id = t2.store_id 
    and t1.quantity > t2.quantity
) t
on s.store_id = t.store_id
order by imbalance_ratio desc, s.store_name;
