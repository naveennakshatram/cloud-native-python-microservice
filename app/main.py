

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def welcome():
    html_content = """
    <html>
        <head>
            <title>Welcome Page</title>
        </head>
        <body>
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