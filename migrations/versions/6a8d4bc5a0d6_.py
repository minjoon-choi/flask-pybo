"""empty message

Revision ID: 6a8d4bc5a0d6
Revises: e141fe45d0ae
Create Date: 2020-09-22 22:01:55.481692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a8d4bc5a0d6'
down_revision = 'e141fe45d0ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideaProd', schema=None) as batch_op:
        batch_op.drop_constraint('uq_ideaProd_agentID', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ideaProd', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_ideaProd_agentID', ['agentID'])

    # ### end Alembic commands ###
