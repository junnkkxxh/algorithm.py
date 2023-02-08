-- String, Date
-- 자동차 대여 기록에서 장기/단기 대여 구분하기
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    IF(
        DATEDIFF(END_DATE, START_DATE) + 1 >= 30,
        '장기 대여',
        '단기 대여'
    ) AS RENT_TYPE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE LIKE '2022-09-%'
ORDER BY
    HISTORY_ID DESC;




------ 날짜 차이는 DATEDIFF(->단순 일 차이) 혹은 TIMESTAMPDIFF
-- SELECT DATEDIFF(start_date, end_date),start_date- end_date 
-- FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY ;