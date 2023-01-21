-- JOIN
-- 없어진 기록 찾기
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM
    ANIMAL_outs as O
    LEFT JOIN ANIMAL_ins as i ON i.animal_id = o.animal_id
where
    i.animal_id is null
order by
    o.ANIMal_id;