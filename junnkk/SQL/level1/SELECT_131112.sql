-- SELECT
-- 강원도에 위치한 생산공장 목록 출력하기
SELECT
    FACTORY_ID,
    FACTORY_NAME,
    ADDRESS
FROM
    FOOD_FACTORY
WHERE
    ADDRESS LIKE '강원도%';