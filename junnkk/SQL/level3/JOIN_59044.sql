-- JOIN
-- 오랜 기간 보호한 동물(1)
SELECT
    i.name,
    i.datetime
from
    animal_ins as i
    left join animal_outs as o on i.animal_id = o.animal_id
where
    o.animal_id is null
order by
    i.datetime
limit
    3;