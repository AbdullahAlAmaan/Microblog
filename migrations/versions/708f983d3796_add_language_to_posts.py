"""add language to posts

Revision ID: 708f983d3796
Revises: c5ede38b966d
Create Date: 2023-05-17 12:50:37.680481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '708f983d3796'
down_revision = 'c5ede38b966d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
