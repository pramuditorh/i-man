from app import db

# Define the User data-model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    phoneNumber = db.Column(db.Integer)
    passwordHash = db.Column(db.String(128))
    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'id: {self.id}, username: {self.username}, name: {self.name}, position: {self.position}, phoneNumber: {self.phoneNumber}, roles: {self.roles}'

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'id: {self.id}, role_name: {self.name}'

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

    def __repr__(self):
        return f'user_id: {self.user_id}, role_id: {self.role_id}'