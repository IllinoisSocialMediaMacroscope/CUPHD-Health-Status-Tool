from flask_login import UserMixin

from config import ADMIN_NETID_LIST


class User(UserMixin):

    def __init__(self, netid):
        self.id = netid
        self.display_name = "C-U Public Health District Administrator"
        self.email = "coronavirus@c-uphd.org"
        self.phone = "(217) 239-7877"

    @staticmethod
    def get(netid):
        user = User(netid=netid)
        return user
