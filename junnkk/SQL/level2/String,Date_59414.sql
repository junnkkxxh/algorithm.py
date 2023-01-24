-- String,Date
-- DATETIME에서 DATE로 형 변환
SELECT
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM
    animal_ins
order by
    animal_id;