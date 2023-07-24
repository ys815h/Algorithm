-- 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별
-- CATEGORY, PRODUCTS(상품 개수) 조회
-- PRODUCT_CODE 기준 오름차순

SELECT SUBSTR(PRODUCT_CODE, 1, 2) AS CATEGORY, COUNT(*) AS PRODUCTS FROM PRODUCT
GROUP BY SUBSTR(PRODUCT_CODE, 1, 2)
ORDER BY SUBSTR(PRODUCT_CODE, 1, 2)
