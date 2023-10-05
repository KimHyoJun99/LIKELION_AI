# 뷰(view)
# 가상의 테이블
# 실체가 없고 진짜 테이블에 연결(link)된 개념
# 뷰를 SELECT 문으로 조회하면 진짜 테이블의 데이터를 조회하는 것과 동일한 결과가 나옴

CREATE VIEW uv_memberTBL 
AS
	SELECT memberName, memberAddress FROM memberTBL;
    
SELECT * FROM uv_memberTBL;