USE project;

CREATE TABLE `client`(
	client_id INT(10) NOT NULL,
	client_name VARCHAR(20) NOT NULL,
	mobile VARCHAR(20) NOT NULL,
	home_address VARCHAR(30) NOT NULL,
	email VARCHAR(30) NOT NULL,
	PRIMARY KEY(client_id),
	UNIQUE(mobile)
);

INSERT INTO `client` VALUES (1, 'huang', '111222333', 'daxue Road', 'huang@hi.com');
INSERT INTO `client` VALUES (2, 'li', '444555666', 'daxue Road', 'li@hi.com');
INSERT INTO `client` VALUES (3, 'niu', '777888999', 'daxue Road', 'niu@hi.com');

CREATE TABLE `goods`(  
	goods_id INT(10) NOT NULL,
	goods_barcode VARCHAR(20) NOT NULL,
    goods_name VARCHAR(20) NOT NULL,
	Production_place VARCHAR(30) NOT NULL,
	PRIMARY KEY(goods_id)
);

INSERT INTO `goods` VALUES (1, '1111111', 'milk', 'Beijing');
INSERT INTO `goods` VALUES (2, '2222222', 'soap', 'Shanghai');
INSERT INTO `goods` VALUES (3, '3333333', 'banana', 'Guang xi');

CREATE TABLE `purchase`(
	purchase_id INT(10) NOT NULL,
    goods_id INT(10) NOT NULL,
    purchase_price DECIMAL(6,2) NOT NULL CHECK( purchase_price >= 0),
    purchase_number INT NOT NULL CHECK( purchase_number >= 0),
    purchase_money DECIMAL(8,2) GENERATED ALWAYS AS (purchase_price * purchase_number) STORED NOT NULL,
    purchase_date DATE NOT NULL,
    PRIMARY KEY(purchase_id),
    FOREIGN KEY (goods_id) REFERENCES goods(goods_id)
);

INSERT INTO `purchase` VALUES (1, 3, 3.00, 3, DEFAULT,'2023-12-01');
INSERT INTO `purchase` VALUES (2, 2, 12.00, 2, DEFAULT, '2023-12-02');
INSERT INTO `purchase` VALUES (3, 1, 18.00, 5, DEFAULT, '2023-12-03');

CREATE TABLE `sale`(
	sale_id INT(10) NOT NULL,
    goods_id INT(10) NOT NULL,
	client_id INT(10) NOT NULL,
    sale_price DECIMAL(6,2) NOT NULL CHECK( sale_price >= 0),
	sale_number INT NOT NULL CHECK( sale_number >= 0),
	sale_sum DECIMAL(8,2) GENERATED ALWAYS AS (sale_price * sale_number) STORED NOT NULL,
    sale_date DATE NOT NULL,
	PRIMARY KEY(sale_id),
	FOREIGN KEY (goods_id) REFERENCES goods(goods_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

INSERT INTO `sale` VALUES (1, 3, 1, 4.00, 1, DEFAULT,'2023-12-11');
INSERT INTO `sale` VALUES (2, 2, 2, 15.00, 2, DEFAULT, '2023-12-12');
INSERT INTO `sale` VALUES (3, 1, 3, 22.00, 1, DEFAULT, '2023-12-13');




