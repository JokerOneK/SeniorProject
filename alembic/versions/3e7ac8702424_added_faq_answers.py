"""added faq answers

Revision ID: 3e7ac8702424
Revises: f352d90aaeff
Create Date: 2024-04-10 11:42:55.716615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e7ac8702424'
down_revision: Union[str, None] = 'f352d90aaeff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('frequently_asked_question', sa.Column('answer', sa.String()))


def downgrade() -> None:
    op.drop_column('frequently_asked_question', 'answer')
