-- Criar tabela de cidadãos de Norktown
CREATE TABLE IF NOT EXISTS customer (
    id SERIAL,
    name VARCHAR(50) NOT NULL,
    idcity VARCHAR(9) NOT NULL,
    phone VARCHAR(16),
    sale_opportunity INTEGER
);

-- Adicionar constraint de PK.
ALTER TABLE customer ADD CONSTRAINT pk_customer PRIMARY KEY (id);

-- Adicionar constraint unique do CPF.
ALTER TABLE customer ADD CONSTRAINT unique_idcity UNIQUE (idcity);

-- Criar tabela de veículos
CREATE TABLE IF NOT EXISTS vehicle(
    id INTEGER PRIMARY KEY,
    name VARCHAR(15),
    model VARCHAR (11),
    color VARCHAR (10),
    customer_id INTEGER
);

-- Adiciona constraint de FK.
ALTER TABLE vehicle ADD CONSTRAINT fk_vehicle_customer FOREIGN KEY (customer_id) REFERENCES customer;

-- Adiciona constraint para manter o campo de modelo com valores válidos (1-hatch, 2-sedan, 3-convertible).
ALTER TABLE vehicle ADD CONSTRAINT check_model CHECK (model IN ('hatch', 'sedan', 'convertible'));

-- Adiciona constraint para manter o campo de cor com valores válidos (1-yellow, 2-blue, 3-gray).
ALTER TABLE vehicle ADD CONSTRAINT check_color CHECK (color IN ('yellow', 'blue', 'gray'));

-- Trigger para que não seja possível existir mais de três carros para um mesmo cidadão.
-- Trigger é disparada após inserção de registro de veículo.
CREATE OR REPLACE FUNCTION fn_check_vehicle_per_customer()
  RETURNS trigger AS
$$
BEGIN
    IF ((SELECT count(*) FROM vehicle WHERE id = NEW.id) >= 3) THEN RETURN NULL;
    END IF;
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';
CREATE TRIGGER trigger_check_vehicle_per_citizen
    BEFORE INSERT ON "vehicle"
    FOR EACH ROW EXECUTE PROCEDURE fn_check_vehicle_per_customer();



-- Tuplas iniciais:
INSERT INTO customer (id,name, idcity, phone, sale_opportunity) VALUES (0,'Carlos Alberto', 'VRU909012','12912344321', 1);
INSERT INTO customer (id,name, idcity, phone, sale_opportunity) VALUES (1,'Gustavo Costa', 'HPD242401','12912344321', 1);
INSERT INTO customer (id,name, idcity, phone, sale_opportunity) VALUES (2,'Anderson Silva', 'KAS802421','12912344321', 0);

INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (0,'Palio', 'hatch','yellow', 1);
INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (1,'Fiesta', 'sedan', 'blue', 0);
INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (2,'Camaro', 'convertible','yellow', 2);
INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (3,'Ranger', 'sedan','gray', 1);
INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (4,'Porshe', 'sedan','blue', 1);
INSERT INTO vehicle (id,name, model, color, customer_id) VALUES (5,'Toro', 'hatch','yellow', 2);