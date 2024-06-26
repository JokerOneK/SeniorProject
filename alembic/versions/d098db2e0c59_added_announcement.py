"""added announcement

Revision ID: d098db2e0c59
Revises: c597e4f166eb
Create Date: 2024-04-06 14:26:45.780002

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd098db2e0c59'
down_revision: Union[str, None] = 'c597e4f166eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('announcement',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id', name='announcement_pkey')
                    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('announcement')
    # ### end Alembic commands ###
