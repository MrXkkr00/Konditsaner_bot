
from utils.db_api.sqlite import Database



db = Database(path_to_db='test.db')
# db.create_table_users()
# db.add_user(user_id="13242414", kon7="2")
# # # db.add_user(2, "olim", "olim@gmail.com", 'uz')
# # # db.add_user(3, 1, 1)
# # # db.add_user(4, 1, 1)
# # # db.add_user(5, "John", "john@mail.com")
    # #
# users = db.select_all_users()
# print(f"Barcha fodyalanuvchilar: {users}")
    # #
user = db.select_user(user_id="123543543514")
print(f"Bitta foydalanuvchini ko'rish: {user}")
if not user:
    print(1)

