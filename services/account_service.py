
class AccountService:

    def __init__(self, mysql):
        self.mysql = mysql

    async def by_cpf(self, cpf):
        return self.mysql.get_account_by_cpf(cpf)
