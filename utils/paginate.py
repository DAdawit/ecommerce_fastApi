from typing import Any, Dict, List

from sqlalchemy import func
from sqlalchemy.orm import Query, Session


def paginate(
    query: Query, db: Session, page: int = 1, per_page: int = 1
) -> Dict[str, Any]:
    """
    Paginate a SQLAlchemy query, supporting related table joins.

    :param query: The SQLAlchemy query builder.
    :param db: The SQLAlchemy session.
    :param page: The current page number.
    :param per_page: The number of items per page.
    :return: Paginated data with metadata.
    """
    offset = (page - 1) * per_page

    # Get total count
    total = db.query(func.count()).select_from(query.subquery()).scalar()
    total_pages = max(1, -(-total // per_page))  # Equivalent to ceil()

    # Ensure page is within valid range
    page = max(1, min(page, total_pages))

    # Fetch paginated data
    results: List[Any] = query.offset(offset).limit(per_page).all()

    # return {"page": page, "per_page": per_page}
    has_prev = page > 1
    has_next = page < total_pages

    return {
        "data": results,
        "total": total,
        "total_pages": total_pages,
        "has_next": has_next,
        "has_prev": has_prev,
        "perPage": per_page,
        "current_page": page,
        "next_link": (
            f"/users?page={page + 1}&per_page={per_page}" if has_next else None
        ),
        "prev_link": (
            f"/users?page={page - 1}&per_page={per_page}" if has_prev else None
        ),
    }
