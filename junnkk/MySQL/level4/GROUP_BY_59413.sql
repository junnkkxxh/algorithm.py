-- GROUP BY
-- 입양 시각 구하기(2)
SET
    @HOUR := -1;

SELECT
    (@HOUR := @HOUR + 1) AS HOUR,
    (
        SELECT
            COUNT(*)
        FROM
            ANIMAL_OUTS
        WHERE
            HOUR(DATETIME) = @HOUR
    ) AS COUNT
FROM
    ANIMAL_OUTS
WHERE
    @HOUR < 23;

-- # SET @HOUR = -1;
-- # SELECT (@HOUR := @HOUR +1) AS HOUR,
-- #     (SELECT COUNT(HOUR(DATETIME)) 
-- #     FROM ANIMAL_OUTS 
-- #     WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
-- #     FROM ANIMAL_OUTS
-- # WHERE @HOUR < 23;
-- # SET @hour := -1; -- 변수 선언
-- # SELECT (@hour := @hour + 1) as HOUR,
-- # (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
-- # FROM ANIMAL_OUTS
-- # WHERE @hour < 23