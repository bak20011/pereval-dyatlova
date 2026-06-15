# class User:
#    login = 'user_login'
#    role = 'Python Developer'
#
#
# u1 = User()
#
# # Установка (либо изменение) нового атрибута класса
# setattr(User, 'email', 'user@gmail.com')
#
# # Установкение) локального атрибута экземпляру класса
# setattr(u1, 'login', 'DEIvanov')
#
# print(u1.login,u1.role,u1.email)
# print(User.email)

class User:
    def set_attrs(self, login, password, name, email, role):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.role = role

    def create_task(self, project, description):
        project.add_task(self, description)

class Team:
    def init_team(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, user):
        self.members.append(user)

    def show_members(self):
        print(f'Team {self.name} members:')
        for i, user in enumerate(self.members):
            print(f'num{i + 1}, login:{user.login}, name {user.name}')

    def get_team_size(self):
        return  len(self.members)

user1 = User()
user1.set_attrs("user1", "password1", "John Doe", "john.doe@example.com",'TechLead')

user2 = User()
user2.set_attrs("user2", "password2", "Jane Doe", "jane.doe@example.com", 'Python Developer')

user3 = User()
user3.set_attrs("user3", "password3", "Bob Smith", "bob.smith@example.com", 'Python Developer')

team = Team()
team.init_team('my_team')
team.add_member(user1)
team.add_member(user2)

print(f'Size of team "{team.name}" : {team.get_team_size()}')

team.show_members()

user1 = User()
user1.set_attrs("user1", "password1", "John Doe", "john.doe@example.com",'TechLead')

user2 = User()
user2.set_attrs("user2", "password2", "Jane Doe", "jane.doe@example.com", 'Python Developer')

user3 = User()
user3.set_attrs("user3", "password3", "Bob Smith", "bob.smith@example.com", 'Python Developer')

team = Team()
team.init_team('my_team')
team.add_member(user1)
team.add_member(user2)

print(f'Size of team "{team.name}" : {team.get_team_size()}')

team.show_members()

class Task:
    def create_task(self, discription):
        self.discription = discription

class Project:
   def create_project(self, name, team):
       self.name = name
       self.team = team
       self.tasks = []

   def add_task(self, user, description):
       if user in self.team.members:
           task = Task()
           task.create_task(description)
           self.tasks.append(task)
           print(f"Task '{description}' added to project '{self.name}'")
       else:
           print(f"User '{user.name}' is not a member of the team working on project '{self.name}'")

