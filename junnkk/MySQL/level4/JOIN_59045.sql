-- JOIN
-- 보호소에서 중성화한 동물
SELECT
    o.animal_id,
    o.animal_type,
    o.name
from
    animal_outs as o
    inner join animal_ins as i on o.animal_id = i.animal_id
where
    i.sex_upon_intake like '%intact%'
    and (
        o.sex_upon_outcome like '%spayed%'
        or o.sex_upon_outcome like '%neutered%'
    )
order by
    o.animal_id;

-- SELECT o.animal_id, o.animal_type, o.name 
-- from animal_outs as o inner join animal_ins as i 
-- where i.animal_id = o.animal_id and i.sex_upon_intake != o.sex_upon_outcome 
-- order by o.animal_id;