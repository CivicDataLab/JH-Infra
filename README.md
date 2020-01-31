# JH-Infra
Infrastructure automation for Justice hub infrastructure 

This repository contains our Infrastructure automation setup and related documentation.

For step by step processes on each, please check out our [wiki](https://github.com/CivicDataLab/JH-Infra/wiki)

### System Requirements

1. Ansible-cli
2. Docker
3. pyhton 3.8 (Use vitrualenv if required)


### Setting up local environment

1. Clone the repository
  ```
  git clone https://github.com/justicehub-in/JH-Infra.git
  cd jh-infra
  ```
2. Install the requirements
  ```
  pip install -r requirements.txt
  ```
3. Setup the JusticeHub platform
  ```
  ansible-playbook  development.yml
  ```
4. Run the application
  ```
  docker exec -it ckan /usr/lib/ckan/ckan-env/bin/paster --plugin=ckan serve /etc/ckan/default/development.ini
  ```
5. Open browser and navigate to localhost:5000

### Contribution Guidelines
If you want to contribute to JusticeHub Infra, be sure to review the  [contribution guidelines](https://github.com/justicehub-in/Justice-Hub/blob/master/.github/CONTRIBUTING/CONTRIBUTING.md). This project adheres to JusticeHub's [code of conduct](https://github.com/justicehub-in/Justice-Hub/blob/master/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

We use GitHub issues for tracking requests and bugs.

### Contact
To contact the team behind JusticeHub, please write to judiciary@civicdatalab.in
