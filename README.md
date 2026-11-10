
# Лабораторна робота №1
Налаштування середовища, Docker Compose, Healthcheck API, керування залежностями та GitHub Actions CI.

Вимоги ПЗ: Git, Docker і Docker Compose.

## Запуск через Docker Compose

1. Клонувати репозиторій:

   ```bash
   git clone https://github.com bedrovkyrylo/TRSK-LAB1.git
   cd НАЗВА_РЕПОЗИТОРІЮ
   ```

2. Запустити:

   ```bash
   docker compose up --build
   ```

3. В іншому терміналі або у браузері:

   ```bash
   curl http://localhost:8080/healthz/live
   curl http://localhost:8080/healthz/ready
   ```

4. Зупинити:

   ```bash
   docker compose down
   ```
