"""add posts cols

Revision ID: d9b68b499557
Revises: d12107204695
Create Date: 2024-05-20 19:01:02.898752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9b68b499557'
down_revision: Union[str, None] = 'd12107204695'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column("posts", sa.Column(
        "created_at", sa.TIMESTAMP(
            timezone=True), server_default=sa.text('now()'), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
