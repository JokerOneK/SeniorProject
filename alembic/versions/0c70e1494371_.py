"""empty message

Revision ID: 0c70e1494371
Revises: d4867f3a4c0a, fb24d7865e5c
Create Date: 2024-04-06 13:44:40.210691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c70e1494371'
down_revision: Union[str, None] = ('d4867f3a4c0a', 'fb24d7865e5c')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
