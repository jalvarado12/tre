CREATE TABLE region(
	id_region char(5),
	name varchar(45),
		PRIMARY KEY(id_region)
);

CREATE TABLE country (
	id_country char(2),
	name varchar(45) NOT NULL,
	id_region_region char(5),
		PRIMARY KEY(id_country),
		FOREIGN KEY(id_region_region)
			REFERENCES region(id_region)
);

CREATE TABLE report (
	id_report serial,
	date date NOT NULL,
	new_cases int NOT NULL,
	cumulative_cases int NOT NULL,
	new_deaths int NOT NULL,
	cumulative_deaths int NOT NULL,
	id_country_country char(2),
		PRIMARY KEY(id_report),
		FOREIGN KEY(id_country_country)
			REFERENCES country(id_country)
);

COPY country FROM 'C:\Nueva carpeta\covid19countries.csv' WITH DELIMITER ';' CSV HEADER;
COPY region FROM 'C:\Nueva carpeta\datos_originales.csv' WITH DELIMITER ';' CSV HEADER;
COPY report(date,id_country_country,new_cases,cumulative_cases,new_deaths,cumulative_deaths) FROM 'C:\Nueva carpeta\covid19.csv' WITH DELIMITER ';' CSV HEADER;
