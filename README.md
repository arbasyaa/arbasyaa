<div align="center">

# Hi, I'm Arbasya 👋

**Backend Engineer** · Politeknik Negeri Cilacap

<sub>Building backends that stay boring in production — API contracts, data integrity, and the unglamorous parts that must not break.</sub>

<br>

[![Email](https://img.shields.io/badge/Email-arbasyaa@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:arbasyaa@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-arbasyaa-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arbasyaa)

</div>

---

## 🧰 Stack

**Languages**  
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

**Backend & Frameworks**  
![Gin](https://img.shields.io/badge/Gin-008ECF?style=flat-square&logo=gin&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white)
![Hono](https://img.shields.io/badge/Hono-E36002?style=flat-square&logo=hono&logoColor=white)
![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)

**Frontend & Data**  
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-FFAE00?style=flat-square&logo=rabbitmq&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

---

## 🚀 Featured Projects

### 🎫 [TixGo Backend](https://github.com/arbasyaa/tixgo-backend) — High-Concurrency Ticketing

Ticketing backend for flash-sale traffic. The hard part isn't the CRUD — it's selling 1000 tickets
for 2000 stock without ever overselling, while payment webhooks arrive twice.

- **Zero overselling** — stock lives in Redis, decremented with `DECRBY` plus a negative check, so the
  race resolves inside Redis instead of in application code.
- **Async order pipeline** — orders are queued in RabbitMQ, a worker persists them to PostgreSQL.
- **Idempotent webhooks** — `SETNX` deduplication with 72h TTL, so a retried callback cannot double-charge.
- **Self-healing stock** — expired pending orders return their stock automatically.

`Go` `Gin` `PostgreSQL` `Redis` `RabbitMQ` `sqlc` `Docker`

> **Verified:** 32/32 QA tests passing · load test of 1000 concurrent orders (qty=1, stock=2000) completed in ~8.1s

### 📈 [Emiten](https://github.com/arbasyaa/emiten-app) — IDX Stock & Crypto Analysis

Real-time analysis for the Indonesian market, with the indicators and scoring a retail investor
actually needs instead of a wall of raw numbers.

- 6+ technical indicators (RSI, MACD, Bollinger Bands, EMA, SMA)
- Fundamental analysis with a 0–100 valuation score
- LQ45 screener with pre-built strategies, portfolio P&L tracker, price alerts
- Bilingual interface (EN/ID)

`Next.js` `TypeScript` `Hono` `Redis` `Zustand` `TradingView Charts`

### 🎓 [SIM Sekolah](https://github.com/arbasyaa/sim-sekolah) — School Management System

Client–server academic administration with real RBAC, not a single-admin afterthought.

- JWT auth with three roles: `SUPERADMIN`, `GURU`, `SISWA`
- Master data (teachers, students, subjects, classes, academic years)
- Operational features: scheduling, attendance, grading

`TypeScript` `Next.js` `Node.js` `PostgreSQL`

---

## 🧠 How I Work

I care more about the *shape* of a system than the framework it's written in:

| | |
|---|---|
| **API contract first** | Agree on the request/response shape before writing handlers, so frontend and backend can work in parallel. |
| **PRD → MVP** | Scope the smallest thing that proves the idea, then earn the next feature. |
| **Failures are features** | Idempotency, retries, and expiry paths get designed up front — they're the paths that run at 3am. |

---

## 📊 GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=arbasyaa&show_icons=true&hide_border=true&bg_color=1e1e2e&title_color=89b4fa&text_color=cdd6f4&icon_color=94e2d5" alt="GitHub stats for arbasyaa" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=arbasyaa&layout=compact&hide_border=true&bg_color=1e1e2e&title_color=89b4fa&text_color=cdd6f4" alt="Most used languages" />

<br>

<img src="https://streak-stats.demolab.com?user=arbasyaa&hide_border=true&background=1e1e2e&ring=89b4fa&fire=f38ba8&currStreakLabel=cdd6f4&sideLabels=94e2d5&currStreakNum=cdd6f4&sideNums=cdd6f4" alt="Contribution streak" />

<br><br>

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=arbasyaa&theme=tokyonight" alt="Contribution summary" />

</div>

---

<div align="center">

**Open to backend engineering roles and interesting problems.**

<sub>Indonesian · English</sub>

</div>
