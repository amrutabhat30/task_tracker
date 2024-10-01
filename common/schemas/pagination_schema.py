from typing import Optional
from pydantic import BaseModel, conint

class PaginationSchema(BaseModel):
    """
    Schema for pagination parameters.

    Attributes:
        page (Optional[conint(ge=0)]):
            The page number for the paginated results. Must be 0 or greater.
            Defaults to 1 if not provided.

        limit (Optional[conint(gt=0)]):
            The maximum number of items per page. Must be greater than 0.
            Defaults to 10 if not provided.
    """
    page: Optional[conint(ge=0)] = 1  # Page must be 0 or greater
    limit: Optional[conint(gt=0)] = 10  # Limit must be greater than 0