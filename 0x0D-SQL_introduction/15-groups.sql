-- Script for counting the number each score come
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
