from sqlalchemy import select, text


text("select * from resumes;")
text("select workload avg(compensation)::int as avg_compensation"
     "from resumes"
     "where title LIKE '%python%' and compensation > 40000"
     "group by workload")
