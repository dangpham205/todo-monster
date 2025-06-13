from fasthtml.common import serve, Div, Span
from monsterui.all import H1, H2, Card, Button, Form, Input, ButtonT, Container, ContainerT, Theme, fast_app

app, router = fast_app(hdrs=Theme.blue.headers())
COUNTER = 0


@router("/inc", methods=["POST"])
def inc():
    global COUNTER
    COUNTER += 1
    return COUNTER


@router("/dec", methods=["POST"])
def dec():
    global COUNTER
    COUNTER -= 1
    return COUNTER


@router("/hello", methods=["POST"])
def hello(name: str):
    return f"Hello, {name}!"


@router
def index():
    return Container(
        H1("So dieu thuoc toi se dung vao ngay mai", cls="text-3xl font-bold text-center mb-6 mt-6"),
        Card(cls="p-6 text-center mb-4")(
            Div(cls="flex justify-center items-center gap-4")(
                Button("---", hx_post="/dec", hx_target="#counter"),
                Span(id="counter", cls="text-2xl font-bold")(COUNTER),
                Button("+++", hx_post="/inc", hx_target="#counter"),
            )
        ),
        Card(cls="p-6 text-center mb-4")(
            Form(hx_post="/hello", hx_target="#hello")(
                Input(name="name", placeholder="Enter your name"), # name is the param of the route
                Button("Hi", cls=ButtonT.primary),
            ),
            Div(id="hello", cls="text-2xl font-bold")
        ),
        cls=ContainerT.sm
    )

serve()
