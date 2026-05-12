from member import Member

class MemberManager:

    def __init__(self):
        self.members = {}   # member_id: Member

    def register_member(self, name, member_id):
        if not member_id.startswith("M") or len(member_id) != 6:
            raise ValueError(f"Invalid member ID: {member_id}")
        if member_id in self.members:
            raise ValueError(f"Member {member_id} already registered.")
        self.members[member_id] = Member(name, member_id)

    def get_member(self, member_id):
        if member_id not in self.members:
            raise KeyError(f"Member {member_id} not found.")
        return self.members[member_id]

    def get_all(self):
        return list(self.members.values())