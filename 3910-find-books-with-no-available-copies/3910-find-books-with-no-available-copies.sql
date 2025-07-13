select book_id, title, author, genre,publication_year, 
total_copies as current_borrowers 
from library_books 
where (book_id, total_copies) in 
            (select book_id, count(1) as no_of_borrowed_books
            from borrowing_records 
            where return_date is null
            group by book_id)
order by total_copies desc, title;
            