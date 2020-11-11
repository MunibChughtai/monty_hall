class Door:
    '''
    This class specified one door object
    '''
    def __init__(self, object_name = None):
        self._object_present_behind=object_name

    def get_object_behind_door(self):
        return self._object_present_behind