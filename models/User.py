from init import users
from pymongo import ReturnDocument
users = users()


class User():

    def __init__(self, data):
        self.username = data["username"]
        self.email = data["email"]
        self.password_digest = data["password_digest"]
        self._active_program_id = 0
        self.body_weight = 0
        self._unit = "kg"
        self.smallest_increment = 0
        self._programs = []
        self._workouts = []
        self._lifts = []
        self._weights = []

    @property
    def programs(self):
        return self._programs

    @programs.setter
    def programs(self, new_program):
        self._programs = (new_program)

    @property
    def workouts(self):
        return self.workouts

    @workouts.setter
    def workouts(self, new_workout):
        self._workouts = (new_workout)

    @property
    def lifts(self):
        return self.lifts

    @lifts.setter
    def lifts(self, new_lifts):
        self._lifts = (new_lifts)

    @property
    def weights(self):
        return self.weights

    @weights.setter
    def weights(self, weights):
        self._weights = (weights)

    @property
    def unit(self):
        return self.unit

    @unit.setter
    def unit(self, new_unit):
        self._unit = new_unit

    @property
    def active_program_id(self):
        return self.active_program_id

    @active_program_id.setter
    def active_program_id(self, new_id):
        self._active_program_id = new_id

    @classmethod
    def find_by_name(self, name):
        user_profile = users.find_one({'username': name})
        # delete data we don't want to return
        if user_profile:
            del user_profile['_id']
            # del user_profile['password_digest']
        return user_profile

    @classmethod
    def get_all(self):
        userList = users.find_one()
        del userList['_id']
        return userList

    @classmethod
    def add_program(self, username, new_program):
        updated_program = users.find_one_and_update({'username': username}, {
            "$push": {'_programs': new_program}}, return_document=ReturnDocument.AFTER)
        return updated_program['_programs']

    
    @classmethod
    def update_program(self, username, update_program):
        print(update_program)
        changed_program = users.find_one_and_update({'username': username}, {
            "$set": {'_programs': update_program}}, return_document=ReturnDocument.AFTER)
        return changed_program['_programs']

    @classmethod
    def add_lift(self, username, new_lift):
        updated_lift = users.find_one_and_update({'username': username}, {
            "$push": {'_lifts': new_lift}}, return_document=ReturnDocument.AFTER)
        return updated_lift['_lifts']

    @classmethod
    def add_weight(self, username, new_weight):
        updated_weight = users.find_one_and_update({'username': username}, {
            "$push": {'_weights': new_weight}}, return_document=ReturnDocument.AFTER)
        return updated_weight['_weights']

    @classmethod
    def add_workout(self, username, new_workout):
        updated_workout = users.find_one_and_update({'username': username}, {
            "$push": {'_workouts': new_workout}}, return_document=ReturnDocument.AFTER)
        return updated_workout['_workouts']

    @classmethod
    def create_user(self, data):
        user = User(data)
        userData = {}
        for key, value in (user.__dict__.items()):
            userData[key] = value
        users.insert_one(userData)
        return user.__dict__

    @classmethod
    def update_program(self, username, update_program, id):
        users.find_one_and_update({'username': username, '_programs.id': id}, {
                                  "$pull": {'_programs': {"id": id}}})
        changed_program = users.find_one_and_update({'username': username}, {
            "$push": {'_programs': update_program}}, return_document=ReturnDocument.AFTER)
        return changed_program['_programs']

    @classmethod
    def update_workout(self, username, update_workout, id):
        users.find_one_and_update({'username': username, '_workouts.id': id}, {
                                  "$pull": {'_workouts': {"id": id}}})
        changed_workout = users.find_one_and_update({'username': username}, {
            "$push": {'_workouts': update_workout}}, return_document=ReturnDocument.AFTER)
        return changed_workout['_workouts']

    @classmethod
    def update_lift(self, username, update_lift, id):
        users.find_one_and_update({'username': username, '_lift.id': id}, {
                                  "$pull": {'_lifts': {"id": id}}})
        changed_lift = users.find_one_and_update({'username': username}, {
            "$push": {'_lifts': update_lift}}, return_document=ReturnDocument.AFTER)
        return changed_lift['_lifts']
 
    @classmethod
    def update_username(self, username, update_username):
        changed_username = users.find_one_and_update({'username': username}, {
            "$set": {'username': update_username}}, return_document=ReturnDocument.AFTER)
        return changed_username['username']
   
    @classmethod
    def update_email(self, username, update_email):
        changed_email = users.find_one_and_update({'username': username}, {
            "$set": {'email': update_email}})
        return changed_email['email']
   
    @classmethod
    def update_password(self, username, update_password):
        changed_password = users.find_one_and_update({'username': username}, {
            "$set": {'password_digest': update_password}})
        return True

    @classmethod
    def update_body_weight(self, username, update_body_weight):
        changed_body_weight = users.find_one_and_update({'username': username}, {
            "$set": {'body_weight': update_body_weight}})
        return changed_body_weight['body_weight']

    @classmethod
    def update_smallest_increment(self, username, update_smallest_increment):
        changed_smallest_increment = users.find_one_and_update({'username': username}, {
            "$set": {'smallest_increment': update_smallest_increment}})
        return changed_smallest_increment['smallest_increment']

    @classmethod
    def update_unit(self, username, update_unit):
        changed_unit = users.find_one_and_update({'username': username}, {
            "$set": {'_unit': update_unit}})
        return changed_unit['_unit']
    

    @classmethod
    def delete_account(self, username):
        deleted_user = users.delete_one({'username': username})
        return deleted_user
    
    
    # @classmethod
    # def update_workout(self, username)
