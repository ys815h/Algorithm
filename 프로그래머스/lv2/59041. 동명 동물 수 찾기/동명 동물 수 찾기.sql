-- 조건 1.동물 이름 중 두 번 이상 쓰인 이름, 해당 이름이 쓰인 횟수를 조회
-- NAME, COUNT
-- 결과는 이름 순으로 조회

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME