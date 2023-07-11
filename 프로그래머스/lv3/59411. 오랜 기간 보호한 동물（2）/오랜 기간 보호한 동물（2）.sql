-- 조건 1. 입양을 간 동물 중
-- 조건 2. 보호 기간이 가장 길었던 동물 두 마리
-- 아이디와 이름을 조회 (보호 기간이 긴 순으로 조회)

SELECT B.ANIMAL_ID, B.NAME
FROM (
    SELECT ROWNUM, A.*
    FROM (
        SELECT TO_DATE(O.DATETIME) - TO_DATE(I.DATETIME) AS CARE, I.NAME, I.ANIMAL_ID
        FROM ANIMAL_INS I JOIN ANIMAL_OUTS O
        ON I.ANIMAL_ID = O.ANIMAL_ID
        WHERE I.DATETIME < O.DATETIME
        ORDER BY CARE DESC
    ) A
) B
WHERE ROWNUM BETWEEN 1 AND 2