-- Write query to get number of graded assignments for each student:
SELECT count(id)
FROM 'assignments'
WHERE grade != '';