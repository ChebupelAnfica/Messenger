"""Initial migration

Revision ID: ef25245372c4
Revises: 4d7a516f35b1
Create Date: 2025-04-04 07:55:25.549212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef25245372c4'
down_revision: Union[str, None] = '4d7a516f35b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
