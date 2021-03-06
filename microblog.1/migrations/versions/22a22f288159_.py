"""empty message

Revision ID: 22a22f288159
Revises: 05898c8cf549
Create Date: 2018-01-30 12:00:21.215615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22a22f288159'
down_revision = '05898c8cf549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playerName', sa.String(length=64), nullable=True),
    sa.Column('playerNationality', sa.String(length=64), nullable=True),
    sa.Column('playerPosition', sa.String(length=64), nullable=True),
    sa.Column('playerClub', sa.String(length=64), nullable=True),
    sa.Column('playerAge', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_players_playerAge'), 'players', ['playerAge'], unique=False)
    op.create_index(op.f('ix_players_playerClub'), 'players', ['playerClub'], unique=False)
    op.create_index(op.f('ix_players_playerName'), 'players', ['playerName'], unique=False)
    op.create_index(op.f('ix_players_playerNationality'), 'players', ['playerNationality'], unique=False)
    op.create_index(op.f('ix_players_playerPosition'), 'players', ['playerPosition'], unique=False)
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teamName', sa.String(length=64), nullable=True),
    sa.Column('homeGround', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_homeGround'), 'team', ['homeGround'], unique=False)
    op.create_index(op.f('ix_team_teamName'), 'team', ['teamName'], unique=False)
    op.create_index(op.f('ix_team_city'), 'team', ['city'], unique=False)
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index(op.f('ix_team_city'), table_name='team')
    op.drop_index(op.f('ix_team_teamName'), table_name='team')
    op.drop_index(op.f('ix_team_homeGround'), table_name='team')
    op.drop_table('team')
    op.drop_index(op.f('ix_players_playerPosition'), table_name='players')
    op.drop_index(op.f('ix_players_playerNationality'), table_name='players')
    op.drop_index(op.f('ix_players_playerName'), table_name='players')
    op.drop_index(op.f('ix_players_playerClub'), table_name='players')
    op.drop_index(op.f('ix_players_playerAge'), table_name='players')
    op.drop_table('players')
    # ### end Alembic commands ###
