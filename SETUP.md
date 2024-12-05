# Setup Instructions

Follow these steps to set up the repository locally and get started:

---

## Prerequisites

1. **Install Git**
   - Download and install Git from [git-scm.com](https://git-scm.com/).

2. **Install Python**
   - Ensure you have Python 3.8 or later installed.  
   - Download it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies**
   - Install `pip` (Python package manager) if not already installed.

---

## Setting Up the Repository

1. **Clone the Repository**
   - Fork the repository to your account and clone it to your local machine:
     ```bash
     git clone https://github.com/<your-username>/<repo-name>.git
     ```

2. **Navigate to the Repository**
   - Move into the project directory:
     ```bash
     cd <repo-name>
     ```

3. **Create a Virtual Environment (Optional but Recommended)**
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```

4. **Install Dependencies**
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

5. **Run Tests**
   - Verify the setup by running all tests:
     ```bash
     python -m unittest discover tests
     ```

---

## Folder Structure

- `problems/`: Contains buggy problem solutions to fix.
- `tests/`: Contains test cases to validate your fixes.
- `docs/`: Documentation, including FAQs and contribution guidelines.

---

## Need Help?

If you encounter any issues during setup, check out the FAQs or open an issue on GitHub.
