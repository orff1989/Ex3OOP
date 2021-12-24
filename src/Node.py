
class Node:


    def __init__(self,_id, _pos : tuple):
        self.pos=_pos;
        self.id=_id

    def __repr__(self):
        return f"pos: {self.pos} id: {self.id}"