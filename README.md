

## **🎓 CGPA Update Calculator**

A simple and responsive web application built with **Flask** and **HTML/CSS/JavaScript** to calculate your updated CGPA, considering:

* Current CGPA & completed credits
* New courses taken with GPA input
* Repeated courses (replacing previous grades)
* Optional **Thesis GPA** (weighted as a 4-credit course)
* Responsive light/dark theme toggle 🌙☀️

---

## **🛠 Features**

* 📘 Form-based GPA input for new and repeated courses
* 📊 Supports Thesis GPA with adjustable credit weight
* 🌗 Light/Dark mode with local theme memory
* 🎯 Animated result display
* 💻 Responsive layout (Form on left, result on right)

---

## 🚀 How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/cgpa-calculator.git
cd cgpa-calculator
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the app:

```bash
python app.py
```

The app will be available at: `http://127.0.0.1:5000/`

---

## 📁 File Structure

```
cgpa-calculator/
│
├── app.py              # Flask backend logic
├── templates/
│   └── index.html      # Frontend form & result view
├── static/             # (Optional for future CSS/JS)
├── requirements.txt    # Python dependencies
└── README.md           # You're here!
```

---

## 🧪 Example Use Case

> You completed 0 credits. Took 1 new course (GPA 4.0) and submitted a thesis (GPA 4.0).
> ✅ Final CGPA: **4.0**

---

## 📄 License

MIT License – feel free to modify and reuse for academic or personal purposes.


