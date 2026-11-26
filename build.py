#!/usr/bin/env python3
"""Writes the site's HTML from the content below. Run: python3 build.py
The output (index.html, contact.html, 404.html, work/*.html) is committed and served as is by GitHub Pages."""
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
EMAIL = "hello@waldre.co.za"
YEAR = 2026

# ---------------------------------------------------------------- projects
WORK = [
    dict(
        slug="shifties", name="Shifties", kind="Rostering & bookings", year="2026",
        lede="Staff rostering, clock-in, leave and bookings for restaurants, guest houses and schools, billed monthly in rand.",
        link=("shifties.co.za", "https://shifties.co.za"), source="Closed, a commercial product",
        shot=("shifties-roster.jpg", "A week's staff roster made by Shift Scatter, with shift times and days off"),
        card="The roster, clock-in and bookings in one place.",
        features=[
            ("Shift Scatter", "Builds the week's roster for you within a wage budget, and respects leave, days off, half days, overtime, minimum staff and rest between shifts."),
            ("Clock-in", "An installable clock-in app and a kiosk mode for a shared tablet: staff clock in with their ID, no login needed."),
            ("Leave and closures", "Leave requests with approval, public holidays and closures that the roster already knows about."),
            ("Bookings", "A public booking page and a bookings screen for the team."),
            ("Budget and forecast", "A turnover target, the wage cost so far and a forecast of where the period will end."),
            ("Schools", "A schools mode with timetables, teachers, subjects and relief cover."),
        ],
        prose=[
            "Shifties is a product I design, build, host and support. A business signs up, adds its people and shifts, and has a roster the same afternoon; there is a demo with a seeded restaurant to try first.",
            "The front end is React and TypeScript; the API is Django with Celery for the background work (roster generation, reminders, reports), PostgreSQL, and Docker, deployed from CI.",
        ],
        stack=["React 19", "TypeScript", "Vite", "Tailwind", "Django", "Django REST", "Celery", "Redis", "PostgreSQL", "Docker"],
        gallery=[("shifties-dashboard.jpg", "The dashboard: team size, shifts this period and hours per day"),
                 ("shifties-control.jpg", "Control panel: today's staff, and who's on shift right now"),
                 ("shifties-budget.jpg", "Budgeting: the turnover target and the projection for the period"),
                 ("shifties-attendance.jpg", "Time & attendance: every clock-in, with anything unusual flagged")],
    ),
    dict(
        slug="seqwence", name="Seqwence", kind="Desktop video editor", year="2026",
        lede="A video editor that runs on your own PC: a multi-track timeline, effects, motion tracking, captions and lossless exports.",
        link=None, source="Source-available (FSL-1.1-MIT)",
        shot=("seqwence-editor.jpg", "The Seqwence editor: library, monitor, timeline and effect controls"),
        card="Edit, track and export, all on your own PC.",
        features=[
            ("A multi-track editor", "Clips, transitions, resizable track lanes, guides with snapping, and a second monitor that shows the clips as they were shot."),
            ("Effects that export as previewed", "Colour and light, glow, green screen, camera shake, flash, RGB split, zoom punch, plus OpenFX, frei0r and LV2 plugins."),
            ("Motion tracking", "Draw a box and an AI tracker follows the object, checking every frame against your box; Track & follow keeps it centred."),
            ("Captions", "Speech to text, including Afrikaans and English mixed, with animated words and text presets."),
            ("Lossless exports", "Exports on the GPU (NVENC), checked frame by frame against the source."),
            ("A Windows installer", "Everything included, a first-run setup, and signed updates that always ask first."),
        ],
        prose=[
            "Seqwence started as a tool to trim and export game clips without losing any quality, and grew into a full editor. The editor runs in a browser window over a local Node server, so projects also open from a phone over your own network.",
            "Exports are built from the same description the live preview draws, so what you see is what is exported, and every lossless export is checked against its source.",
        ],
        stack=["Node.js", "JavaScript", "WebGL", "FFmpeg", "Electron", "ONNX Runtime", "C++ (OpenFX host)"],
        gallery=[("seqwence-tracking.jpg", "Track & follow: the tracked object's box and path on the monitor"),
                 ("seqwence-compare.jpg", "Compare: the edit beside the clips as they were shot")],
    ),
    dict(
        slug="fit", name="Fit", kind="Training log app", year="2026",
        lede="An installable training log: a gym timer, streaks, a year heatmap, weight, sleep and food, and training groups.",
        link=("fit.waldre.co.za", "https://fit.waldre.co.za"), source="Closed",
        shot=None, card="A year of training, one square a day.", colour="c2",
        features=[
            ("Workouts", "A live session screen with a timer and supersets, or just \"I went\"; plans you can share."),
            ("Streaks and a year heatmap", "Every training day on one grid, with progress charts per exercise, goals and challenges."),
            ("Food and water", "A food diary with macros, barcode scanning with an Open Food Facts lookup, kJ or kcal, and one-tap water."),
            ("An exercise catalogue", "About 250 exercises with pictures and demonstrations, and search by describing the movement."),
            ("Friends, groups and gyms", "Add friends by tag and train together, with reminders sent as push notifications."),
            ("An admin console", "Users, the catalogue, gyms, patch notes and email settings, all in the app."),
        ],
        prose=[
            "Fit is a progressive web app: it installs from the browser on Android and iPhone and works like a native app, with push reminders.",
            "It is a Next.js app with Prisma on SQLite, its own session login, and Web Push, hosted on my own server.",
        ],
        stack=["Next.js 16", "TypeScript", "Tailwind", "Prisma", "SQLite", "Web Push", "Recharts"],
        gallery=[],
    ),
    dict(
        slug="household", name="Household", kind="Home & money app", year="2026",
        lede="Shared shopping lists, a grocery price finder across South African retailers, a budget and a meal planner.",
        link=None, source="Private, made for one household",
        shot=None, card="One search, every shop's price.", colour="c3",
        features=[
            ("A grocery price finder", "Searches Checkers, Shoprite, Pick n Pay, Woolworths, SPAR, Clicks, Dis-Chem and Takealot at once, matches the same product across shops, and compares pack sizes."),
            ("Specials and leaflets", "This week's specials and the shops' leaflets, in the app."),
            ("Shared shopping lists", "Grouped by shop, with favourites and the best price next to each item."),
            ("A budget", "Expenses split per person and per period, with amounts that can be hidden."),
            ("A meal planner", "Meals and recipes scaled to the household, costed from live prices, and sent to the shopping list."),
            ("Deploys that roll themselves back", "Every release runs the tests and checks the live site; if anything fails, the old version is put back automatically."),
        ],
        prose=[
            "Household is a private app for one family, so there is nothing to sign up for. Its price finder is the interesting part: each shop has its own adapter, and the results are normalised so a 2 kg bag and two 1 kg bags compare fairly.",
            "It is a Next.js app on SQLite, with Playwright driving a headless browser for the shops that need one, tests in Vitest, and a deploy script that snapshots the database first.",
        ],
        stack=["Next.js 16", "React 19", "TypeScript", "Ant Design", "SQLite", "Playwright", "Vitest", "PM2", "nginx"],
        gallery=[],
    ),
    dict(
        slug="entroonce", name="Entroonce", kind="Discord bot", year="2026",
        lede="A Discord bot that plays each person's intro when they join a voice channel, set up from a page in the browser.",
        link=None, source="Source-available (FSL-1.1-MIT)",
        shot=("entroonce-setup.png", "Entroonce's setup page, finished and ready"),
        card="Everyone gets an intro.",
        features=[
            ("Intros and outros", "When someone joins the voice channel, one of their intros plays; when they leave, their outro."),
            ("Fair turns", "Intros take turns, least played first, so a new one is heard next."),
            ("A setup page, not config files", "It checks the bot token with Discord, makes the invite link and lists your servers, roles and channels to pick from."),
            ("Clips from Seqwence", "Seqwence sends a cut clip to the bot with one button, after a one-time link."),
            ("Runs anywhere", "A Windows installer, Docker for a server, or systemd on Linux; everything lives in one data folder."),
        ],
        prose=["Entroonce is written in Python. It runs without a token at first, serving its own setup page, and starts the Discord side once a token is saved."],
        stack=["Python", "discord.py", "aiohttp", "SQLite", "Docker"],
        gallery=[],
    ),
    dict(
        slug="clipstor", name="Clipstor", kind="Windows desktop tool", year="2022",
        lede="Batch-trim, compress, convert and sort game recordings on Windows, without opening an editor.",
        link=None, source="Closed",
        shot=None, card="A folder of clips, sorted by game and date.", colour="c1",
        features=[
            ("A clip sorter", "Reads the file names NVIDIA and AMD recording software write, and sorts a folder into one per game, with an undo."),
            ("Batch renaming", "Rename a whole folder of clips to one pattern."),
            ("A clip viewer", "A table of every clip's details with generated thumbnails."),
            ("A trimmer and render queue", "Set in and out points while watching, add the trim to a queue, and let it render in order."),
            ("Export presets", "H.265 quality, resolution, threads, audio bitrate and per-track names, saved as presets."),
        ],
        prose=["Clipstor is a Windows Forms app in C# on .NET Framework, with FFmpeg bundled for the encoding."],
        stack=["C#", ".NET Framework 4.8", "Windows Forms", "FFmpeg"],
        gallery=[],
    ),
    dict(
        slug="examprepper", name="ExamPrepper", kind="Study tool", year="2023",
        lede="Build practice exams from five question types, then sit them as practice tests.",
        link=("github.com/RoyaleNite/ExamPrepper", "https://github.com/RoyaleNite/ExamPrepper"), source="Open source",
        shot=None, card="Five kinds of question, one practice exam.", colour="c4",
        features=[
            ("Five question types", "Open questions, multiple choice, true or false, fill in the blank, and match the columns."),
            ("Subjects and collections", "Group questions by subject and put them together as an exam or a quick quiz."),
            ("Sit a test", "One question at a time, back and forth, with results at the end."),
            ("No database", "Everything is saved as JSON files next to the app."),
        ],
        prose=["A study project in C# and Windows Forms on .NET 7, written to turn notes into practice tests. It is unfinished, and the code is open on GitHub."],
        stack=["C#", ".NET 7", "Windows Forms", "JSON"],
        gallery=[],
    ),
]

# ---------------------------------------------------------------- shared parts
def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://royalenite.github.io{path}">
<meta property="og:image" content="https://royalenite.github.io/assets/social.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#151412">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def top(current=""):
    def nav(href, label, key, cls=""):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{href}"{cur}{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>{label}</a>'
    return f"""<header class="top">
  <a class="monogram" href="/" aria-label="Waldre Roos, home">WR</a>
  <nav aria-label="Main">
    {nav("/#work", "Work", "work", "hide-s")}
    {nav("/#about", "About", "about", "hide-s")}
    {nav("/contact", "Contact", "contact")}
    <a class="button" href="mailto:{EMAIL}?subject=A%20project">Start a project</a>
  </nav>
</header>
"""

def foot(invite="Outgrown the spreadsheet?"):
    return f"""<footer class="foot">
  <div class="invite" data-reveal>
    <p>{e(invite)}</p>
    <a class="button dark" href="/contact">Start a project <span class="arrow" aria-hidden="true">→</span></a>
  </div>
  <div class="links" data-reveal style="--i:1">
    <a href="mailto:{EMAIL}">{EMAIL}</a>
    <a href="https://github.com/RoyaleNite">GitHub</a>
    <a href="https://shifties.co.za">Shifties</a>
    <a href="/#work">All work</a>
  </div>
  <div class="legal">
    <span>© {YEAR} Waldre Roos · Mbombela, South Africa</span>
    <span>Set in Instrument Serif and Instrument Sans</span>
  </div>
  <p class="name" aria-hidden="true">Waldre Roos</p>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

def contact_block(heading_tag="h2"):
    return f"""<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="col">
    <{heading_tag} class="prompt" id="contact-h" data-reveal>What does your business run on now?</{heading_tag}>
    <p class="prompt-2" data-reveal>Tell me, and what it should do instead.</p>
    <form data-mail action="mailto:{EMAIL}" method="post" enctype="text/plain" data-reveal style="--i:1">
      <label class="sr-only" for="msg">Your message</label>
      <textarea id="msg" name="message" rows="1" placeholder="We do the roster in Excel and…"></textarea>
      <button type="submit" aria-label="Send by email">→</button>
    </form>
    <p class="next" data-reveal style="--i:2">Sending opens your email app with your message in it, addressed to me. I read and answer every one myself.</p>
    <dl data-reveal style="--i:3">
      <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
      <dt>Based in</dt><dd>Mbombela, South Africa</dd>
      <dt>Code</dt><dd><a href="https://github.com/RoyaleNite">github.com/RoyaleNite</a></dd>
    </dl>
  </div>
</section>
"""

def picture_or_card(p, cls="", lazy=True):
    if p["shot"]:
        src, alt = p["shot"]
        return f'<img class="{cls}" src="/assets/img/{src}" alt="{e(alt)}" width="1600" height="1000"{" loading=" + chr(34) + "lazy" + chr(34) if lazy else ""}>'
    return f'<div class="typecard {p.get("colour", "c1")} {cls}" aria-hidden="true">{e(p["card"])}</div>'

# ---------------------------------------------------------------- home
def home():
    names = "\n".join(
        f'      <li><a href="/work/{p["slug"]}">{picture_or_card(p, "pic")}<span class="n">{e(p["name"])}</span></a></li>'
        for p in WORK)
    frames = "\n".join(f"    {picture_or_card(p, lazy=False)}" for p in WORK)
    choices = [
        ("sheet", "A spreadsheet", "A system that does the sums for you.",
         "The roster, the budget or the stock list moves out of a file only one person can open and into an app everyone signs in to, on their phone, with the same numbers for all.",
         'In <a href="/work/shifties">Shifties</a>, Shift Scatter makes the whole week\'s roster within a wage budget, the job most restaurants do in Excel.',
         "Moving off a spreadsheet", "Hi Waldre,\n\nWe run [what] in a spreadsheet at the moment. It would help if…\n"),
        ("chat", "A WhatsApp group", "One place where the answer stays put.",
         "Leave requests, swaps and \"who's on tomorrow?\" get asked once, answered once and kept, instead of scrolling back through a group chat.",
         '<a href="/work/shifties">Shifties</a> handles leave requests with approval, and staff clock in on a shared tablet instead of messaging the manager.',
         "Getting out of the WhatsApp group", "Hi Waldre,\n\nAt the moment we organise [what] in a WhatsApp group. It would help if…\n"),
        ("paper", "A paper diary", "Bookings people can make themselves.",
         "Customers book from a link at any hour, you see the day at a glance, and nothing is double-booked because the system already knows what's taken.",
         '<a href="/work/shifties">Shifties</a> has a public booking page and a bookings screen for the team, next to the roster.',
         "Bookings instead of a paper diary", "Hi Waldre,\n\nWe take bookings in a paper diary / by phone. It would help if…\n"),
        ("almost", "Software that almost fits", "The missing part, built to fit.",
         "Most businesses already pay for software that does nearly everything. I build the part around it: the import, the report, the price check, the job that runs every night.",
         'The price finder in <a href="/work/household">Household</a> searches eight South African retailers at once and compares the same product across them.',
         "The part our software doesn't do", "Hi Waldre,\n\nWe use [software], but it doesn't…\n"),
    ]
    btns = "\n".join(
        f'      <li><button class="choice" type="button" data-key="{k}" aria-pressed="false" aria-controls="answer">{e(label)}</button></li>'
        for k, label, *_ in choices)
    panels = "\n".join(
        f'''    <div class="panel" data-key="{k}" data-subject="{e(subj)}" data-body="{e(body)}">
      <h3>{e(h)}</h3>
      <p>{e(txt)}</p>
      <p class="proof">{proof}</p>
      <a class="button dark" href="mailto:{EMAIL}?subject={e(subj.replace(" ", "%20"))}">Email me about this <span class="arrow" aria-hidden="true">→</span></a>
    </div>''' for k, label, h, txt, proof, subj, body in choices)

    services = [
        ("Build", [
            ("var(--hl-1)", "Web applications that work properly on a phone, with logins, payments, email and admin screens", "React · Django"),
            ("var(--hl-1)", "Booking, rostering and admin systems to replace the spreadsheet, the group chat and the diary", "Shifties"),
            ("var(--hl-1)", "Automation and internal tools: price scrapers, reports, imports, exports and nightly jobs", "Node · Python"),
            ("var(--hl-1)", "Windows desktop tools, mostly for video", "C# · FFmpeg"),
        ]),
        ("Run", [
            ("var(--hl-2)", "Hosting on my own Linux servers", "nginx · Docker"),
            ("var(--hl-2)", "Backups, updates and deploys that test themselves first", "Every release"),
            ("var(--hl-2)", "Support: one person to call, who built it", "When it breaks"),
        ]),
        ("Stack", [
            ("var(--hl-3)", "Front end", "React · Next.js · TypeScript · Tailwind"),
            ("var(--hl-3)", "Back end", "Django · Celery · Node.js · PostgreSQL · SQLite"),
            ("var(--hl-3)", "Payments", "Paystack"),
        ]),
    ]
    svc = "\n".join(
        f'''    <div class="group" data-reveal style="--i:{gi}">
      <p>{g}</p>
      <ul>
{chr(10).join(f'        <li><span class="name"><span class="dot" style="background:{c}"></span><span>{e(n)}</span></span><span class="val">{e(v)}</span></li>' for c, n, v in rows)}
      </ul>
    </div>''' for gi, (g, rows) in enumerate(services))

    return head("Waldre Roos · Software for small businesses",
                "Freelance software developer in Mbombela, South Africa. I design, build and host the rostering, booking and admin software small businesses run on.", "/") + top() + f"""<main id="main">
<section class="hero" aria-label="Introduction">
  <h1><span class="line"><span data-line style="--i:0">Waldre</span></span><span class="line two"><span data-line style="--i:1">Roos</span></span></h1>
  <p class="say" data-rise>I build the software small businesses actually run on.<a href="#work" class="link">See the work ↓</a></p>
</section>

<section class="now" aria-labelledby="now-h">
  <h2 id="now-h" data-reveal>What runs your business today?</h2>
  <ul class="choices" role="list" data-reveal style="--i:1">
{btns}
  </ul>
  <div class="answer" id="answer" aria-live="polite" data-reveal style="--i:2">
{panels}
  </div>
</section>

<section class="work" id="work" aria-labelledby="work-h">
  <h2 id="work-h" data-reveal>Selected work</h2>
  <ul class="names" data-reveal style="--i:1">
{names}
  </ul>
  <div class="frame" aria-hidden="true">
{frames}
  </div>
</section>

<figure class="band">
  <video src="/assets/img/shifties-scatter.mp4" poster="/assets/img/shifties-scatter-poster.jpg" width="1600" height="1000" autoplay muted loop playsinline preload="metadata" aria-label="Shifties: Shift Scatter switching between the timeline, the roster and the printable preview"></video>
  <figcaption>Shifties: a week's roster, made by Shift Scatter</figcaption>
</figure>

<section class="about" id="about" aria-label="About">
  <div class="story" data-reveal>
    <p><strong>I'm Waldre Roos,</strong> a freelance software developer in <mark class="hl a">Mbombela, South Africa</mark>. I make the software a <mark class="hl b">small business</mark> uses every day: the roster, the bookings, the leave forms, the price list, and the report someone used to put together by hand every Friday.</p>
    <p>I design it, build it and then <mark class="hl c">host it on my own servers</mark>, so when something needs to change there is one person to call, and that person built it. <mark class="hl a">Shifties</mark>, my rostering and clock-in product, runs restaurants, guest houses and schools and is <mark class="hl b">billed monthly in rand</mark>.</p>
    <p>Everything is made for the <mark class="hl c">phone in your pocket</mark> first, because that is where your staff will use it. <a class="hl" href="/contact">Tell me what yours runs on.</a></p>
  </div>
</section>

<section class="services" aria-labelledby="svc-h">
  <div class="col">
    <h2 id="svc-h" data-reveal>What I do</h2>
{svc}
  </div>
</section>

{contact_block()}
</main>
""" + foot()

# ---------------------------------------------------------------- case studies
def case(i, p):
    nxt = WORK[(i + 1) % len(WORK)]
    words = p["name"]
    bits = [e(p["kind"]), p["year"], e(p["source"])]
    if p["link"]:
        bits.append(f'<a href="{p["link"][1]}">{e(p["link"][0])}</a>')
    facts = " · ".join(bits)
    if p["shot"]:
        src, alt = p["shot"]
        visual = f'<figure class="case-shot" data-reveal><img src="/assets/img/{src}" alt="{e(alt)}" width="1600" height="1000"></figure>'
    else:
        visual = f'<div class="case-type typecard {p.get("colour", "c1")}" data-reveal><span>{e(p["card"])}</span></div>'
    feats = "\n".join(f'      <li data-reveal style="--i:{j}"><b>{e(t)}</b><p>{e(d)}</p></li>' for j, (t, d) in enumerate(p["features"]))
    prose = "\n".join(f"      <p>{e(t)}</p>" for t in p["prose"])
    stack = "".join(f"<li>{e(s)}</li>" for s in p["stack"])
    gallery = ""
    if p["gallery"]:
        figs = "\n".join(f'  <figure data-reveal><img src="/assets/img/{s}" alt="{e(a)}" width="1600" height="1000" loading="lazy"><figcaption>{e(a)}</figcaption></figure>' for s, a in p["gallery"])
        gallery = f'<section class="gallery" aria-label="More screens">\n{figs}\n</section>\n'
    return head(f"{p['name']} · Waldre Roos", p["lede"], f"/work/{p['slug']}") + top("work") + f"""<main id="main">
<section class="case-head">
  <h1><span class="line"><span data-line>{e(words)}</span></span></h1>
  <p class="lede" data-rise>{e(p["lede"])}</p>
  <p class="facts" data-rise style="--i:1">{facts}</p>
</section>
{visual}
<section class="case-body">
  <h2 data-reveal>What it does</h2>
  <ul class="feat">
{feats}
  </ul>
  <h2 data-reveal>How it's made</h2>
  <div class="prose" data-reveal>
{prose}
  </div>
  <ul class="stack" aria-label="Built with" data-reveal>{stack}</ul>
</section>
{gallery}<a class="next-case" href="/work/{nxt['slug']}"><strong>Next: {e(nxt['name'])} →</strong></a>
</main>
""" + foot()

def contact_page():
    return head("Contact · Waldre Roos", "Start a project with Waldre Roos, a freelance software developer in Mbombela, South Africa.", "/contact") + top("contact") + f"""<main id="main">
<section class="case-head">
  <h1><span class="line"><span data-line>Start a project</span></span></h1>
  <p class="lede" data-rise>Tell me what your business runs on now and what gets in the way. You'll get a plain answer about whether I can help, and how.</p>
</section>
{contact_block("h2")}
</main>
""" + foot("Rather see the work first?")

def lost():
    return head("Not found · Waldre Roos", "This page doesn't exist.", "/404") + top() + f"""<main id="main" class="lost">
  <h1>Not here.</h1>
  <p>That page doesn't exist, or it moved. The work and the contact details are on the home page.</p>
  <p><a class="button" href="/">Go to the home page</a></p>
</main>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""

if __name__ == "__main__":
    (ROOT / "work").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(home())
    (ROOT / "contact.html").write_text(contact_page())
    (ROOT / "404.html").write_text(lost())
    for i, p in enumerate(WORK):
        (ROOT / "work" / f"{p['slug']}.html").write_text(case(i, p))
    print("wrote", 3 + len(WORK), "pages")
