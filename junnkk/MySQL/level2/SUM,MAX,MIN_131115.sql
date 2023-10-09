-- SUM, MAX, MIN
-- 가격이 제일 비싼 식품의 정보 출력하기

--
-- 방법 1. MAX 사용
SELECT
    *
FROM
    FOOD_PRODUCT
WHERE
    PRICE = (
        SELECT
            MAX(PRICE)
        FROM
            FOOD_PRODUCT
    );

--
-- 방법2. ORDER BY와 LIMIT 사용
SELECT
    *
FROM
    FOOD_PRODUCT
ORDER BY
    PRICE DESC
LIMIT
    1;


-- 실패 1.
-- 가장 첫 번째 행의 식품 ID, 식품 이름, 식품 코드, 식품분류가 나오고 테이블에서 가격의 최댓값이 나온다.
-- SELECT
--     PRODUCT_ID,
--     PRODUCT_NAME,
--     PRODUCT_CD,
--     CATEGORY,
--     MAX(PRICE) AS PRICE
-- FROM
--     FOOD_PRODUCT;
