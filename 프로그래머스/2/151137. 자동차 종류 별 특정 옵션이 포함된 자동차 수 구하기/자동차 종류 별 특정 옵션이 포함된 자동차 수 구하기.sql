-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(CAR_TYPE) as CARS from CAR_RENTAL_COMPANY_CAR where OPTIONS LIKE '%시트%' group by car_type order by car_type