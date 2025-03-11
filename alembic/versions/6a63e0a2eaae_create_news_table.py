"""create news table

Revision ID: 6a63e0a2eaae
Revises: 
Create Date: 2025-03-11 21:24:15.991814

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a63e0a2eaae'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'news',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('url', sa.String(), nullable=False)
    )
    op.create_index('ix_news_title', 'news', ['title']) 


def downgrade() -> None:
    op.drop_index('ix_news_title', table_name='news') 
    op.drop_table('news')
