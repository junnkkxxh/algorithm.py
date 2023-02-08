-- JOIN
-- 상품 별 오프라인 매출 구하기
SELECT
    p.PRODUCT_CODE,
    sum(o.SALES_AMOUNT) * p.price AS SALES
FROM
    OFFLINE_SALE o
    JOIN PRODUCT p ON o.product_ID = p.product_id
GROUP BY
    p.PRODUCT_ID
ORDER BY
    SALES DESC,
    p.PRODUCT_CODE;