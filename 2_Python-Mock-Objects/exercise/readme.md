# 🔍 Creating Mock Objects

## 🎯 Challenge

Your task is to explore the creation and usage of mock objects in testing. You will implement mock objects to replace actual components in your tests, ensuring your tests run in isolation.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to create mock objects using Python's `unittest.mock` library.
- How to use mock objects to replace actual components in your tests.

## 👤 User Story

As a Python developer, I want to be able to replace real components with mock objects during testing to isolate the functionality being tested.

## ✅ Acceptance Criteria

- The Python script is named `mock_objects_exercise.py`.
- The script demonstrates:
  - A service class that uses a database class.
  - Tests that use mock objects to verify the behavior of the service without connecting to a real database.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `mock_objects_exercise.py`.

2. **🖊️ Write a class with an external dependency**: Create a class (e.g., `DataService`) that interacts with another class (e.g., `Database`).

3. **✏️ Write tests using mock objects**: Write tests for the service class using mock objects to replace the actual database interaction.

4. **📤 Print results**: Ensure your results include the outcomes of your tests.

5. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Additional Resources

- [Python unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Real Python: Mocking in Python](https://realpython.com/python-mocking/)

## Submission

Once you complete the task, submit the `mock_objects_exercise.py` file to your instructor.

Good luck, and happy mocking!