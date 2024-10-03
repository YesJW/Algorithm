-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, sum(f.TOTAL_ORDER) as TOTAL_ORDER from icecream_info i, FIRST_HALF f
where f.flavor = i.flavor
group by i.INGREDIENT_TYPE
order by f.total_order