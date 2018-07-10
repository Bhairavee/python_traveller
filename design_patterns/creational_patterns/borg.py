# multiple instances share the same state which is present in their attribute __dict__
# used for managing database connections
# by doing self.__dict__ = some var all dicts  refer to same memory location


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


instance1 = Borg()
instance2 = Borg()

instance1.state = 'Idle'
instance2.state = 'Running'

print("instance 1 {0}".format(instance1))
print("instance 2 {0}".format(instance2))
print("shred", Borg._Borg__shared_state)

# all refer to same address in memory
print(hex(id(instance1.__dict__)) == hex(id(instance2.__dict__)) == hex(id(Borg._Borg__shared_state)))

instance3 = YourBorg()

instance3.state = "Killed"

print("instance 1 {0}".format(instance1))
print("instance 2 {0}".format(instance2))
