"""empty message

Revision ID: 524b97fe83c4
Revises: 
Create Date: 2020-08-31 15:27:04.053738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '524b97fe83c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('package_multilang',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('package_id', sa.UnicodeText,
                  sa.ForeignKey("package.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column('field', sa.UnicodeText, nullable=False, index=True),
        sa.Column('field_type', sa.UnicodeText, nullable=False, index=True),
        sa.Column('lang', sa.UnicodeText, nullable=False, index=True),
        sa.Column('text', sa.UnicodeText, nullable=False, index=True)
    )

    op.create_table('group_multilang',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('group_id', sa.UnicodeText,
                  sa.ForeignKey("group.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column('name', sa.UnicodeText, nullable=False, index=True),
        sa.Column('field', sa.UnicodeText, nullable=False, index=True),
        sa.Column('lang', sa.UnicodeText, nullable=False,  index=True),
        sa.Column('text', sa.UnicodeText, nullable=False, index=True)
    )

    op.create_table('resource_multilang',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('resource_id', sa.UnicodeText,
                  sa.ForeignKey("resource.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column('field', sa.UnicodeText, nullable=False, index=True),
        sa.Column('lang', sa.UnicodeText, nullable=False, index=True),
        sa.Column('text', sa.UnicodeText, nullable=False, index=True)
    )

    op.create_table('tag_multilang',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('tag_id', sa.UnicodeText,
                  sa.ForeignKey("tag.id", ondelete="CASCADE"),
                  nullable=False),
        sa.Column('tag_name', sa.UnicodeText, nullable=False, index=True),
        sa.Column('lang', sa.UnicodeText, nullable=False, index=True),
        sa.Column('text', sa.UnicodeText, nullable=False, index=True)
    )


def downgrade():
    op.drop_table("package_multilang")
    op.drop_table("group_multilang")
    op.drop_table("resource_multilang")
    op.drop_table("tag_multilang")
    pass
