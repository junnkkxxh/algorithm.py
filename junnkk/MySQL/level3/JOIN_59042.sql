-- JOIN
-- 있었는데요 없었습니다
SELECT
    o.animal_id,
    o.name
from
    animal_outs as o
    inner join animal_ins as i on o.animal_id = i.animal_id
where
    o.datetime < i.datetime
order by
    i.datetime;