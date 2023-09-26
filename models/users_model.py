# Admin role
class Admin:
    ADMINS = {203506853}  # 164940743

    @staticmethod
    def is_admin(user_id: int):
        return user_id in Admin.ADMINS
