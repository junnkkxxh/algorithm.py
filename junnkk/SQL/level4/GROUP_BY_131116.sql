-- GROUP BY
-- 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT
    category,
    price as max_price,
    product_name
from
    food_product
where
    category in ('식용유', '국', '과자', '김치')
    and price in (
        select
            max(price)
        from
            food_product
        group by
            category
    )
order by
    price desc;