-- String, Date
-- 자동차 대여 기록 별 대여 금액 구하기
SELECT
    HISTORY_ID,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 7
        AND 29 THEN FLOOR(
            (DATEDIFF(END_DATE, START_DATE) + 1) * b.DAILY_FEE * 0.95
        )
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 BETWEEN 30
        AND 89 THEN FLOOR(
            (DATEDIFF(END_DATE, START_DATE) + 1) * b.DAILY_FEE * 0.03
        )
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 90 THEN FLOOR(
            (DATEDIFF(END_DATE, START_DATE) + 1) * b.DAILY_FEE * 0.9
        )
        ELSE FLOOR((DATEDIFF(END_DATE, START_DATE) + 1) * b.DAILY_FEE)
    END AS FEE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY a
    JOIN CAR_RENTAL_COMPANY_CAR b ON a.CAR_ID = b.CAR_ID
WHERE
    b.CAR_TYPE = '트럭'
ORDER BY
    FEE DESC,
    HISTORY_ID DESC;