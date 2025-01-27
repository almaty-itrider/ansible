# Ansible Playbook Setup Instructions

This is Ansible repository for installing and configuring some services.

---

- First of all, you need to install ansible on your machine. You can do it by running the following command:
Debian-based:
```bash
sudo apt install ansible
```
or

RedHat-based:
```bash
sudo dnf install ansible
```

- After that, you need to clone this repository:
```bash
git clone <repository_url>
```

- Next, create a file named `hosts.ini` in the path `inventory/<environment>/hosts.ini`. This file should include the IP addresses of the servers you want to configure. An example file `hosts.ini.example` is provided in the repository for reference.

- Additionally, create a file named `vault.yml` in the path `inventory/<environment>/group_vars/<environment>/vault.yml`. This file should store the sensitive variables required by the roles. An example file `vault.yml.example` is also included in the repository for your guidance.

  You can encrypt the file using the following command:
```bash
ansible-vault encrypt inventory/<environment>/group_vars/<environment>/vault.yml
```

- After that, you can run the following command to install and configure the services:
```bash
ansible-playbook -i inventory/<environment>/hosts.ini postgres_exporter.yml --ask-vault-pass
```

Note: Don't forget to replace `<environment>` with the environment you are working on (e.g. `dev`, `staging`, `test`, `production`). Also, you need to replace `postgres_exporter.yml` with the name of the service you want to install and configure. And finally, don't forget use `ansible-lint` to check the syntax of the playbook.
```bash
ansible-lint postgres_exporter.yml
```
