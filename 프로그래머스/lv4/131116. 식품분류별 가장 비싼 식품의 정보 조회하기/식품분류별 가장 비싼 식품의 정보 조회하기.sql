-- 식품분류별로 가격이 제일 비싼 식품
-- CATEGORY, MAX_PRICE, PRODUCT_NAME 조회
-- 조건 1. '과자', '김치', '식용유'
-- MAX_PRICE 기준 내림차순
-- PRODUCT_NAME

-- SELECT A.CATEGORY, A.MAX_PRICE, B.PRODUCT_NAME
-- FROM (
--     SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
--     FROM FOOD_PRODUCT
--     WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
--     GROUP BY CATEGORY
--     ORDER BY MAX_PRICE DESC
-- ) A JOIN FOOD_PRODUCT B
-- ON A.CATEGORY = B.CATEGORY AND A.MAX_PRICE = B.PRICE
-- ORDER BY A.MAX_PRICE DESC


SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT
    -- WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
    HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
    )
ORDER BY MAX_PRICE DESC