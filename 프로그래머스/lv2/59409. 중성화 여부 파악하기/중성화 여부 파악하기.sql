-- ANIMAL_ID	NAME	중성화(SEX_UPON_INTAKE) -> 아이디 순으로 조회하
-- 조건 1. Neutered Male OR Spayed Female 있으면 O, 아니면 X
-- SELECT * FROM ANIMAL_INS


SELECT ANIMAL_ID, NAME
, DECODE(SEX_UPON_INTAKE, 'Neutered Male', 'O'
         , DECODE(SEX_UPON_INTAKE, 'Spayed Female', 'O', 'X')) AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- SELECT * FROM ANIMAL_INS
-- WHERE SEX_UPON_INTAKE = 'Intact Male'