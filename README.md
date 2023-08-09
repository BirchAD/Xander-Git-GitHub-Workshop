# Git and GitHub Workshop - Cohort 11 Names Collection Exercise

Welcome to the Git and GitHub Workshop Cohort 11 Names Collection Exercise!

## Overview

This workshop aims to teach participants the basics of using Git and GitHub for version control and collaborative development. In this exercise, participants will collaborate on a Python script to collect names from each individual and eventually create a list of names for everyone in Cohort 11.

## How the Exercise Works

1. **Clone the Repository**:
   Each participant should clone the repository to their own machine.
   Alternatively, you can use the "Clone or download" button on GitHub and then click the "Download ZIP" option to download the repository as a ZIP file. Extract the contents to your local machine:

```
git clone https://github.com/BirchAD/Xander-Git-GitHub-Workshop.git
```
2. **Create Branch**:
   Create a branch to add your name:

```
git checkout -b <your-name-branch>
```

3. **Add Your Name**:
   Open the `names_exercise.py` Python script and add your name to the `names` list, where it says "Add participant names below this comment." Make sure to save the changes.

3. **Commit and Push**:
   After adding your name, commit the changes, push and create a pull request.

```
git add names_exercise.py
git commit -m "Added [Your Name] to the names list"
git push origin <your-branch-name>
```

3. **Create Pull Request**:


   1. Go to the repository and click on the "Pull requests" tab located near the top of the repository.
   2. Click on the green "New pull request" button.
   3 .In the "base" dropdown, select the target branch (usually "main" or "master") that you want to merge your changes into.
   4. n the "compare" dropdown, select your branch that contains the changes you've made.
   5. Review the changes that will be included in the pull request.
   6. Add a title and description for your pull request, explaining what changes you've made and why they should be merged.
   7. If necessary, you can assign reviewers to your pull request and make other adjustments.
   8. Once you're satisfied, click the green "Create pull request" button.
   9. Your pull request will be created, and reviewers will be able to provide feedback and discuss the changes before the merge.
   
   Alternatively, via the branch tab:
   
   1. After you've pushed your changes to your branch on GitHub, navigate to your branch in the repository.
   2. Near the top of the page, you'll see a notification prompting you to create a pull request comparing your branch with the target branch (usually "main"). Click on that notification.
   3. You'll be taken to a page where you can review the changes between your branch and the target branch.
   4. Add a title and description for your pull request, explaining the purpose of your changes.
   5. If needed, you can assign reviewers and make other adjustments.
   6. Once you're ready, click the "Create pull request" button.
   7. Your pull request will be created, and the reviewers can provide feedback and discuss the changes before the merge.
   
5. **Merge**:
   After all the changes are made and reviewed, the organiser will merge the pull requests into the original repository (`Xander-Git-GitHub-Workshop`).

6. **Create Conflicts**:
   As part of the collaboration process, participants should deliberately make conflicting changes to the `names` list. For example, each participant should change the first    line in the `names` list, or change variable names. This step will demonstrate how to resolve conflicts during collaboration.

   **Stretch Goal**: Fork the repo, clone to your machine and experiment using rebase and squash.  Then create a pull request to the BirchAD repo.
   
## Running the Script

To see the current list of names, run the `names_exercise.py` script:

```python names_exercise.py```

The script will display different messages based on the number of names in the list: "No names added" if the list is empty, "Hello, my name is ..." if there's only one name, and "List of names for everyone in cohort 11" if there are multiple names in the list.

Happy coding!
