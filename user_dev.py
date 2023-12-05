from logger_base import log

class User_dev:
    def __init__(self, id_dev=None, name=None, email=None, years_experience=None, level_experience=None, skills=None, request=None):
        self._id_dev = id_dev
        self._name = name
        self._email = email
        self._years_experience = years_experience
        self._level_experience = level_experience
        self._skills = skills
        self._request = request

    def __str__(self):
        return f'''
            Id Developer: {self._id_dev}, Name: {self._name}, email: {self._email},
            Years of experience: {self._years_experience}, Level of experience: {self._level_experience}
        '''
    @property
    def id_dev(self):
        return self._id_dev

    @id_dev.setter
    def id_dev(self, id_dev):
        self._id_dev = id_dev

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def years_experience(self):
        return self._years_experience
    
    @years_experience.setter
    def years_experience(self, years_experience):
        self.years_experience = years_experience

    @property
    def level_experience(self):
        return self._level_experience

    @level_experience.setter
    def level_experience(self, level_experience):
        self._level_experience = level_experience

    @property
    def request(self):
        return self._request

    @request.setter
    def request(self, request):
        self._request = request



if __name__ == '__main__':
    #dev1 = User_dev(1, 'jperez', '123')
    #log.debug(dev1)

    # Simular un insert
    dev1 = User_dev(id_dev=1, name='John Doe', email='jdoe@mail.com', years_experience=1)
    log.debug(dev1)

    # # Simular un delete
    # usuario1 = Persona(id_usuario=1)
    # log.debug(usuario1)