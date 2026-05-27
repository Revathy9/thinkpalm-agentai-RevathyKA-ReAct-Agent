# Capstone Sandbox — Full Agent Pipeline: ReAct AI Agent

## 👤 Developer Profile
- **Name**: Revathy
- **Track**: Backend Dev
- **Lab Name**: Capstone Sandbox — Full Agent Pipeline

---

## 📝 Project Description
This project demonstrates a simple ReAct (Reasoning + Acting) AI Agent built using Python.

The agent:
- Accepts a user query
- Thinks step-by-step (Reasoning)
- Selects a tool (Action)
- Executes the tool (Action Execution)
- Observes the result (Observation)
- Returns the final answer

---

# AURA: Premium Agentic Weather & Reminder Assistant

AURA is a dual-agent smart assistant powered by Google Gemini and FastAPI. It processes natural language queries to seamlessly integrate real-time weather analytics and proactive task reminders.

---

## 🛠️ Tools & Technologies Used

### Backend Component
- **Python**: Core programming language.
- **FastAPI**: A high-performance, asynchronous web framework for building APIs.
- **Uvicorn**: An ASGI web server implementation for Python.
- **Google Generative AI SDK (`google-generativeai`)**: Connects to the Google Gemini model endpoints.
- **Python Dotenv (`python-dotenv`)**: Manage environment variables securely.
- **Requests**: For communicating with external HTTP endpoints.
- **wttr.in**: Minimalist weather information service used as an agentic tool.

### Frontend Component
- **React (v18)**: Interactive component-driven user interface.
- **Axios**: Promised-based HTTP client for API communication.
- **HTML5 & CSS3**: Modern styling layout and typography.

---

## 🚀 How to Run the Application

### 1. Prerequisites
Ensure you have the following installed:
* **Node.js** (v16+)
* **Python** (v3.9+)
* A **Google Gemini API Key** (obtainable from [Google AI Studio](https://aistudio.google.com/))

---

### 2. Backend Setup & Run

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Create a Python Virtual Environment (recommended):
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables:
   * Create a file named `.env` in the `backend/` directory.
   * Add your Gemini API Key in the following format:
     ```env
     GEMINI_API_KEY=AIzaSyYourActualKeyGoesHere
     ```

5. Run the FastAPI development server:
   ```bash
   uvicorn main:app --reload
   ```
   *The backend will be running at:* `http://127.0.0.1:8000`

---

### 3. Frontend Setup & Run

1. Navigate to the `frontend` folder:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   *The frontend will automatically open at:* `http://localhost:3000`

---

## 📝 Observations & Debugging Insights

During the development and testing phases, we resolved two critical configuration blockers:

### 🔍 1. Environment Path Resolution (`.env`)
* **Observation**: The server previously used `load_dotenv()` without specifying the path. This meant that if the backend server was started from the root directory (`d:\Training Project\weather-agent`), the application would fail to load the `.env` file from the `backend/` subdirectory.
* **Resolution**: We upgraded `backend/gemini_config.py` to dynamically load the `.env` relative to its own file path, preventing directory startup issues:
  ```python
  backend_dir = os.path.dirname(os.path.abspath(__file__))
  dotenv_path = os.path.join(backend_dir, ".env")
  load_dotenv(dotenv_path)
  ```

### 🔍 2. Gemini Model Retirement (`gemini-1.5-flash`)
* **Observation**: Trying to initialize the Gemini API with `"gemini-1.5-flash"` returned a `404 NotFound` error:
  `models/gemini-1.5-flash is not found for API version v1beta`
  This occurs because `gemini-1.5-flash` has been retired from the API endpoints in 2026.
* **Resolution**: We queried the list of active models via the `ModelService` and migrated the codebase to use **`gemini-2.5-flash`**. This modern, faster model is fully supported and works perfectly out-of-the-box.

### 🔍 3. Google API Key Validation
* **Observation**: 
  * If the key starts with an incorrect prefix (e.g. `AAIzaSy`), it fails local structural verification and returns `400 API key not valid`.
  * If the key has a correct prefix (`AIzaSy`) but is deactivated or invalid, the API server allows the request to pass local validation but throws a `404 Not Found` when trying to resolve the model.

---

## 🏁 Conclusion

This minimal project serves as a perfect stepping stone into the exciting world of AI agents. By understanding this basic loop of reasoning and acting, you are now prepared to explore more advanced agents that utilize Large Language Models (LLMs) and complex toolchains!
