"""add_qa_document_language

Revision ID: 2c8af9671032
Revises: 8d2d099ceb74
Create Date: 2023-08-01 18:57:27.294973

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '2c8af9671032'
down_revision = '5022897aaceb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doc_language', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('documents', schema=None) as batch_op:
        batch_op.drop_column('doc_language')

    # ### end Alembic commands ###