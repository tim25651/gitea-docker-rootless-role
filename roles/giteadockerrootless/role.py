#%%
"""JSON schema for Gitea Docker Rootless Ansible role."""
from __future__ import annotations

from typing import Annotated, Literal, TypeAlias

from msgspec import Meta, Struct
import defaults_schema
semantic_version_regex = r"^(0|[1-9])[0-9]*\.(0|[1-9])[0-9]*\.(0|[1-9])[0-9]*$"
Version: TypeAlias = Annotated[str, Meta(pattern=semantic_version_regex)]


class GiteaDockerRootlessConfig(Struct):
    """Configuration for Gitea Docker Rootless Ansible role."""
    git_user: str = "git"
    gitea_version: Version = "1.22.3"
    gitea_db_type: Literal["sqlite3", "mysql", "postgres"] = "sqlite3"
    gitea_db_host: str = "localhost"
    gitea_db_port: int = 3306
    gitea_db_name: str = "gitea"
    gitea_db_user: str = "gitea"
    gitea_db_root_pass: str = "gitea"
    gitea_db_pass: str = "gitea"
    gitea_dir: str = "{{ git_home }}/gitea"
    gitea_http_port: int = 3000
    db_dir: str = "{{ git_home }}/{{ gitea_db_type }}"
    docker_buildx_version: str = "0.18.0"
    docker_compose_version: str = "2.30.3"
    purge_data: bool = False
    purge_docker: bool = True
    remove_user: bool = False

defaults_schema.build(GiteaDockerRootlessConfig, __file__)
# %%
