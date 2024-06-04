class User:
    def __init__(self, id, name, description, created):
        self.id = id
        self.name = name
        self.description = description
        self.created = created

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created": self.created,
        }