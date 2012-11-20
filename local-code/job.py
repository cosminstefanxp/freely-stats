
class Job:
    def __init__(self, id, name, projects_count):
        self.id = id
        self.name = name
        self.projects_count = projects_count
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["name"] = self.name
        out["projects_count"] = self.projects_count
        return out
    

         