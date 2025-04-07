"""nitial migration

Revision ID: bb9926e5a53c
Revises: a673390cad75
Create Date: 2025-04-05 04:05:27.593976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb9926e5a53c'
down_revision: Union[str, None] = 'a673390cad75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
