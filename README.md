# Git and GitHub Workshop - Cohort 11 Names Collection Exercise

Welcome to the Git and GitHub Workshop Cohort 11 Names Collection Exercise!

## Overview

This workshop aims to teach participants the basics of using Git and GitHub for version control and collaborative development. In this exercise, participants will collaborate on a Python script to collect names from each individual and eventually create a list of names for everyone in Cohort 11.

## How the Exercise Works

1. **Clone the Repository**: Each participant should clone their forked repository to their local machine using the following command (replace `<username>` with your GitHub username).   Alternatively, you can use the "Clone or download" button on GitHub and then click the "Download ZIP" option to download the repository as a ZIP file. Extract the contents to your local machine:

```
git clone https://github.com/<username>/Xander-Git-GitHub-Workshop.git
```
2. **Create Branch**: Create a branch to add your name.  :

```
git checkout -b <your-name-branch>
```

3. **Add Your Name**: Open the `names_exercise.py` Python script and add your name to the `names` list, where it says "Add participant names below this comment." Make sure to save the changes.

3. **Commit and Push**: After adding your name, commit the changes, push and create a pull request.

```
git add names_exercise.py
git commit -m "Added [Your Name] to the names list"
git push origin <your-branch-name>
```
   
4. **Merge**: After all the changes are made and reviewed, the organiser will merge the pull requests into the original repository (`Xander-Git-GitHub-Workshop`).

5. **Create Conflicts**: As part of the collaboration process, participants should deliberately make conflicting changes to the `names` list. For example, each participant should change the same line in the `names` list. This step will demonstrate how to resolve conflicts during collaboration.
   
## Running the Script

To see the current list of names, run the `names_exercise.py` script:

```python names_exercise.py```

The script will display different messages based on the number of names in the list: "No names added" if the list is empty, "Hello, my name is ..." if there's only one name, and "List of names for everyone in cohort 11" if there are multiple names in the list.

Happy coding!
