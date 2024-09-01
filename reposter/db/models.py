from tortoise.models import Model
from tortoise import fields


class Msg(Model):
    src_msg = fields.IntField()
    src_chat = fields.IntField()
    target_msg = fields.IntField()
    target_chat = fields.IntField()

