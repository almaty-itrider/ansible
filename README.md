# Ansible Playbook Setup Instructions

## EN

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

- Next, create a file named `hosts.ini` in the path `inventories/<environment>/hosts.ini`. This file should include the IP addresses of the servers you want to configure. An example file `hosts.ini.example` is provided in the repository for reference.

- Additionally, create a file named `vault.yml` in the path `inventories/<environment>/group_vars/<environment>/vault.yml`. This file should store the sensitive variables required by the roles. An example file `vault.yml.example` is also included in the repository for your guidance.

  You can encrypt the file using the following command:
```bash
ansible-vault encrypt inventories/<environment>/group_vars/<environment>/vault.yml
```

- After that, you can run the following command to install and configure the services:
```bash
ansible-playbook -i inventories/<environment>/hosts.ini playbooks/postgres_exporter.yml --ask-vault-pass
```

Note: Don't forget to replace `<environment>` with the environment you are working on (e.g. `dev`, `staging`, `test`, `production`). Also, you need to replace `postgres_exporter.yml` with the name of the service you want to install and configure. And finally, don't forget use `ansible-lint` to check the syntax of the playbook.
```bash
ansible-lint postgres_exporter.yml
```

---

## RU

Инструкция по установке и настройке сервисов с помощью Ansible

---

- Во-первых, вам нужно установить Ansible. Для этого выполните следующую команду:

Debian-based:
```bash
sudo apt install ansible
```
или

RedHat-based:
```bash
sudo dnf install ansible
```

- Затем склонируйте этот репозиторий с помощью следующей команды:
```bash
git clone <repository_url>
```

- Далее вам нужно создать файл `hosts.ini` в папке `inventories/<environment>/hosts.ini`. Этот файл должен содержать IP-адреса серверов, на которых вы хотите установить и настроить сервисы. Пример файла `hosts.ini.example` также включен в репозиторий для вашего удобства.

- Также вам нужно создать файл `vault.yml` в папке `inventories/<environment>/group_vars/<environment>/vault.yml`. Этот файл должен содержать переменные, которые вы хотите зашифровать. Пример файла `vault.yml.example` также включен в репозиторий для вашего удобства.

  Вы можете зашифровать файл `vault.yml` с помощью следующей команды:
```bash
ansible-vault encrypt inventories/<environment>/group_vars/<environment>/vault.yml
```

- И наконец, вы можете запустить плейбук Ansible с помощью следующей команды:
```bash
ansible-playbook -i inventories/<environment>/hosts.ini playbooks/postgres_exporter.yml --ask-vault-pass
```

Примечание: Не забудьте заменить `<environment>` на окружение, в котором вы работаете (например, `dev`, `staging`, `test`, `production`). Также вам нужно заменить `postgres_exporter.yml` на имя сервиса, который вы хотите установить и настроить. И наконец, не забудьте использовать `ansible-lint` для проверки синтаксиса плейбука.
```bash
