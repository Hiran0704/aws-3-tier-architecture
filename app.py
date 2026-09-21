from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "YOUR_RDS_ENDPOINT"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", "YOUR_DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "feedbackdb"),
    "port": 3306
}


@app.route("/")
def home():
    return jsonify({"status": "Flask is running"})


@app.route("/submit", methods=["POST"])
def submit_feedback():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    feedback = data.get("feedback")

    try:
        connection = pymysql.connect(**DB_CONFIG)

        with connection.cursor() as cursor:
            query = """
                INSERT INTO feedback (name, email, feedback)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (name, email, feedback))

        connection.commit()
        connection.close()

        return jsonify({
            "message": "Feedback submitted successfully!"
        })

    except Exception as e:
        return jsonify({
            "error": "Database connection failed"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
