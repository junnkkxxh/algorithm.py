-- String, Date
-- 취소되지 않은 진료 예약 조회하기
SELECT
    a.APNT_NO,
    b.PT_NAME,
    a.PT_NO,
    a.MCDP_CD,
    c.DR_NAME,
    a.APNT_YMD
FROM
    (
        APPOINTMENT a
        JOIN PATIENT b ON a.PT_NO = b.PT_NO
    )
    JOIN DOCTOR c ON a.MDDR_ID = c.DR_ID
WHERE
    a.APNT_YMD LIKE '2022-04-13%'
    AND a.APNT_CNCL_YN = 'N'
    AND a.MCDP_CD = 'CS'
ORDER BY
    a.APNT_YMD;