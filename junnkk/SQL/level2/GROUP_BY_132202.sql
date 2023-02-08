-- GROUP BY
-- 진료과별 총 예약 횟수 출력하기
SELECT
    MCDP_CD AS '진료과코드',
    COUNT(MCDP_CD) AS '5월예약건수'
FROM
    APPOINTMENT
WHERE
    APNT_YMD LIKE '2022-05-%'
GROUP BY
    MCDP_CD
ORDER BY
    5 월예약건수,
    진료과코드;