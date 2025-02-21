from math import ceil


def paginate(Model, page, per_page, data):
    total_users = Model.query.count()
    total_pages = ceil(total_users / per_page)
    offset = (page - 1) * per_page
    users = Model.query.limit(per_page).offset(offset).all()

    has_prev = page > 1
    has_next = page < total_pages

    return {
        "data": users,
        "totalPages": total_pages,
        "has_prev": has_prev,
        "has_next": has_next,
        "per_page": per_page,
        "next_link": (f"?page={page + 1}&per_page={per_page}" if has_next else None),
        "prev_link": (f"?page={page - 1}&per_page={per_page}" if has_prev else None),
    }
