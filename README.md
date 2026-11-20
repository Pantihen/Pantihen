<!-- ═══════════════════════════  HEADER  ═══════════════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=230&color=0:0d1117,65:0b3d0b,100:39ff14&section=header&text=Pantihen&fontColor=39ff14&fontSize=80&fontAlignY=36&desc=Python%20%C2%B7%20Django%20%C2%B7%20Backend&descSize=22&descAlignY=58&animation=twinkling" alt="Pantihen" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/Pantihen">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2600&pause=900&color=39FF14&center=true&vCenter=true&width=640&lines=%3E+booting+profile...;%3E+import+django%3B+django.setup()+%E2%9C%94;%3E+Python+%2F+Django+Backend+Developer;%3E+DRF+%7C+Celery+%7C+PostgreSQL+%7C+Redis+%7C+Docker;%3E+0+N%2B1+queries+in+production" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Pantihen&style=for-the-badge&color=39ff14&label=PROFILE+VIEWS" alt="Profile views" />
  <img src="https://img.shields.io/badge/status-%E2%98%A6%EF%B8%8F%20locked%20in-0d1117?style=for-the-badge&labelColor=39ff14&color=0d1117" alt="Locked in" />
  <img src="https://img.shields.io/badge/manage.py%20check-0%20issues-0d1117?style=for-the-badge&logo=django&logoColor=39ff14&labelColor=092E20" alt="manage.py check" />
</p>

<!-- ═══════════════════════════  BOOT  ═══════════════════════════ -->

```console
pantihen@github:~$ figlet -f "ANSI Shadow" pantihen

██████╗  █████╗ ███╗   ██╗████████╗██╗██╗  ██╗███████╗███╗   ██╗
██╔══██╗██╔══██╗████╗  ██║╚══██╔══╝██║██║  ██║██╔════╝████╗  ██║
██████╔╝███████║██╔██╗ ██║   ██║   ██║███████║█████╗  ██╔██╗ ██║
██╔═══╝ ██╔══██║██║╚██╗██║   ██║   ██║██╔══██║██╔══╝  ██║╚██╗██║
██║     ██║  ██║██║ ╚████║   ██║   ██║██║  ██║███████╗██║ ╚████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝

pantihen@github:~$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 5.x, using settings 'pantihen.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### `$ curl -s localhost:8000/api/v1/me/ | jq`

```json
{
  "name": "Bogdan Maksimenko",
  "handle": "@Pantihen",
  "role": "Python / Django Backend Developer",
  "about": [
    "Пишу бэкенд на Python и Django",
    "REST API на Django REST Framework, фоновые задачи на Celery",
    "Люблю чистую архитектуру, быстрые запросы и зелёные пайплайны"
  ],
  "stack": {
    "core": ["Python", "Django", "DRF", "FastAPI"],
    "data": ["PostgreSQL", "Redis", "Celery", "RabbitMQ"],
    "ops":  ["Docker", "Nginx", "Gunicorn", "GitHub Actions"]
  },
  "principles": ["select_related > N+1", "tests before deploy", "no deploys on Friday"],
  "status": "☦️ locked in"
}
```

### `$ tail -f /var/log/pantihen/now.log`

```diff
+ [build] DevSpace — соцсеть для разработчиков: Django + DRF + PostgreSQL
+ [build] REST API, JWT/RBAC, фоновые задачи на Celery + Redis
+ [infra] Docker → Gunicorn → Nginx → VPS, CI/CD на GitHub Actions
+ [learn] мониторинг: Prometheus + Grafana, автоматизация через Ansible
@@ next: async Django, профилирование ORM, высокие нагрузки @@
- [never] N+1 запросы в продакшене
- [never] деплой в пятницу вечером
```

<!-- ═══════════════════════════  STACK  ═══════════════════════════ -->

### `$ pip freeze --stack`

<table>
  <tr>
    <td align="center" width="140"><b>🐍 core</b></td>
    <td><img src="https://skillicons.dev/icons?i=python,django,fastapi&theme=dark" alt="Python, Django, FastAPI" />
      <br/>
      <img src="https://img.shields.io/badge/DRF-A30000?style=flat-square&logo=django&logoColor=white" alt="Django REST Framework" />
      <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white" alt="Celery" />
      <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest" />
      <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT" />
      <img src="https://img.shields.io/badge/Swagger-85EA2D?style=flat-square&logo=swagger&logoColor=black" alt="Swagger" />
    </td>
  </tr>
  <tr>
    <td align="center"><b>🗄️ data</b></td>
    <td><img src="https://skillicons.dev/icons?i=postgres,redis,rabbitmq,prisma&theme=dark" alt="PostgreSQL, Redis, RabbitMQ, Prisma" /></td>
  </tr>
  <tr>
    <td align="center"><b>🚀 ops</b></td>
    <td><img src="https://skillicons.dev/icons?i=docker,nginx,linux,bash,githubactions,prometheus,grafana,ansible&theme=dark" alt="Docker, Nginx, Linux, Bash, GitHub Actions, Prometheus, Grafana, Ansible" />
      <br/>
      <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white" alt="Gunicorn" />
      <img src="https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white" alt="Railway" />
    </td>
  </tr>
  <tr>
    <td align="center"><b>🧰 also</b></td>
    <td><img src="https://skillicons.dev/icons?i=nodejs,express,js,go,git,postman&theme=dark" alt="Node.js, Express, JavaScript, Go, Git, Postman" /></td>
  </tr>
</table>

<!-- ═══════════════════════════  PROJECTS  ═══════════════════════════ -->

### `$ ls -la ~/projects --sort=impact`

| | Проект | Что внутри |
|:-:|:--|:--|
| 🌐 | **[DevSpace](https://github.com/mrDisa/Devspace)** | Соцсеть для разработчиков: посты, лента, роли и права, админка. Django + DRF + PostgreSQL, Docker → Gunicorn → Nginx → VPS. Команда из двух человек |
| ✅ | **[fastapi-task-tracker](https://github.com/Pantihen/fastapi-task-tracker)** | Task Tracker API: PostgreSQL + Alembic, JWT/RBAC, фоновые задачи Celery + Redis, Docker, CI/CD |
| 🐳 | **[fastapi-docker-deploy](https://github.com/Pantihen/fastapi-docker-deploy)** | FastAPI + PostgreSQL + Redis + Celery в Docker, CI на GitHub Actions, деплой на Railway |
| 📈 | **[devops-final](https://github.com/Pantihen/devops-final)** | Docker, мониторинг Prometheus + Grafana, сборка в GHCR через GitHub Actions, раскатка Ansible |
| 📉 | **[Prolongo](https://github.com/mrDisa/Prolongo)** | Анализатор рисков оттока клиентов на Go |
| 📝 | **[kt06](https://github.com/Pantihen/kt06)** | API блог-платформы: Express, Prisma/PostgreSQL, Redis, JWT, RBAC, Socket.io, Swagger, Docker |

<!-- ═══════════════════════════  STATS  ═══════════════════════════ -->

### `$ git log --stats`

<p align="center">
  <img width="100%" src="./profile-summary-card-output/github_dark/0-profile-details.svg" alt="Profile details" />
</p>

<p align="center">
  <img height="170" src="./profile-summary-card-output/github_dark/3-stats.svg" alt="GitHub stats" />
  <img height="170" src="./profile-summary-card-output/github_dark/2-most-commit-language.svg" alt="Top languages" />
</p>

<p align="center">
  <img height="170" src="./profile-summary-card-output/github_dark/4-productive-time.svg" alt="Productive time" />
  <img height="170" src="https://streak-stats.demolab.com?user=Pantihen&hide_border=true&background=0d1117&ring=39ff14&fire=39ff14&currStreakLabel=39ff14&sideLabels=c9d1d9&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=8b949e&stroke=30363d" alt="GitHub streak" />
</p>

### `$ python manage.py run_snake`

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Pantihen/Pantihen/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Pantihen/Pantihen/output/github-snake.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/Pantihen/Pantihen/output/github-snake-dark.svg" />
  </picture>
</p>

<!-- ═══════════════════════════  FOOTER  ═══════════════════════════ -->

```console
pantihen@github:~$ exit
logout
Connection to github.com closed. Thanks for visiting! ⭐
```

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&color=0:39ff14,45:0b3d0b,100:0d1117&section=footer&animation=twinkling" alt="footer" width="100%" />
</p>
