"""nitial migration

Revision ID: a673390cad75
Revises: ef25245372c4
Create Date: 2025-04-05 04:04:58.880979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a673390cad75'
down_revision: Union[str, None] = 'ef25245372c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
