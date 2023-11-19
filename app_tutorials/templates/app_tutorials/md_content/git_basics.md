<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Git Basics</b>
<br>


Here's an expanded table of Git commands, including local Git commands for initial configuration, repository management, branching, tagging, and remote operations. This table starts with the initial setup and goes through the various stages of using Git, including adding, modifying, merging, deleting files, managing branches and tags, and interacting with remote repositories.

| Purpose                             | Command                                  | Description                                                                                      |
|-------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Initial Configuration**           |                                          |                                                                                                  |
| Set username                        | `git config --global user.name "[name]"` | Sets the global username for commits.                                                            |
| Set email                           | `git config --global user.email "[email]"`| Sets the global email for commits.                                                               |
| **Repository Initialization**       |                                          |                                                                                                  |
| Initialize repository               | `git init`                               | Initializes a new Git repository in the current directory.                                       |
| **Staging & Snapshotting**          |                                          |                                                                                                  |
| Stage files                         | `git add [file]`                         | Adds files to the staging area for Git.                                                          |
| Commit changes                      | `git commit -m "[message]"`              | Records the staged snapshot to the project history.                                              |
| **Branching & Merging**             |                                          |                                                                                                  |
| List branches                       | `git branch`                             | Lists all local branches in the repository.                                                      |
| Create branch                       | `git branch [branch-name]`               | Creates a new branch.                                                                            |
| Switch branch                       | `git checkout [branch-name]`             | Switches to the specified branch and updates the working directory.                              |
| Merge branch                        | `git merge [branch-name]`                | Merges the specified branch into the current branch.                                             |
| **Modifying Operations**            |                                          |                                                                                                  |
| Rename file                         | `git mv [file-original] [file-renamed]`  | Renames a file.                                                                                  |
| Remove file                         | `git rm [file]`                          | Removes a file from the working directory and stages the deletion.                               |
| **Tagging**                         |                                          |                                                                                                  |
| Create tag                          | `git tag [tag-name]`                     | Creates a tag for marking specific points in history as important.                               |
| **Remote Operations**               |                                          |                                                                                                  |
| Add remote repository               | `git remote add [remote-name] [url]`     | Adds a new remote Git repository.                                                                |
| Fetch from remote                   | `git fetch [remote-name]`                | Fetches branches and their respective commits from the remote repository.                        |
| Push to remote                      | `git push [remote-name] [branch-name]`   | Pushes branch to the remote repository.                                                          |
| Pull from remote                    | `git pull [remote-name] [branch-name]`   | Fetches and merges changes on the remote server to your working directory.                       |
| **Viewing Changes**                 |                                          |                                                                                                  |
| View changes                        | `git status`                             | Lists all new or modified files to be committed.                                                 |
| Show file differences               | `git diff`                               | Shows file differences not yet staged.                                                           |
| Show log                            | `git log`                                | Shows the commit logs.                                                                           |

These commands form the foundation of most interactions with Git and are essential for effective version control in software development projects. 
Remember, each command can have additional options and parameters to customize its behavior,
 so it's always helpful to refer to the Git documentation for more detailed usage.