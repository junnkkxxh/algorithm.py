-- GROUP BY
-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT
    CAR_TYPE,
    COUNT(*) AS CARS
FROM
    CAR_RENTAL_COMPANY_CAR
WHERE
    OPTIONS LIKE '%시트%'
GROUP BY
    CAR_TYPE
ORDER BY
    CAR_TYPE;

-- fail -> options는 varchar 이므로 in 이 아닌 like를 사용하는 게 적합
-- SELECT
--     CAR_TYPE,
--     COUNT(CAR_TYPE) AS CARS
-- FROM
--     CAR_RENTAL_COMPANY_CAR
-- WHERE
--     OPTIONS in ('통풍시트', '열선시트', '가죽시트')
-- GROUP BY
--     CAR_TYPE
-- ORDER BY
--     CAR_TYPE;