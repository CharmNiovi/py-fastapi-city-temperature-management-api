"""empty message

Revision ID: e7466c4db13a
Revises: 
Create Date: 2024-06-27 16:42:32.465080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7466c4db13a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('additional_info', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('temperatures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temperatures')
    op.drop_table('city')
    # ### end Alembic commands ###