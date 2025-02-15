"""Added Audition and Role Table Classes

Revision ID: f4f808f68423
Revises: d074a65912e9
Create Date: 2024-02-15 11:51:13.208051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4f808f68423'
down_revision = 'd074a65912e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('actor', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('hired', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_name', sa.String(), nullable=True),
    sa.Column('audition_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['audition_id'], ['auditions.id'], name=op.f('fk_roles_audition_id_auditions')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.drop_table('auditions')
    # ### end Alembic commands ###
