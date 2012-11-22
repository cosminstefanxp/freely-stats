
class Job:
    def __init__(self, id, name, projects_count, seo_url):
        self.id = id
        self.name = name
        self.projects_count = projects_count
        self.seo_url = seo_url
        
    def to_dict(self):
        out = {}
        out["id"] = self.id
        out["name"] = self.name
        out["projects_count"] = self.projects_count
        out["seo_url"] = self.seo_url
        return out
