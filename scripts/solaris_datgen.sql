SET @insert_sum = 0;

CREATE TABLE admins (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_active BIT NOT NULL,
    is_superuser BIT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT admin_is_active_chk CHECK (is_active IN (0, 1)),
    CONSTRAINT admin_is_superuser_chk CHECK (is_superuser IN (0, 1)),
    CONSTRAINT admin_name_chk CHECK (name <> ''),
    CONSTRAINT admin_email_chk CHECK (email <> ''),
    CONSTRAINT admin_password_chk CHECK (password <> '')
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    kwargs JSON,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT client_name_chk CHECK (name <> ''),
    CONSTRAINT client_email_chk CHECK (email <> '')
);

-- PROCEDURES
CREATE PROCEDURE insert_admin(
    IN name VARCHAR(255),
    IN email VARCHAR(255),
    IN password VARCHAR(255),
    IN is_active BIT,
    IN is_superuser BIT
) BEGIN
    INSERT INTO admins (name, email, password, is_active, is_superuser)
    VALUES (name, email, password, is_active, is_superuser);
END;


CREATE PROCEDURE insert_client(
    IN name VARCHAR(255),
    IN email VARCHAR(255),
    IN kwargs JSON
) BEGIN
    INSERT INTO clients (name, email, kwargs)
    VALUES (name, email, kwargs);
END;


-- TRIGGERS
CREATE TRIGGER admin_insert_trigger BEFORE INSERT ON admins
    FOR EACH ROW
    BEGIN
        SET @insert_sum = @insert_sum + 1;
        SET NEW.id = @insert_sum;
    END;


CREATE TRIGGER client_insert_trigger BEFORE INSERT ON clients
    FOR EACH ROW
    BEGIN
        SET @insert_sum = @insert_sum + 1;
        SET NEW.id = @insert_sum;
    END;


-- VIEWS
CREATE VIEW admins_view AS
    SELECT
        id,
        name,
        email,
        password,
        is_active,
        is_superuser,
        created_at,
        updated_at
    FROM admins;


CREATE VIEW clients_view AS
    SELECT
        id,
        name,
        email,
        kwargs,
        created_at,
        updated_at
    FROM clients;