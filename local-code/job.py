
class Job:
    def __init__(self, id, name, projects_count):
        self.id = id
        self.name = name
        self.projects_count = projects_count
        
    def to_dict(self):
        dict = []
        dict["id"] = self.id
        dict["name"] = self.name
        dict["projects_count"] = self.projects_count
        return dict
    

         