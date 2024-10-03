-- 코드를 입력하세요
SELECT TRUNCATE(price, -4) AS price_group, COUNT(product_id) as products from product group by price_group
order by price_group