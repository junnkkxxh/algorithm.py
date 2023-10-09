-- String, Date
-- 조건별로 분류하여 주문상태 출력하기
SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS DATE_FORMAT,
    CASE
        WHEN DATEDIFF('2022-05-01', OUT_DATE) >= 0 THEN '출고완료'
        WHEN DATEDIFF('2022-05-01', OUT_DATE) < 0 THEN '출고대기'
        ELSE "출고미정"
    END AS '출고여부'
FROM
    FOOD_ORDER
ORDER BY
    ORDER_ID;