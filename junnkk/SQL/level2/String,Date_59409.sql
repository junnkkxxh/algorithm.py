-- String,Date
-- 중성화 여부 파악하기
-- 방법 1. when 사용
-- SELECT ANIMAL_ID, NAME,
-- CASE 
--     WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
--         THEN 'O'
--     ELSE 'X'
--     END AS '중성화'
-- FROM ANIMAL_INS
-- ORDER BY ANIMAL_ID;

-- 방법 2. if 사용
SELECT
    ANIMAL_ID,
    NAME,
    IF (
        SEX_UPON_INTAKE LIKE '%Neutered%'
        OR SEX_UPON_INTAKE LIKE '%Spayed%',
        'O',
        'X'
    ) AS '중성화'
FROM
    ANIMAL_INS
ORDER BY
    ANIMAL_ID;