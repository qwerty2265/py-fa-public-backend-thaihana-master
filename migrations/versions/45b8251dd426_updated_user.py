"""updated user

Revision ID: 45b8251dd426
Revises: 5c0d14a3fb35
Create Date: 2023-09-23 17:13:34.525991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45b8251dd426'
down_revision = '5c0d14a3fb35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    op.drop_column('user', 'is_active')
    op.add_column('user', sa.Column('mobile_phone', sa.String(), nullable=False, unique=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'mobile_phone')
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('email', sa.String(length=320), nullable=False))
    # ### end Alembic commands ###
