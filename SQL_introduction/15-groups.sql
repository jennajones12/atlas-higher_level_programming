-- computes the score average of all records in the table
-- displays the score and number of records for this score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
