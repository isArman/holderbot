"""add node excluded monitorings

Revision ID: 10ce718f423f
Revises: 4abf3adb8ab8
Create Date: 2024-11-08 04:53:18.184923

"""
# pylint: disable=all

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "10ce718f423f"
down_revision: Union[str, None] = "4abf3adb8ab8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "settings", sa.Column("node_excluded_monitorings", sa.JSON(), default=[])
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("settings", "node_excluded_monitorings")
    # ### end Alembic commands ###
