-- 코드를 입력하세요
SELECT o.ANIMAL_ID, o.NAME from ANIMAL_OUTS o LEFT OUTER JOIN ANIMAL_INS i on o.ANIMAL_ID = i.ANIMAL_ID
where i.animal_id is NULL 
order by i.animal_id
