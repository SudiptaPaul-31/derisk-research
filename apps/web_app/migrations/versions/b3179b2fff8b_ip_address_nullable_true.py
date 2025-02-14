"""ip address nullable true

Revision ID: b3179b2fff8b
Revises: f4baaac5103f
Create Date: 2024-11-29 18:44:44.613470

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision: str = "b3179b2fff8b"
down_revision: Union[str, None] = "f4baaac5103f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "notification",
        "ip_address",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "notification",
        "ip_address",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )
    # ### end Alembic commands ###
