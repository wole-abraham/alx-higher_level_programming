-- joins 2 tables based on their corresponding fk/pk
SELECT cities.id, cities.name AS name, states.name AS name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;

