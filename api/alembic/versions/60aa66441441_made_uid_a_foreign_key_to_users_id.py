"""Made uid a foreign key to users.id

Revision ID: 60aa66441441
Revises: 20555694e30d
Create Date: 2024-03-05 11:33:31.341388

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60aa66441441'
down_revision: Union[str, None] = '20555694e30d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'links', 'users', ['uid'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'links', type_='foreignkey')
    # ### end Alembic commands ###