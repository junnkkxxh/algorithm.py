-- SELECT
-- 조건에 맞는 회원수 구하기
SELECT
    COUNT(USER_ID) AS USERS
FROM
    USER_INFO
WHERE
    JOINED LIKE '2021%'
    and AGE >= 20
    and AGE <= 29;
    -- AGE BETWEEN 20 and 29