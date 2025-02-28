[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/TJsoBWDHTD5Vn1FhyTgTtn/Y3fusjn4CegNoYAiSmuZww/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/TJsoBWDHTD5Vn1FhyTgTtn/Y3fusjn4CegNoYAiSmuZww/tree/main)

Designing for Testability
- Separation of Concerns: I organized the API request and response logic into distinct functions for easier testing.
- Mocking External APIs: I used mocking to simulate GitHub API responses, avoiding rate limits and delays.
- Error Handling: To enhance reliability, implemented error handling for network issues and invalid user IDs t- Clear Inputs and Outputs: The function takes a GitHub user ID and returns a list of repositories with commit counts, simplifying testing.

Testing Strategy
- I wrote unit tests for each function, addressing valid and invalid user IDs and API failures.
- Mocked API responses using `unit test.mock` to test various scenarios.
- Integrated testing into a CircleCI pipeline for automatic testing with each push.

Connecting GitHub, PyCharm, and CircleCI
- Cloned the repository in PyCharm, set up a virtual environment, and configured it to run tests with pytest.
- Signed up for CircleCI, added the repository, and created a `.circleci/config.yml` for the CI pipeline.

Challenges Faced
- API Rate Limits: Used mocking to circumvent limits during testing.
- Dynamic Data:  Focused on testing response structures rather than specific values.
- Error Handling: Developed comprehensive error handling and edge case tests.
- CircleCI Setup: Resolved initial configuration challenges with documentation.

 Lessons Learned
- Modular code is more straightforward to test.
- Mocking is crucial for efficient testing.
- CI/CD automation improves code reliability.
- Addressing edge cases strengthens the project.

 Conclusion
I created maintainable and extendable code by focusing on testability, modular design, and robust error handling. The integration of GitHub, PyCharm, and CircleCI optimized development and automated testing kept the code functional.
![image](https://github.com/user-attachments/assets/145460cc-9a4e-4cd4-8139-65f645c9b85b)
