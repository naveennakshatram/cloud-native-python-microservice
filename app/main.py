from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

COMMON_TITLE = "Welcome Page"

@app.get("/", response_class=HTMLResponse)
async def welcome():
    html_content = f"""
    <html>
        <head>
            <title>{COMMON_TITLE}</title>
        </head>
        <body>
            <nav style="text-align: center; margin-bottom: 20px;">
                <a href="/" style="margin: 10px; font-size: 24px;">Home</a>
                <a href="/about" style="margin: 10px; font-size: 24px;">About Us</a>
            </nav>
            <h1 style="color: green; font-size: 100px; text-align: center;">
                Welcome
            </h1>
            <h2 style="color: red; font-size: 80px; text-align: center;">
                Python With Naveen
            </h2>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/about", response_class=HTMLResponse)
async def about_us():
    html_content = f"""
    <html>
        <head>
            <title>{COMMON_TITLE}</title>
        </head>
        <body>
            <nav style="text-align: center; margin-bottom: 20px;">
                <a href="/" style="margin: 10px; font-size: 24px;">Home</a>
                <a href="/about" style="margin: 10px; font-size: 24px;">About Us</a>
            </nav>
            <h1 style="color: navy; font-size: 80px; text-align: center;">
                About Us
            </h1>
            <p style="font-size: 24px; text-align: center; max-width: 800px; margin: auto;">
                This is a sample FastAPI application created by Naveen to demonstrate web development using Python.
                Explore the simplicity and power of FastAPI for building modern APIs and web services.
            </p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
