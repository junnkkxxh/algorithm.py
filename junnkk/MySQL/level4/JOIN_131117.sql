-- JOIN
-- 5월의 식품들의 총매출 조회하기
SELECT
    F.PRODUCT_ID,
    F.PRODUCT_NAME,
    (F.PRICE * S.AMOUNT) AS TOTAL_SALES
FROM
    FOOD_PRODUCT AS F
    JOIN (
        #ID가 같은 상품 AMOUNT 합산
        SELECT
            PRODUCT_ID,
            SUM(AMOUNT) AS AMOUNT
        FROM
            (
                #생산일자(PRODUCE_DATE) 2022년 5월 식품들만 필터링
                SELECT
                    PRODUCT_ID,
                    AMOUNT
                FROM
                    FOOD_ORDER
                WHERE
                    DATE_FORMAT(PRODUCE_DATE, "%Y/%m") = "2022/05"
            ) AS FILTER
        GROUP BY
            PRODUCT_ID
    ) AS S ON F.PRODUCT_ID = S.PRODUCT_ID
ORDER BY
    TOTAL_SALES DESC