
<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Git Examples</b>
<br>


Here are some Git command examples

### 1. Create a New Directory
```bash
mkdir project1        # Creates a new directory named "project1"
cd project1           # Enters the "project1" directory
```

### 2. Initialize a Git Repository
```bash
git init              # Initializes an empty Git repository in the current directory
```

### 3. Configure Git User Information
```bash
git config --global user.name "Your Name"       # Set your username
git config --global user.email "your@email.com" # Set your email
```

### 4. Create a File and Add Content
```bash
echo "Hello, Git!" > hello.txt    # Creates a file named "hello.txt" and adds content
```

### 5. Check the Status of Your Repository
```bash
git status            # Checks the current status of your Git repository
```

### 6. Stage Changes
```bash
git add hello.txt     # Stages the changes made to hello.txt for commit
```

### 7. Commit Changes
```bash
git commit -m "Add a greeting message"   # Commits the staged changes with a message
```

### 8. Connect to a Remote Repository
For instance, if you have a repository on GitHub:
```bash
git remote add origin <repository_URL>   # Connects your local repo to a remote repo
```

### 9. Push Changes to the Remote Repository
```bash
git push -u origin master   # Pushes committed changes to the "master" branch of the remote repo
```

These commands demonstrate the basic workflow of creating a Git repository, adding content, committing changes, and pushing them to a remote repository. You can replace `<repository_URL>` with the actual URL of your remote repository.
