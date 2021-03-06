"""Role add info

Revision ID: 0443b7c6e56c
Revises: 3949bbea2472
Create Date: 2018-05-16 18:06:32.444212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0443b7c6e56c'
down_revision = '3949bbea2472'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('info', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'info')
    # ### end Alembic commands ###
