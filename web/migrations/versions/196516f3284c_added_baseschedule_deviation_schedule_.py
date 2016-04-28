"""Added BaseSchedule, Deviation, Schedule, Workday, WorkPeriod.

Revision ID: 196516f3284c
Revises: 7cf47cd2a016
Create Date: 2016-04-27 10:48:10.946882

"""

# revision identifiers, used by Alembic.
revision = '196516f3284c'
down_revision = '7cf47cd2a016'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('work_periods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start', sa.Date(), nullable=True),
    sa.Column('end', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workdays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('start', sa.Time(), nullable=True),
    sa.Column('lunch_start', sa.Time(), nullable=True),
    sa.Column('lunch_end', sa.Time(), nullable=True),
    sa.Column('end', sa.Time(), nullable=True),
    sa.Column('base_schedule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['base_schedule_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('work_period_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['work_period_id'], ['work_periods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('base_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('deviations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start', sa.Time(), nullable=True),
    sa.Column('lund_start', sa.Time(), nullable=True),
    sa.Column('lunch_end', sa.Time(), nullable=True),
    sa.Column('end', sa.Time(), nullable=True),
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deviations')
    op.drop_table('base_schedules')
    op.drop_table('schedules')
    op.drop_table('workdays')
    op.drop_table('work_periods')
    ### end Alembic commands ###