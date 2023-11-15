<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Git Introduction</b>
<br>

# Git Introduction

Git is a version control system and Github is an online hosting of Git repositories (both Public, Private collaboration space for development purpose)

Here's a comprehensive list of Git commands and explanations for each step, from configuring Git to common operations like creating a repository, working with branches, merging, deleting, tagging, and viewing history.

### Configuring Git:

**Setting Global User Configurations:**
   - Configure your name:
```
git config --global user.name "Your Name"
```
   - Configure your email:
```
git config --global user.email "your.email@example.com"
```

**Checking Git Configuration:**
   - Verify your global configuration settings:
```
git config --global --list
```

### Creating a Repository:

**Initializing a New Repository:**
   - Create a new Git repository in the current directory:
```
git init
```

**Cloning an Existing Repository:**
   - Clone an existing remote repository:
```
git clone <repository_url>
```

### Local Git Workflow:

**Checking Repository Status:**
   - Check the status of your working directory:
```
git status
```

**Staging Changes:**
   - Add files to the staging area:
```
git add <file_name>
```

**Committing Changes:**
   - Commit changes in the staging area with a message:
```
git commit -m "Your commit message"
```

**Viewing Commit History:**
   - View the commit history:
```
git log
```

**Creating Branches:**
   - Create a new branch:
```
git branch <branch_name>
```

**Switching Branches:**
    - Switch to a different branch:
```
git checkout <branch_name>
```

**Merging Branches:**
    - Merge changes from one branch into the current branch:
```
git merge <branch_name>
```

**Deleting Branches:**
    - Delete a branch (local):
```
git branch -d <branch_name>
```
    - Force delete a branch (local):
```
git branch -D <branch_name>
```

### Remote Git Workflow:

**Adding a Remote Repository:**
    - Add a remote repository:
```
git remote add <remote_name> <repository_url>
```

**Pushing Changes to Remote:**
    - Push changes to a remote repository:
```
git push <remote_name> <branch_name>
```

**Pulling Changes from Remote:**
    - Fetch remote changes:
```
git fetch <remote_name>
```
    - Merge remote changes into the current branch:
```
git merge <remote_name>/<branch_name>
```
    - Pull remote changes into the current branch (fetch + merge):
```
git pull <remote_name> <branch_name>
```

**Viewing Remote Configuration:**
    - View remote configuration:
```
git remote -v
```

### Tagging:

**Creating Tags:**
    - Create a lightweight (annotated) tag:
```
git tag <tag_name>
```
    - Create an annotated tag with a message:
```
git tag -a <tag_name> -m "Tag message"
```

**Pushing Tags to Remote:**
    - Push tags to remote repository:
```
git push <remote_name> <tag_name>
```
    - Push all tags to remote repository:
```
git push --tags
```

### Deleting and Renaming:

**Deleting Commits:**
    - Delete the most recent commit (soft reset):
```
git reset HEAD~1
```
    - Delete a commit and all changes (hard reset):
```
git reset --hard HEAD~1
```

**Renaming Branches:**
    - Rename a local branch:
```
git branch -m <new_branch_name>
```
    - Rename a remote branch (caution: must force push):
```
git push origin --delete <old_branch_name>
git branch -m <old_branch_name> <new_branch_name>
git push origin <new_branch_name>
```

### Viewing History and Diffs:

**Viewing Commit Details:**
    - View the details of a specific commit:
```
git show <commit_sha>
```

**Viewing Differences:**
    - View the differences between commits or branches:
```
git diff <commit_or_branch_1> <commit_or_branch_2>
```

**Viewing Staged Changes:**
    - View differences for staged changes:
```
git diff --staged
```

These Git commands cover various aspects of working with Git, from configuring Git initially to common daily tasks like committing, branching, merging, and collaborating with remote repositories.