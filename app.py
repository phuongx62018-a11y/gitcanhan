from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    male = None
    female = None

    if request.method == "POST":
        male = int(request.form["male"])
        female = int(request.form["female"])

        labels = ["Nam", "Nữ"]
        values = [male, female]

        # Tạo biểu đồ
        plt.figure(figsize=(6, 4))
        plt.bar(labels, values)

        plt.xlabel("Giới tính")
        plt.ylabel("Số sinh viên")
        plt.title("Số lượng sinh viên nam và nữ")

        # Trục Y chỉ hiển thị số nguyên
        plt.yticks(range(0, max(values) + 2))

        plt.grid(axis="y", linestyle="--", alpha=0.3)

        # Lưu biểu đồ
        plt.savefig("static/chart.png")
        plt.close()

    return render_template(
        "index.html",
        male=male,
        female=female
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5175
    )