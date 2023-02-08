-- JOIN
-- 주문량이 많은 아이스크림들 조회하기
SELECT
    f.FLAVOR
FROM
    FIRST_HALF f
    JOIN (
        SELECT
            FLAVOR,
            SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM
            JULY
        GROUP BY
            FLAVOR
    ) j ON f.FLAVOR = j.FLAVOR
ORDER BY
    f.TOTAL_ORDER + j.TOTAL_ORDER DESC
LIMIT
    3;