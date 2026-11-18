from playwright.sync_api import sync_playwright
import contextlib
@contextlib.contextmanager
def page(url, w=1440, h=860):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-proxy-server"])
        ctx = b.new_context(viewport={"width":w,"height":h}, storage_state="/home/claude/state.json", device_scale_factor=1.5)
        pg = ctx.new_page(); pg.goto(url); pg.wait_for_timeout(5000)
        try: yield pg
        finally: b.close()
