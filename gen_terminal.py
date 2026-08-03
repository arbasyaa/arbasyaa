#!/usr/bin/env python3
import html

W = 980
PAD = 24
FS = 13.5
LH = 21
ART_FS = 9
ART_LH = 12

BG = "#1e1e2e"
TITLEBAR = "#181825"
TXT = "#cdd6f4"
BLUE = "#89b4fa"
PINK = "#f38ba8"
TEAL = "#94e2d5"
GREEN = "#a6e3a1"
YELLOW = "#f9e2af"
PURPLE = "#cba6f7"
GRAY = "#6c7086"

y = 34 + 22
lines = []

def esc(t):
    return html.escape(t)

def segline(segs, x=PAD, fs=FS):
    global y
    tspan = "".join(
        f'<tspan x="{x}" dy="{LH if i else 0}" fill="{c}" font-weight="{700 if b else 400}">{esc(t)}</tspan>'
        for i, (t, c, b) in enumerate(segs)
    )
    lines.append(f'<text font-family="monospace" font-size="{fs}">{tspan}</text>')
    y += LH

def plain(t, c=TXT, x=PAD, fs=FS, bold=False):
    segline([(t, c, bold)], x, fs)

def art(lines_in, x=PAD, fs=ART_FS, color=BLUE):
    global y
    for i, l in enumerate(lines_in):
        dy = ART_LH if i else 0
        lines.append(f'<text font-family="monospace" font-size="{fs}" fill="{color}" xml:space="preserve"><tspan x="{x}" dy="{dy}">{esc(l)}</tspan></text>')
    y += ART_LH * len(lines)

def gap(n=1):
    global y
    y += LH * n * 0.5

def prompt():
    segline([("arbasyaa", BLUE, True), ("@", PINK, False), ("github", BLUE, True), (" ", TXT, False), ("~", TEAL, False), ("  ", TXT, False), ("via \U0001f439 v1.26", GRAY, False)])

def cmd(name):
    segline([("$", GREEN, True), (" ", TXT, False), (name, TXT, False)])

def section(title):
    plain(f"[{title}]", PURPLE, bold=True)

def kv(label, value):
    segline([(label, YELLOW, False), (" ", TXT, False), (value, TXT, False)])

def link(url):
    segline([("\U0001f517 ", TEAL, False), (url, TEAL, False)])

OCTOCAT = [
"\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2811\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2813\u2811\u2811\u2800",
"\u2800\u2800\u2811\u2815\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2815\u2811\u2800",
"\u2800\u2810\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2816\u2800",
"\u2801\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2813\u2800",
"\u2801\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2813\u2800",
"\u2801\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2807\u2811\u2801\u2815\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2813\u2800",
"\u2813\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2807\u2801\u2800\u2800\u2800\u2800\u2800\u2800\u2811\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2803\u2800",
"\u2800\u2815\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2807\u2801\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2813\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2815\u2800",
"\u2800\u2800\u2811\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2801\u2800\u2800\u2801\u2817\u2817\u2815\u2817\u2800\u2800\u2800\u2801\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2807\u2800",
"\u2800\u2800\u2800\u2800\u2819\u2817\u2817\u2817\u2817\u2817\u2817\u2802\u2800\u2800\u2813\u2811\u2800\u2800\u2800\u2800\u2800\u2813\u2811\u2800\u2800\u2801\u2817\u2817\u2817\u2817\u2817\u2817\u2817\u2816\u2800",
"\u2800\u2800\u2800\u2800\u2800\u2800\u2819\u2817\u2817\u2817\u2817\u2802\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2801\u2815\u2817\u2817\u2817\u2817\u2816\u2800",
"\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2819\u2811\u2817\u2817\u2817\u2811\u2811\u2815\u2815\u2811\u2815\u2811\u2817\u2817\u2817\u2817\u2811\u2819\u2800",
"\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2800\u2813\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2811\u2803\u2800",
]

prompt()
cmd("fastfetch")

art_y = y
gap(-0.2)
art(OCTOCAT)
info_y = art_y + 14
g = y
y = info_y
segline([("arbasyaa@github", BLUE, True)], x=300, fs=15)
segline([("\u2500" * 40, GRAY, False)], x=300)
kv("Name        ", "Arbasya")
kv("Role        ", "Backend Engineer")
kv("Status      ", "Fresh Graduate D3 TI")
kv("School      ", "Politeknik Negeri Cilacap")
kv("Achievement ", "DBS x Dicoding Coding Camp Graduate")
kv("Focus       ", "Problem Solving & System Architecture")
y = max(g, y) + 8

cmd("cat skills.txt")
gap()
section("Languages")
plain("JavaScript \U0001f4e6  \u2022  Go \U0001f439  \u2022  PHP \U0001f418  \u2022  Python \U0001f40d")
gap(0.5)
section("Frameworks & Libraries")
plain("Next.js \u25b2  \u2022  React \u269b\ufe0f  \u2022  Node.js \U0001f7e2  \u2022  Hono \U0001f525  \u2022  Express \U0001f682")
plain("Gin \U0001f378  \u2022  Django \U0001f3af  \u2022  Laravel \U0001f3bc  \u2022  TALL Stack \U0001f3d4\ufe0f")
gap(0.5)
section("Expertise")
for s in ["Backend Development", "Problem Solving & Logic", "System Architecture Design",
          "Product Requirements Document (PRD)", "Minimum Viable Product (MVP)", "API Contract Design"]:
    segline([("\u2713 ", GREEN, True), (s, TXT, False)], x=PAD + 16)

gap()
cmd("ls projects/ -la")
gap(0.3)
for name in ["emiten-app", "tixgo-backend"]:
    segline([("drwxr-xr-x", BLUE, False), ("  2 arbasyaa  staff   64B Aug  3 19:17  ", TXT, False), (name, TEAL, True)], x=PAD + 16)
plain("2 directories", GRAY, x=PAD + 16)
gap(0.3)

cmd("cat projects/emiten-app/README.md")
gap()
segline([("\U0001f4c8 Emiten \u2014 Advanced Financial Decision-Making Platform", YELLOW, True)], fs=14.5)
plain("Real-time stock & crypto analysis for Indonesian market (IDX) with technical indicators,")
plain("fundamentals, screener, and portfolio tracking.")
gap(0.3)
section("Tech Stack")
plain("Next.js \u2022 TypeScript \u2022 Hono \u2022 TradingView Charts \u2022 Zustand")
gap(0.3)
section("Features")
for s in [
    "6+ Technical indicators (RSI, MACD, Bollinger Bands, EMA, SMA)",
    "Fundamental analysis with 0-100 valuation scoring",
    "LQ45 stock screener with pre-built strategies",
    "Portfolio tracker with real-time P&L calculation",
    "Price alerts with browser notifications",
    "Bilingual interface (EN/ID)",
]:
    plain("\u2022 " + s, x=PAD + 16)
gap(0.3)
section("Architecture")
plain("Next.js frontend + Hono backend + Redis cache")
gap(0.3)
link("https://github.com/arbasyaa/emiten-app")
gap(0.6)

cmd("cat projects/tixgo-backend/README.md")
gap()
segline([("\U0001f3ab TixGo Backend \u2014 High-Concurrency Ticketing System", YELLOW, True)], fs=14.5)
plain("Production-ready backend for flash-sale scenarios with atomic stock management and")
plain("async order processing.")
gap(0.3)
section("Tech Stack")
plain("Go \u2022 Gin \u2022 PostgreSQL \u2022 Redis \u2022 RabbitMQ \u2022 Docker")
gap(0.3)
section("Features")
for s in [
    "Redis atomic DECRBY (zero overselling guarantee)",
    "RabbitMQ async order processing",
    "Idempotent payment webhooks with HMAC-SHA256",
    "Automatic stock recovery on order expiry",
    "Admin dashboard with real-time metrics",
    "Circuit breaker for external calls",
]:
    plain("\u2022 " + s, x=PAD + 16)
gap(0.3)
section("QA Results")
segline([("32/32 ", GREEN, True), ("tests passed (100%)", TXT, False)], x=PAD + 16)
section("Load Test")
plain("1000 concurrent orders in ~8.1s", x=PAD + 16)
gap(0.3)
link("https://github.com/arbasyaa/tixgo-backend")
gap(0.6)

cmd("cat contact.txt")
gap(0.3)
segline([("\U0001f4e7 Email ", YELLOW, False), (": arbasyaa@gmail.com", TXT, False)], x=PAD + 16)
segline([("\U0001f419 GitHub", YELLOW, False), (": github.com/arbasyaa", TXT, False)], x=PAD + 16)
gap(0.6)

prompt()
segline([("$", GREEN, True), (" ", TXT, False), ("\u258c", TXT, False)])

H = y + 14
body = f'<rect x="0" y="0" width="{W}" height="{H}" fill="{BG}"/>'
titlebar = f'<rect x="0" y="0" width="{W}" height="34" fill="{TITLEBAR}"/>'
dots = "".join(
    f'<circle cx="{20 + i * 18}" cy="17" r="6" fill="{c}"/>'
    for i, c in enumerate([PINK, YELLOW, GREEN])
)
title = f'<text x="{W/2}" y="22" font-family="monospace" font-size="12.5" fill="{GRAY}" text-anchor="middle">arbasyaa@github: ~ \u2014 zsh</text>'

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="monospace">
{body}
{titlebar}
{dots}
{title}
{chr(10).join(lines)}
</svg>
'''

out = "/Users/arbasya/Code/terminal.svg"
with open(out, "w") as f:
    f.write(svg)
print(f"OK height={H}")
