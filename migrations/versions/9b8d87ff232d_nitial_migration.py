"""nitial migration

Revision ID: 9b8d87ff232d
Revises: bb9926e5a53c
Create Date: 2025-04-05 04:07:59.818438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b8d87ff232d'
down_revision: Union[str, None] = 'bb9926e5a53c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
