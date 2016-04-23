"""empty message

Revision ID: 6e5cc49befb9
Revises: f973bc56a35e
Create Date: 2016-04-23 19:31:38.229028

"""

# revision identifiers, used by Alembic.
revision = '6e5cc49befb9'
down_revision = 'f973bc56a35e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('errors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('error_msg', sa.String(), nullable=True),
    sa.Column('exception', sa.String(), nullable=True),
    sa.Column('traceback', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('errors')
    ### end Alembic commands ###
