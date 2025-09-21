# create files if not exists
touch requirements.txt
touch setup.py
touch README.md
touch LICENSE
touch .gitignore
touch .env
touch app.py
touch Dockerfile
touch elasticsearch.yaml
touch filebeat.yaml
touch kibana.yaml
touch logstash.yaml
touch k8s-deployment.yaml


# create directories if not exists
mkdir -p src
touch src/__init__.py
mkdir -p src/utils
touch src/utils/__init__.py
mkdir -p src/core
touch src/core/__init__.py
mkdir -p src/config
touch src/config/__init__.py
mkdir -p src/chains
touch src/chains/__init__.py
