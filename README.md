# giteadockerrootless
This role installs Gitea in a rootless docker mode.
Because of permissions problems mounting the .ssh directory,
to the container (either the host directory has the uid of the container user
or the container .ssh has the uid of container root), I sync the .ssh directory
with inotifywait.
does not use konstruktoid.docker_rootless as it fails on arm64
needs root permission to:
- create the git user
- enable linger
- install the dependencies (uidmap, slirp4netns, fuse-overlayfs)
- become the git user
- create the ssh forwarding script
- remove the git user and the ssh forwarding script for uninstallation

# Configuration
Defaults:
```yaml
git_user: git
gitea_version: 1.22.3
gitea_db_type: sqlite3 # either mysql, postgres or sqlite3
gitea_db_host: localhost # used with mysql and postgres
gitea_db_port: 3306 # used with mysql and postgres
gitea_db_name: gitea # used with mysql and postgres
gitea_db_user: gitea # used with mysql and postgres
gitea_db_root_pass: gitea # only used with mysql
gitea_db_pass: gitea # used with mysql and postgres
gitea_dir: '{{ git_home }}/gitea'
gitea_http_port: 3000
db_dir: '{{ git_home }}/{{ gitea_db_type }}' # used with mysql and postgres
docker_buildx_version: 0.18.0
docker_compose_version: 2.30.3
purge_data: false # if all data should be removed
purge_docker: true # if all images etc. should be removed
remove_user: false # if the git user should be removed during uninstallation. implies purge_data and purge_docker
```

# Usage
```bash
export MAIN_USER=$USER
export HOST=$HOST
pip install ansible
echo 'giteabox ansible_connection=ssh ansible_host=$HOST ansible_user=$MAIN_USER' > inventory
ansible-playbook -i inventory install.yml --ask-become-pass --ask-pass
# for uninstallation
# ansible-playbook -i inventory uninstall.yml --ask-become-pass --ask-pass
```

# TODO
- switch cp to rsync in the syncer container
- allow for changes in the app.ini
- create initial user via playwright or a similar tool
