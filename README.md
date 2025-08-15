# Black-Scholes Option Pricing & PnL Heatmap Tool

A Python-based **Black-Scholes option pricing model** with a **Streamlit** web frontend.  
This tool allows users to calculate **Call** and **Put** option prices, visualize **PnL heatmaps** over a range of spot prices and volatilities, and determine if an option is **undervalued** or **overvalued**.

---

## 📌 Features
- **Black-Scholes pricing** for European call & put options
- Interactive **Streamlit web app**
- **PnL heatmaps** for both call and put options
- Displays **current option prices** in rectangular info boxes
- Indicates **undervalued/overvalued** status based on PnL
- Fully interactive — adjust parameters via sidebar inputs

---

## 📂 Project Structure
```
BSM_model/
│
├── bs_model.py          # Black-Scholes pricing logic
├── streamlit_app.py     # Streamlit frontend
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/marvelousjr/black_sholes_pricer
cd BSM_model
```

### 2️⃣ Create and activate a virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate   # Windows (PowerShell)
# OR
source .venv/bin/activate  # macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is missing, install manually:)*  
```bash
pip install streamlit numpy scipy matplotlib seaborn
```

---

## ▶️ Running the Application
```bash
streamlit run streamlit_app.py
```
Then open the **Local URL** provided in your browser (default: [http://localhost:8501](http://localhost:8501)).

---

## 🖼 How It Works
1. Enter **Spot Price, Strike Price, Time to Maturity, Risk-Free Rate, Volatility**, and **Purchase Price** for the option.
2. Define a **range** for Spot Price and Volatility.
3. The app:
   - Calculates Call & Put prices
   - Displays them in info boxes
   - Shows **Undervalued** / **Overvalued** status
   - Generates **PnL heatmaps** for each option type

---

## 📊 Example Output
- **Info Boxes:** Show current Call & Put prices
- **PnL Heatmaps:** X-axis = Spot Price, Y-axis = Volatility, Color = Profit/Loss
- Green = Profit, Red = Loss

---

## 🧮 Formula Used (Black-Scholes Model)
For a Call option:
```
C = S*N(d1) - K*e^(-rT)*N(d2)
```
For a Put option:
```
P = K*e^(-rT)*N(-d2) - S*N(-d1)
```
Where:
```
d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 - σ√T
```
- `S` = Spot Price  
- `K` = Strike Price  
- `T` = Time to Maturity (in years)  
- `r` = Risk-Free Interest Rate  
- `σ` = Volatility  
- `N()` = Cumulative distribution function of the standard normal distribution

---

## 📜 License
This project is open-source and free to use under the MIT License.

---

## ✨ Author
Developed by **Satwik Gupta**  
Feel free to connect or contribute!
