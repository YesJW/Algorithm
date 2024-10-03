-- 코드를 작성해주세요
select YEAR(YM) as YEAR, round(avg(PM_VAL1),2) as PM10, round(AVG(PM_VAL2),2) as 'PM2.5' from AIR_POLLUTION where location2 = '수원'
group by YEAR(YM)
order by YEAR(YM)