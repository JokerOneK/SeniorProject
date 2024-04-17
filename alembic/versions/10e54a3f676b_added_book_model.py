"""Added book model

Revision ID: 10e54a3f676b
Revises: 3e7ac8702424
Create Date: 2024-04-14 17:02:02.400923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10e54a3f676b'
down_revision: Union[str, None] = '3e7ac8702424'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('book',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('authors', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('previewLink', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('publisher', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('publishedDate', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('infoLink', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('categories', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('ratingsCount', sa.FLOAT(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='book_pkey')
                    )


def downgrade() -> None:
    op.drop_table('book')
