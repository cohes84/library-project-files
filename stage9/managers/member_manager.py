import json
from models.member import Member
from exceptions import MemberNotFoundError, MemberAlreadyExistsError, InvalidMemberIDError


class MemberManager:

    FILE = "data/members.json"

    def __init__(self):
        self.members = {}
        self.load()

    def register_member(self, name, member_id):
        if not member_id.startswith("M") or len(member_id) != 6:
            raise InvalidMemberIDError(
                f"Invalid member ID: {member_id}. Must start with M and be 6 characters."
            )
        if member_id in self.members:
            raise MemberAlreadyExistsError(f"Member {member_id} already exists.")
        self.members[member_id] = Member(name, member_id)
        self.save()

    def get_member(self, member_id):
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member {member_id} not found.")
        return self.members[member_id]

    def get_all(self):
        return list(self.members.values())

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(
                [member.to_dict() for member in self.members.values()],
                f, indent=2
            )

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                records = json.load(f)
                for data in records:
                    member = Member.from_dict(data)
                    self.members[member.member_id] = member
        except FileNotFoundError:
            pass