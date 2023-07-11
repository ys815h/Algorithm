-- 조건 1. 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty
-- 동물의 아이디와 이름, 성별 및 중성화 여부를 조회 (아이디 순으로 조회)
-- ANIMAL_ID, NAME, SEX_UPON_INTAKE

-- SELECT * FROM ANIMAL_INS

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = 'Lucy'
OR NAME = 'Ella'
OR NAME = 'Pickle'
OR NAME = 'Rogan'
OR NAME = 'Sabrina'
OR NAME = 'Mitty'
ORDER BY ANIMAL_ID
