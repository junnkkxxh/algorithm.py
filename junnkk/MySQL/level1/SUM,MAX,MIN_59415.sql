-- SUM,MAX,MIN
-- 최댓값 구하기
-- SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1;
-- SELECT MAX(DATETIME) FROM ANIMAL_INS;
SELECT
    DATETIME
FROM
    ANIMAL_INS
WHERE
    DATETIME = MAX(DATETIME);