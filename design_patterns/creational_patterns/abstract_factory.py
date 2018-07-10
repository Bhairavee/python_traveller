# one abstract factory is used to create appropriate factory at runtime
# software developer jobs is the abstract factory that can create frontend/backend/devops


class SoftwareDeveloperJobs(object):
    def __init__(self, developer_factory=None):
        self.developer_factory = developer_factory

    def __str__(self):
        job = self.developer_factory()
        out_str = "This is a " + str(job.type) + "job. Description:- " + str(job)
        return out_str


class Backend(object):
    type = "Backend Developer(Python)"

    def __str__(self):
        return """Should have knowledge of OOPS concepts, Data Structures, Algorithms, Python.
        Should have knowledge of REST/SOAP APIs. Good in problem solving."""


class Frontend(object):
    type = "Frontend Developer"

    def __str__(self):
        return "Should know HTML/CSS/ Javascript and Frameworks- Knockout and react library."


class DevOps(object):
    type = "DevOps Engineer"

    def __str__(self):
        return "Linux/Windows system knowledge, System administration and Apache/IIS server management."


print("************Backend developer job profile************")
print
print(SoftwareDeveloperJobs(Backend))
print
print("************Frontend developer job profile************")
print
print(SoftwareDeveloperJobs(Frontend))
print
print("************DevOps Engineer job profile************")
print
print(SoftwareDeveloperJobs(DevOps))
print
