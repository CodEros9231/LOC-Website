#!/usr/bin/python3

import cgi

print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()

selected_admin = form.getvalue('admin')

# Dictionary to store admin names and corresponding Calendly links
admin_calendly_links = {
    "Eros": "https://calendly.com/eroskuikel/for-splitease",
    "Snehil": "https://calendly.com/snehil/for-splitease",
    "Moeez": "https://calendly.com/moeez/for-splitease"
}

# Select the Calendly link based on the selected admin
calendly_link = admin_calendly_links.get(selected_admin, "")

print("""

<!DOCTYPE HTML>
<head>
<title>Contact Us</title>
<link rel='stylesheet' href='style.css'>
</head>
<body>
<header>
    <h1>Contact Us</h1>
    <div class="social-links mt-3 text-center">
        <a href="https://github.com/CodEros9231" class="github"><i class="bx bxl-github"></i></a>
        <a href="https://twitter.com/ErosKuikel" class="twitter"><i class="bx bxl-twitter"></i></a>
        <a href="https://www.linkedin.com/in/eroskuikel/" class="linkedin"><i class="bx bxl-linkedin"></i></a>
        <a href="mailto:eros.kuikel@nyu.edu" class="email-link"><i class="bx bx-envelope"></i> Email</a>
        <a href="tel:+971501923106" class="phone-link"><i class="bx bx-phone"></i> Phone</a>
    </div>
</header>

<div class="container">
    <h2>Contact the Admins</h2>
    <form action="/send-message" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Your Phone Number:</label>
        <input type="tel" id="phone" name="phone"><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>

        <label for="admin">Contact Admin:</label>
        <select id="admin" name="admin">
            <option value="Eros">Eros</option>
            <option value="Snehil">Snehil</option>
            <option value="Moeez">Moeez</option>
        </select><br><br>

        <!-- Print the Calendly link if it exists -->
        """)

if calendly_link:
    print(f'<a href="{calendly_link}">Schedule a meeting with {selected_admin}</a><br><br>')

print("""
        <button type="submit">Send Message</button>
    </form>
</div>

<footer>
    <p>&copy; 2024 Split Ease. All rights reserved.</p>
</footer>
</body>
</html> """)
