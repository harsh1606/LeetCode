WITH meeting_weeks AS (
    SELECT
        employee_id,
        DATE_SUB(meeting_date, INTERVAL WEEKDAY(meeting_date) DAY) AS week_start,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY employee_id, week_start
),
meeting_heavy_weeks AS (
    SELECT
        employee_id,
        COUNT(*) AS meeting_heavy_weeks
    FROM meeting_weeks
    WHERE total_hours > 20
    GROUP BY employee_id
),
final_result AS (
    SELECT
        e.employee_id,
        e.employee_name,
        e.department,
        m.meeting_heavy_weeks
    FROM employees e
    LEFT JOIN meeting_heavy_weeks m ON e.employee_id = m.employee_id
    WHERE m.meeting_heavy_weeks >= 2
)
SELECT *
FROM final_result
ORDER BY meeting_heavy_weeks DESC, employee_name ASC;
