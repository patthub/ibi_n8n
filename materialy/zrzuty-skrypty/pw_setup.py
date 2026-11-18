from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-proxy-server"])
    ctx = b.new_context(viewport={"width":1440,"height":900}, locale="en-US")
    pg = ctx.new_page()
    pg.goto("http://127.0.0.1:5678/setup"); pg.wait_for_timeout(3000)
    inputs = pg.locator("input")
    vals = ["prowadzacy@example.com","Jan","Kowalski","ZmienMnie2026"]
    for i,v in enumerate(vals): inputs.nth(i).fill(v)
    pg.get_by_role("button", name="Next").click(); pg.wait_for_timeout(5000)
    print(pg.url); print(pg.inner_text("body")[:600])
    pg.screenshot(path="/home/claude/shots/after_setup.png")
    ctx.storage_state(path="/home/claude/state.json")
    b.close()
