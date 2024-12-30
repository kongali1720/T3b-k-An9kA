from flask import Flask, render_template_string, request
from datetime import datetime, timedelta

app = Flask(_name_)

# The list of numbers
numbers = [
    1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
    1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163,
    1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249,
    1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,
    1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439,
    1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
    1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601,
    1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693,
    1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783,
    1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877,
    1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
    1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069,
    2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143,
    2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267,
    2269
]

correct_number = 2267  # The correct number

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        guess = request.form.get("guess")
        if guess:
            try:
                guess = int(guess)
                if guess == correct_number:
                    message = "SELAMAT ANDA MENDAPKAN HADIAH KEBERUNTUNG SEBESAR Rp.50,000,000.00."
                else:
                    message = "Coba lagi...! Kali ini mungking ANDA yang HOKI CUAN...."
            except ValueError:
                message = "Please enter a valid number."
    
    # Calculate the date and time of the event (e.g., 3 days from now)
    event_time = datetime.now() + timedelta(days=3)

    # Format remaining time as hours, minutes, and seconds
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEBAK KEBERUNTUNGAN HARI INI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            text-align: center;
            color: white;
            height: 100vh;
            overflow: hidden;
            position: relative;
            background: linear-gradient(45deg, #ff6a00, #ff0000, #ff73c5);
            background-size: 600% 600%;
            animation: gradientShift 5s ease infinite, waveEffect 2s ease-in-out infinite;
        }

        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        @keyframes waveEffect {
            0% {
                transform: translateX(0);
            }
            25% {
                transform: translateX(20px);
            }
            50% {
                transform: translateX(0);
            }
            75% {
                transform: translateX(-20px);
            }
            100% {
                transform: translateX(0);
            }
        }

        marquee {
            font-size: 18px;
            color: limegreen;
            margin-bottom: 20px;
        }

        h1 {
            background-color: orange;
            color: white;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
            animation: blink 1s infinite;
        }

        @keyframes blink {
            50% {
                opacity: 0.6;
            }
        }

        p {
            font-size: 18px;
            margin-bottom: 20px;
        }

        .numbers {
            margin: 20px 0;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
        }

        .numbers span {
            display: inline-block;
            margin: 10px;
            padding: 20px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.3s ease;
            background-color: #f1f1f1;
        }

        .numbers span:hover {
            transform: scale(1.1);
            box-shadow: 0 0 10px white;
        }

        .form-container {
            margin-top: 20px;
        }

        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            border: 2px solid orange;
            border-radius: 5px;
            width: 200px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            color: white;
            background-color: orange;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }

        button:hover {
            background-color: darkorange;
            transform: scale(1.1);
        }

        .message {
            margin-top: 20px;
            font-size: 24px;
            font-weight: bold;
            color: limegreen;
        }

        .countdown {
            margin-top: 20px;
            font-size: 48px;
            color: yellow;
            font-weight: bold;
        }

        .previous-winner {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            color: lightgreen;
            text-align: center;
        }

        table {
            margin: 0 auto;
            border-collapse: collapse;
            width: 50%;
            margin-top: 20px;
        }

        td {
            padding: 10px;
            text-align: left;
            border: 1px solid white;
        }

        th {
            padding: 10px;
            text-align: left;
            border: 1px solid white;
            background-color: #333;
        }

    </style>
</head>
<body>
    <marquee behavior="scroll" direction="left">WELCOME TO THE LOTTERY GAME! TRY YOUR LUCK AND WIN BIG!</marquee>

    <h1>TEBAK KEBERUNTUNGAN HARI INI</h1>

    <p>Find the right number to win big!</p>

    <div class="numbers">
        {% for number in numbers %}
        <span class="random-color" id="number-{{ number }}">{{ number }}</span>
        {% endfor %}
    </div>

    <div class="form-container">
        <form method="post">
            <input type="text" name="guess" placeholder="Enter your guess here">
            <button type="submit">SUBMIT</button>
        </form>
    </div>

    <div class="message">{{ message }}</div>

    <div class="countdown" id="countdown">
        <!-- Countdown will be updated by JavaScript -->
    </div>

    <div class="previous-winner">
        <p>Previous Winner:</p>
        <table>
            <tr>
                <th>No</th>
                <th>Pemenang Periode Lalu</th>
                <th>ID No.</th>
                <th>Total</th>
            </tr>
            <tr>
                <td>1</td>
                <td>27/12/2024</td>
                <td>2001007</td>
                <td>Rp.10,000,000.00</td>
            </tr>
        </table>
    </div>

    <div class="bottom-buttons">
        <button>Contact us</button>
        <button>Terms & Conditions</button>
        <button>Privacy Policy</button>
    </div>

    <script>
        // Function to generate a random color
        function getRandomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        // Function to apply random colors to the numbers
        function applyRandomColors() {
            const numberElements = document.querySelectorAll('.random-color');
            numberElements.forEach(element => {
                element.style.backgroundColor = getRandomColor();
                element.style.color = getRandomColor();
            });
        }

        // JavaScript to calculate the countdown
        function updateCountdown() {
            const eventTime = new Date("{{ event_time }}").getTime();
            const now = new Date().getTime();
            const timeLeft = eventTime - now;

            if (timeLeft <= 0) {
                document.getElementById("countdown").innerHTML = "Event started!";
                return;
            }

            const hours = Math.floor((timeLeft / (1000 * 60 * 60)) % 24);
            const minutes = Math.floor((timeLeft / (1000 * 60)) % 60);
            const seconds = Math.floor((timeLeft / 1000) % 60);

            document.getElementById("countdown").innerHTML = ${hours}h ${minutes}m ${seconds}s;

            setTimeout(updateCountdown, 1000); // update every second
        }

        // Apply random colors every 2 seconds
        setInterval(applyRandomColors, 2000);

        updateCountdown(); // start the countdown
    </script>
</body>
</html>
    """, numbers=numbers, event_time=event_time)

if _name_ == "_main_":
    app.run(debug=True)
