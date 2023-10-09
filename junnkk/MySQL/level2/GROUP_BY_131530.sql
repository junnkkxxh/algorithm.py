-- GROUP BY
-- 가격대 별 상품 개수 구하기
-- tuncate 활용하기
SELECT
    TRUNCATE(PRICE, -4) AS PRICE_GROUP,
    COUNT(*) AS PRODUCTS
FROM
    product
GROUP BY
    PRICE_GROUP
ORDER BY
    PRICE_GROUP 
    
-- select truncate(price, -4) from product