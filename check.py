from user_dev import User_dev
from constantes import Constant

class check:
    @classmethod
    def check_year(cls, years):
        if years <= 1:
            User_dev.level_experience = 'Trainee'
            User_dev.skills = Constant.TRAINEE_SKILL
            User_dev.request = Constant.TRAINEE_REQ
        elif 2 <= years <= 3:
            User_dev.level_experience = 'Junior'
            User_dev.skills = Constant.JUNIOR_SKILL
            User_dev.request = Constant.JUNIOR_REQ
        elif 4 <= years <= 5:
            User_dev.level_experience = 'Middle'
            User_dev.skills = Constant.MIDDLE_SKILL
            User_dev.request = Constant.MIDDLE_REQ
        elif 6 <= years <= 8:
            User_dev.level_experience = 'Senior'
            User_dev.skills = Constant.SENIOR_SKILL
            User_dev.request = Constant.SENIOR_REQ
        elif years >= 9:
            User_dev.years_experience = 'Lead'
        return User_dev.level_experience, User_dev.skills, User_dev.request

