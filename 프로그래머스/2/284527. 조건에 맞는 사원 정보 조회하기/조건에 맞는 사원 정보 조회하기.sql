-- 코드를 작성해주세요
SELECT sum(G.SCORE) as SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL FROM HR_EMPLOYEES E inner join HR_GRADE G
on E.EMP_NO = G.EMP_NO
group by YEAR, EMP_NO
HAVING G.YEAR = '2022'
order by 1 desc
limit 1