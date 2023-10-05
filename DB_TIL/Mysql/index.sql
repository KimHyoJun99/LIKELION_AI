# 인덱스(index)

# employees 데이터 불러오고 확인하기
CREATE TABLE indexTBL (first_name varchar(14), last_name varchar(16), hire_date date);
INSERT INTO indexTBL 
	SELECT first_name, last_name, hire_date 
    FROM employees.employees 
    LIMIT 500;

SELECT * FROM indexTBL;

# 인덱스가 없는 상태에서 쿼리 작동 확인
SELECT * FROM indexTBL WHERE first_name = "Mary";

# 인덱스 생성 후 쿼리 작동 확인
# Non-Unique key Lookup으로 변경된 것을 확인, 속도 측면에서 효율적임
CREATE INDEX idx_indexTBL_firstname ON indexTBL(first_name);

SELECT * FROM indexTBL WHERE first_name = "Mary"; 