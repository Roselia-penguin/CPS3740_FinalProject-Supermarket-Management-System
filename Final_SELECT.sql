-- SELECT * FROM client;
-- SELECT * FROM goods;
-- SELECT * FROM purchase;
-- SELECT * FROM sale;

-- SELECT * FROM `purchase`
-- WHERE goods_id IN (1, 2);

-- SELECT * FROM `purchase`
-- WHERE purchase_price BETWEEN 10.00 AND 20.00;

-- SELECT * FROM `client`
-- WHERE email LIKE '%@hi.com';

/* SELECT purchase_id, goods_id, purchase_price, purchase_number, purchase_money, purchase_date
FROM `purchase`
UNION
SELECT sale_id, goods_id, sale_price, sale_number, sale_sum, sale_date
FROM `sale`; */

/* SELECT DISTINCT p.goods_id
FROM purchase p
INNER JOIN sale s ON p.goods_id = s.goods_id; */

/* SELECT goods_id FROM purchase
UNION
SELECT goods_id FROM sale; */

/* SELECT goods.goods_id, goods_name, purchase_id, purchase_price, purchase_number, purchase_money, purchase_date
FROM goods
LEFT OUTER JOIN purchase ON goods.goods_id = purchase.goods_id; */

/*SELECT sale.sale_id, client_name, sale_price, sale_number, sale_sum, sale_date
FROM client
RIGHT OUTER JOIN sale ON client.client_id = sale.client_id;*/

/* SELECT client.client_id, client_name, sale_id, sale_price, sale_number, sale_sum, sale_date
FROM client
LEFT OUTER JOIN sale ON client.client_id = sale.client_id;*/

/*
SELECT SUM(sale_sum) AS total_sale_amount
FROM sale
WHERE client_id = (
    SELECT client_id
    FROM client
    WHERE client_name = 'li'
);*/

/* SELECT client_id
FROM client
WHERE client_name = 'huang';*/

/*SELECT client_name, email
FROM client
WHERE client_id IN (
    SELECT DISTINCT client_id
    FROM sale
);*/

/* SELECT g.goods_id, g.goods_name, SUM(p.purchase_money) AS total_purchase_money
FROM goods g
JOIN purchase p ON g.goods_id = p.goods_id
GROUP BY g.goods_id, g.goods_name; */

/* SELECT c.client_id, c.client_name, SUM(s.sale_sum) AS total_sales
FROM client c
JOIN sale s ON c.client_id = s.client_id
GROUP BY c.client_id
HAVING total_sales > 10;*/

/*CREATE VIEW client_purchase_view AS
SELECT c.client_id, c.client_name, p.purchase_id, p.purchase_price, p.purchase_number, p.purchase_money,
       g.goods_id, g.goods_name
FROM client c
JOIN sale s ON c.client_id = s.client_id
JOIN purchase p ON s.goods_id = p.goods_id
JOIN goods g ON p.goods_id = g.goods_id; 

SELECT * FROM client_purchase_view;*/

/* CREATE VIEW sale_goods_client_view AS
SELECT s.sale_id, s.sale_price, s.sale_number, s.sale_sum,
       g.goods_id, g.goods_name, g.Production_place,
       c.client_id, c.client_name, c.mobile, c.home_address, c.email
FROM sale s
JOIN goods g ON s.goods_id = g.goods_id
JOIN client c ON s.client_id = c.client_id;

SELECT * FROM sale_goods_client_view; */

/*
DELIMITER //
CREATE PROCEDURE update_purchase_total()
BEGIN
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE purchase_id_val INT(10);
    DECLARE purchase_price_val DECIMAL(6,2);
    DECLARE purchase_number_val INT;
    
    DECLARE purchase_cursor CURSOR FOR
        SELECT purchase_id, purchase_price, purchase_number
        FROM purchase;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    OPEN purchase_cursor;
    
    read_loop: LOOP
        FETCH purchase_cursor INTO purchase_id_val, purchase_price_val, purchase_number_val;
        
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Perform any calculations or updates here
        -- For example, you can update the total in the purchase table
        UPDATE purchase
        SET purchase_money = purchase_price_val * purchase_number_val
        WHERE purchase_id = purchase_id_val;
    END LOOP;
    
    CLOSE purchase_cursor;
END //
DELIMITER ; */

/*
-- Trigger
DELIMITER //
CREATE TRIGGER update_purchase_money
AFTER INSERT ON purchase
FOR EACH ROW
BEGIN
  UPDATE purchase SET purchase_money = NEW.purchase_price * NEW.purchase_number WHERE purchase_id = NEW.purchase_id;
END;
//
DELIMITER ; */

