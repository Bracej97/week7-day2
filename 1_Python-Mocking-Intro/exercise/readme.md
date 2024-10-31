# 🔍 Introduction to Mocking

## 🎯 Challenge

Your task is to explore the concept of mocking in testing. You will implement a mock to isolate your tests from external dependencies and understand how mocking enhances your testing strategy.

## 📚 Key Learnings

By completing this exercise, you will learn:

- What mocking is and its importance in testing.
- How to use mocking to isolate tests from external dependencies like API calls and databases.

## 👤 User Story

As a Python developer, I want to ensure that my tests can run independently of external systems, allowing for faster and more reliable test execution.

## ✅ Acceptance Criteria

- The Python script is named `mocking_exercise.py`.
- The script demonstrates:
  - A function that interacts with an external service (e.g., API).
  - Tests that use mocking to isolate the function from its external dependency.

## 🛠️ Steps to Complete

1. **📁 Create a new Python file**: Name the file `mocking_exercise.py`.

2. **🖊️ Write a function**: Create a function that interacts with an external service (e.g., fetching data from an API).

3. **✏️ Write tests without mocking**: Write a test for the function without using mocking to demonstrate its limitations.

4. **🔍 Implement mocking**: Use the `unittest.mock` library to mock the external dependency in your test.

5. **📤 Print results**: Ensure your results include the outcomes of your tests.

6. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## Additional Resources

- [Python unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- [Real Python: Testing with Mocks](https://realpython.com/python-mocking/)
- [Mocking in Python with unittest](https://docs.python.org/3/library/unittest.mock.html)
- [Example APIS](https://catfact.ninja/fact, https://api.agify.io?name=meelad)

## Submission

Once you complete the task, submit the `mocking_exercise.py` file to your instructor.

Good luck, and happy mocking!