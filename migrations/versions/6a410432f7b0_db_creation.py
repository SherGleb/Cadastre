"""db creation

Revision ID: 6a410432f7b0
Revises: 
Create Date: 2023-11-14 19:24:08.186691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a410432f7b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('query',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cadastral_number', sa.String(length=16), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('result', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('query')
    # ### end Alembic commands ###