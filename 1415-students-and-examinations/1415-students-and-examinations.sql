select A.Student_id, A.student_name, B.subject_name,
#COALESCE(COUNT(e.student_id), 0) AS attended_exams
COALESCE(count(C.student_id),0) as attended_exams
from Students as A
cross join Subjects as B
left join Examinations as C
on A.Student_id = C.student_id
and B.subject_name = C.subject_name
group by A.Student_id, A.student_name, B.subject_name
order by A.Student_id, A.student_name
