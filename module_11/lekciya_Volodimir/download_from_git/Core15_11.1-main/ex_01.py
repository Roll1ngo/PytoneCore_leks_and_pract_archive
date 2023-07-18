class Phone:
    def __init__(self, value):
        self.value = value
    
    def replace_plus(self):
        return self.value.replace("+", "")
    
    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)

class User:
    def __init__(self, 
                 name="Bill", 
                 age=22,
                 phone=None,
                 address="Ukraine",
                 email="user@com.ua") -> None:
        self.name = name
        self.age = age
        self.phones = []
        self.address = address
        self.email = email
        if phone:
            self.add_phone(phone)
    
    def add_phone(self, phone:Phone):
        self.phones.append(phone)
    
    def __str__(self) -> str:
        # phones = f"{', phones ' + '; '.join(p.replace_plus() for p in self.phones) if self.phones else ''}"
        return "User {}, age {}{}".format(self.name,
                                          self.age,
                                          self.phones)
    def __repr__(self) -> str:
        return str(self)
if __name__ == "__main__":
    user_bill = User("Garry")
    user_marry = User("Merry", phone=Phone("+380975677676"))
    user_marry.add_phone(Phone("+380734562323"))

    print(user_bill, user_marry)