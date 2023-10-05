# 스토어드 프로시저(stored procedure)
# SQL 문을 하나로 묶어 편리하게 사용하는 기능
# 반복적으로 수행해야 하는 작업을 쉽게 관리, 코드의 재사용성을 높임

SELECT * FROM memberTBL WHERE memberName = "토마스";
SELECT * FROM productTBL WHERE productName = "냉장고";

DELIMITER //  # 명령어의 끝을 나타내는 문자를 (//)로 변경
CREATE PROCEDURE myProc()
BEGIN
		SELECT * FROM memberTBL WHERE memberName = "토마스";
        SELECT * FROM productTBL WHERE productName = "냉장고";
END//
DELIMITER ;  # 명령어의 끝을 나타내는 문자를 (;)로 변경

CALL myProc()