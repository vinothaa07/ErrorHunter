# Contribution Guidelines

Thank you for your interest in contributing to this repository! Follow these guidelines to get started with fixing problems and contributing effectively.

---

## How to Contribute

1. **Fork the Repository**
   - Click on the `Fork` button on the top-right corner of this repository to create your copy.

2. **Clone Your Fork**
   - Clone your fork to your local machine using:
     ```bash
     git clone https://github.com/<your-username>/<repo-name>.git
     ```
   - Replace `<your-username>` and `<repo-name>` with your GitHub username and the repository name.

3. **Create a Branch**
   - Create a new branch to work on the issue:
     ```bash
     git checkout -b fix-problem1
     ```

4. **Solve the Problem**
   - Navigate to the `problems/` folder and find the buggy solution for the problem.
   - Fix the solution and test it using the provided test cases.

5. **Run the Tests**
   - Use the test scripts in the `tests/` folder to ensure your solution is correct:
     ```bash
     python -m unittest discover tests
     ```

6. **Commit Your Changes**
   - Once the solution is fixed, stage and commit your changes:
     ```bash
     git add problems/easy/problem1.py
     git commit -m "fix: corrected logic for problem1"
     ```

7. **Push Your Changes**
   - Push your branch to your forked repository:
     ```bash
     git push origin fix-problem1
     ```

8. **Create a Pull Request**
   - Go to the original repository on GitHub.
   - Click `Compare & Pull Request` and submit your PR with a descriptive message.

---

## Coding Guidelines

- Use descriptive variable names.
- Add comments to explain complex logic.
- Ensure all test cases pass before submitting a PR.
- Follow Python's PEP 8 style guide for clean and consistent code.

---

## Issue Tracking

- Check the `Issues` tab for problems to work on.
- Issues labeled as `good first issue` are beginner-friendly.
- Assign yourself an issue before working on it to avoid duplication of effort.

---

## Need Help?

If you're stuck or have questions, feel free to:
- Call the Mentor : Mathi Yuvarajan T.K 
- Comment on the issue you're working on.
- Reach out to the maintainers in the Discussions tab.

We’re excited to see your contributions. Happy coding!
