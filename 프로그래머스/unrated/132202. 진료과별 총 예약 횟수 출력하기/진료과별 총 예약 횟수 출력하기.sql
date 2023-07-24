-- 조건 1. APNT_YMD = 2022년 5월, 진료과코드 별 조회
-- 조건 2. 컬럼명은 '진료과 코드', '5월예약건수'로 지정
-- 예약한 환자 수를 기준으로 오름차순 정렬, 진료과 코드를 기준으로 오름차순 정렬

-- SELECT * FROM APPOINTMENT
 --  
 
SELECT MCDP_CD AS "진료과코드", COUNT(MCDP_CD) AS "5월예약건수"
FROM APPOINTMENT
WHERE TO_CHAR(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과코드"