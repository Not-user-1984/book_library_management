# import unittest
# import os
# from src.json_manager import JsonManager
# from src.interface import DATABASE_FILE


# class TestJsonManager(unittest.TestCase):

#     def setUp(self):
#         self.json_manager = JsonManager()
#         self.library = self.json_manager.load_library(DATABASE_FILE)
#         self.user = self.json_manager.create_user(self.library, 'test', '1234')
#         self.library.append(self.user)
#         self.json_manager.save_library(self.library, DATABASE_FILE)

#     def tearDown(self):
#         if os.path.exists(DATABASE_FILE):
#             os.remove(DATABASE_FILE)

#     def test_add_book(self):
#         self.json_manager.add_book(
#             self.user['books'], 'Test Book', 'Test Author', '2023')
#         self.assertEqual(len(self.user['books']), 1)
#         self.assertEqual(self.user['books'][0]['title'], 'Test Book')


#     # def test_remove_book(self):
#     #     self.json_manager.add_book(self.user['books'], 'Test Book', 'Test Author', '2023')
#     #     book_id = self.user['books'][0]['id']
#     #     self.json_manager.remove_book(self.user['books'], book_id)
#     #     self.assertEqual(len(self.user['books']), 0)

#     def test_change_status(self):
#         self.json_manager.add_book(self.user['books'], 'Test Book', 'Test Author', '2023')
#         book_id = self.user['books'][0]['id']
#         self.json_manager.change_status(self.user['books'], book_id, 'выдана')
#         self.assertEqual(self.user['books'][0]['status'], 'выдана')

# if __name__ == '__main__':
#     unittest.main()