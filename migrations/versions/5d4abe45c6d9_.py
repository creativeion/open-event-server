"""empty message

Revision ID: 5d4abe45c6d9
Revises: 5aea50727992
Create Date: 2016-06-21 10:54:57.068213

"""

# revision identifiers, used by Alembic.
revision = '5d4abe45c6d9'
down_revision = '5aea50727992'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient', sa.String(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('action', sa.String(), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mails')
    ### end Alembic commands ###