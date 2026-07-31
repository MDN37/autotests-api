from faker import Faker

fake = Faker('ru_Ru')

print(fake.name())
print(fake.address())
print(fake.email())