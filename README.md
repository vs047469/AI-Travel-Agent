# AI Travel Planner ✈️

> Describe your trip and let AI agents plan your journey.

AI Travel Planner is an **agentic AI travel planning application** that takes a user's natural-language travel request and creates a personalized travel plan. The system uses AI agents to understand the user's requirements, reason about the trip, and generate a structured itinerary.

## 🚀 Features

* 🧠 **AI-powered trip planning**
* 💬 Describe your trip using natural language
* 🤖 **Agentic workflow** for breaking down travel-planning tasks
* 📍 Destination and activity planning
* 🗓️ Day-by-day itinerary generation
* 🏨 Accommodation suggestions
* 🍴 Food and restaurant recommendations
* 🚗 Transportation planning
* 💰 Budget-aware planning
* 🔄 Dynamic multi-step agent workflow
* 📋 Structured and easy-to-follow travel itinerary

## 🏗️ Architecture

The application follows an **Agentic AI architecture** where specialized agents collaborate to generate the final travel plan.

```text
                    ┌─────────────────────┐
                    │       User          │
                    │ "Plan my trip..."   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Travel Planner    │
                    │       Agent         │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ Destination│  │ Itinerary   │  │  Activity   │
       │    Agent   │  │    Agent    │  │    Agent    │
       └─────────────┘  └─────────────┘  └─────────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │  Final Travel Plan  │
                    │     / Itinerary     │
                    └─────────────────────┘
```

## 🧩 Agent Workflow

A typical request flows through multiple stages:

1. **User Input**

   * User describes the destination, dates, budget, interests, and preferences.

2. **Request Understanding**

   * The planner agent identifies the important travel requirements.

3. **Task Planning**

   * The main agent breaks the request into smaller tasks.

4. **Specialized Agents**

   * Individual agents handle different aspects of the trip such as destinations, activities, itinerary, and recommendations.

5. **Result Aggregation**

   * The outputs from the agents are combined into a coherent travel plan.

6. **Final Response**

   * The system generates a structured day-by-day itinerary for the user.

## 🛠️ Tech Stack

### AI / LLM

* Python
* LangChain
* LangGraph
* Large Language Models (LLMs)
* Prompt Engineering
* Agentic AI

### Backend

* FastAPI
* Python
* REST APIs
* Pydantic

### Frontend

* Angular
* TypeScript
* HTML
* CSS
* Angular Material

### Development Tools

* Git
* GitHub
* VS Code
* Postman
* Uvicorn

## 📂 Project Structure

```text
AI-Travel-Planner/
│
├── frontend/
│   └── Angular application
│
├── backend/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── destination_agent.py
│   │   ├── itinerary_agent.py
│   │   └── activity_agent.py
│   │
│   ├── tools/
│   │   └── travel_tools.py
│   │
│   ├── services/
│   │   └── llm_service.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── .env
├── .gitignore
└── README.md
```

> The exact structure may vary depending on the current implementation.

## ⚙️ How It Works

The user can provide a request such as:

```text
Plan a 5-day trip to Dubai for two people.
My budget is ₹1,50,000.
I am interested in adventure activities,
shopping and local food.
```

The AI system processes the request and generates a personalized plan containing information such as:

```text
Day 1
├── Morning: Dubai Marina
├── Afternoon: Burj Khalifa
├── Evening: Dubai Mall
└── Dinner: Local restaurant

Day 2
├── Morning: Desert Safari
├── Afternoon: Adventure activities
└── Evening: Desert camp

...
```

## 🧠 Why LangGraph?

LangGraph is useful for this project because travel planning is naturally a **multi-step reasoning workflow**.

Instead of relying on a single LLM call, the workflow can:

* Maintain state between agents
* Execute multiple tasks
* Route requests between agents
* Handle conditional workflows
* Combine outputs from different agents
* Add validation and retry logic

A simplified workflow can be represented as:

```text
START
  │
  ▼
Understand Request
  │
  ▼
Create Travel Plan
  │
  ├───────────────┐
  ▼               ▼
Destination     Activities
Agent            Agent
  │               │
  └───────┬───────┘
          ▼
      Itinerary
        Agent
          │
          ▼
    Validate Plan
          │
          ▼
         END
```

## 🔑 Environment Variables

Create a `.env` file in the backend directory:

```env
OPENAI_API_KEY=your_api_key
```

If another LLM provider is used, configure the corresponding API key according to the implementation.

> Never commit API keys or other secrets to GitHub.

## ▶️ Running the Project

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI-Travel-Planner
```

### 2. Create a Virtual Environment

```bash
python -m venv virtualEnv
```

Activate it on Windows:

```bash
virtualEnv\Scripts\activate
```

### 3. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### 4. Configure Environment Variables

Create the `.env` file and add your required API keys.

### 5. Start the Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

### 6. Start the Frontend

Navigate to the frontend directory:

```bash
cd frontend
npm install
ng serve
```

The Angular application will normally be available at:

```text
http://localhost:4200
```

The FastAPI backend will normally be available at:

```text
http://localhost:8000
```

## 💡 Example Prompts

Try prompts such as:

```text
Plan a 7-day budget trip to Himachal Pradesh for two people.
```

```text
Create a 5-day family trip to Dubai with a budget of ₹2 lakh.
```

```text
Plan a romantic 4-day trip to Goa with beaches, restaurants
and relaxing activities.
```

```text
I have 3 days in Jaipur. Create an itinerary focused on
history, culture and local food.
```

## 🎯 Project Goals

The primary goal of this project is to demonstrate how **Generative AI and Agentic AI** can be used to solve a practical real-world problem.

The project demonstrates:

* LLM integration
* Prompt engineering
* Agent-based architecture
* LangGraph workflows
* State management
* Multi-agent collaboration
* API development
* Full-stack AI application development

## 🔮 Future Enhancements

Potential improvements include:

* 🌐 Real-time flight and hotel APIs
* 🗺️ Google Maps integration
* 🌦️ Weather-aware itinerary planning
* 💱 Real-time currency conversion
* 💰 Dynamic budget optimization
* 🏨 Real-time hotel availability
* ✈️ Flight search integration
* 📍 Location-aware recommendations
* 🧳 Personalized travel profiles
* 💬 Conversational itinerary modification
* 🔐 User authentication
* 📱 Mobile application
* 🧠 Long-term user preferences and memory

## 📸 Screenshots

Add screenshots of the application here:

```text
screenshots/
├── home.png
├── travel-planner.png
└── itinerary.png
```

Example:

```markdown
![AI Travel Planner](screenshots/travel-planner.png)
```

## 👨‍💻 Author

**Vicky Singh**

Software Engineer | Generative AI | Agentic AI | Full-Stack Development

---

⭐ If you find this project useful, consider giving the repository a star!


## Start Application: 
**************   streamlit run app.py **************