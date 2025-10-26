DELETE FROM grades
WHERE score < 60
  AND date < '2025-10-08';
