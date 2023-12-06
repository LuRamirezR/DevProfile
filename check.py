from user_dev import User_dev
from constantes import Constant

class check:
    @classmethod
    def check_year(cls, years):
        if years <= 1:
            level_experience = 'Trainee'
            skills = Constant.TRAINEE_SKILL
            request = Constant.TRAINEE_REQ
        elif 2 <= years <= 3:
            level_experience = 'Junior'
            skills = Constant.JUNIOR_SKILL
            request = Constant.JUNIOR_REQ
        elif 4 <= years <= 5:
            level_experience = 'Middle'
            skills = Constant.MIDDLE_SKILL
            request = Constant.MIDDLE_REQ
        elif 6 <= years <= 8:
            level_experience = 'Senior'
            skills = Constant.SENIOR_SKILL
            request = Constant.SENIOR_REQ
        elif 9 <= years <= 12:
            level_experience = 'Lead'
            skills = Constant.LEAD_SKILL
            request = Constant.LEAD_REQ
        return level_experience, skills, request

