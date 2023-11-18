# Postgres pgvector Extension - Vector Database with PostgreSQL / Langchain Integration

- PostgreSQL database has an extension for handling and saving vector-data.
- OpenAI is used for generating that vector-data.
- We use Docker-container to hold our PostgreSQL-database.

## Downloadables

<https://github.com/hwchase17/chroma-langchain/blob/master/state_of_the_union.txt>

## Virtual environment (venv)

In Visual Studio Code ... (all inputs in terminal)

Creating a virtual environment:

    python -m venv venv .... (or with a specific installed python version)
    python3.10 -m venv venv310

Activate venv in bash-terminal:

    . venv/bin/activate ... (or)
    source venv/bin/activate

## requirements.txt

Good advice found here: <https://learnpython.com/blog/python-requirements-file/>

    pip freeze > requirements.txt ... (creating file)
    pip install -r requirements.txt ... (installing from file)
    pip install -U -r requirements.txt ... (update file)

## OpenAI Embeddings

<https://platform.openai.com/docs/api-reference/embeddings>
<https://platform.openai.com/docs/guides/embeddings/what-are-embeddings>

## Docker

<https://docs.docker.com/engine/install/>
<https://hub.docker.com/r/ankane/pgvector>
 
    docker pull ankane/pgvector

### Installing Docker on Fedora Linux

<https://developer.fedoraproject.org/tools/docker/docker-installation.html>

    sudo dnf install dnf-plugins-core

    sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

    sudo dnf install docker-ce docker-ce-cli containerd.io

    sudo systemctl start docker

    sudo docker run hello-world

> Hello from Docker!
This message shows that your installation appears to be working correctly.

Enabling Docker right at boot, type ..

    sudo systemctl enable docker
> Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /usr/lib/systemd/system/docker.service.
