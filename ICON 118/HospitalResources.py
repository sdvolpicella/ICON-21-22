class HospitalResources:
    time: int
    ambulanceType: int
    doctors: int
    nurses: int
    rescuers: int

    def __init__(self):
        self.time = 0
        self.ambulanceType = 0
        self.doctors = 0
        self.nurses = 0
        self.rescuers = 0

    def __init__(self, time, ambulanceType, doctors, nurses, rescuers, node):
        self.time = time
        self.ambulanceType = ambulanceType
        self.doctors = doctors
        self.nurses = nurses
        self.rescuers = rescuers
        self.node = node



