"""added active column

Revision ID: 5c0d14a3fb35
Revises: c7ad5df0e4be
Create Date: 2023-09-17 19:48:50.983954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c0d14a3fb35'
down_revision = 'c7ad5df0e4be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'active')
    # ### end Alembic commands ###