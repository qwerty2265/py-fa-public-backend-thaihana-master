"""cart_product

Revision ID: 795a527eb5eb
Revises: 4b7643354393
Create Date: 2023-08-11 12:40:19.321199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795a527eb5eb'
down_revision = '4b7643354393'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_product',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('modified_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_product')
    # ### end Alembic commands ###
