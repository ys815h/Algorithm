-- 조건 1.  '통풍시트', '열선시트', '가죽시트' 옵션 하나 이상 포함
-- 자동차 종류 별, 수량(CARS)
-- 자동차 종류별 오름차순

SELECT CAR_TYPE, COUNT(CAR_TYPE) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE

 