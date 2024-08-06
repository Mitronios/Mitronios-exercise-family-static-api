
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._next_id = 1
        self._members = []

   
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)

        return member

    def delete_member(self, id):
        # fill this method and update the return
        # Find the member to delete
        member_to_delete = None
        for member in self._members:
            if member["id"] == id:
                member_to_delete = member
                break
    
    # If a member is found, delete it
        if member_to_delete:
            self._members.remove(member_to_delete)
            return member_to_delete
        else:
            return None

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member
            
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members