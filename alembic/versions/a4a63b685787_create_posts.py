"""create posts

Revision ID: a4a63b685787
Revises: 
Create Date: 2024-05-20 18:24:14.751302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a4a63b685787'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts", sa.Column(
        "id", sa.Integer(), nullable=False, primary_key=True))


def downgrade() -> None:
    op.drop_table("posts")
