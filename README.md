# Auth Almighty 🔐

**Auth Almighty** is a flexible, high-performance, and database-agnostic authentication system built in Python. It focuses on providing secure and reusable authentication flows without handling data storage directly.

This initial version supports seamless OAuth2 integration with **Google** and **GitHub**.

## ✨ Features

- 🌐 OAuth2 login via Google and GitHub
- 🔒 Database-agnostic by design — no storage or ORM coupling
- 🔑 Stateless token generation (JWT)
- 🔁 Extensible and plug-and-play architecture
- 🧪 Easy to test, integrate, and scale

## 🚀 Use Case

Use `auth-almighty` in any backend system (FastAPI, Django, Flask, etc.) to:

- Authenticate users via Google or GitHub
- Validate OAuth tokens and extract user profile info
- Integrate with your own database or identity system

## 🛠 Technologies

- Python 3.10+
- `httpx` (async OAuth requests)
- `PyJWT`
- `Pydantic`

## 🧠 Philosophy

**Auth Almighty** focuses on clean separation between **auth logic** and **data persistence**, enabling use across microservices, monoliths, and headless systems.

---

> Designed with ❤️ by [La-Programmer](https://github.com/La-Programmer)
