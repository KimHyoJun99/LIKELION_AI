USE mysql;
DROP DATABASE IF EXISTS cookDB; -- 만약 cookDB가 존재하면 우선 삭제한다.
CREATE DATABASE cookDB;

USE cookDB;
CREATE TABLE userTbl -- 회원 테이블
( userID  	CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  userName    	VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr	  	CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1	CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2	CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    	SMALLINT,  -- 키
  mDate    	DATE  -- 회원 가입일
);
CREATE TABLE buyTbl -- 회원 구매 테이블
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID  	CHAR(8) NOT NULL, -- 아이디(FK)
   prodName 	CHAR(6) NOT NULL, --  물품명
   groupName 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 단가
   amount    	SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES userTbl(userID)
);

INSERT INTO userTbl VALUES('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-8-8');
INSERT INTO userTbl VALUES('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-7-7');
INSERT INTO userTbl VALUES('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-9-9');
INSERT INTO userTbl VALUES('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-5-5');
INSERT INTO userTbl VALUES('KJD', '김제동', 1974, '경남', NULL , NULL      , 173, '2013-3-3');
INSERT INTO userTbl VALUES('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-4-4');
INSERT INTO userTbl VALUES('SDY', '신동엽', 1971, '경기', NULL , NULL      , 176, '2008-10-10');
INSERT INTO userTbl VALUES('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-4-4');
INSERT INTO userTbl VALUES('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12');
INSERT INTO userTbl VALUES('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-5-5');

INSERT INTO buyTbl VALUES(NULL, 'KHD', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'KHD', '노트북', '전자', 1000, 1);
INSERT INTO buyTbl VALUES(NULL, 'KYM', '모니터', '전자', 200,  1);
INSERT INTO buyTbl VALUES(NULL, 'PSH', '모니터', '전자', 200,  5);
INSERT INTO buyTbl VALUES(NULL, 'KHD', '청바지', '의류', 50,   3);
INSERT INTO buyTbl VALUES(NULL, 'PSH', '메모리', '전자', 80,  10);
INSERT INTO buyTbl VALUES(NULL, 'KJD', '책'    , '서적', 15,   5);
INSERT INTO buyTbl VALUES(NULL, 'LHJ', '책'    , '서적', 15,   2);
INSERT INTO buyTbl VALUES(NULL, 'LHJ', '청바지', '의류', 50,   1);
INSERT INTO buyTbl VALUES(NULL, 'PSH', '운동화', NULL   , 30,   2);
INSERT INTO buyTbl VALUES(NULL, 'LHJ', '책'    , '서적', 15,   1);
INSERT INTO buyTbl VALUES(NULL, 'PSH', '운동화', NULL   , 30,   2);

SELECT * FROM userTbl;
SELECT * FROM buyTbl;

SELECT * FROM userTBL WHERE userName = '강호동';

# 조건 연산자와 관계 연산자
SELECT userID, userName FROM userTBL WHERE birthYear >= 1970 and height >= 182;
SELECT userID, userName FROM userTBL WHERE birthYear >= 1970 or height >= 182;

# BEETWEEN ... AND, IN(), LIKE
SELECT userName, height FROM userTBL WHERE height >= 180 and height <= 182;
SELECT userName, height FROM userTBL WHERE height BETWEEN 180 and 182;

SELECT userName, addr FROM userTBL WHERE addr='경남' or addr='충남' or addr='경북';
SELECT userName, addr FROM userTBL WHERE addr IN('경남', '충남', '경북');

SELECT userName, height FROM userTBL WHERE userName LIKE '김%';

SELECT userName, height FROM userTBL WHERE userName LIKE '_경규';

# 서브쿼리와 ANY, ALL, SOME 연산자
SELECT userName height FROM userTBL WHERE height > 177;
SELECT userName height FROM userTBL WHERE height > (SELECT height FROM userTBL WHERE userName='김용만');

SELECT userName, height FROM userTBL WHERE height >= (SELECT height FROM userTBL WHERE addr='경기');  # subquery returns more than 1 row
SELECT userName, height FROM userTBL WHERE height >= ANY (SELECT height FROM userTBL WHERE addr='경기');

# ORDER BY
SELECT userName, mDate FROM userTBL ORDER BY mDate;
SELECT userName, mDate FROM userTBL ORDER BY mDate DESC;

SELECT userName, height FROM userTBL ORDER BY height DESC, userName ASC;

# DISTINCT
SELECT addr FROM userTBL;
SELECT addr FROM userTBL ORDER BY addr;

SELECT DISTINCT addr FROM userTBL;

# LIMIT
USE employees;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC;

SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 5;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 0, 5;  # OFFSET 0

# CREATE TABLE ... SELECT, 기본키와 외래키 등의 제약 조건은 복사되지 않음
CREATE TABLE buyTBL2 (SELECT * FROM buyTBL);
SELECT * FROM buyTBL2;

CREATE TABLE buyTBL3 (SELECT userID, prodName FROM buyTBL);
SELECT * FROM buyTBL3;

# GROUP BY
SELECT userID, amount FROM buyTBL ORDER BY userID;

SELECT userID, SUM(amount) FROM buyTBL GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'
FROM buyTBL GROUP BY userID;

SELECT userID AS '사용자 아이디', SUM(price * amount) AS '총 구매액'
FROM buyTBL GROUP BY userID;