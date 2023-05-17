class Task():
    def __init__(self, name, dueDate, priority, status):
        self.id = id
        self.name = name
        self.due_date = dueDate
        self.priority = priority
        self.status = status
    
    def setName(self, name):
        self.name = name
    
    def setDueDate(self, dueDate):
        self.dueDate = dueDate

    def setPriority(self, priority):
        self.priority = priority

    def setStatus(self, status):
        self.status = status

    def getName(self, name):
        return name
    
    def getDueDate(self, dueDate):
        return dueDate

    def getPriority(self, priority):
        return priority
    
    def getStatus(self, status):
        return status
    