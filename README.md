# Ansible Playbook Setup Instructions

## EN

This is an Ansible repository for installing and configuring various services.

---

### Prerequisites

- First, you need to install `uv` to manage dependencies efficiently:
```bash
pip install uv
```

- Clone this repository:
```bash
git clone https://github.com/almaty-itrider/ansible.git
```

- Navigate to the project directory:
```bash
cd ansible
```

- Install the required dependencies:
```bash
uv sync
```

- Activate the virtual environment:
```bash
source .venv/bin/activate
```

### Configuration

- Create an inventory file named `hosts.ini` inside `inventories/<environment>/hosts.ini`. This file should include the IP addresses of the servers you want to configure. An example file `hosts.ini.example` is provided in the repository for reference.

- Additionally, create a file named `vault.yml` inside `inventories/<environment>/group_vars/<environment>/vault.yml`. This file should store sensitive variables required by the roles. An example file `vault.yml.example` is included in the repository for guidance.

  You can encrypt the file using the following command:
```bash
ansible-vault encrypt inventories/<environment>/group_vars/<environment>/vault.yml
```

### Running Playbooks

- Execute the following command to install and configure services:
```bash
ansible-playbook -i inventories/<environment>/hosts.ini playbooks/postgres_exporter.yml --ask-vault-pass
```

> **Note:** Replace `<environment>` with your target environment (e.g., `dev`, `staging`, `test`, `production`). Also, replace `postgres_exporter.yml` with the specific service playbook you want to execute.

- Use `ansible-lint` to check the syntax of your playbooks:
```bash
ansible-lint playbooks/postgres_exporter.yml
```

### Running Tests with Molecule

- To test Ansible roles using Molecule, run:
```bash
molecule test
```

If you want to test a specific scenario, use:
```bash
molecule test -s <scenario_name>
```

---

## RU

Инструкция по установке и настройке сервисов с помощью Ansible

---

### Предварительные требования

- Сначала установите `uv` для управления зависимостями:
```bash
pip install uv
```

- Склонируйте репозиторий:
```bash
git clone https://github.com/almaty-itrider/ansible.git
```

- Перейдите в директорию проекта:
```bash
cd ansible
```

- Установите необходимые зависимости:
```bash
uv sync
```

- Активируйте виртуальное окружение:
```bash
source .venv/bin/activate
```

### Конфигурация

- Создайте файл `hosts.ini` в папке `inventories/<environment>/hosts.ini`. Этот файл должен содержать IP-адреса серверов, на которых будет производиться установка и настройка сервисов. В репозитории доступен пример файла `hosts.ini.example`.

- Также создайте файл `vault.yml` в папке `inventories/<environment>/group_vars/<environment>/vault.yml`. В этом файле должны храниться чувствительные переменные. Пример файла `vault.yml.example` включен в репозиторий.

  Вы можете зашифровать файл `vault.yml` с помощью следующей команды:
```bash
ansible-vault encrypt inventories/<environment>/group_vars/<environment>/vault.yml
```

### Запуск Playbook

- Для установки и настройки сервисов выполните команду:
```bash
ansible-playbook -i inventories/<environment>/hosts.ini playbooks/postgres_exporter.yml --ask-vault-pass
```

> **Примечание:** Замените `<environment>` на нужное окружение (например, `dev`, `staging`, `test`, `production`). Также замените `postgres_exporter.yml` на имя плейбука, который хотите выполнить.

- Проверьте синтаксис плейбука с помощью `ansible-lint`:
```bash
ansible-lint playbooks/postgres_exporter.yml
```

### Запуск тестов с Molecule

- Чтобы протестировать роли Ansible с помощью Molecule, выполните:
```bash
molecule test
```

Если необходимо протестировать конкретный сценарий, используйте:
```bash
molecule test -s <scenario_name>
```
