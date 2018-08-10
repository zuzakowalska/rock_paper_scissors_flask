"""add win column

Revision ID: 6b3f42a79826
Revises: 316f17b36b26
Create Date: 2018-08-10 12:34:11.580354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3f42a79826'
down_revision = '316f17b36b26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_data', sa.Column('name', sa.String(length=32), nullable=True))
    op.add_column('game_data', sa.Column('score', sa.Integer(), nullable=True))
    op.add_column('game_data', sa.Column('win', sa.Boolean(), nullable=True))
    op.drop_index('ix_game_data_game_id', table_name='game_data')
    op.drop_column('game_data', 'player_score')
    op.drop_column('game_data', 'game_id')
    op.drop_column('game_data', 'player_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_data', sa.Column('player_name', sa.VARCHAR(length=32), nullable=True))
    op.add_column('game_data', sa.Column('game_id', sa.INTEGER(), nullable=True))
    op.add_column('game_data', sa.Column('player_score', sa.INTEGER(), nullable=True))
    op.create_index('ix_game_data_game_id', 'game_data', ['game_id'], unique=1)
    op.drop_column('game_data', 'win')
    op.drop_column('game_data', 'score')
    op.drop_column('game_data', 'name')
    # ### end Alembic commands ###