"""third migration

Revision ID: fb24d7865e5c
Revises: 972433b13226
Create Date: 2023-11-19 19:41:13.304167

"""
from typing import Sequence, Union
from src.db.base_class import Base
from src.db.session import engine
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb24d7865e5c'
down_revision: Union[str, None] = '972433b13226'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    Base.metadata.create_all(bind=engine)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
