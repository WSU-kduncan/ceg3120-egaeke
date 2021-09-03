Setup
1. Repositories: To set up for the creation of a repository, you have to have a working SSH key pair. Once you've logged   into the instance, you want to initialize the repo using the commmand git init with --bare if you want to initialize    an empty repo.

2. Users, folders, permissions: To add a new user you use the command su <username> and then type in the password.         Depending on the permissions given to the user which are chosen with the command chmod, said user has limited access    to folders, files, permissions, etc. To creat a folder as the new user, you use the command mkdir <foldername>.

3. SSH key directions: Once you have a key pair (public and private) you want to store the public key to your profile in   order to get into the instance. To do this you want to cd .ssh --> cd authorized_keys and paste the contents of the     public key into the file. Once you do that you can use the command ssh -i <reponame> <user>@<IP_Address>

Usage Guide
1. Clone usage & description: To clone a repo is to sync your repo between two locations. For example from a server to a   local device. In order to clone a repo you enter the command git clone git@<URL>:<user>:<reponame>.

2. Init usage & description: To initialize a repo you use the command git init to create a new repository.

3. Add usage & description: To add to a repo, you use the command git add <repo> which stages it to be commited and        later pushed to the remote server. 

4. Commit usage & description: To commit a repo, you use the command git commit (usually with -m to add a message). A      commit is basically a snapshot of what you are going to push to the repo and save.

5. Push usage & description: To push a repo, you use the command git push which pushes all the staged content to the       remote repository.
