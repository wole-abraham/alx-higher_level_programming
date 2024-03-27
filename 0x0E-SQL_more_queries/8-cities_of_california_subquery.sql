-- sscripts that list all the cities of california that can be found in the database
SELECT * cities WHERE state_id = (SELECT * FROM states WHERE name = 'california') ORDER BY id ASC;

