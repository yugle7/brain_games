MAX_TITLE_LEN = 100
MAX_SLUG_LEN = 100
MAX_QUERY_LEN = 100

SORT_BY = {
    'person': (
        (1, 'rating'),
        (2, 'contribution'),
        (3, 'money'),
        (4, 'last_visit_time'),
        (5, 'date_joined'),
        (6, 'puzzles_author'),
        (7, 'puzzles_author'),
        (8, 'reviews_opened'),
        (9, 'reviews_closed'),
    ),
    'discuss': (
        (1, 'comments_count'),
        (2, 'update_time')
    ),
    'poll': (
        (1, 'persons_count'),
        (2, 'time_update'),
    ),
    'puzzle': (
        (1, 'weight'),
        (2, 'create_time'),
        (3, 'solved_count'),
        (4, 'interest'),
        (5, 'complexity'),
    )
}

COMMENT_KIND = (
    (1, 'public'),
    (2, 'private'),
    (3, 'closed'),
)
