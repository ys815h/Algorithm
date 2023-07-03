-- 조건 1. 2022-05에 진료예약일시(APNT_YMD)
-- '진료과코드', '5월예약건수'로 컬러명 지정

-- 진료과별(MCDP_CD) 예약한 환자 수(5월예약건수)를 기준 오름차순
-- , 환자수 같을경우 진료과 코드(MCDP_CD) 기준 오름차순
-- 한글 Alias에는 반드시 더블쿼테이션("")을 붙여야 함

SELECT MCDP_CD AS "진료과코드", COUNT(MCDP_CD) AS "5월예약건수" FROM APPOINTMENT
WHERE TO_CHAR(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY MCDP_CD
ORDER BY "5월예약건수", "진료과코드"


-- SELECT TO_CHAR(APNT_YMD, 'YYYY-MM'), MCDP_CD FROM APPOINTMENT