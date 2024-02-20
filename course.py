class Course:
    def __init__(self, course_id, code, description, prerequisites, restrictions, stage):
        print(course_id)
        self.id = course_id
        self.code = code
        self.description = description
        self.prerequisites = prerequisites
        self.restrictions = restrictions
        self.stage = stage