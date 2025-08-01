"""initial migration

Revision ID: ba82ab28b52f
Revises: 
Create Date: 2025-04-13 21:39:27.377281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ba82ab28b52f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_verification_entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('verification_token', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('verification_code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_verification_entries_email'), 'email_verification_entries', ['email'], unique=True)
    op.create_index(op.f('ix_email_verification_entries_id'), 'email_verification_entries', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('image', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('google_user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('google_token', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('user_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_email_verified', sa.Boolean(), nullable=False),
    sa.Column('is_blocked', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('login_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('notification_token', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('refresh_expires_at', sa.DateTime(), nullable=False),
    sa.Column('is_logged_out', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_login_sessions_id'), 'login_sessions', ['id'], unique=False)
    op.create_table('threads',
    sa.Column('id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_threads_id'), 'threads', ['id'], unique=False)
    op.create_table('thread_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('task_text', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_thread_tasks_id'), 'thread_tasks', ['id'], unique=False)
    op.create_table('thread_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('thread_task_id', sa.Integer(), nullable=True),
    sa.Column('thread_chat_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('thread_chat_from', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('chain_of_thought', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], ),
    sa.ForeignKeyConstraint(['thread_task_id'], ['thread_tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_thread_messages_id'), 'thread_messages', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_thread_messages_id'), table_name='thread_messages')
    op.drop_table('thread_messages')
    op.drop_index(op.f('ix_thread_tasks_id'), table_name='thread_tasks')
    op.drop_table('thread_tasks')
    op.drop_index(op.f('ix_threads_id'), table_name='threads')
    op.drop_table('threads')
    op.drop_index(op.f('ix_login_sessions_id'), table_name='login_sessions')
    op.drop_table('login_sessions')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_email_verification_entries_id'), table_name='email_verification_entries')
    op.drop_index(op.f('ix_email_verification_entries_email'), table_name='email_verification_entries')
    op.drop_table('email_verification_entries')
    # ### end Alembic commands ###
