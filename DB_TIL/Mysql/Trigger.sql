# 트리거(trigger)
# 테이블에 부착되어 테이블에 INSERT(삽입), UPDATE(수정), DELETE(삭제) event가 발생하면 실행되는 코드
# 만약 memberTBL에서 토마스의 정보를 삭제하면, 나중에 회원 탈퇴를 한 사람인지 알 수 없음
# 트리거를 사용하여 삭제 작업이 일어날 때 다른 곳에 그 데이터를 '자동으로' 저장

# 데이터를 삽입, 수정, 삭제하는 SQL 문
INSERT INTO memberTBL VALUES ('Soccer', '흥민', '서울시 서대문구 북가좌동');
SELECT * FROM memberTBL;

UPDATE memberTBL SET memberAddress = '서울 강남구 역삼동' WHERE memberName = '흥민';
SELECT * FROM memberTBL;

DELETE FROM memberTBL WHERE memberName = '흥민';
SELECT * FROM memberTBL;

# 삭제된 데이터를 보관할 테이블 생성
CREATE TABLE deletedMemberTBL
(memberID char(8),
memberName char(5),
memberAddress char(20),
deletedDate date  # 삭제한 날짜
);

# 삭제된 데이터가 기뢱되는 트리거 생성
DELIMITER //
CREATE TRIGGER trg_deletedMemberTBL
	AFTER DELETE  # 삭제 후에 작동
    ON memberTBL  # 트리거를 부착할 테이블
    FOR EACH ROW  # 각 행마다 적용
BEGIN
	# OLD 테이블의 내용을 백업 테이블에 삽입
	INSERT INTO deletedMemberTBL
		VALUES(OLD.memberID, OLD.memberName, OLD.memberAddress, CURATED());
END //
DELIMITER ;

