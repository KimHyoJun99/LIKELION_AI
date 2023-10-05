SELECT * FROM productTBL;

# Index
CREATE INDEX idx_productTBL on productTBL(productName);
SELECT * FROM productTBL WHERE productName = '냉장고';

# View
CREATE VIEW uv_productTBL
as
	SELECT productName, company FROM productTBL;

SELECT * FROM uv_productTBL

# Stored Procedure
DELIMITER //
CREATE PROCEDURE Proc()
BEGIN
	INSERT INTO productTBL VALUES('티비', 30, '2020-09-17', 'LG', 9);
END //
DELIMITER ;

CALL Proc();

SELECT * FROM productTBL;