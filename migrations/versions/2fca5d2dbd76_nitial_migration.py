"""nitial migration

Revision ID: 2fca5d2dbd76
Revises: 9b8d87ff232d
Create Date: 2025-04-05 04:17:15.735160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2fca5d2dbd76'
down_revision: Union[str, None] = '9b8d87ff232d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
