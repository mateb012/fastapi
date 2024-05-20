"""add cols

Revision ID: 8c4bf55ad06d
Revises: a4a63b685787
Create Date: 2024-05-20 18:35:35.030169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c4bf55ad06d'
down_revision: Union[str, None] = 'a4a63b685787'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    op.add_column("posts", sa.Column("title", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
    op.drop_column("posts", "title")
