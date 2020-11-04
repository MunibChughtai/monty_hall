class Door:
    '''
    This class specified one door object
    '''
    def __init__(self, object_name):
        self._object_present=object_name
        self._door_opened=False

    def get_object_behind_door(self):
        #self._door_opened=True
        return self._object_present


    #def put_object_behind(self, object_name):
    #    self._object_present=object_name
