from fasthtml.common import *
from app.application import rt


def nav_bar(user_email):
    nav_items = []
    for item in [("Home", "/"), ("About", "#about"), ("Services", "#services"), ("Contact", "#contact")]:
        nav_items.append(A(item[0], href=item[1], cls="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"))
    return Nav(
        Div(
            Div(
                Div(*nav_items, cls="md:block ml-10 flex items-baseline space-x-4"),
                cls="flex items-center"
            ),
            Div(
                A(
                    "Sign In" if not user_email else "Dashboard",
                    href="/login" if not user_email else "/dashboard",
                    cls="bg-gray-800 text-white px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-700"
                ),
                cls="ml-4 flex items-center md:ml-6"
            ),
            cls="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between"
        ),
        cls="bg-gray-800"
    )


def header():
    return Header(
        Div(
            H1("Welcome to Our App", cls="text-4xl font-bold text-white mb-6"),
            P("Discover amazing features and boost your productivity.", cls="text-xl text-gray-300 mb-8"),
            A("Get Started", href="#", cls="mt-10 bg-white text-gray-800 font-bold py-3 px-6 rounded hover:bg-gray-200"),
            cls="max-w-7xl mx-auto text-center py-32"
        ),
        cls="bg-gradient-to-r from-purple-600 to-blue-600"
    )


def about_section():
    return Section(
        H2("About Us", cls="text-3xl font-bold mb-6", id="about"),
        P("We are a team of passionate developers creating innovative solutions.", cls="text-gray-600 text-lg"),
        cls="max-w-7xl mx-auto py-32 px-4 sm:px-6 lg:px-8"
    )


def services_section():
    return Section(
        Div(
            H2("Our Services", cls="text-3xl font-bold mb-8", id="services"),
            Div(
                Div(
                    H3("Web Development", cls="text-xl font-semibold mb-3"),
                    P("Custom web applications tailored to your needs.", cls="text-gray-600"),
                    cls="bg-white p-8 rounded-lg shadow-md"
                ),
                Div(
                    H3("Mobile Apps", cls="text-xl font-semibold mb-3"),
                    P("Intuitive and responsive mobile applications.", cls="text-gray-600"),
                    cls="bg-white p-8 rounded-lg shadow-md"
                ),
                Div(
                    H3("Cloud Solutions", cls="text-xl font-semibold mb-3"),
                    P("Scalable and secure cloud infrastructure.", cls="text-gray-600"),
                    cls="bg-white p-8 rounded-lg shadow-md"
                ),
                cls="grid grid-cols-1 md:grid-cols-3 gap-8"
            ),
            cls="max-w-7xl mx-auto py-32 px-4 sm:px-6 lg:px-8"
        ),
        cls="bg-gray-100 w-full"
    )


def contact_section():
    return Section(
        H2("Contact Us", cls="text-3xl font-bold mb-6", id="contact"),
        P("Get in touch with us for any inquiries or support.", cls="text-gray-600 mb-6 text-lg"),
        A("Contact Support", href="mailto:support@example.com", cls="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded text-lg"),
        cls="max-w-7xl mx-auto py-32 px-4 sm:px-6 lg:px-8"
    )


def footer():
    return Footer(
        P("© 2023 Our App. All rights reserved.", cls="text-center text-gray-500"),
        cls="bg-gray-100 py-8"
    )


@rt('/')
def get(session):
    user_email = session.get('email')

    return Main(
        nav_bar(user_email),
        header(),
        Main(
            about_section(),
            services_section(),
            contact_section(),
            cls="bg-white"
        ),
        footer(),
        cls="min-h-screen flex flex-col"
    )
