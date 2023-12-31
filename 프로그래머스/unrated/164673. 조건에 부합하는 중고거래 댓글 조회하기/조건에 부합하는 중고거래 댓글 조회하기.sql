 -- 댓글 작성일 기준 오름차순, 같으면 게시글 제목을 기준으로 오름차순
 -- 조건 1. 2022년 10월에 작성된 게시글 리스트 가져오기

 SELECT B.TITLE, R.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, TO_CHAR(R.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE
 FROM USED_GOODS_BOARD B JOIN USED_GOODS_REPLY R
 ON B.BOARD_ID = R.BOARD_ID
 WHERE TO_CHAR(B.CREATED_DATE, 'YYYY-MM-DD') LIKE '2022-10%'
 ORDER BY CREATED_DATE ASC, TITLE ASC;
