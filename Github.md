- 1. How to add folders to the git repo?
"git add <folder>/*" and then commit
https://stackoverflow.com/questions/8775850/how-do-i-add-files-and-folders-into-github-repos

- 2. How to remove the file only from the git repo, but not remove it from the file system?
"git rm --cached filename" and then push changes to the remote repo. 
https://stackoverflow.com/questions/2047465/how-can-i-delete-a-file-from-git-repo

- 3. Remove directory from git and local:
git rm -r one-of-the-directories
git commit -m "Remove duplicated directory"
git push origin <your-git-branch> (typically 'master', but not always)

- 4. How  to create a folder in github repo website?
   step1: go to the folder inside which you want to create another folder
   step2: click on New file
   step3: on the text field for the file name, first write the folder name you want to create, then type /, this creates a folder

- 5. If the file name has white space, when using git add, use " git add 'file name' ".
