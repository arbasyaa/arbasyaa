#!/usr/bin/env python3
import html

W, PAD, FS, LH = 920, 20, 13, 20
BG, TBG = "#1e1e2e", "#181825"
TXT, BLUE, PINK, TEAL, GREEN, YELLOW, PURPLE, GRAY = "#cdd6f4", "#89b4fa", "#f38ba8", "#94e2d5", "#a6e3a1", "#f9e2af", "#cba6f7", "#6c7086"

def esc(t): return html.escape(t)

class T:
    def __init__(self):
        self.lines = []
        self.y = 38
    
    def text(self, txt, x=PAD, color=TXT, bold=False, size=FS):
        w = 700 if bold else 400
        self.lines.append(f'<text x="{x}" y="{self.y:.0f}" font-family="monospace" font-size="{size}" font-weight="{w}" fill="{color}">{esc(txt)}</text>')
        self.y += LH
    
    def texts(self, parts, x=PAD, size=FS):
        for i, (txt, color, bold) in enumerate(parts):
            w = 700 if bold else 400
            self.lines.append(f'<text x="{x}" y="{self.y:.0f}" font-family="monospace" font-size="{size}" font-weight="{w}" fill="{color}">{esc(txt)}</text>')
            x += len(txt) * (size * 0.6)
        self.y += LH
    
    def gap(self, n=0.5):
        self.y += LH * n
    
    def cmd(self, c):
        self.text("$ " + c, PAD, GREEN)
    
    def section(self, t):
        self.text(f"[{t}]", PAD, PURPLE, True)
    
    def kv(self, k, v):
        self.text(f"{k}: {v}", PAD + 16, TXT)
    
    def link(self, url):
        self.text("🔗 " + url, PAD + 16, TEAL)

t = T()

t.texts([("arbasyaa", BLUE, True), ("@", PINK, False), ("github", BLUE, True), (" ~ ", TXT, False), ("via 🐹 v1.26", GRAY, False)])
t.cmd("fastfetch")
t.gap(0.3)

ART = [
"         ⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⡀",
"         ⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄",
"         ⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆",
"         ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀",
"         ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
"         ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇",
"         ⠘⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠃",
"         ⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⡟",
"         ⠀⠀⠻⣿⣿⣿⣿⠁⠀⢀⣴⠇⠀⠀⢸⣦⡀⠀⠈⣿⣿⣿⣿⠟",
"         ⠀⠀⠀⠙⢿⣿⣿⡄⠀⠘⠿⠀⠀⠀⠀⠿⠃⠀⢠⣿⣿⡿⠋",
"         ⠀⠀⠀⠀⠀⠙⢿⣿⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣿⡿⠋",
"         ⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣶⣤⣤⣶⣾⣿⠟⠋",
"         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠉",
]
for line in ART:
    t.text(line, PAD + 50, BLUE, size=8)
t.gap(0.5)

t.text("arbasyaa@github", PAD + 280, BLUE, True, 14)
t.text("─" * 35, PAD + 280, GRAY)
t.kv("Name", "Arbasya")
t.kv("Role", "Backend Engineer")
t.kv("Status", "Fresh Graduate D3 TI")
t.kv("School", "Politeknik Negeri Cilacap")
t.kv("Achievement", "DBS x Dicoding Coding Camp Graduate")
t.kv("Focus", "Problem Solving & System Architecture")
t.gap()

t.cmd("cat skills.txt")
t.gap(0.3)
t.section("Languages")
t.text("JavaScript 📦 • Go 🐹 • PHP 🐘 • Python 🐍", PAD + 16)
t.gap(0.3)
t.section("Frameworks & Libraries")
t.text("Next.js ▲ • React ⚛️ • Node.js 🟢 • Hono 🔥 • Express 🚂", PAD + 16)
t.text("Gin 🍸 • Django 🎯 • Laravel 🎼 • TALL Stack 🏔️", PAD + 16)
t.gap(0.3)
t.section("Expertise")
for s in ["Backend Development", "Problem Solving & Logic", "System Architecture Design", "Product Requirements Document (PRD)", "Minimum Viable Product (MVP)", "API Contract Design"]:
    t.text("✓ " + s, PAD + 16, GREEN)
t.gap()

t.cmd("ls projects/ -la")
t.gap(0.3)
t.text("drwxr-xr-x  2 arbasyaa  staff   64B Aug  3 19:17", PAD + 16, BLUE)
t.text("emiten-app", PAD + 300, TEAL, True)
t.text("drwxr-xr-x  2 arbasyaa  staff   64B Aug  3 19:17", PAD + 16, BLUE)
t.text("tixgo-backend", PAD + 300, TEAL, True)
t.text("2 directories", PAD + 16, GRAY)
t.gap()

t.cmd("cat projects/emiten-app/README.md")
t.gap(0.3)
t.text("📈 Emiten — Advanced Financial Decision-Making Platform", PAD, YELLOW, True, 14)
t.text("Real-time stock & crypto analysis for Indonesian market (IDX) with", PAD)
t.text("technical indicators, fundamentals, screener, and portfolio tracking.", PAD)
t.gap(0.3)
t.text("Tech Stack: Next.js • TypeScript • Hono • TradingView Charts • Zustand", PAD + 16)
t.gap(0.2)
t.text("Features:", PAD + 16, PURPLE, True)
for s in ["• 6+ Technical indicators (RSI, MACD, Bollinger Bands, EMA, SMA)", "• Fundamental analysis with 0-100 valuation scoring", "• LQ45 stock screener with pre-built strategies", "• Portfolio tracker with real-time P&L calculation", "• Price alerts with browser notifications", "• Bilingual interface (EN/ID)"]:
    t.text(s, PAD + 16)
t.gap(0.2)
t.text("Architecture: Next.js frontend + Hono backend + Redis cache", PAD + 16)
t.gap(0.2)
t.link("https://github.com/arbasyaa/emiten-app")
t.gap()

t.cmd("cat projects/tixgo-backend/README.md")
t.gap(0.3)
t.text("🎫 TixGo Backend — High-Concurrency Ticketing System", PAD, YELLOW, True, 14)
t.text("Production-ready backend for flash-sale scenarios with atomic stock", PAD)
t.text("management and async order processing.", PAD)
t.gap(0.3)
t.text("Tech Stack: Go • Gin • PostgreSQL • Redis • RabbitMQ • Docker", PAD + 16)
t.gap(0.2)
t.text("Features:", PAD + 16, PURPLE, True)
for s in ["• Redis atomic DECRBY (zero overselling guarantee)", "• RabbitMQ async order processing", "• Idempotent payment webhooks with HMAC-SHA256", "• Automatic stock recovery on order expiry", "• Admin dashboard with real-time metrics", "• Circuit breaker for external calls"]:
    t.text(s, PAD + 16)
t.gap(0.2)
t.text("QA Results: 32/32 tests passed (100%)", PAD + 16)
t.text("Load Test: 1000 concurrent orders in ~8.1s", PAD + 16)
t.gap(0.2)
t.link("https://github.com/arbasyaa/tixgo-backend")
t.gap()

t.cmd("cat contact.txt")
t.gap(0.3)
t.text("📧 Email: arbasyaa@gmail.com", PAD + 16)
t.text("🐙 GitHub: github.com/arbasyaa", PAD + 16)
t.gap()

t.texts([("arbasyaa", BLUE, True), ("@", PINK, False), ("github", BLUE, True), (" ~", TXT, False)])
t.text("$ ▌", PAD, GREEN)

H = int(t.y + 16)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="32" fill="{TBG}"/>
<circle cx="16" cy="16" r="5" fill="{PINK}"/><circle cx="32" cy="16" r="5" fill="{YELLOW}"/><circle cx="48" cy="16" r="5" fill="{GREEN}"/>
<text x="{W//2}" y="21" font-family="monospace" font-size="11" fill="{GRAY}" text-anchor="middle">arbasyaa@github: ~ — zsh</text>
{chr(10).join(t.lines)}
</svg>'''

with open("/var/folders/f4/_8_jhg4j0_9gy05rn8ss5r6r0000gn/T/opencode/arbasyaa/profile.svg", "w") as f:
    f.write(svg)
print(f"OK height={H}")
