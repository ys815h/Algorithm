-- 조건 1. 이름에 "%EL%" 이 들어감
-- ANIMAL_ID	NAME 조회
-- 이름순 조회

-- SELECT * FROM ANIMAL_INS

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE UPPER(NAME) LIKE '%EL%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME