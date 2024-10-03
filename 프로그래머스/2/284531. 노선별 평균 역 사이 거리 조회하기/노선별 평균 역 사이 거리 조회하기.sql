-- 코드를 작성해주세요
select ROUTE, concat(round(sum(D_BETWEEN_DIST),1),'km') TOTAL_DISTANCE, CONCAT(round(AVG(D_BETWEEN_DIST),2),'km') AVERAGE_DISTANCE
from subway_distance
group by ROUTE
ORDER BY ROUND(SUM(D_BETWEEN_DIST), 1) DESC;