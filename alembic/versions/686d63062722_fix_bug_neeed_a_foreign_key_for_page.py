"""Fix bug: Neeed a foreign key for page

Revision ID: 686d63062722
Revises: ae666acb7bd8
Create Date: 2024-07-31 00:25:19.665419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '686d63062722'
down_revision: Union[str, None] = 'ae666acb7bd8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('page', sa.Column('section_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'page', 'section', ['section_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'page', type_='foreignkey')
    op.drop_column('page', 'section_id')
    # ### end Alembic commands ###