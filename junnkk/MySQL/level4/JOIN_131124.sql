-- JOIN
-- 그룹별 조건에 맞는 식당 목록 출력하기
SELECT
    member_name,
    review_text,
    review_date
from
    rest_review as r
    inner join member_profile as m on r.member_id = m.member_id
where
    r.member_id in (
        SELECT
            D.MEMBER_ID
        FROM
            (
                # MEMBER_ID 카운트의 랭크 매기기
                SELECT
                    C.MEMBER_ID,
                    RANK() OVER (
                        ORDER BY
                            C.COUNTS DESC
                    ) AS RANKS
                FROM
                    (
                        # MEMBER_ID 당 카운트 세기
                        SELECT
                            MEMBER_ID,
                            COUNT(MEMBER_ID) AS "COUNTS"
                        FROM
                            REST_REVIEW
                        GROUP BY
                            MEMBER_ID
                    ) as C
            ) as D
        WHERE
            D.RANKS = 1
    )
order by
    r.review_date;