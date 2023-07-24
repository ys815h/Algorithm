-- 조건 1. 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty 인 동물
-- ANIMAL_ID	NAME	SEX_UPON_INTAKE 조회
-- 결과는 아이디 순으로 조회

-- SELECT * FROM ANIMAL_INS

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID