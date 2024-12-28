"""add UserQuery model

Revision ID: 1176c0fd22cd
Revises: 44781a16b7d9
Create Date: 2024-12-27 19:29:04.240927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1176c0fd22cd'
down_revision = '44781a16b7d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_queries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('queried_github_login', sa.String(length=80), nullable=False),
    sa.Column('queried_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_queries')
    # ### end Alembic commands ###
