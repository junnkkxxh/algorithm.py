-- SELECT
-- 3월에 태어난 여성 회원 목록 출력하기
SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM
    MEMBER_PROFILE
WHERE
    DATE_OF_BIRTH LIKE '_____03%' -- MONTH(DATE_OF_BITRH) = 3
    AND GENDER = 'W'
    AND TLNO IS NOT NULL
ORDER BY
    MEMBER_ID