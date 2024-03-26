from playwright.sync_api import sync_playwright

def extract_full_body_html(url, waitfor=None):
    # TIMEOUT=90000
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        page.evaluate('() => window.scroll(0, document.body.scrollHeight)')
        page.wait_for_load_state('domcontentloaded')
        if waitfor:
            page.wait_for_selector(waitfor)
        # page.screenshot(path='steam.png', full_page=True)
        html = page.inner_html('body')
        return html